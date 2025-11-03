# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
from itertools import product

from spack_repo.builtin.build_systems.autotools import AutotoolsBuilder, AutotoolsPackage
from spack_repo.builtin.build_systems.cmake import CMakeBuilder, CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Hypre(CMakePackage, AutotoolsPackage, CudaPackage, ROCmPackage):
    """Hypre is a library of high performance preconditioners that
    features parallel multigrid methods for both structured and
    unstructured grid problems."""

    homepage = "https://llnl.gov/casc/hypre"
    url = "https://github.com/hypre-space/hypre/archive/v2.14.0.tar.gz"
    git = "https://github.com/hypre-space/hypre.git"
    tags = ["e4s", "radiuss"]

    maintainers("victorapm", "rfalgout", "oseikuffuor1", "liruipeng", "waynemitchell", "balay")

    test_requires_compiler = True

    # License
    license("Apache-2.0 OR MIT")

    # Support both CMake and Autotools. CMake is available and default only for v3+.
    build_system(conditional("cmake", when="@3:"), "autotools", default="cmake")

    # Package versions
    version("develop", branch="master")
    version("3.0.0", sha256="d9dbfa34ebd07af1641f04b06338c7808b1f378e2d7d5d547514db9f11dffc26")
    version("2.33.0", sha256="0f9103c34bce7a5dcbdb79a502720fc8aab4db9fd0146e0791cde7ec878f27da")
    version("2.32.0", sha256="2277b6f01de4a7d0b01cfe12615255d9640eaa02268565a7ce1a769beab25fa1")
    version("2.31.0", sha256="9a7916e2ac6615399de5010eb39c604417bb3ea3109ac90e199c5c63b0cb4334")
    version("2.30.0", sha256="8e2af97d9a25bf44801c6427779f823ebc6f306438066bba7fcbc2a5f9b78421")
    version("2.29.0", sha256="98b72115407a0e24dbaac70eccae0da3465f8f999318b2c9241631133f42d511")
    version("2.28.0", sha256="2eea68740cdbc0b49a5e428f06ad7af861d1e169ce6a12d2cf0aa2fc28c4a2ae")
    version("2.27.0", sha256="507a3d036bb1ac21a55685ae417d769dd02009bde7e09785d0ae7446b4ae1f98")
    version("2.26.0", sha256="c214084bddc61a06f3758d82947f7f831e76d7e3edeac2c78bb82d597686e05d")
    version("2.25.0", sha256="f9fc8371d91239fca694284dab17175bfda3821d7b7a871fd2e8f9d5930f303c")
    version("2.24.0", sha256="f480e61fc25bf533fc201fdf79ec440be79bb8117650627d1f25151e8be2fdb5")
    version("2.23.0", sha256="8a9f9fb6f65531b77e4c319bf35bfc9d34bf529c36afe08837f56b635ac052e2")
    version("2.22.1", sha256="c1e7761b907c2ee0098091b69797e9be977bff8b7fd0479dc20cad42f45c4084")
    version("2.22.0", sha256="2c786eb5d3e722d8d7b40254f138bef4565b2d4724041e56a8fa073bda5cfbb5")
    version("2.21.0", sha256="e380f914fe7efe22afc44cdf553255410dc8a02a15b2e5ebd279ba88817feaf5")
    version("2.20.0", sha256="5be77b28ddf945c92cde4b52a272d16fb5e9a7dc05e714fc5765948cba802c01")
    version("2.19.0", sha256="466b19d8a86c69989a237f6f03f20d35c0c63a818776d2cd071b0a084cffeba5")
    version("2.18.2", sha256="28007b5b584eaf9397f933032d8367788707a2d356d78e47b99e551ab10cc76a")
    version("2.18.1", sha256="220f9c4ad024e815add8dad8950eaa2d8f4f231104788cf2a3c5d9da8f94ba6e")
    version("2.18.0", sha256="62591ac69f9cc9728bd6d952b65bcadd2dfe52b521081612609804a413f49b07")
    version("2.17.0", sha256="4674f938743aa29eb4d775211b13b089b9de84bfe5e9ea00c7d8782ed84a46d7")
    version("2.16.0", sha256="33f8a27041e697343b820d0426e74694670f955e21bbf3fcb07ee95b22c59e90")
    version("2.15.1", sha256="50d0c0c86b4baad227aa9bdfda4297acafc64c3c7256c27351f8bae1ae6f2402")
    version("2.15.0", sha256="2d597472b473964210ca9368b2cb027510fff4fa2193a8c04445e2ed4ff63045")
    version("2.14.0", sha256="705a0c67c68936bb011c50e7aa8d7d8b9693665a9709b584275ec3782e03ee8c")
    version("2.13.0", sha256="3979602689c3b6e491c7cf4b219cfe96df5a6cd69a5302ccaa8a95ab19064bad")
    version("2.12.1", sha256="824841a60b14167a0051b68fdb4e362e0207282348128c9d0ca0fd2c9848785c")
    version("2.11.2", sha256="25b6c1226411593f71bb5cf3891431afaa8c3fd487bdfe4faeeb55c6fdfb269e")
    version("2.11.1", sha256="6bb2ff565ff694596d0e94d0a75f0c3a2cd6715b8b7652bc71feb8698554db93")
    version("2.10.1", sha256="a4a9df645ebdc11e86221b794b276d1e17974887ead161d5050aaf0b43bb183a")
    version("2.10.0b", sha256="b55dbdc692afe5a00490d1ea1c38dd908dae244f7bdd7faaf711680059824c11")

    variant("shared", default=False, description="Build shared library (disables static library)")
    variant(
        "pic", default=True, when="@2.21: ~shared", description="Build position independent code"
    )
    # Use internal SuperLU routines for FEI - version 2.12.1 and below
    variant(
        "internal-superlu",
        default=False,
        when="@:2.12.1",
        description="Use internal SuperLU routines",
    )
    variant(
        "superlu-dist",
        default=False,
        when="@2.13:",
        description="Activates support for SuperLU_Dist library",
    )
    variant("lapack", default=True, description="Use external blas/lapack")
    variant("int64", default=False, description="Use 64bit integers")
    variant(
        "mixedint",
        default=False,
        when="@2.16:",
        description="Use 64bit integers while reducing memory use",
    )
    variant("complex", default=False, description="Use complex values")
    variant(
        "gpu-aware-mpi", default=False, when="@2.18:", description="Enable GPU-aware MPI support"
    )
    variant(
        "gpu-profiling",
        default=False,
        when="@2.21:",
        description="Enable GPU profiling markers support",
    )
    variant("mpi", default=True, description="Enable MPI support")
    variant("openmp", default=False, description="Enable OpenMP support")
    variant("debug", default=False, description="Build debug instead of optimized version")
    variant("unified-memory", default=False, description="Use unified memory")
    variant("fortran", default=False, description="Enables fortran bindings")
    variant("gptune", default=False, description="Add the GPTune hookup code")
    variant("umpire", default=False, when="@2.21:", description="Enable Umpire support")
    variant("sycl", default=False, when="@2.24:", description="Enable SYCL support")
    variant("magma", default=False, when="@2.29:", description="Enable MAGMA interface")
    variant("caliper", default=False, description="Enable Caliper support")
    variant(
        "precision",
        default="double",
        values=("single", "double", "longdouble", conditional("mixed", when="@3:")),
        multi=False,
        when="@2.12.1:",
        description="Floating point precision",
    )
    variant(
        "cxxstd",
        default="17",
        values=("11", "14", "17", "20", "23"),
        multi=False,
        description="C++ language standard (for GPU builds)",
    )

    # Patch to fix hip build (+rocm) via CMake for hypre v3.0.0
    patch(
        "https://github.com/hypre-space/hypre/pull/1394.patch?full_index=1",
        sha256="c9a98fb6aa6469c830fa7c12548c3be532d54bee5b7841e1550370ef497c5490",
        when="@3.0.0 +rocm",
    )

    # Patch to add gptune hookup codes
    patch("ij_gptune.patch", when="+gptune@2.19.0")

    # Patch to add ppc64le in config.guess
    patch("ibm-ppc64le.patch", when="@:2.11.1")

    # Patch to build shared libraries on Darwin
    patch("darwin-shared-libs-for-hypre-2.13.0.patch", when="+shared@2.13.0 platform=darwin")
    patch("darwin-shared-libs-for-hypre-2.14.0.patch", when="+shared@2.14.0 platform=darwin")
    patch("superlu-dist-link-2.15.0.patch", when="+superlu-dist @2.15:2.16.0")
    patch("superlu-dist-link-2.14.0.patch", when="+superlu-dist @:2.14.0")
    patch("hypre21800-compat.patch", when="@2.18.0")
    # Patch to get config flags right
    patch("detect-compiler.patch", when="@2.15.0:2.20.0")
    # The following patch may not work for all versions, so apply it only when
    # it is needed:
    patch("hypre-precision-fix.patch", when="precision=single")
    patch("hypre-precision-fix.patch", when="precision=longdouble")

    @when("@2.26.0")
    def patch(self):  # fix sequential compilation in 'src/seq_mv'
        filter_file("\tmake", "\t$(MAKE)", "src/seq_mv/Makefile")

    # Compiler dependencies
    depends_on("c", type="build")
    depends_on("cxx", type="build", when="+cuda")
    depends_on("cxx", type="build", when="+rocm")
    depends_on("cxx", type="build", when="+sycl")
    depends_on("fortran", type="build", when="+fortran")

    # If using CMake, we require at least the following version
    with when("build_system=cmake"):
        depends_on("cmake@3.21:", type="build")

    # General dependencies and conflicts
    depends_on("mpi", when="+mpi")
    depends_on("blas", when="+lapack")
    depends_on("lapack", when="+lapack")
    depends_on("magma", when="+magma")
    depends_on("superlu-dist", when="+superlu-dist+mpi")
    depends_on("caliper", when="+caliper")
    conflicts("+gptune", when="~mpi")

    # Patch to build shared libraries on Darwin does not apply to
    # versions before 2.13.0
    conflicts("+shared@:2.12 platform=darwin")

    # GPU-related dependencies and conflicts
    gpu_pkgs = ["magma", "umpire"]
    conflicts("+unified-memory", when="~cuda~rocm~sycl")
    conflicts("+gpu-profiling", when="~cuda~rocm~sycl")
    conflicts("+gpu-aware-mpi", when="~cuda~rocm~sycl")
    with when("+cuda"):
        depends_on("umpire+c+cuda", when="@3:")

        conflicts("@:2.18")
        conflicts("cuda_arch=none")
        conflicts("precision=longdouble")
        conflicts("precision=mixed")
        conflicts("+shared +umpire")
        conflicts("+int64", msg="Use +mixedint for 64-bit integer support for GPUs!")
        conflicts("+rocm", msg="CUDA and ROCm are mutually exclusive")
        conflicts("+sycl", msg="CUDA and SYCL are mutually exclusive")
        conflicts("cxxstd=11", when="^cuda@13:")
        conflicts("cxxstd=14", when="^cuda@13:")
        depends_on("cuda@:11", when="@:2.28.0")
        for pkg, sm_ in product(gpu_pkgs, CudaPackage.cuda_arch_values):
            requires(f"^{pkg} cuda_arch={sm_}", when=f"+{pkg} cuda_arch={sm_}")

    with when("+rocm"):
        depends_on("umpire+c+rocm", when="@3:")
        depends_on("rocsparse")
        depends_on("rocthrust")
        depends_on("rocrand")
        depends_on("rocprim")
        depends_on("rocsolver", when="@2.29.0:")
        depends_on("rocblas", when="@2.29.0:")
        depends_on("hipblas", when="+superlu-dist")
        depends_on("hip@:6", when="@:3.0.0")

        conflicts("@:2.20")
        conflicts("amdgpu_target=none")
        conflicts("precision=longdouble")
        conflicts("precision=mixed")
        conflicts("+int64", msg="Use +mixedint for 64-bit integer support for GPUs!")
        conflicts("+sycl", msg="ROCm and SYCL are mutually exclusive")
        conflicts("cxxstd=11", when="^hip@7:")
        conflicts("cxxstd=14", when="^hip@7:")
        for pkg, gfx in product(gpu_pkgs, ROCmPackage.amdgpu_targets):
            requires(f"^{pkg} amdgpu_target={gfx}", when=f"+{pkg} amdgpu_target={gfx}")

    with when("+sycl"):
        requires("%c,cxx=oneapi", msg="SYCL backend must be compiled with oneapi compilers")

        depends_on("intel-oneapi-compilers")
        depends_on("intel-oneapi-mkl")
        depends_on("intel-oneapi-dpl")

        conflicts("precision=longdouble")
        conflicts("precision=mixed")
        conflicts("+int64", msg="Use +mixedint for 64-bit integer support for GPUs!")
        conflicts("+gpu-profiling", msg="GPU profiling not available for SYCL!")

    def url_for_version(self, version):
        if version >= Version("2.12.0"):
            url = f"https://github.com/hypre-space/hypre/archive/v{version}.tar.gz"
        else:
            url = (
                f"http://computing.llnl.gov/project/linear_solvers/download/hypre-{version}.tar.gz"
            )

        return url

    # build/install phases are implemented in the AutotoolsBuilder
    extra_install_tests = join_path("src", "examples")

    @run_after("install")
    def cache_test_sources(self):
        cache_extra_test_sources(self, self.extra_install_tests)

        # Customize the makefile to use the installed package
        makefile = join_path(install_test_root(self), self.extra_install_tests, "Makefile")
        filter_file(r"^HYPRE_DIR\s* =.*", f"HYPRE_DIR = {self.prefix}", makefile)
        filter_file(r"^CC\s*=.*", f"CC = {os.environ['CC']}", makefile)
        if "cxx" in self.spec:
            filter_file(r"^CXX\s*=.*", f"CXX = {os.environ['CXX']}", makefile)
        if self.spec.satisfies("+fortran"):
            filter_file(r"^F77\s*=.*", f"F77 = {os.environ['F77']}", makefile)

    @property
    def _cached_tests_work_dir(self):
        """The working directory for cached test sources."""
        return join_path(self.test_suite.current_test_cache_dir, self.extra_install_tests)

    def test_bigint(self):
        """build and run bigint tests"""
        if self.spec.satisfies("~mpi"):
            raise SkipTest("Package must be installed with +mpi")

        # build and run cached examples
        with working_dir(self._cached_tests_work_dir):
            make = which("make")
            make("bigint")

            for name in ["ex5big", "ex15big"]:
                with test_part(self, f"test_bigint_{name}", f"ensure {name} runs"):
                    exe = which(name)
                    if exe is None:
                        raise SkipTest(f"{name} does not exist in version {self.version}")
                    exe()

    @property
    def headers(self):
        """Export the main hypre header, HYPRE.h; all other headers can be found
        in the same directory.
        Sample usage: spec['hypre'].headers.cpp_flags
        """
        hdrs = find_headers("HYPRE", self.prefix.include, recursive=False)
        return hdrs or None

    @property
    def libs(self):
        """Export the hypre library.
        Sample usage: spec['hypre'].libs.ld_flags
        """
        is_shared = self.spec.satisfies("+shared")
        libs = find_libraries("libHYPRE", root=self.prefix, shared=is_shared, recursive=True)
        return libs or None


