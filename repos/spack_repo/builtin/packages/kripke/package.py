# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Kripke(CMakePackage, CudaPackage, ROCmPackage):
    """Kripke is a simple, scalable, 3D Sn deterministic particle
    transport proxy/mini app.
    """

    homepage = "https://computing.llnl.gov/projects/co-design/kripke"
    git = "https://github.com/LLNL/Kripke.git"

    tags = ["proxy-app"]

    maintainers("rchen20")

    license("BSD-3-Clause")

    version("develop", branch="develop", submodules=False)
    version(
        "1.2.8",
        preferred=True,
        submodules=False,
        tag="v1.2.8",
        commit="46563d6d19afe7fdf65fc564638c7ec13615866f",
    )
    version("2025.12.0", submodules=False, commit="01f6f85c02ceffcd2bc06e42cee997867dd142c5")
    version("2025.07.0", submodules=False, commit="8cf38433a6a11e0dcd17864e649b2d045159ee9c")
    version("1.2.7.0", submodules=False, commit="db920c1f5e1dcbb9e949d120e7d86efcdb777635")
    version(
        "1.2.7", submodules=True, tag="v1.2.7", commit="ddcac43cdad999f0346eb682065ef0af1847029d"
    )
    version(
        "1.2.6", submodules=True, tag="v1.2.6", commit="55b39f34b68c68b2d828a33a75568abd66e1019f"
    )
    version(
        "1.2.5", submodules=True, tag="v1.2.5", commit="20e9ea975f1bf567829323a18927b69bed3f4ebd"
    )
    version(
        "1.2.4", submodules=False, tag="v1.2.4", commit="d85c6bc462f17a2382b11ba363059febc487f771"
    )
    version(
        "1.2.3", submodules=True, tag="v1.2.3", commit="66046d8cd51f5bcf8666fd8c810322e253c4ce0e"
    )
    version(
        "1.2.2",
        submodules=True,
        tag="v1.2.2-CORAL2",
        commit="a12bce71e751f8f999009aa2fd0839b908b118a4",
    )
    version(
        "1.2.1",
        submodules=True,
        tag="v1.2.1-CORAL2",
        commit="c36453301ddd684118bb0fb426cfa62764d42398",
    )
    version(
        "1.2.0",
        submodules=True,
        tag="v1.2.0-CORAL2",
        commit="67e4b0a2f092009d61f44b5122111d388a3bec2a",
    )

    variant("mpi", default=True, description="Build with MPI.")
    variant("chai", default=True, description="Build with CHAI/Umpire.")
    variant(
        "direct-device-plane",
        default=False,
        description="Use direct device allocator in Umpire for plane fields",
    )
    variant("openmp", default=False, description="Build with OpenMP enabled.")
    variant("caliper", default=False, description="Build with Caliper support enabled.")
    variant("gpu-aware-mpi", default=False, description="Enable GPU-aware MPI")

    depends_on("cxx", type="build")  # generated

    depends_on("mpi", when="+mpi")
    depends_on("blt", type="build", when="@:1.2.7")

    depends_on("raja@2026.07.1: ~examples~exercises cxxstd=20", when="@develop")
    depends_on("raja@2026.07.1 ~examples~exercises cxxstd=20", when="@1.2.8")
    depends_on("raja@2025.12.0 ~examples~exercises cxxstd=17", when="@2025.12.0")
    depends_on("raja@2024.07.0 ~examples~exercises cxxstd=14", when="@1.2.7.0,2025.07.0")
    depends_on("raja@:2024.02.1~exercises~examples", when="@:1.2.7")

    with when("+chai"):
        depends_on("chai+mpi", when="+mpi")

        depends_on("chai@2026.07.1: ~examples +raja cxxstd=20", when="@develop")
        depends_on("chai@2026.07.1 ~examples +raja cxxstd=20", when="@1.2.8")
        depends_on("chai@2025.12.0 ~examples +raja cxxstd=17", when="@2025.12.0")
        depends_on("chai@2024.07.0 ~examples +raja cxxstd=14", when="@1.2.7.0,2025.07.0")
        depends_on("chai~examples+raja", when="@:1.2.7")
        depends_on("chai+openmp", when="+openmp")
        depends_on("chai~openmp", when="~openmp")
        depends_on("chai+cuda", when="+cuda")
        depends_on("chai~cuda", when="~cuda")
        depends_on("chai~rocm", when="~rocm")
        depends_on("fmt@9.1", when="^chai@2024.07.0")

        depends_on("umpire@2026.07.2: ~examples", when="@develop")
        depends_on("umpire@2026.07.2 ~examples", when="@1.2.8")
        depends_on("umpire@2025.12.0 ~examples", when="@2025.12.0")
        depends_on("umpire@2024.07.0 ~examples", when="@1.2.7.0,2025.07.0")
        depends_on("umpire~examples", when="@:1.2.7")
        depends_on("umpire+openmp", when="+openmp")
        depends_on("umpire~openmp", when="~openmp")
        depends_on("umpire+cuda", when="+cuda")
        depends_on("umpire~cuda", when="~cuda")

        with when("+cuda"):
            for sm_ in CudaPackage.cuda_arch_values:
                depends_on(f"umpire cuda_arch={sm_}", when=f"cuda_arch={sm_}")
                depends_on(f"chai cuda_arch={sm_}", when=f"cuda_arch={sm_}")

        depends_on("umpire+rocm", when="+rocm")
        depends_on("umpire~rocm", when="~rocm")
        with when("+rocm @1.2.5:"):
            for arch in ROCmPackage.amdgpu_targets:
                depends_on(f"umpire amdgpu_target={arch}", when=f"amdgpu_target={arch}")
                depends_on(f"chai amdgpu_target={arch}", when=f"amdgpu_target={arch}")

        conflicts("^blt@0.7:", when="^chai@:2024.07.0")

    depends_on("caliper", when="+caliper")
    depends_on("adiak@0.4:", when="+caliper")
    conflicts("^blt@:0.3.6", when="+rocm")

    depends_on("blt@0.6.2:", type="build", when="@1.2.7:")

    with when("+cuda~chai"):
        depends_on("umpire@2026.07.2: ~examples", when="@develop")
        depends_on("umpire@2026.07.2 ~examples", when="@1.2.8")
        depends_on("umpire@2025.12.0 ~examples", when="@2025.12.0")
        depends_on("umpire@2024.07.0 ~examples", when="@1.2.7.0,2025.07.0")
        depends_on("umpire+cuda")
        for sm_ in CudaPackage.cuda_arch_values:
            depends_on(f"umpire cuda_arch={sm_}", when=f"cuda_arch={sm_}")

    with when("+rocm~chai"):
        depends_on("umpire@2026.07.2: ~examples", when="@develop")
        depends_on("umpire@2026.07.2 ~examples", when="@1.2.8")
        depends_on("umpire@2025.12.0 ~examples", when="@2025.12.0")
        depends_on("umpire@2024.07.0 ~examples", when="@1.2.7.0,2025.07.0")
        depends_on("umpire+rocm")
        for arch in ROCmPackage.amdgpu_targets:
            depends_on(f"umpire amdgpu_target={arch}", when=f"amdgpu_target={arch}")

    depends_on("raja+openmp", when="+openmp")
    depends_on("raja~openmp", when="~openmp")

    depends_on("raja+cuda", when="+cuda")
    depends_on("raja~cuda", when="~cuda")
    with when("+cuda"):
        for sm_ in CudaPackage.cuda_arch_values:
            depends_on(f"raja cuda_arch={sm_}", when=f"cuda_arch={sm_}")

    depends_on("raja+rocm", when="+rocm")
    depends_on("raja~rocm", when="~rocm")
    with when("+rocm"):
        for arch in ROCmPackage.amdgpu_targets:
            depends_on(f"raja amdgpu_target={arch}", when=f"amdgpu_target={arch}")

    # googletest folder version hasn't been updated in over 5 years
    # and is commented out in later releases
    patch("001-remove-googletest-from-cmake.patch", when="@1.2.5:1.2.6")

    def setup_build_environment(self, env):
        spec = self.spec
        if "+cuda" in spec:
            if "+mpi" in spec:
                env.set("CUDAHOSTCXX", self.spec["mpi"].mpicxx)
            else:
                env.set("CUDAHOSTCXX", self.compiler.cxx)

    def setup_run_environment(self, env):
        super().setup_run_environment(env)

        if self.compiler.extra_rpaths:
            for rpath in self.compiler.extra_rpaths:
                env.prepend_path("LD_LIBRARY_PATH", rpath)

    def cmake_args(self):
        spec = self.spec
        args = []
        if spec.satisfies("@develop") or spec.satisfies("@1.2.8"):
            blt_cxx_std = "c++20"
        elif spec.satisfies("@2025.12.0"):
            blt_cxx_std = "c++17"
        elif spec.satisfies("@:2025.7.0"):
            blt_cxx_std = "c++14"

        args.extend(
            [
                "-Dcamp_DIR=%s" % self.spec["raja"]["camp"].prefix,
                "-DBLT_SOURCE_DIR=%s" % self.spec["blt"].prefix,
                "-DRAJA_DIR=%s" % self.spec["raja"].prefix,
                "-DBLT_CXX_STD=%s" % blt_cxx_std,
            ]
        )

        args.append(self.define_from_variant("ENABLE_CHAI", "chai"))
        if "+chai" in spec:
            args.extend(
                [
                    "-Dchai_DIR=%s" % self.spec["chai"].prefix,
                    "-Dumpire_DIR=%s" % self.spec["umpire"].prefix + "/lib64/cmake/umpire",
                ]
            )

        args.append(self.define_from_variant("ENABLE_GPU_AWARE_MPI", "gpu-aware-mpi"))
        if "+gpu-aware-mpi" in spec:
            args.append(
                self.define_from_variant(
                    "ENABLE_DIRECT_UMPIRE_PLANE_STORAGE", "direct-device-plane"
                )
            )
        args.append(self.define_from_variant("ENABLE_OPENMP", "openmp"))
        args.append(self.define_from_variant("ENABLE_CALIPER", "caliper"))

        args.append(self.define_from_variant("ENABLE_MPI", "mpi"))
        if "+mpi" in spec:
            args.append(self.define("CMAKE_CXX_COMPILER", self.spec["mpi"].mpicxx))
            args.append("-DMPI_CXX_LINK_FLAGS='%s'" % self.spec["mpi"].libs.ld_flags)

        args.append(self.define_from_variant("ENABLE_HIP", "rocm"))
        if "+rocm" in spec:
            # Set up the hip macros needed by the build
            args.append("-Dumpire_DIR=%s" % self.spec["umpire"].prefix + "/lib64/cmake/umpire")
            args.append("-DHIP_ROOT_DIR={0}".format(spec["hip"].prefix))
            rocm_archs = spec.variants["amdgpu_target"].value
            if "none" not in rocm_archs:
                arch_str = ",".join(rocm_archs)
                args.append(f"-DHIP_HIPCC_FLAGS=--amdgpu-target={arch_str}")
                args.append(f"-DCMAKE_HIP_ARCHITECTURES={arch_str}")

        args.append(self.define_from_variant("ENABLE_CUDA", "cuda"))
        if "+cuda" in spec:
            args.append("-Dumpire_DIR=%s" % self.spec["umpire"].prefix + "/lib64/cmake/umpire")
            if "+mpi" in spec:
                args.append(self.define("CMAKE_CUDA_HOST_COMPILER", self.spec["mpi"].mpicxx))
            else:
                args.append(self.define("CMAKE_CUDA_HOST_COMPILER", self.compiler.cxx))
            if not spec.satisfies("cuda_arch=none"):
                cuda_arch = spec.variants["cuda_arch"].value
                args.append(f"-DCUDA_ARCH={cuda_arch[0]}")
                args.append(f"-DCMAKE_CUDA_ARCHITECTURES={cuda_arch[0]}")
            if "+mpi" in spec:
                args.append(
                    "-DCMAKE_CUDA_FLAGS=--extended-lambda -I=%s"
                    % (self.spec["mpi"].prefix.include)
                )

        return args

    def install(self, spec, prefix):
        # Kripke does not provide install target, so we have to copy
        # things into place.
        mkdirp(prefix.bin)
        if spec.satisfies("@:1.2.4") or spec.satisfies("@1.2.7:"):
            install(join_path(self.build_directory, "kripke.exe"), prefix.bin)
        else:
            install(join_path(self.build_directory, "bin", "kripke.exe"), prefix.bin)
