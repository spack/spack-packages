# Copyright 2023 Lawrence Livermore National Security, LLC and other
# Benchpark Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: Apache-2.0

from spack.package import *
from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage


class Branson(CMakePackage, CudaPackage, ROCmPackage):
    """Branson's purpose is to study different algorithms for parallel Monte
    Carlo transport. Currently it contains particle passing and mesh passing
    methods for domain decomposition."""

    homepage = "https://github.com/lanl/branson"
    url = "https://github.com/lanl/branson/archive/refs/tags/0.90.tar.gz"
    git = "https://github.com/LANL/branson.git"

    maintainers("alexrlongne")

    tags = ["proxy-app"]

    license("MIT")

    version("develop", branch="develop")

    version(
        "0.90",
        sha256="6a710f546b4d954e93db689b63fd5edcf52a57b01f3b72dcc4c90951cc4150dd",
        preferred=True,
    )
    version(
        "0.82",
        sha256="7d83d41d0c7ab9c1c906a902165af31182da4604dd0b69aec28d709fe4d7a6ec",
    )
    version("0.81", sha256="493f720904791f06b49ff48c17a681532c6a4d9fa59636522cf3f9700e77efe4")
    version("0.8", sha256="85ffee110f89be00c37798700508b66b0d15de1d98c54328b6d02a9eb2cf1cb8")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    variant("metis", default=True, description="Enable METIS support")
    variant("openmp", default=False, description="Enable OpenMP support")
    variant("caliper", default=False, description="Enable Caliper monitoring")
    variant("n_groups", default="30", values=int, description="Number of groups")
    variant("umpire", default=False, description="Use umpire memory pool")

    with when("+umpire"):
        depends_on("umpire@2026.07.2:", when="@develop")
        depends_on("umpire@2026.07.2", when="@0.90")

        depends_on("umpire+cuda", when="+cuda")
        for sm_ in CudaPackage.cuda_arch_values:
            depends_on("umpire cuda_arch={0}".format(sm_), when="cuda_arch={0}".format(sm_))

        depends_on("umpire+rocm", when="+rocm")
        for arch in ROCmPackage.amdgpu_targets:
            depends_on("umpire amdgpu_target={0}".format(arch), when="amdgpu_target={0}".format(arch))

        conflicts("~cuda~rocm")

    depends_on("mpi@2:")

    depends_on("metis", when="+metis")
    depends_on("parmetis", when="@:0.81 +metis")
    depends_on("caliper", when="+caliper")
    depends_on("adiak", when="+caliper")

    root_cmakelists_dir = "src"

    flag_handler = build_system_flags

    def setup_run_environment(self, env):
      if self.compiler.extra_rpaths:
        for rpath in self.compiler.extra_rpaths:
          env.prepend_path("LD_LIBRARY_PATH", rpath)

    def cmake_args(self):
        spec = self.spec
        args = []

        args.append(f"-DCMAKE_C_COMPILER={spec['mpi'].mpicc}")
        args.append(f"-DCMAKE_CXX_COMPILER={spec['mpi'].mpicxx}")
        args.append(f"-DCMAKE_Fortran_COMPILER={spec['mpi'].mpifc}")
        args.append(f"-DCMAKE_CXX_STANDARD=17")
        args.append(f"-DMPI_C_COMPILER={spec['mpi'].mpicc}")
        args.append(f"-DMPI_CXX_COMPILER={spec['mpi'].mpicxx}")

        if '+metis' in spec:
            args.append(f"-DMETIS_ROOT_DIR={spec['metis'].prefix}")

        if '+cuda' in spec:
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
            if '+rocm' in spec:
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

        if '+umpire' in spec:
            args.append("-DUSE_UMPIRE=ON")
            args.append(f"-Dumpire_DIR={spec['umpire'].prefix}")

        args.append(self.define_from_variant("USE_OPENMP", "openmp"))

        if '+caliper' in spec:
            args.append(self.define_from_variant("USE_CALIPER", "caliper"))
            args.append(f"-Dcaliper_DIR={spec['caliper'].prefix}")

        args.append("-DBUILD_TESTING=OFF")
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