# Builder implementations
class CMakeBuilder(CMakeBuilder):
    root_cmakelists_dir = "src"

    def cmake_args(self):
        pkg = self.pkg
        spec = pkg.spec
        args = []

        # Library toggles
        args.append(self.define_from_variant("BUILD_SHARED_LIBS", "shared"))
        args.append(self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"))
        args.append(self.define_from_variant("CMAKE_POSITION_INDEPENDENT_CODE", "pic"))
        if spec.satisfies("+complex %gcc@14:"):
            args.append(self.define("CMAKE_C_FLAGS", "-Wno-error=incompatible-pointer-types"))

        # Core toggles
        args.append(self.define_from_variant("HYPRE_ENABLE_MPI", "mpi"))
        args.append(self.define_from_variant("HYPRE_ENABLE_OPENMP", "openmp"))
        args.append(self.define_from_variant("HYPRE_ENABLE_FORTRAN", "fortran"))
        args.append(self.define_from_variant("HYPRE_ENABLE_COMPLEX", "complex"))
        args.append(self.define_from_variant("HYPRE_ENABLE_BIGINT", "int64"))
        args.append(self.define_from_variant("HYPRE_ENABLE_MIXEDINT", "mixedint"))

        # Floating point precision
        args.append(self.define("HYPRE_ENABLE_SINGLE", spec.satisfies("precision=single")))
        args.append(
            self.define("HYPRE_ENABLE_LONG_DOUBLE", spec.satisfies("precision=longdouble"))
        )
        args.append(self.define("HYPRE_ENABLE_MIXED_PRECISION", spec.satisfies("precision=mixed")))

        # External BLAS/LAPACK when +lapack (Note +lapack works for blas as well)
        args.append(self.define_from_variant("HYPRE_ENABLE_HYPRE_BLAS", "lapack"))
        args.append(self.define_from_variant("HYPRE_ENABLE_HYPRE_LAPACK", "lapack"))

        # GPU backends
        args.append(self.define_from_variant("HYPRE_ENABLE_CUDA", "cuda"))
        args.append(self.define_from_variant("HYPRE_ENABLE_HIP", "rocm"))
        args.append(self.define_from_variant("HYPRE_ENABLE_SYCL", "sycl"))
        if spec.satisfies("+cuda"):
            args.append(self.define("CUDAToolkit_ROOT", self.spec["cuda"].prefix))

        # GPU auxiliary options
        args.append(self.define_from_variant("HYPRE_ENABLE_GPU_AWARE_MPI", "gpu-aware-mpi"))
        args.append(self.define_from_variant("HYPRE_ENABLE_GPU_PROFILING", "gpu-profiling"))
        args.append(self.define_from_variant("HYPRE_ENABLE_UNIFIED_MEMORY", "unified-memory"))

        # TPLs
        args.append(self.define_from_variant("HYPRE_ENABLE_UMPIRE", "umpire"))
        args.append(self.define_from_variant("HYPRE_ENABLE_CALIPER", "caliper"))
        args.append(self.define_from_variant("HYPRE_ENABLE_DSUPERLU", "superlu-dist"))
        args.append(self.define_from_variant("HYPRE_ENABLE_MAGMA", "magma"))

        # GPU architectures
        cuda_arch_vals = spec.variants.get("cuda_arch", None)
        if cuda_arch_vals and cuda_arch_vals.value:
            arch_list = sorted(list(cuda_arch_vals.value))
            args.append(self.define("CMAKE_CUDA_ARCHITECTURES", ";".join(arch_list)))

        amdgpu_vals = spec.variants.get("amdgpu_target", None)
        if amdgpu_vals and amdgpu_vals.value:
            gfx_list = sorted(list(amdgpu_vals.value))
            args.append(self.define("CMAKE_HIP_ARCHITECTURES", ";".join(gfx_list)))

        return args


class AutotoolsBuilder(AutotoolsBuilder):
    configure_directory = "src"

    def configure_args(self):
        pkg = self.pkg
        spec = pkg.spec
        configure_args = [f"--prefix={pkg.prefix}"]

        # Note: --with-(lapack|blas)_libs= needs space separated list of names
        if spec.satisfies("+lapack"):
            configure_args.append("--with-lapack")
            configure_args.append("--with-blas")
            configure_args.append("--with-lapack-libs=%s" % " ".join(spec["lapack"].libs.names))
            configure_args.append("--with-blas-libs=%s" % " ".join(spec["blas"].libs.names))
            configure_args.append(
                "--with-lapack-lib-dirs=%s" % " ".join(spec["lapack"].libs.directories)
            )
            configure_args.append(
                "--with-blas-lib-dirs=%s" % " ".join(spec["blas"].libs.directories)
            )

        if spec.satisfies("+mpi"):
            os.environ["CC"] = spec["mpi"].mpicc
            os.environ["CXX"] = spec["mpi"].mpicxx
            if spec.satisfies("+fortran"):
                os.environ["F77"] = spec["mpi"].mpif77
                os.environ["FC"] = spec["mpi"].mpifc
            configure_args.append("--with-MPI")
            configure_args.append(f"--with-MPI-lib-dirs={spec['mpi'].prefix.lib}")
            configure_args.append(f"--with-MPI-include={spec['mpi'].prefix.include}")
        else:
            configure_args.append("--without-MPI")

        configure_args.extend(pkg.with_or_without("openmp"))

        if spec.satisfies("+int64"):
            configure_args.append("--enable-bigint")
        else:
            configure_args.append("--disable-bigint")

        configure_args.extend(pkg.enable_or_disable("debug"))
        configure_args.extend(pkg.enable_or_disable("mixedint"))
        configure_args.extend(pkg.enable_or_disable("complex"))
        configure_args.extend(pkg.enable_or_disable("shared"))
        configure_args.extend(pkg.enable_or_disable("unified-memory"))
        configure_args.extend(pkg.enable_or_disable("gpu-aware-mpi"))
        configure_args.extend(pkg.enable_or_disable("gpu-profiling"))
        configure_args.extend(pkg.enable_or_disable("fortran"))
        if spec.satisfies("+pic"):
            configure_args.append("--with-extra-CFLAGS=-fPIC")

        if spec.satisfies("+complex %gcc@14:"):
            configure_args.append("--with-extra-CFLAGS=-Wno-error=incompatible-pointer-types")

        if spec.satisfies("+cuda") or spec.satisfies("+rocm") or spec.satisfies("+sycl"):
            configure_args.append(f"--with-cxxstandard={self.spec.cxxstd}")
            if spec.satisfies("+pic"):
                configure_args.append("--with-extra-CXXFLAGS=-fPIC")

        if spec.satisfies("precision=single"):
            configure_args.append("--enable-single")
        elif spec.satisfies("precision=longdouble"):
            configure_args.append("--enable-longdouble")
        elif spec.satisfies("precision=mixed"):
            configure_args.append("--enable-mixed-precision")

        if spec.satisfies("~internal-superlu"):
            configure_args.append("--without-superlu")
            # MLI and FEI do not build without superlu on Linux
            configure_args.append("--without-mli")
            # FEI option was removed in hypre 2.17
            if pkg.version < Version("2.17.0"):
                configure_args.append("--without-fei")

        if spec.satisfies("+superlu-dist"):
            configure_args.append(
                "--with-dsuperlu-include=%s" % spec["superlu-dist"].prefix.include
            )
            configure_args.append("--with-dsuperlu-lib=%s" % spec["superlu-dist"].libs)
            configure_args.append("--with-dsuperlu")

        if spec.satisfies("+umpire"):
            configure_args.append("--with-umpire-include=%s" % spec["umpire"].prefix.include)
            configure_args.append("--with-umpire-lib-dirs=%s" % spec["umpire"].prefix.lib)
            configure_args.append("--with-umpire-libs=umpire camp")
            if spec.satisfies("~cuda~rocm"):
                configure_args.append("--with-umpire-host")
            else:
                configure_args.append("--with-umpire")
        else:
            configure_args.append("--without-umpire")

        if spec.satisfies("+caliper"):
            configure_args.append("--with-caliper")
            configure_args.append("--with-caliper-include=%s" % spec["caliper"].prefix.include)
            configure_args.append("--with-caliper-lib=%s" % spec["caliper"].libs)

        if spec.satisfies("+cuda"):
            configure_args.append(f"--with-cuda-home={spec['cuda'].prefix}")
            configure_args.extend(["--with-cuda", "--enable-curand", "--enable-cusparse"])
            cuda_arch_vals = spec.variants["cuda_arch"].value
            if cuda_arch_vals:
                cuda_arch_sorted = list(sorted(cuda_arch_vals, reverse=True))
                cuda_arch = cuda_arch_sorted[0]
                configure_args.append(f"--with-gpu-arch={cuda_arch}")
            # New in 2.21.0: replaces --enable-cub
            if spec.satisfies("@2.21.0: ~umpire"):
                configure_args.append("--enable-device-memory-pool")
            elif spec.satisfies("@:2.20.99"):
                configure_args.append("--enable-cub")
            if spec.satisfies("@2.29.0:"):
                configure_args.extend(["--enable-cublas", "--enable-cusolver"])
        else:
            configure_args.extend(["--without-cuda", "--disable-curand", "--disable-cusparse"])
            if spec.satisfies("@:2.20.99"):
                configure_args.append("--disable-cub")
            if spec.satisfies("@2.29:"):
                configure_args.append("--disable-cusolver")

        if spec.satisfies("+rocm"):
            configure_args.append("--with-hip")
            rocm_pkgs = ["rocthrust", "rocprim", "rocrand", "rocsparse"]
            if spec.satisfies("+superlu-dist"):
                rocm_pkgs.append("hipblas")
            if spec.satisfies("@2.29.0:"):
                rocm_pkgs.extend(["rocblas", "rocsolver"])
                configure_args.extend(["--enable-rocblas", "--enable-rocsolver"])
            rocm_inc = " ".join(set(spec[pkg_].headers.include_flags for pkg_ in rocm_pkgs))
            configure_args.extend(
                ["--enable-rocrand", "--enable-rocsparse", f"--with-extra-CUFLAGS={rocm_inc}"]
            )
            rocm_arch_vals = spec.variants["amdgpu_target"].value
            if rocm_arch_vals:
                rocm_arch_sorted = list(sorted(rocm_arch_vals, reverse=True))
                rocm_arch = rocm_arch_sorted[0]
                configure_args.append(f"--with-gpu-arch={rocm_arch}")
        else:
            configure_args.extend(["--without-hip", "--disable-rocrand", "--disable-rocsparse"])
            if spec.satisfies("@2.29.0:"):
                configure_args.extend(["--disable-rocblas", "--disable-rocsolver"])

        if spec.satisfies("+sycl"):
            configure_args.append("--with-sycl")

        if spec.satisfies("+magma"):
            configure_args.append("--with-magma-include=%s" % spec["magma"].prefix.include)
            configure_args.append("--with-magma-lib=%s" % spec["magma"].libs)
            configure_args.append("--with-magma")

        return configure_args

    def build(self, pkg, spec, prefix):
        with working_dir("src"):
            make()

    def install(self, pkg, spec, prefix):
        # Hypre's sources are staged under ./src so we'll have to manually cd into it
        with working_dir("src"):
            if pkg.run_tests:
                make("check")
                make("test")
                Executable(join_path("test", "ij"))()
                sstruct = Executable(join_path("test", "struct"))
                sstruct()
                sstruct("-in", "test/sstruct.in.default", "-solver", "40", "-rhsone")
            make("install")
            if spec.satisfies("+gptune"):
                make("test")
                mkdirp(pkg.prefix.bin)
                install(join_path("test", "ij"), pkg.prefix.bin)

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        spec = self.spec
        # Limit toolchain wrapper and flags to Autotools builds
        if spec.satisfies("build_system=autotools +mpi"):
            env.set("CC", spec["mpi"].mpicc)
            env.set("CXX", spec["mpi"].mpicxx)
            if spec.satisfies("+fortran"):
                env.set("F77", spec["mpi"].mpif77)

        if spec.satisfies("build_system=autotools +cuda"):
            env.set("CUDA_HOME", spec["cuda"].prefix)
            env.set("CUDA_PATH", spec["cuda"].prefix)
            # In CUDA builds hypre currently doesn't handle flags correctly
            env.append_flags("CXXFLAGS", "-O2" if spec.satisfies("~debug") else "-g")

        if spec.satisfies("build_system=autotools +rocm"):
            # As of 2022/04/05, the following are set by 'llvm-amdgpu' and
            # override hypre's default flags, so we unset them.
            env.unset("CFLAGS")
            env.unset("CXXFLAGS")
