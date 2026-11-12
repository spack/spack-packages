# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Triton(CMakePackage, CudaPackage, ROCmPackage):
    """The Two-dimensional Runoff Inundation Toolkit for Operational Needs
    (TRITON) is an open-source, computationally efficient two-dimensional
    flood modeling toolkit that scales from a laptop to supercomputers. It
    solves the full shallow-water equations on CPUs and GPUs to produce fast,
    reproducible flood-inundation maps.
    """

    homepage = "https://triton-ornl.readthedocs.io"
    git = "https://code.ornl.gov/hydro/triton.git"

    license("BSD-3-Clause")

    version(
        "2.1.1",
        tag="2.1.1",
        commit="d18ed5b7a9daabca6aeb50d51c088e85bdd05b1b",
    )

    patch("use-external-dependencies.patch", when="@2.1.1")
    patch("use-cwd-as-project-root.patch", when="@2.1.1")

    variant("openmp", default=False, description="Build with the Kokkos OpenMP backend")
    variant("ensemble", default=False, description="Build ensemble simulation support")
    variant("gdal", default=False, description="Build GeoTIFF output support with GDAL")
    variant(
        "native_launcher",
        default=False,
        description="Use TRITON native GPU kernel launcher instead of Kokkos::parallel_for",
    )
    variant(
        "precision",
        default="double",
        values=("single", "double"),
        multi=False,
        description="Floating point precision",
    )
    variant("tests", default=False, description="Build TRITON regression tests")

    conflicts("+cuda", when="+rocm", msg="TRITON backends are mutually exclusive")
    conflicts("+openmp", when="+cuda", msg="TRITON backends are mutually exclusive")
    conflicts("+openmp", when="+rocm", msg="TRITON backends are mutually exclusive")
    conflicts(
        "+native_launcher",
        when="~cuda~rocm",
        msg="TRITON native launcher only applies to CUDA or ROCm builds",
    )
    conflicts("+cuda", when="cuda_arch=none")
    conflicts("+rocm", when="amdgpu_target=none")
    conflicts("%cxx=gcc@:12", msg="TRITON requires GCC 13 or newer")
    conflicts("%cxx=llvm@:15", msg="TRITON requires Clang 16 or newer")
    conflicts("%cxx=cce@:15", msg="TRITON requires Cray CCE 16 or newer")
    conflicts("%cxx=oneapi@:2023", msg="TRITON requires Intel oneAPI 2024 or newer")

    depends_on("cxx", type="build")
    depends_on("cmake@3.20:", type="build")
    depends_on("python", type="build")
    depends_on("mpi", type=("build", "link", "run"))
    depends_on("kokkos@5.1.1:5 cxxstd=20")
    depends_on("kokkos ~openmp", when="~openmp")
    depends_on("kokkos ~cuda", when="~cuda")
    depends_on("kokkos ~rocm", when="~rocm")
    depends_on("kokkos +serial", when="~openmp~cuda~rocm")
    depends_on("kokkos +openmp", when="+openmp")
    depends_on("kokkos +cuda +cuda_constexpr", when="+cuda")
    depends_on("kokkos +wrapper", when="+cuda %cxx=gcc")
    depends_on("kokkos +rocm", when="+rocm")
    depends_on("yaml-cpp", when="+ensemble")
    depends_on("gdal", when="+gdal")
    depends_on("cuda@12.4:", when="+cuda", type=("build", "link", "run"))
    depends_on("hip@6.2: +rocm", when="+rocm", type=("build", "link", "run"))

    for cuda_arch in CudaPackage.cuda_arch_values:
        depends_on(
            "kokkos +cuda cuda_arch={0}".format(cuda_arch),
            when="+cuda cuda_arch={0}".format(cuda_arch),
        )

    for amdgpu_value in ROCmPackage.amdgpu_targets:
        depends_on(
            "kokkos +rocm amdgpu_target={0}".format(amdgpu_value),
            when="+rocm amdgpu_target={0}".format(amdgpu_value),
        )

    def _backend(self):
        if "+cuda" in self.spec:
            return "CUDA"
        elif "+rocm" in self.spec:
            return "HIP"
        elif "+openmp" in self.spec:
            return "OPENMP"
        return "SERIAL"

    def _rocm_arch_flag(self):
        targets = self.spec.variants["amdgpu_target"].value
        if not targets:
            return None

        if isinstance(targets, str):
            targets = (targets,)

        targets = tuple(x for x in targets if x != "none")
        if not targets:
            return None

        return self.hip_flags(targets)

    def _mpi_launcher(self):
        mpi = self.spec["mpi"]
        search_paths = (os.path.dirname(mpi.mpicxx), str(mpi.prefix.bin))

        for name in ("mpiexec", "mpirun"):
            for path in search_paths:
                launcher = join_path(path, name)
                if os.path.isfile(launcher):
                    return launcher

        return "mpiexec"

    def _machine_file(self):
        spec = self.spec
        machine_file = join_path(self.stage.path, "spack-triton-machine.sh")
        compiler_flags = []
        linker_flags = []
        compiler = spec["mpi"].mpicxx

        for lib_dir in spec["mpi"].libs.directories:
            linker_flags.append("-Wl,-rpath,{0}".format(lib_dir))

        dtags = os.environ.get("SPACK_DTAGS_TO_ADD")
        if dtags:
            linker_flags.append("-Wl,{0}".format(dtags))

        if spec.variants["precision"].value == "single":
            compiler_flags.append("-DUSE_SINGLE_PRECISION")

        if "+openmp" in spec:
            compiler_flags.append(self.compiler.openmp_flag)
            linker_flags.append(self.compiler.openmp_flag)

        if "+cuda" in spec:
            if "%cxx=gcc" in spec:
                compiler = self["kokkos"].kokkos_cxx
            if "+native_launcher" in spec:
                compiler_flags.append("-DTRITON_CUDA_LAUNCHER")
            compiler_flags.append(spec["mpi"].headers.cpp_flags)
            linker_flags.append(spec["mpi"].libs.ld_flags)

        if "+rocm" in spec:
            compiler = spec["hip"].hipcc
            if "+native_launcher" in spec:
                compiler_flags.append("-DTRITON_HIP_LAUNCHER")
            compiler_flags.append(spec["mpi"].headers.cpp_flags)
            linker_flags.append(spec["mpi"].libs.ld_flags)
            arch_flag = self._rocm_arch_flag()
            if arch_flag:
                compiler_flags.append(arch_flag)
                linker_flags.append(arch_flag)

        with open(machine_file, "w", encoding="utf-8") as f:
            f.write("#!/usr/bin/env bash\n")
            f.write("export TRITON_BACKEND={0}\n".format(self._backend()))
            f.write('export TRITON_COMPILER="{0}"\n'.format(compiler))
            f.write('export TRITON_COMPILER_FLAGS="{0}"\n'.format(" ".join(compiler_flags)))
            f.write('export TRITON_LINKER_FLAGS="{0}"\n'.format(" ".join(linker_flags)))
            f.write("export TRITON_DEBUG=OFF\n")
            f.write('export TRITON_RUN_COMMAND="{0} -n 1"\n'.format(self._mpi_launcher()))
            if "+cuda" in spec:
                f.write('export CUDA_DIR="{0}"\n'.format(spec["cuda"].prefix))
                f.write('export CUDA_HOME="{0}"\n'.format(spec["cuda"].prefix))

        return machine_file

    def cmake_args(self):
        return [
            self.define("MACHINE", self._machine_file()),
            self.define("TRITON_USE_EXTERNAL_DEPS", True),
            self.define("TRITON_USE_CWD_AS_PROJECT_ROOT", True),
            self.define_from_variant("ENABLE_GDAL", "gdal"),
            self.define_from_variant("ENSEMBLE_BUILD", "ensemble"),
            self.define_from_variant("BUILD_TESTS", "tests"),
        ]

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        mkdirp(prefix.share.triton)

        executable = prefix.bin.triton
        install(join_path(self.build_directory, "triton.exe"), executable)
        with working_dir(prefix.bin):
            symlink("triton", "triton.exe")
        install(join_path(self.build_directory, "triton_env.sh"), prefix.share.triton)

        install_tree(join_path(self.stage.source_path, "input"), prefix.share.triton.input)
        install_tree(join_path(self.stage.source_path, "licenses"), prefix.share.triton.licenses)
        install(join_path(self.stage.source_path, "LICENSE"), prefix.share.triton)
