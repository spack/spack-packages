from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *

class Erf(CMakePackage, CudaPackage):
    """ERF solves the compressible Navier-Stokes on a Arakawa C-grid
    for large-scale weather modeling.
    """

    homepage = "https://erf.readthedocs.io/en/latest/index.html"
    url = "https://github.com/erf-model/ERF/archive/refs/tags/25.08.tar.gz"
    git = "https://github.com/erf-model/ERF.git"
    test_requires_compiler = True

    maintainers("larenspear")

    license("BSD-3-Clause", checked_by="larenspear")

    version("25.10", tag="25.10", submodules=True, sha256="611f0a7e8714b762f63fee34cc3dbb83343d21e7")
    version("25.08", tag="25.08", submodules=True, sha256="e0b8be35990d01ba65a5502dbd23e351b57b72d4")
    version("25.07", tag="25.07", submodules=True, sha256="54fbee6f1bc1dfa356313545556578944c564295")
    version("25.06", tag="25.06", submodules=True, sha256="af8ec6cce9db12dcd9fdf8f081cb1f768e4f0528")
    version("25.05", tag="25.05", submodules=True, sha256="bbe22c5f6c0938ea82d174cc84a4e93eb5db7863")
    version("25.04", tag="25.04", submodules=True, sha256="55358ec26377fe14f93275bc72f0c8e442921bb7")
    version("25.03", tag="25.03", submodules=True, sha256="3030bae1c20bf5ee36e43fb0568a822c47c2a473")
    version("25.01", tag="25.01", submodules=True, sha256="481e7f50d78ce73f0aad4df108b51247df0984bd")
    version("24.11", tag="24.11", submodules=True, sha256="9428c70c5c299fd8c11bc0b15634b917e16bdf7b")
    version("24.10", tag="24.10", submodules=True, sha256="9597ac13d4e136895165ac79e21a30408f38ee19")
    version("24.09", tag="24.09", submodules=True, sha256="16e75b3e4de96ba9c4ca38b945d2a452d028244a")
    version("24.08", tag="24.08", submodules=True, sha256="e3ff1bf8b76da36adac9bbfe83fc06eafa4cbb16")
    version("24.06", tag="24.06", submodules=True, sha256="6f794f2fa7ac618a2dff77a573f973946809bab9")
    version("24.05", tag="24.05", submodules=True, sha256="22931d4f402ade07b60440bcc7f678f585e8adec")
    version("24.04", tag="24.04", submodules=True, sha256="5eb01f4a611d5eb80ab323468657db8ec53be9e5")
    version("24.03", tag="24.03", submodules=True, sha256="5621a11955c27f57b9955a11d611b41c70cb42d3")
    version("24.02", tag="24.02", submodules=True, sha256="a7762e8530d86b1cc654c0c1d5e45f07196fc350")
    version("24.01", tag="24.01", submodules=True, sha256="850aa4079b6b71eeb376be0558e1927d3b999775")
    version("23.12", tag="23.12", submodules=True, sha256="c0a1c9f212511c200a337c1b55f65e157a92df48")
    version("23.11", tag="23.11", submodules=True, sha256="885a8c432fd8c81dc32863bfc51c6ee1542531bc")
    version("23.10", tag="23.10", submodules=True, sha256="de410c8d03f61a008cafb2326c44a9a739785359")

    variant("mpi", default=False, description="Enable MPI support")
    variant("openmp", default=False, description="Enable OpenMP support")
    variant("netcdf", default=False, description="Enable NetCDF support")
    variant("particles", default=False, description="Enable particle support")
    variant("multiblock", default=False, description="Enable multiblock support")
    variant("radiation", default=False, description="Enable radiation support")
    variant("tests", default=False, description="Enable tests")
    variant("fcompare", default=False, description="Enable fcompare")
    variant("fft", default=False, description="Enable FFT support")

    with default_args(type="build"):
        depends_on("cmake@3.20:")
        depends_on("git")
        depends_on("c")
        depends_on("cxx")
        depends_on("fortran")
        depends_on("pkgconf")

    with default_args(type=("build", "link")):
        depends_on("amrex")
        for v in ("mpi", "openmp", "cuda", "particles"):
            depends_on(f"amrex+{v}", when=f"+{v}")
            depends_on(f"amrex~{v}", when=f"~{v}")
        for sm in CudaPackage.cuda_arch_values:
            depends_on(f"amrex+cuda cuda_arch={sm}", when=f"+cuda cuda_arch={sm}")
        depends_on("mpi", when="+mpi")
        depends_on("cuda@11.0:", when="+cuda")
        depends_on("fftw", when="+fft")

        with when("+netcdf"):
            depends_on("netcdf-c+mpi+parallel-netcdf", when="+mpi")
            depends_on("netcdf-c~mpi+parallel-netcdf", when="~mpi")
            depends_on("hdf5+mpi", when="+mpi")
            depends_on("hdf5~mpi", when="~mpi")


    conflicts("+openmp", when="+cuda", msg="Cannot enable both OpenMP and CUDA")
    conflicts("+fft", when="~mpi", msg="FFT support requires MPI")
    conflicts("+radiation", when="platform=darwin", msg="Radiation is not supported on macOS")

    _KOKKOS_SM_TO_FLAG = {
        "70": "Kokkos_ARCH_VOLTA70",
        "72": "Kokkos_ARCH_VOLTA72",
        "75": "Kokkos_ARCH_TURING75",
        "80": "Kokkos_ARCH_AMPERE80",
        "86": "Kokkos_ARCH_AMPERE86",
        "89": "Kokkos_ARCH_ADA89",
        "90": "Kokkos_ARCH_HOPPER90",
    }

    def _kokkos_flags_from_cuda_arch(self, sm_list):
        for sm in sm_list:
            flag = self._KOKKOS_SM_TO_FLAG.get(sm)
            if flag:
                yield flag

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
        args.append(self.define("ERF_USE_EXTERNAL_AMREX", True))
        args.append(self.define("ERF_CLONE_AMREX", False))
        args.append(self.define("GIT_SUBMODULE_PROTOCOL", "https"))
        args.append(self.define("MPIEXEC_PREFLAGS", "--oversubscribe"))
        args.append(self.define("ERF_DIM", "3"))

        if "+netcdf" in self.spec:
            args.extend(
                [
                    self.define("NetCDF_C_PATH", self.spec["netcdf-c"].prefix),
                    self.define("NetCDF_FORTRAN_PATH", self.spec["netcdf-fortran"].prefix),
                ]
            )

        if "+radiation" in self.spec:
            args.extend(
                [
                    self.define("ERF_ENABLE_KOKKOS", True),
                    self.define("ERF_ENABLE_EKAT", True),
                    self.define("ERF_ENABLE_RRTMGP", True),
                ]
            )
            if "+cuda" in self.spec:
                sm_list = self.spec.variants["cuda_arch"].value or ["80"]
                for kdef in self._kokkos_flags_from_cuda_arch(sm_list):
                    args.append(self.define(kdef, True))

        if "+cuda" in self.spec:
            archs = self.spec.variants["cuda_arch"].value or ["80"]
            args.append(self.define("CMAKE_CUDA_ARCHITECTURES", ";".join(archs)))
            args.extend(
                [
                    self.define("ERF_ENABLE_CUDA", "ON"),
                    self.define("CUDAToolkit_ROOT", self.spec["cuda"].prefix),
                ]
            )

        return args

    def setup_build_environment(self, env):
        super().setup_build_environment(env)
        env.set("GIT_CONFIG_COUNT", "1")
        env.set("GIT_CONFIG_KEY_0", "url.https://github.com/.insteadOf")
        env.set("GIT_CONFIG_VALUE_0", "git@github.com:")
        env.set("AMREX_HOME", self.spec["amrex"].prefix)
        if "+openmp" in self.spec:
            if "%clang" in self.spec or "%gcc" in self.spec:
                env.append_flags("CFLAGS", self.compiler.openmp_flag)
                env.append_flags("CXXFLAGS", self.compiler.openmp_flag)
                env.append_flags("FFLAGS", self.compiler.openmp_flag)
