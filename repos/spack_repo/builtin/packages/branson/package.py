# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Branson(CMakePackage, CudaPackage, ROCmPackage):
    """Branson's purpose is to study different algorithms for parallel Monte
    Carlo transport. Currently it contains particle passing and mesh passing
    methods for domain decomposition."""

    homepage = "https://github.com/lanl/branson"
    url = "https://github.com/lanl/branson/archive/refs/tags/0.90.tar.gz"
    git = "https://github.com/lanl/branson.git"

    maintainers("alexrlongne")

    tags = ["proxy-app"]

    license("BSD-3-Clause")

    version("develop", branch="develop")

    version(
        "0.90",
        sha256="e2a3bccc291caf136739f31e4908e41ca46b12561f362030a02d2f06ab1d89c8",
    )

    depends_on("cxx", type="build")

    variant("metis", default=True, description="Enable METIS support")
    variant("openmp", default=False, description="Enable OpenMP support")
    variant("caliper", default=False, description="Enable Caliper monitoring")
    variant("n_groups", default="30", values=int, description="Number of groups")
    variant("tests", default=False, description="Build tests")
    variant("umpire", default=False, description="Use umpire memory pool")

    with when("+umpire"):
        depends_on("umpire@2026.07.2:", when="@0.90:")

        depends_on("umpire+cuda", when="+cuda")
        for sm_ in CudaPackage.cuda_arch_values:
            depends_on("umpire cuda_arch={0}".format(sm_), when="cuda_arch={0}".format(sm_))

        depends_on("umpire+rocm", when="+rocm")
        for arch in ROCmPackage.amdgpu_targets:
            depends_on(
                "umpire amdgpu_target={0}".format(arch), when="amdgpu_target={0}".format(arch)
            )

        conflicts("~cuda~rocm")

    depends_on("mpi@2:")

    depends_on("metis", when="+metis")
    depends_on("caliper", when="+caliper")

    root_cmakelists_dir = "src"

    flag_handler = build_system_flags

    def cmake_args(self):
        spec = self.spec
        args = []

        args.append(f"-DCMAKE_C_COMPILER={spec['mpi'].mpicc}")
        args.append(f"-DCMAKE_CXX_COMPILER={spec['mpi'].mpicxx}")
        args.append(f"-DCMAKE_Fortran_COMPILER={spec['mpi'].mpifc}")
        args.append(f"-DMPI_CXX_COMPILER={spec['mpi'].mpicxx}")

        args.append("-DCMAKE_CXX_STANDARD=17")

        if spec.satisfies("+metis"):
            args.append(f"-DMETIS_ROOT_DIR={spec['metis'].prefix}")

        if spec.satisfies("+cuda"):
            args.append("-DUSE_CUDA=ON")
            args.append("-DUSE_GPU=ON")
            args.append(f"-DCMAKE_CUDA_COMPILER={spec['cuda'].prefix}/bin/nvcc")
            cuda_arch_vals = spec.variants["cuda_arch"].value
            if cuda_arch_vals:
                cuda_arch_sorted = list(sorted(cuda_arch_vals, reverse=True))
                cuda_arch = cuda_arch_sorted[0]
                args.append(f"-DCUDA_ARCH={cuda_arch}")
        else:
            args.append("-DUSE_CUDA=OFF")
            if spec.satisfies("+rocm"):
                args.append("-DUSE_HIP=ON")
                args.append("-DUSE_GPU=ON")
                rocm_arch_vals = spec.variants["amdgpu_target"].value
                args.append(f"-DROCM_PATH={spec['hip'].prefix}")
                if rocm_arch_vals:
                    rocm_arch_sorted = list(sorted(rocm_arch_vals, reverse=True))
                    rocm_arch = rocm_arch_sorted[0]
                    args.append(f"-DROCM_ARCH={rocm_arch}")
                    args.append(f"-DHIP_ARCH={rocm_arch}")
            else:
                args.append("-DUSE_HIP=OFF")
                args.append("-DUSE_GPU=OFF")

        if spec.satisfies("+umpire"):
            args.append("-DUSE_UMPIRE=ON")
            args.append(f"-Dumpire_DIR={spec['umpire'].prefix}")

        args.append(self.define_from_variant("USE_OPENMP", "openmp"))

        if spec.satisfies("+caliper"):
            args.append(self.define_from_variant("USE_CALIPER", "caliper"))
            args.append(f"-Dcaliper_DIR={spec['caliper'].prefix}")

        args.append(self.define_from_variant("BUILD_TESTING", "tests"))

        args.append(f"-DN_GROUPS={self.spec.variants['n_groups'].value}")

        args.append(f"-DMPI_CXX_LINK_FLAGS={spec['mpi'].libs.ld_flags}")

        return args

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        mkdir(prefix.doc)
        install(join_path(self.build_directory, "BRANSON"), prefix.bin)
        install("LICENSE.md", prefix.doc)
        install("README.md", prefix.doc)
        install_tree("inputs", prefix.inputs)
