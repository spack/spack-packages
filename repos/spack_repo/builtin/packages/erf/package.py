import os

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage

from spack.package import *


def submodules(package):
    submodules = []

    if package.spec.satisfies("+noahmp"):
        submodules.append("Submodules/Noah-MP")

    if package.spec.satisfies("+rrtmgp"):
        submodules.append("Submodules/RRTMGP")
        submodules.append("Submodules/ekat")

    return submodules


class Erf(CMakePackage, CudaPackage):
    """ERF solves the compressible Navier-Stokes on a Arakawa C-grid
    for large-scale weather modeling.
    """

    homepage = "https://erf.readthedocs.io/en/latest/index.html"
    url = "https://github.com/erf-model/ERF/archive/refs/tags/25.10.tar.gz"
    git = "https://github.com/erf-model/ERF.git"

    def url_for_version(self, version):
        return f"https://github.com/erf-model/ERF/archive/refs/tags/{version}.tar.gz"

    test_requires_compiler = True

    maintainers("larenspear")

    license("BSD-3-Clause", checked_by="larenspear")

    version("26.04", tag="26.04", submodules=submodules)
    version("26.03", tag="26.03", submodules=submodules)
    version("26.02", tag="26.02", submodules=submodules)
    version("26.01", tag="26.01", submodules=submodules)
    version("25.12", tag="25.12", submodules=submodules)
    version("25.11", tag="25.11", submodules=submodules)
    version("25.10", tag="25.10", submodules=submodules)
    version("25.08", tag="25.08", submodules=submodules)
    version("25.07", tag="25.07", submodules=submodules)
    version("25.06", tag="25.06", submodules=submodules)
    version("25.05", tag="25.05", submodules=submodules)
    version("25.04", tag="25.04", submodules=submodules)
    version("25.03", tag="25.03", submodules=submodules)
    version("25.01", tag="25.01", submodules=submodules)
    version("24.11", tag="24.11", submodules=submodules)
    version("24.10", tag="24.10", submodules=submodules)
    version("24.09", tag="24.09", submodules=submodules)
    version("24.08", tag="24.08", submodules=submodules)
    version("24.06", tag="24.06", submodules=submodules)
    version("24.05", tag="24.05", submodules=submodules)
    version("24.04", tag="24.04", submodules=submodules)
    version("24.03", tag="24.03", submodules=submodules)
    version("24.02", tag="24.02", submodules=submodules)
    version("24.01", tag="24.01", submodules=submodules)
    version("23.12", tag="23.12", submodules=submodules)
    version("23.11", tag="23.11", submodules=submodules)
    version("23.10", tag="23.10", submodules=submodules)

    variant("mpi", default=False, description="Enable MPI support")
    variant("openmp", default=False, description="Enable OpenMP support")
    variant("netcdf", default=False, description="Enable NetCDF support")
    variant("particles", default=False, description="Enable particle support")
    variant("multiblock", default=False, description="Enable multiblock support")
    variant("tests", default=False, description="Enable tests")
    variant("fcompare", default=False, description="Enable fcompare")
    variant("fft", default=False, description="Enable FFT support")
    variant("noahmp", default=False, description="Enable Noah-MP")
    variant("rrtmgp", default=False, description="Enable RRTMGP radiation support via EKAT")

    with default_args(type="build"):
        depends_on("cmake@3.20:")
        depends_on("cmake@3.21:", when="+rrtmgp")
        depends_on("git")
        depends_on("c")
        depends_on("cxx")
        depends_on("fortran")
        depends_on("pkgconfig")

    with default_args(type=("build", "link")):
        depends_on("amrex+pic")
        for v in ("mpi", "openmp", "cuda", "particles"):
            depends_on(f"amrex+{v}", when=f"+{v}")
            depends_on(f"amrex~{v}", when=f"~{v}")
        for sm in CudaPackage.cuda_arch_values:
            depends_on(f"amrex+cuda cuda_arch={sm}", when=f"+cuda cuda_arch={sm}")
        depends_on("mpi", when="+mpi")
        depends_on("cuda@11.0:", when="+cuda")
        depends_on("fftw", when="+fft")

        with when("+netcdf"):
            depends_on("amrex+mpi")
            depends_on("netcdf-c+mpi+parallel-netcdf")
            depends_on("netcdf-fortran")
            depends_on("hdf5+mpi", when="+mpi")

        with when("+rrtmgp"):
            depends_on("kokkos@4.5:")
            depends_on("yaml-cpp")
            for sm in CudaPackage.cuda_arch_values:
                depends_on(f"kokkos+cuda cuda_arch={sm}", when=f"+cuda cuda_arch={sm}")

    conflicts("+openmp", when="+cuda", msg="Cannot enable both OpenMP and CUDA")
    conflicts("+fft", when="~mpi", msg="FFT support requires MPI")
    conflicts("+rrtmgp", when="~mpi", msg="RRTMGP support requires MPI")
    conflicts("+rrtmgp", when="~netcdf", msg="RRTMGP support requires NetCDF")

    def patch(self):
        if self.spec.satisfies("+rrtmgp"):
            ekat_dir = os.path.join(self.stage.source_path, "Submodules", "ekat")
            gitmodules = os.path.join(ekat_dir, ".gitmodules")

            # Rewrite spdlog SSH URL to HTTPS so it works without SSH keys
            if os.path.exists(gitmodules):
                filter_file("git@github.com:", "https://github.com/", gitmodules, string=True)

            # Fetch spdlog submodule (nested under ekat, can't be fetched
            # from top-level .gitmodules)
            git = which("git")
            git("-C", ekat_dir, "submodule", "update", "--init", "extern/spdlog")

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
            self.define_from_variant("ERF_ENABLE_NOAHMP", "noahmp"),
            self.define_from_variant("ERF_ENABLE_RRTMGP", "rrtmgp"),
            self.define("ERF_DIM", "3"),
            self.define("ERF_USE_INTERNAL_AMREX", False),
            self.define("ERF_CLONE_AMREX", False),
            self.define("GIT_SUBMODULE_PROTOCOL", "https"),
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

        if "+rrtmgp" in self.spec:
            # Write a cmake include file that injects find_package() calls
            # for Spack-provided Kokkos and yaml-cpp. This is needed because
            # ERF uses add_subdirectory() for EKAT which tries to build its
            # own Kokkos/yaml-cpp. CMAKE_PROJECT_INCLUDE runs right after
            # ERF's project() call, making Spack targets visible first.
            include_file = os.path.join(self.stage.source_path, "spack_find_deps.cmake")
            with open(include_file, "w") as f:
                f.write("find_package(Kokkos REQUIRED)\n")
                f.write("find_package(yaml-cpp REQUIRED)\n")
            args.append(self.define("CMAKE_PROJECT_INCLUDE", include_file))

        return args

    def setup_build_environment(self, env):
        super().setup_build_environment(env)
        env.set("AMREX_HOME", self.spec["amrex"].prefix)
        if "+openmp" in self.spec:
            if "%clang" in self.spec or "%gcc" in self.spec:
                env.append_flags("CFLAGS", self.compiler.openmp_flag)
                env.append_flags("CXXFLAGS", self.compiler.openmp_flag)
                env.append_flags("FFLAGS", self.compiler.openmp_flag)
