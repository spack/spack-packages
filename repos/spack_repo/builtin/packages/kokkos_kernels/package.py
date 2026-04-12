# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage

from spack.package import *


class KokkosKernels(CMakePackage, CudaPackage):
    """Kokkos Kernels provides math kernels, often BLAS or LAPACK
    for small matrices, that can be used in larger Kokkos parallel routines"""

    homepage = "https://github.com/kokkos/kokkos-kernels"
    git = "https://github.com/kokkos/kokkos-kernels.git"
    url = "https://github.com/kokkos/kokkos-kernels/releases/download/4.4.01/kokkos-kernels-4.4.01.tar.gz"

    tags = ["e4s"]

    test_requires_compiler = True

    maintainers("lucbv", "srajama1", "brian-kelley")

    license("Apache-2.0 WITH LLVM-exception")

    version("develop", branch="develop")

    version("5.0.2", sha256="7c7af2c3659ecc620cc7b7016876330d9f288e8c6fd7b70b70907687df823b43")
    version("5.0.1", sha256="c9d0b507ab754b347b71b530683e9dea8dbf4d2e3cdadb863dcb494b07bbf0b2")
    version("5.0.0", sha256="e1d7e7040b86f141004126c3fa5711f28697803d921c3558d82192a32156b1b2")
    version("4.7.03", sha256="902701e3481b2c535925a02e0918baed6f82186a25297e45314712b0905d9780")
    version("4.7.02", sha256="2d3b3e10ac112e382b88c50d66e4222ce543fca5d42be6d8376a684b82b8b238")
    version("4.7.01", sha256="f3e1452db0e182c8e32c61632465e3a829159b9ae0645d9e4cd97b4fa09c36e1")
    version("4.7.00", sha256="5c7c8c8f91817ab22dbc50ea72f02292bbd6c5b412d6f1588b27574600c478ef")
    version("4.6.02", sha256="a953f445660ed5aaab10e18fc4a90c4c178291e9d9d97d20abd4e6027f1193ec")
    version("4.6.01", sha256="95b9357f37ab3b9c3913c00741acb2501831c28ea8664de67818ae79c69c5908")
    version("4.6.00", sha256="f2b18f3df78c3c8dd970fe8ead54e05c8c09c8ac6d1893655c2a1769d33aa364")
    version("4.5.01", sha256="c111a6561f23a85af9850d1df1e9015f37a586f1da0be4b6fb1e98001d75e074")
    version("4.5.00", sha256="94726a64e349adf6cd276e9fdc1b2bf7ff81efec833e479a5d3024b83f165a59")
    version("4.4.01", sha256="4a32bc8330e0113856bdf181df94cc4f9902e3cebb5dc7cea5948f30df03bfa1")
    version("4.4.00", sha256="66d5c3f728a8c7689159c97006996164ea00fd39702476220e3dbf2a05c49e8f")
    version(
        "4.3.01",
        sha256="749553a6ea715ba1e56fa0b13b42866bb9880dba7a94e343eadf40d08c68fab8",
        url="https://github.com/kokkos/kokkos-kernels/archive/4.3.01.tar.gz",
    )
    version(
        "4.3.00",
        sha256="03c3226ee97dbca4fa56fe69bc4eefa0673e23c37f2741943d9362424a63950e",
        url="https://github.com/kokkos/kokkos-kernels/archive/4.3.00.tar.gz",
    )
    version(
        "4.2.01",
        sha256="058052b3a40f5d4e447b7ded5c480f1b0d4aa78373b0bc7e43804d0447c34ca8",
        url="https://github.com/kokkos/kokkos-kernels/archive/4.2.01.tar.gz",
    )
    version(
        "4.2.00",
        sha256="c65df9a101dbbef2d8fd43c60c9ea85f2046bb3535fa1ad16e7c661ddd60401e",
        url="https://github.com/kokkos/kokkos-kernels/archive/4.2.00.tar.gz",
    )
    version(
        "4.1.00",
        sha256="d6a4108444ea226e43bf6a9c0dfc557f223a72b1142bf81aa78dd60e16ac2d56",
        url="https://github.com/kokkos/kokkos-kernels/archive/4.1.00.tar.gz",
    )
    version(
        "4.0.01",
        sha256="3f493fcb0244b26858ceb911be64092fbf7785616ad62c81abde0ea1ce86688a",
        url="https://github.com/kokkos/kokkos-kernels/archive/4.0.01.tar.gz",
    )
    version(
        "4.0.00",
        sha256="750079d0be1282d18ecd280e130ca303044ac399f1e5864488284b92f5ce0a86",
        url="https://github.com/kokkos/kokkos-kernels/archive/4.0.00.tar.gz",
    )
    version(
        "3.7.02",
        sha256="43b1d4f726bccd8d7d632ae8b81c8edc7d7afa347fbab0654f7ca0c664edf05c",
        url="https://github.com/kokkos/kokkos-kernels/archive/3.7.02.tar.gz",
    )

    variant("shared", default=True, description="Build shared libraries")
    variant(
        "execspace_cuda",
        default=False,
        description="Whether to pre instantiate kernels for the execution space Kokkos::Cuda",
    )
    variant(
        "execspace_openmp",
        default=False,
        description="Whether to pre instantiate kernels for the execution space "
        "Kokkos::Experimental::OpenMPTarget",
    )
    variant(
        "execspace_threads",
        default=False,
        description="Whether to pre instantiate kernels for the execution space Kokkos::Threads",
    )
    variant(
        "execspace_serial",
        default=False,
        description="Whether to pre instantiate kernels for the execution space Kokkos::Serial",
    )
    variant(
        "memspace_cudauvmspace",
        default=False,
        description="Whether to pre instantiate kernels for the memory space Kokkos::CudaUVMSpace",
    )
    variant(
        "memspace_cudaspace",
        default=False,
        description="Whether to pre instantiate kernels for the memory space Kokkos::CudaSpace",
    )
    variant("serial", default=False, description="Enable serial backend")
    variant("openmp", default=False, description="Enable OpenMP backend")
    variant("threads", default=False, description="Enable C++ threads backend")
    variant(
        "ordinals", default="int", values=["int", "int64_t"], multi=True, description="Ordinals"
    )
    variant(
        "offsets",
        default="int,size_t",
        values=["int", "size_t"],
        multi=True,
        description="Offsets",
    )
    variant("layouts", default="left", values=["left", "right"], description="Layouts")
    variant(
        "scalars",
        default="double",
        values=["float", "double", "complex_float", "complex_double"],
        multi=True,
        description="Scalars",
    )

    depends_on("cxx", type="build")
    for tpl in ("blas", "mkl"):
        depends_on("c", type="build", when=f"+{tpl}")
        depends_on("fortran", type="build", when=f"+{tpl}")
    depends_on("kokkos")
    depends_on("kokkos@develop", when="@develop")
    depends_on("kokkos@5.0.2", when="@5.0.2")
    depends_on("kokkos@5.0.1", when="@5.0.1")
    depends_on("kokkos@5.0.0", when="@5.0.0")
    depends_on("kokkos@4.7.03", when="@4.7.03")
    depends_on("kokkos@4.7.02", when="@4.7.02")
    depends_on("kokkos@4.7.01", when="@4.7.01")
    depends_on("kokkos@4.7.00", when="@4.7.00")
    depends_on("kokkos@4.6.02", when="@4.6.02")
    depends_on("kokkos@4.6.01", when="@4.6.01")
    depends_on("kokkos@4.6.00", when="@4.6.00")
    depends_on("kokkos@4.5.01", when="@4.5.01")
    depends_on("kokkos@4.5.00", when="@4.5.00")
    depends_on("kokkos@4.4.01", when="@4.4.01")
    depends_on("kokkos@4.4.00", when="@4.4.00")
    depends_on("kokkos@4.3.01", when="@4.3.01")
    depends_on("kokkos@4.3.00", when="@4.3.00")
    depends_on("kokkos@4.2.01", when="@4.2.01")
    depends_on("kokkos@4.2.00", when="@4.2.00")
    depends_on("kokkos@4.1.00", when="@4.1.00")
    depends_on("kokkos@4.0.01", when="@4.0.01")
    depends_on("kokkos@4.0.00", when="@4.0.00")
    depends_on("kokkos@3.7.02", when="@3.7.02")
    depends_on("kokkos+pic", when="+shared")
    depends_on("kokkos+cuda", when="+execspace_cuda")
    depends_on("kokkos+openmp", when="+execspace_openmp")
    depends_on("kokkos+threads", when="+execspace_threads")
    depends_on("kokkos+serial", when="+execspace_serial")
    depends_on("kokkos+cuda", when="+memspace_cudauvmspace")
    depends_on("kokkos+cuda", when="+memspace_cudaspace")
    depends_on("kokkos+serial", when="+serial")
    depends_on("kokkos+cuda", when="+cuda")
    depends_on("kokkos+openmp", when="+openmp")
    depends_on("kokkos+threads", when="+threads")
    depends_on("kokkos+cuda_lambda", when="@4+cuda")
    depends_on("cmake@3.16:", type="build")

    tpls = {
        # variant name   #deflt   #spack name  #root var name  #supporting versions  #docstring
        "blas": (False, "blas", "BLAS", "@3.0.00:", "Link to system BLAS"),
        "lapack": (False, "lapack", "LAPACK", "@3.0.00:", "Link to system LAPACK"),
        "mkl": (False, "mkl", "MKL", "@3.0.00:", "Link to system MKL"),
        "cublas": (False, "cuda", None, "@3.0.00:", "Link to CUDA BLAS library"),
        "cusparse": (False, "cuda", None, "@3.0.00:", "Link to CUDA sparse library"),
        "superlu": (False, "superlu", "SUPERLU", "@3.1.00:", "Link to SuperLU library"),
        "cblas": (False, "cblas", "CBLAS", "@3.1.00:", "Link to CBLAS library"),
        "lapacke": (False, "clapack", "LAPACKE", "@3.1.00:", "Link to LAPACKE library"),
        "rocblas": (False, "rocblas", "ROCBLAS", "@3.6.00:", "Link to AMD BLAS library"),
        "rocsparse": (False, "rocsparse", "ROCSPARSE", "@3.6.00:", "Link to AMD sparse library"),
        "cusolver": (False, "cuda", None, "@4.3.00:", "Link to CUDA solver library"),
        "rocsolver": (False, "rocsolver", "ROCSOLVER", "@4.3.00:", "Link to AMD solver library"),
    }

    for tpl in tpls:
        deflt_bool, spackname, rootname, condition, descr = tpls[tpl]
        variant(tpl, default=deflt_bool, when=f"{condition}", description=descr)
        depends_on(spackname, when=f"+{tpl}")

    # lapack TPL depends on blas TPL
    conflicts("+lapack", when="~blas")

    patch("pr_2296_430.patch", when="@4.3.00:4.4.00")
    patch("pr_2296_400.patch", when="@4.0.00:4.2.01")

    # sanity check
    sanity_check_is_file = [join_path("include", "KokkosKernels_config.h")]
    sanity_check_is_dir = ["include"]

    def cmake_args(self):
        spec = self.spec
        options = [
            self.define_from_variant("KokkosKernels_INST_EXECSPACE_CUDA", "execspace_cuda"),
            self.define_from_variant("KokkosKernels_INST_EXECSPACE_OPENMP", "execspace_openmp"),
            self.define_from_variant("KokkosKernels_INST_EXECSPACE_THREADS", "execspace_threads"),
            self.define_from_variant("KokkosKernels_INST_EXECSPACE_SERIAL", "execspace_serial"),
            self.define_from_variant("KokkosKernels_INST_EXECSPACE_SERIAL", "execspace_serial"),
            self.define_from_variant(
                "KokkosKernels_INST_MEMSPACE_CUDAUVMSPACE", "memspace_cudauvmspace"
            ),
            self.define_from_variant(
                "KokkosKernels_INST_MEMSPACE_CUDASPACE", "memspace_cudaspace"
            ),
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
        ]

        options.append(self.define("Kokkos_ROOT", spec["kokkos"].prefix))
        if spec.satisfies("^kokkos+rocm") and not (
            spec.satisfies("^kokkos %cxx=clang") or spec.satisfies("^kokkos %cxx=rocmcc")
        ):
            options.append(self.define("CMAKE_CXX_COMPILER", spec["hip"].hipcc))
        else:
            options.append(self.define("CMAKE_CXX_COMPILER", self["kokkos"].kokkos_cxx))

        if self.run_tests:
            options.append(self.define("KokkosKernels_ENABLE_TESTS", True))

        for tpl in self.tpls:
            dflt, spackname, rootname, condition, descr = self.tpls[tpl]
            if spec.satisfies(f"+{tpl}"):
                options.append(self.define(f"KokkosKernels_ENABLE_TPL_{tpl.upper()}", True))
                if rootname:
                    options.append(self.define(f"{rootname}_ROOT", spec[spackname].prefix))
                else:
                    pass

        for val in spec.variants["ordinals"].value:
            options.append(self.define(f"KokkosKernels_INST_ORDINAL_{val.upper()}", True))
        for val in spec.variants["offsets"].value:
            options.append(self.define(f"KokkosKernels_INST_OFFSET_{val.upper()}", True))
        for val in spec.variants["scalars"].value:
            options.append(self.define(f"KokkosKernels_INST_{val.upper()}", True))
        layout_value = spec.variants["layouts"].value
        options.append(self.define(f"KokkosKernels_INST_LAYOUT{layout_value.upper()}", True))

        return options
