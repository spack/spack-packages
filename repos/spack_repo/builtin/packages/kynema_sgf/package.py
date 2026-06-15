# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class KynemaSgf(CMakePackage, CudaPackage, ROCmPackage):
    """Kynema-SGF is a massively parallel, block-structured adaptive-mesh,
    incompressible flow solver for the Kynema project."""

    homepage = "https://github.com/Kynema/kynema-sgf"
    url = "https://github.com/Kynema/kynema-sgf/archive/refs/tags/v3.9.1.tar.gz"
    git = "https://github.com/Kynema/kynema-sgf.git"

    maintainers("jrood-nrel")

    tags = ["ecp", "ecp-apps"]
    submodules = True

    license("BSD-3-Clause")

    version("main", branch="main")

    variant("hypre", default=False, description="Enable Hypre integration")
    variant("ascent", default=False, description="Enable Ascent integration")
    variant("masa", default=False, description="Enable MASA integration")
    variant("mpi", default=True, description="Enable MPI support")
    variant("netcdf", default=False, description="Enable NetCDF support")
    variant("openfast", default=False, description="Enable OpenFAST integration")
    variant("kynema-fmb", default=False, description="Enable Kynema integration")
    variant("openmp", default=False, description="Enable OpenMP for CPU builds")
    variant("pic", default=True, description="Position independent code")
    variant("shared", default=True, description="Build shared libraries")
    variant("tests", default=True, description="Activate regression tests")
    variant("tiny_profile", default=False, description="Activate tiny profile")
    variant("hdf5", default=False, description="Enable HDF5 plots with ZFP compression")
    variant("umpire", default=False, description="Enable UMPIRE memory pooling")
    variant("sycl", default=False, description="Enable SYCL backend")
    variant("gpu-aware-mpi", default=False, description="Enable GPU aware MPI")
    variant("helics", default=False, description="Enable HELICS support for control interface")
    variant(
        "waves2amr", default=False, description="Enable Waves2AMR support for ocean wave input"
    )
    variant("fft", default=False, description="Enable FFT support for MAC projection")
    variant("single-precision", default=False, description="Use single precision")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build", when="+openfast")
    depends_on("mpi", when="+mpi")
    depends_on("hdf5~mpi", when="+hdf5~mpi")
    depends_on("hdf5+mpi", when="+hdf5+mpi")
    # New versions of HDF5 have CMake problems finding ZLIB::ZLIB target
    depends_on("hdf5@:1.14.4-3", when="+hdf5")
    depends_on("h5z-zfp", when="+hdf5")
    depends_on("zfp", when="+hdf5")
    depends_on("hypre~int64@2.29.0:", when="+hypre")
    depends_on("hypre+mpi", when="+hypre+mpi")
    depends_on("hypre+umpire", when="+hypre+umpire")
    depends_on("hypre+sycl", when="+hypre+sycl")
    depends_on("hypre+gpu-aware-mpi", when="+hypre+gpu-aware-mpi")
    depends_on("masa", when="+masa")
    depends_on("ascent~mpi", when="+ascent~mpi")
    depends_on("ascent+mpi", when="+ascent+mpi")
    depends_on("netcdf-c", when="+netcdf")
    depends_on("netcdf-c+mpi", when="+netcdf+mpi")
    depends_on("py-netcdf4", when="+netcdf")
    depends_on("py-numpy@2:", when="+netcdf")
    depends_on("py-matplotlib", when="+masa")
    depends_on("py-pandas", when="+masa")
    depends_on("openfast+cxx@3.5.0:3.5.9,4.1:", when="+openfast")
    depends_on("openfast+netcdf", when="+openfast+netcdf")
    depends_on("kynema-fmb", when="+kynema-fmb")
    depends_on("helics@:3.3.2", when="+helics")
    depends_on("helics@:3.3.2+mpi", when="+helics+mpi")
    depends_on("fftw", when="+waves2amr")
    depends_on("fftw", when="+fft")
    depends_on("rocrand", when="+rocm")
    depends_on("rocprim", when="+rocm")

    requires("+mpi", when="+kynema-fmb")
    requires("+mpi", when="+openfast")

    for arch in CudaPackage.cuda_arch_values:
        depends_on("hypre+cuda cuda_arch=%s" % arch, when="+cuda+hypre cuda_arch=%s" % arch)
    for arch in ROCmPackage.amdgpu_targets:
        depends_on(
            "hypre+rocm amdgpu_target=%s" % arch, when="+rocm+hypre amdgpu_target=%s" % arch
        )
    for arch in CudaPackage.cuda_arch_values:
        depends_on("ascent+cuda cuda_arch=%s" % arch, when="+ascent+cuda cuda_arch=%s" % arch)

    conflicts("+openmp", when="+cuda")
    conflicts("+shared", when="+cuda")

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        # Avoid compile errors with Intel interprocedural optimization
        if self.spec.satisfies("%intel"):
            env.append_flags("CXXFLAGS", "-no-ipo")
        if self.spec.satisfies("+cuda"):
            env.set("CUDAHOSTCXX", spack_cxx)

    def cmake_args(self):
        define = self.define
        spec = self.spec

        vs = [
            "mpi",
            "cuda",
            "openmp",
            "netcdf",
            "hypre",
            "masa",
            "ascent",
            "openfast",
            "rocm",
            "tests",
            "tiny_profile",
            "fft",
            "helics",
            "umpire",
            "sycl",
        ]

        args = [self.define_from_variant("KYNEMA_SGF_ENABLE_%s" % v.upper(), v) for v in vs]

        args.append(self.define_from_variant("KYNEMA_SGF_ENABLE_KYNEMA_FMB", "kynema-fmb"))
        args.append(self.define_from_variant("BUILD_SHARED_LIBS", "shared"))

        if spec.satisfies("+mpi"):
            args.append(define("MPI_HOME", spec["mpi"].prefix))
            args.append(define("MPI_CXX_COMPILER", spec["mpi"].mpicxx))
            args.append(define("MPI_C_COMPILER", spec["mpi"].mpicc))

        if spec.satisfies("+hdf5"):
            args.append(self.define_from_variant("KYNEMA_SGF_ENABLE_HDF5", "hdf5"))
            args.append(self.define_from_variant("KYNEMA_SGF_ENABLE_HDF5_ZFP", "hdf5"))
            # Help AMReX understand if HDF5 is parallel or not.
            # Building HDF5 with CMake as Spack does, causes this inspection to break.
            args.append(define("HDF5_IS_PARALLEL", spec.satisfies("+mpi")))

        if spec.satisfies("+cuda"):
            args.append(define("CMAKE_CUDA_ARCHITECTURES", spec.variants["cuda_arch"].value))

        if spec.satisfies("+rocm"):
            args.append(define("CMAKE_CXX_COMPILER", spec["hip"].hipcc))
            targets = spec.variants["amdgpu_target"].value
            args.append("-DAMReX_AMD_ARCH=" + ";".join(str(x) for x in targets))

        if spec.satisfies("+umpire"):
            args.append(define("UMPIRE_DIR", spec["umpire"].prefix))

        if spec.satisfies("+helics"):
            args.append(define("HELICS_DIR", spec["helics"].prefix))

        if spec.satisfies("+waves2amr"):
            args.append(self.define_from_variant("KYNEMA_SGF_ENABLE_W2A", "waves2amr"))
            args.append(define("FFTW_DIR", spec["fftw"].prefix))

        if spec.satisfies("+fft"):
            args.append(define("FFTW_DIR", spec["fftw"].prefix))

        if spec.satisfies("+sycl"):
            requires(
                "%dpcpp",
                "%oneapi",
                policy="one_of",
                msg=(
                    "AMReX's SYCL GPU Backend requires DPC++ (dpcpp) "
                    "or the oneAPI CXX (icpx) compiler."
                ),
            )

        if spec.satisfies("+openfast"):
            args.append(define("KYNEMA_SGF_OPENFAST_VERSION", spec["openfast"].version))

        if spec.satisfies("+single-precision"):
            args.append(define("KYNEMA_SGF_PRECISION", "SINGLE"))

        return args
