from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage

from spack.package import *


class Erf(CMakePackage, CudaPackage):
    """ERF solves the compressible Navier-Stokes on a Arakawa C-grid
    for large-scale weather modeling.
    """

    homepage = "https://erf.readthedocs.io/en/latest/index.html"
    url = "https://github.com/erf-model/ERF/archive/refs/tags/25.10.tar.gz"
    git = "https://github.com/erf-model/ERF.git"
    test_requires_compiler = True

    maintainers("larenspear")

    license("BSD-3-Clause", checked_by="larenspear")

    version("25.10", sha256="92575d25a8e87266f1b3a9a0c16a5755b84c45d489a060abeec6ddea8b8d8fe0")
    version("25.08", sha256="c8723384e00fb4bbb694385bdbc5187f38ee1509a0a18a23efc1094212fd21f4")
    version("25.07", sha256="bee8c136872c4e5400fdf2f6a432c8dc17f9b8384715158d9780a2c561a51642")
    version("25.06", sha256="dd1d627faf67477e3fa1f58b006f7e2b00316c66e8c99baf8b6cfbedce37b5f2")
    version("25.05", sha256="eb56a44d915d6af3ad30438dff6b96d9c489ae7c610fe4cdd0c17f2f26cc4b28")
    version("25.04", sha256="fc6837b252c1cebd0f2d38cdb3cea8ad55c837e4163c76e5d3508d973b282a42")
    version("25.03", sha256="3068c0c5f66538bcc1a12ee8c3eb142e5d02b73b71ab1cfbb244a053e8d5cf4a")
    version("25.01", sha256="11e48aadfc420c3f9adb05a0c5778776d6cb0915476532fd7a095d9f167ef584")
    version("24.11", sha256="19e7ce4829a46c98baf55b1dc4b2cefc508f2db41182e47c0ca788fe9280783f")
    version("24.10", sha256="7c9ba35374e71103fab8c5ba3ea107b4574e3270038bc3e8cbdcbe30eba26e7a")

    variant("mpi", default=False, description="Enable MPI support")
    variant("openmp", default=False, description="Enable OpenMP support")
    variant("netcdf", default=False, description="Enable NetCDF support")
    variant("particles", default=False, description="Enable particle support")
    variant("multiblock", default=False, description="Enable multiblock support")
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
            depends_on("netcdf-fortran")
            depends_on("hdf5+mpi", when="+mpi")
            depends_on("hdf5~mpi", when="~mpi")

    conflicts("+openmp", when="+cuda", msg="Cannot enable both OpenMP and CUDA")
    conflicts("+fft", when="~mpi", msg="FFT support requires MPI")

    def cmake_args(self):
        args = [
            self.define_from_variant("ERF_ENABLE_MPI", "mpi"),
            self.define_from_variant("ERF_ENABLE_OMP", "openmp"),
            self.define_from_variant("ERF_ENABLE_NETCDF", "netcdf"),
            self.define_from_variant("ERF_ENABLE_PARTICLES", "particles"),
            self.define_from_variant("ERF_ENABLE_MULTIBLOCK", "multiblock"),
            self.define_from_variant("ERF_BUILD_TESTS", "tests"),
            self.define_from_variant("ERF_BUILD_FCOMPARE", "fcompare"),
            self.define_from_variant("ERF_ENABLE_FFT", "fft"),
            self.define("ERF_DIM", "3"),
            self.define("ERF_USE_EXTERNAL_AMREX", True),
            self.define("ERF_CLONE_AMREX", False),
            self.define("GIT_SUBMODULE_PROTOCOL", "https"),
            self.define("MPIEXEC_PREFLAGS", "--oversubscribe"),
            self.define("ERF_DIM", "3"),
        ]

        if "+netcdf" in self.spec:
            args.extend(
                [
                    self.define("NetCDF_C_PATH", self.spec["netcdf-c"].prefix),
                    self.define("NetCDF_FORTRAN_PATH", self.spec["netcdf-fortran"].prefix),
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
