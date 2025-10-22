from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Erf(CMakePackage, CudaPackage, ROCmPackage):
    """ERF solves the compressible Navier-Stokes on a Arakawa C-grid
    for large-scale weather modeling.
    """

    homepage = "https://erf.readthedocs.io/en/latest/index.html"
    url = "https://github.com/erf-model/ERF/archive/refs/tags/25.08.tar.gz"
    git = "https://github.com/erf-model/ERF.git"
    test_requires_compiler = True

    maintainers("larenspear")

    license("BSD-3-Clause", checked_by="larenspear")

    version("25.10", tag="25.10", submodules=True)
    version("25.08", tag="25.08", submodules=True)
    version("25.07", tag="25.08", submodules=True)
    version("25.06", tag="25.08", submodules=True)
    version("25.05", tag="25.08", submodules=True)
    version("25.04", tag="25.08", submodules=True)
    version("25.03", tag="25.08", submodules=True)
    version("25.01", tag="25.08", submodules=True)
    version("24.11", tag="25.08", submodules=True)
    version("24.10", tag="25.08", submodules=True)
    version("24.09", tag="25.08", submodules=True)
    version("24.08", tag="25.08", submodules=True)
    version("24.06", tag="25.08", submodules=True)
    version("24.05", tag="25.08", submodules=True)
    version("24.04", tag="25.08", submodules=True)
    version("24.03", tag="25.08", submodules=True)
    version("24.02", tag="25.08", submodules=True)
    version("24.01", tag="25.08", submodules=True)
    version("23.12", tag="25.08", submodules=True)
    version("23.11", tag="25.08", submodules=True)
    version("23.10", tag="25.08", submodules=True)

    variant("mpi", default=False, description="Enable MPI support")
    variant("openmp", default=False, description="Enable OpenMP support")
    variant("hip", default=False, description="Enable HIP/rocm support")
    variant("sycl", default=False, description="Enable SYCL support")
    variant("netcdf", default=False, description="Enable NetCDF support")
    variant("particles", default=False, description="Enable particle support")
    variant("multiblock", default=False, description="Enable multiblock support")
    variant("radiation", default=False, description="Enable radiation support")
    variant("tests", default=False, description="Enable tests")
    variant("fcompare", default=False, description="Enable fcompare")
    variant("fft", default=False, description="Enable FFT support")
    variant("debug", default=False, description="Enable debug build")

    depends_on("cmake@3.20:", type="build")
    depends_on("git", type="build")
    depends_on("amrex", type=("build", "link", "run"))
    for v in ("mpi", "openmp", "cuda", "sycl", "particles"):
        depends_on(f"amrex+{v}", when=f"+{v}")
        depends_on(f"amrex~{v}", when=f"~{v}")
    for sm in CudaPackage.cuda_arch_values:
        depends_on(f"amrex+cuda cuda_arch={sm}", when=f"+cuda cuda_arch={sm}")
    depends_on("amrex+rocm", when="+hip")
    depends_on("amrex~rocm", when="~hip")
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")
    depends_on("mpi", when="+mpi")
    depends_on("cuda@11.0:", when="+cuda")
    depends_on("hip@4.0:", when="+hip")
    depends_on("rocm-openmp-extras", when="+hip")
    depends_on("intel-oneapi-dpl", when="+sycl")
    depends_on("intel-oneapi-mkl", when="+sycl")
    depends_on("amrex@23.05:", when="@25.04")
    depends_on("amrex@23.08:", when="@25.08")
    depends_on("pkgconf", type="build")

    with when("+netcdf"):
        depends_on("netcdf-c+mpi+parallel-netcdf", when="+mpi")
        depends_on("netcdf-c~mpi+parallel-netcdf", when="~mpi")
        depends_on("netcdf-fortran")
        depends_on("hdf5+mpi", when="+mpi")
        depends_on("hdf5~mpi", when="~mpi")

    depends_on("fftw", when="+fft")

    conflicts("+cuda", when="+hip", msg="Cannot enable both CUDA and HIP")
    conflicts("+openmp", when="+cuda", msg="Cannot enable both OpenMP and CUDA")
    conflicts("+openmp", when="+hip", msg="Cannot enable both OpenMP and HIP")
    conflicts("+cuda", when="+sycl", msg="Cannot enable both CUDA and SYCL")
    conflicts("+hip", when="+sycl", msg="Cannot enable both HIP and SYCL")
    conflicts("+fft", when="~mpi", msg="FFT support requires MPI")
    conflicts("+radiation", when="platform=darwin", msg="Radiation is not supported on macOS")

    def cmake_args(self):
        args = [
            self.define_from_variant("ERF_ENABLE_MPI", "mpi"),
            self.define_from_variant("ERF_ENABLE_OMP", "openmp"),
            self.define_from_variant("ERF_ENABLE_NETCDF", "netcdf"),
            self.define_from_variant("ERF_ENABLE_PARTICLES", "particles"),
            self.define_from_variant("ERF_ENABLE_MULTIBLOCK", "multiblock"),
            self.define_from_variant("ERF_ENABLE_RADIATION", "radiation"),
            self.define_from_variant("ERF_BUILD_TESTS", "tests"),
            self.define_from_variant("ERF_BUILD_FCOMPARE", "fcompare"),
            self.define_from_variant("ERF_ENABLE_FFT", "fft"),
            self.define("ERF_DIM", "3"),
        ]
        args.append(self.define("ERF_USE_EXTERNAL_AMREX", False))
        args.append(self.define("ERF_CLONE_AMREX", True))
        args.append(self.define("GIT_SUBMODULE_PROTOCOL", "https"))
        args.append(self.define("MPIEXEC_PREFLAGS", "--oversubscribe"))
        args.append(self.define("CMAKE_BUILD_TYPE", "Release"))
        args.append(self.define("ERF_DIM", "3"))

        if "+netcdf" in self.spec:
            args.extend(
                [
                    self.define("NetCDF_C_PATH", self.spec["netcdf-c"].prefix),
                    self.define("NetCDF_FORTRAN_PATH", self.spec["netcdf-fortran"].prefix),
                ]
            )

        if "+radiation" in self.spec:
            if "+cuda" in self.spec:
                args.append(self.define("Kokkos_ARCH_AMPERE80", True))
            args.extend(
                [
                    self.define("ERF_ENABLE_KOKKOS", True),
                    self.define("Kokkos_ARCH_AMPERE", True),
                    self.define("ERF_ENABLE_EKAT", True),
                    self.define("ERF_ENABLE_RRTMGP", True),
                ]
            )

        if "+cuda" in self.spec:
            archs = self.spec.variants["cuda_arch"].value or ["80"]
            args.append(self.define("CMAKE_CUDA_ARCHITECTURES", ";".join(archs)))
            args.extend(
                [
                    self.define("ERF_ENABLE_CUDA", "ON"),
                    self.define("CUDAToolkit_ROOT", self.spec["cuda"].prefix),
                ]
            )

        if "+hip" in self.spec:
            args.append(self.define("CMAKE_HIP_ARCHITECTURES", "gfx906;gfx908;gfx90a"))

        print(args)
        return args

    def setup_build_environment(self, env):
        super(Erf, self).setup_build_environment(env)
        env.set("GIT_CONFIG_COUNT", "1")
        env.set("GIT_CONFIG_KEY_0", "url.https://github.com/.insteadOf")
        env.set("GIT_CONFIG_VALUE_0", "git@github.com:")
        env.set("AMREX_HOME", self.spec["amrex"].prefix)
        if "+hip" in self.spec:
            env.set("HIPCXX", self.spec["hip"].prefix.bin.hipcc)
        if "+openmp" in self.spec:
            if "%clang" in self.spec or "%gcc" in self.spec:
                env.append_flags("CFLAGS", self.compiler.openmp_flag)
                env.append_flags("CXXFLAGS", self.compiler.openmp_flag)
                env.append_flags("FFLAGS", self.compiler.openmp_flag)
            elif "%intel" in self.spec:
                env.append_flags("CFLAGS", "-qopenmp")
                env.append_flags("CXXFLAGS", "-qopenmp")
                env.append_flags("FFLAGS", "-qopenmp")
                print(self.compiler.openmp_flag)

    def configure_args(self):
        args = super(Erf, self).configure_args()
        return args
