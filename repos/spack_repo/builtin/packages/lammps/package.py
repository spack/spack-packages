# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
import datetime as dt
import os

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.python import PythonExtension, PythonPipBuilder
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Lammps(CMakePackage, CudaPackage, ROCmPackage, PythonExtension):
    """LAMMPS stands for Large-scale Atomic/Molecular Massively
    Parallel Simulator.
    """

    homepage = "https://www.lammps.org/"
    url = "https://github.com/lammps/lammps/archive/patch_1Sep2017.tar.gz"
    git = "https://github.com/lammps/lammps.git"

    tags = ["ecp", "ecp-apps", "e4s"]

    maintainers("rbberger")

    license("GPL-2.0-only")

    # rules for new versions and deprecation
    # * new stable versions should be added to stable_versions set
    # * a stable version that has updates and any of its outdated update releases should be
    #   marked deprecated=True
    # * patch releases older than a stable release should be marked deprecated=True
    version("develop", branch="develop")

    # patch releases since last stable
    version("20261113", sha256="069aad4681f6a7b756e8aace2a6f4cf46f266eb4e51057ea021687a41049144d")

    # current stable release
    version(
        "20260930.1",
        sha256="fbaaba35ff3334b1b7e4f7434aeadbfd4572111a0dfc553dcbf4abf65eb00a49",
        preferred=True,
    )

    # old stable versions (keeping last 2 as not deprecated)
    version(
        "20250722.6", sha256="40780d0269c656ffa983a8e3e6ed047fedfe1d0b7344b77ace25bf8c7c535f01"
    )
    version(
        "20240829.4", sha256="e7d6d60b94ada5acc2e1e9966ae12547fd550d6967d4511b8655c77e24878728"
    )

    with default_args(deprecated=True):
        # deprecated patch releases
        version(
            "20260902", sha256="df89defbca87aad40f6c55ab6fca05b910089d831774219ba5a8ddbb9fa4c5dc"
        )
        version(
            "20260704", sha256="be9deffba169d140c337fd29570d3f5469332ece7e77280cce998f6caaad5534"
        )
        version(
            "20260330", sha256="395f00e166836ac0164793d65ba0d957d79dd0848a79c36fa903855e8b49b7e0"
        )
        version(
            "20260211", sha256="b9ba0e368ee5af93f038b913e09a02b777a365ac6aea141842ded9b98b1efa8e"
        )
        version(
            "20251210", sha256="175afc62a7314970d56e93b54745f4e6132e8f688155fff3dd70b298ec077c0e"
        )
        version(
            "20250910", sha256="475d5cda1b289ca3b3dcc97c1ee199f67fa6ad736951213e9b6ec08069d70f0c"
        )

        # deprecated stable versions
        version(
            "20260930", sha256="56e6670161cc0e4c5a4816a95edc80c00c9507a98445d0756b9ad8b5eb29748e"
        )
        version(
            "20250722.5", sha256="9d1eb62c47b8bb1c2003dfe5b5e82b3ebef4223b51593f9aec2410c5ec983977"
        )
        version(
            "20250722.4", sha256="411088d9c03339e025f6a975e0a5741bb9e3f351cc39eda220ab22ac318fe2fb"
        )

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    # ml-quip require Fortran, but not available in Spack
    for fc_pkg in ("kim", "scafacos", "qmmm-xtb"):
        depends_on("fortran", type="build", when=f"+{fc_pkg}")

    stable_versions = {
        "20260930.1",
        "20260930",
        "20250722.6",
        "20250722.5",
        "20250722.4",
        "20240829.4",
    }

    def url_for_version(self, version):
        split_ver = str(version).split(".")
        vdate = dt.datetime.strptime(split_ver[0], "%Y%m%d")
        if len(split_ver) < 2:
            update = ""
        else:
            update = "_update{0}".format(split_ver[1])

        return "https://github.com/lammps/lammps/archive/{0}_{1}{2}.tar.gz".format(
            "stable" if str(version) in Lammps.stable_versions else "patch",
            vdate.strftime("%d%b%Y").lstrip("0"),
            update,
        )

    # List of supported optional packages
    # Note: package `openmp` in this recipe is called `openmp-package`, to avoid clash
    # with the pre-existing `openmp` variant
    # version ranges generates using utility script:
    # https://gist.github.com/rbberger/fdaa38ff08e5961c4741624a4719cdb6
    supported_packages = {
        "adios": {"when": "@20210702:"},
        "amoeba": {"when": "@20220803:"},
        "asphere": {},
        "atc": {"when": "@20210702:20250722"},
        "awpmd": {"when": "@20210702:20250722"},
        "bocs": {"when": "@20210702:"},
        "body": {},
        "bpm": {"when": "@20220504:"},
        "brownian": {"when": "@20210702:"},
        "cg-dna": {"when": "@20210702:"},
        "cg-spica": {"when": "@20220803:"},
        "class2": {},
        "colloid": {},
        "colvars": {"when": "@20210702:"},
        "compress": {},
        "coreshell": {},
        "dielectric": {"when": "@20210702:"},
        "diffraction": {"when": "@20210702:"},
        "dipole": {},
        "dpd-basic": {"when": "@20210702:"},
        "dpd-meso": {"when": "@20210702:"},
        "dpd-react": {"when": "@20210702:"},
        "dpd-smooth": {"when": "@20210702:"},
        "drude": {"when": "@20210702:"},
        "eff": {"when": "@20210702:"},
        "electrode": {"when": "@20220504:"},
        "extra-command": {"when": "@20240829:"},
        "extra-compute": {"when": "@20210728:"},
        "extra-dump": {"when": "@20210728:"},
        "extra-fix": {"when": "@20210728:"},
        "extra-molecule": {"when": "@20210728:"},
        "extra-pair": {"when": "@20210728:"},
        "fep": {"when": "@20210702:"},
        "granular": {},
        "gransurf": {"when": "@20260704:"},
        "graphics": {"when": "@20260211:"},
        "h5md": {"when": "@20210702:"},
        "intel": {"when": "@20210702:"},
        "interlayer": {"when": "@20210728:"},
        "kim": {},
        "kokkos": {"when": "@20201029:"},
        "kspace": {"default": True},
        "latboltz": {"when": "@20210702:"},
        "lepton": {"when": "@20230208:"},
        "machdyn": {"when": "@20210702:"},
        "manifold": {"when": "@20210702:"},
        "manybody": {"default": True},
        "mc": {},
        "mdi": {"when": "@20210702:"},
        "meam": {"when": "@20210702:"},
        "mesont": {"when": "@20210702:"},
        "mgpt": {"when": "@20210702:"},
        "misc": {},
        "ml-hdnnp": {"when": "@20210702:"},
        "ml-iap": {"when": "@20210702:"},
        "ml-pace": {"when": "@20210702:"},
        "ml-pod": {"when": "@20221222:"},
        "ml-rann": {"when": "@20210702:20260704"},
        "ml-snap": {"when": "@20210702:"},
        "ml-uf3": {"when": "@20240627:"},
        "mofff": {"when": "@20210702:"},
        "molecule": {"default": True},
        "molfile": {"when": "@20210702:"},
        "netcdf": {"when": "@20210702:"},
        "openmp-package": {},
        "opt": {},
        "orient": {"when": "@20210728:"},
        "peri": {},
        "phonon": {"when": "@20210702:"},
        "plugin": {"when": "@20210408:"},
        "plumed": {"when": "@20210702:"},
        "poems": {"when": "@:20250722"},
        "ptm": {"when": "@20210702:"},
        "python": {},
        "qeq": {},
        "qtb": {"when": "@20210702:"},
        "qmmm-xtb": {"when": "@20260902:"},
        "reaction": {"when": "@20210702:"},
        "reaxff": {"when": "@20210702:"},
        "rheo": {"when": "@20240829:"},
        "replica": {},
        "rigid": {"default": True},
        "scafacos": {"when": "@20210702:"},
        "shock": {},
        "smtbq": {"when": "@20210702:"},
        "sph": {"when": "@20210702:"},
        "spin": {"when": "@20180629:"},
        "srd": {},
        "tally": {"when": "@20210702:"},
        "uef": {"when": "@20210702:"},
        "voronoi": {},
        "vtk": {"when": "@20210702:20260704"},
        "yaff": {"when": "@20210702:"},
        # "fenix": {"when": "@20260902:"}, no fenix package
        # "mbx": {"when": "@20260211:"}, no mbx package
        # "ml-runner": {"when": "@20260902:"}, no runner package
        # "ml-quip": {"when": "@20210702:"}, no quip package
    }

    for pkg_name, pkg_options in supported_packages.items():
        variant(
            pkg_name,
            default=pkg_options.get("default", False),
            description="Activate the {} package".format(pkg_name.replace("-package", "")),
            when=pkg_options.get("when", None),
        )
    variant("lib", default=True, description="Build the liblammps in addition to the executable")
    variant("mpi", default=True, description="Build with mpi")
    variant("jpeg", default=False, description="Build with jpeg support")
    variant("png", default=False, description="Build with png support")
    variant("ffmpeg", default=False, description="Build with ffmpeg support")
    variant("curl", default=False, description="Build with curl support", when="@20240829:")
    variant("openmp", default=True, description="Build with OpenMP")
    variant("opencl", default=False, description="Build with OpenCL")
    variant(
        "cuda_mps",
        default=False,
        description="(CUDA only) Enable tweaks for running "
        + "with Nvidia CUDA Multi-process services daemon",
    )

    variant(
        "lammps_sizes",
        default="smallbig",
        description="LAMMPS integer sizes (smallsmall: all 32-bit, smallbig:"
        + "64-bit #atoms #timesteps, bigbig: also 64-bit imageint, 64-bit atom ids)",
        values=("smallbig", "bigbig", "smallsmall"),
        multi=False,
    )
    variant(
        "fftw_precision",
        default="double",
        when="+kspace",
        description="Select FFTW precision (used by Kspace)",
        values=("single", "double"),
        multi=False,
    )
    variant(
        "fft",
        default="fftw3",
        when="+kspace",
        description="FFT library for KSPACE package",
        values=("kiss", "fftw3", "mkl", "nvpl"),
        multi=False,
    )
    variant(
        "heffte",
        default=False,
        when="+kspace @20240207:",
        description="Use heffte as distubuted FFT engine",
    )

    variant(
        "fft_kokkos",
        default="fftw3",
        when="@20240417: +kspace+kokkos",
        description="FFT library for Kokkos-enabled KSPACE package",
        values=("kiss", "fftw3", "mkl", "mkl_gpu", "nvpl", "hipfft", "cufft"),
        multi=False,
    )
    for cond in ("cuda", "rocm", "opencl"):
        variant("gpu", default=True, when=f"+{cond}", description="Activate the GPU package")
        variant(
            "gpu_precision",
            default="mixed",
            when=f"+gpu+{cond}",
            description="Select GPU precision (used by GPU package)",
            values=("double", "mixed", "single"),
            multi=False,
        )
    variant("tools", default=False, description="Build LAMMPS tools (msi2lmp, binary2txt, chain)")

    depends_on("cmake@3.16:", when="@20231121:", type="build")
    depends_on("cmake@3.20:", when="@20250910:", type="build")
    depends_on("mpi", when="+mpi")
    depends_on("fftw-api@3", when="+kspace fft=fftw3")
    depends_on("heffte", when="+heffte")
    depends_on("heffte+fftw", when="+heffte fft=fftw3")
    depends_on("heffte+mkl", when="+heffte fft=mkl")
    depends_on("mkl", when="+kspace fft=mkl")
    depends_on("hipfft", when="+kokkos+kspace+rocm fft_kokkos=hipfft")
    depends_on("fftw-api@3", when="+kokkos+kspace fft_kokkos=fftw3")
    depends_on("mkl", when="+kokkos+kspace fft_kokkos=mkl")
    depends_on("nvpl-fft", when="+kspace fft=nvpl")
    depends_on("nvpl-fft", when="+kokkos+kspace fft_kokkos=nvpl")
    depends_on("voropp", when="+voronoi")
    depends_on("netcdf-c+mpi", when="+netcdf")
    depends_on("blas", when="+atc")
    depends_on("blas", when="+qmmm-xtb")
    depends_on("lapack", when="+atc")
    depends_on("opencl", when="+opencl")
    depends_on("python", when="+python")
    depends_on("python@3.6:", when="@20250402: +python")
    depends_on("mpi", when="+latboltz")
    depends_on("mpi", when="+h5md")
    depends_on("pkg-config", when="+qmmm-xtb")
    depends_on("xtb@6.7:", when="+qmmm-xtb")
    depends_on("mctc-lib", when="+qmmm-xtb")
    depends_on("hdf5", when="+h5md")
    depends_on("jpeg", when="+jpeg")
    depends_on("kim-api", when="+kim")
    depends_on("curl", when="@20190329:+kim")
    depends_on("curl", when="+curl")
    depends_on("libpng", when="+png")
    depends_on("ffmpeg", when="+ffmpeg")
    depends_on("kokkos+shared", when="+kokkos")
    depends_on("kokkos@3.7.01:", when="@20230208: +kokkos")
    depends_on("kokkos@4.3.00:", when="@20240417: +kokkos")
    depends_on("kokkos@4.3.01:", when="@20240627: +kokkos")
    depends_on("kokkos@4.4.01:", when="@20241119: +kokkos")
    depends_on("kokkos@4.5.01:", when="@20250204: +kokkos")
    depends_on("kokkos@4.6.00:", when="@20250402: +kokkos")
    depends_on("kokkos@4.6.02:", when="@20250722: +kokkos")
    depends_on("kokkos@4.7.01:", when="@20251210: +kokkos")
    depends_on("kokkos@5.0.2:", when="@20260211: +kokkos")
    depends_on("kokkos@5.1.0:", when="@20260704: +kokkos")
    depends_on("kokkos@5.2.1:", when="@20260902: +kokkos")
    depends_on("adios2", when="+adios")
    depends_on("plumed", when="+plumed")
    depends_on("eigen@3", when="+machdyn")
    depends_on("pace", when="+ml-pace")
    depends_on("py-cython", when="+ml-iap+python", type="build")
    depends_on("py-mdi", when="+mdi", type=("build", "run"))
    depends_on("py-pip", when="+python", type="build")
    depends_on("py-wheel", when="+python", type="build")
    depends_on("py-build", when="+python", type="build")
    depends_on("py-numpy", when="+python", type=("build", "run"))
    depends_on("py-mpi4py", when="+python+mpi", type=("build", "run"))
    depends_on("py-setuptools@42:", when="@20220217:+python", type=("build", "run"))
    with when("+ml-hdnnp"):
        depends_on("n2p2@2.1.4:")
        depends_on("n2p2+shared", when="+lib")
    depends_on("scafacos", when="+scafacos")
    depends_on("scafacos cflags=-fPIC cxxflags=-fPIC fflags=-fPIC", when="+scafacos+lib")
    depends_on("vtk", when="+vtk")
    depends_on("hipcub", when="~kokkos +rocm")
    depends_on("hipcub@:6", when="@:20260704 ~kokkos +rocm")
    depends_on("llvm-amdgpu ", when="+rocm", type="build")
    # Only needed for llvm-amdgpu@:7.2; later versions build OpenMP.
    depends_on("rocm-openmp-extras", when="+rocm +openmp ^llvm-amdgpu@:7.2", type="build")
    depends_on("llvm-openmp", when="+openmp %apple-clang", type="build")
    depends_on("gsl@2.6:", when="+rheo")
    depends_on("tbb", when="+intel %oneapi")

    # propagate CUDA and ROCm architecture when +kokkos
    for arch in CudaPackage.cuda_arch_values:
        depends_on("kokkos+cuda cuda_arch=%s" % arch, when="+kokkos+cuda cuda_arch=%s" % arch)

    for arch in ROCmPackage.amdgpu_targets:
        depends_on(
            "kokkos+rocm amdgpu_target=%s" % arch, when="+kokkos+rocm amdgpu_target=%s" % arch
        )

    depends_on("googletest", type="test")
    depends_on("libyaml", type="test")

    extends("python", when="+python")

    conflicts(
        "lammps_sizes=smallsmall",
        when="@20250402:",
        msg="smallsmall support has been removed in version 20250402",
    )
    conflicts("+cuda", when="+opencl")
    conflicts("+rocm", when="+opencl")
    conflicts("+python", when="~lib")
    conflicts("+qeq", when="~manybody")
    conflicts("+atc", when="~manybody")
    conflicts("+phonon", when="~kspace")
    conflicts("+qmmm-xtb", when="~kspace")
    conflicts("+dielectric", when="~kspace")
    conflicts("+dielectric", when="@20210728:~extra-pair")
    conflicts("+electrode", when="~kspace")
    conflicts("+ml-iap", when="~ml-snap")
    conflicts(
        "+adios +mpi",
        when="^adios2~mpi",
        msg="With +adios, mpi setting for adios2 and lammps must be the same",
    )
    conflicts(
        "+adios ~mpi",
        when="^adios2+mpi",
        msg="With +adios, mpi setting for adios2 and lammps must be the same",
    )
    conflicts("+intel", when="%aocc@:3.2.9999", msg="+intel with AOCC requires version 4 or newer")
    conflicts("fft=nvpl", when="@:20240829", msg="fft=nvpl requires newer LAMMPS version")
    conflicts(
        "fft_kokkos=nvpl", when="@:20240829", msg="fft_kokkos=nvpl requires newer LAMMPS version"
    )
    conflicts(
        "fft_kokkos=mkl_gpu",
        when="@:20240829",
        msg="fft_kokkos=mkl_gpu requires newer LAMMPS version",
    )

    # Fixed in https://github.com/lammps/lammps/pull/4305
    patch(
        "https://github.com/lammps/lammps/commit/49bdc3e26449634f150602a66d0dab34d09dbc0e.patch?full_index=1",
        sha256="b8d1f08a82329e493e040de2bde9d2291af173a0fe6c7deb24750cc22823c421",
        when="@20240829 %cce",
    )
    # Fixes OpenMP detection with AppleClang https://github.com/lammps/lammps/pull/4550
    patch(
        "https://github.com/lammps/lammps/commit/4e69046e5481f18f6d1402bca04fb3412991eec9.patch?full_index=1",
        sha256="24f5dc45ac603486a023dc7aead5367e44a739e081b91f7da238f10fd5920d96",
        when="@20221103:20250402 +openmp %apple-clang",
    )

    # Older LAMMPS does not compile with Kokkos 5.x
    conflicts(
        "^kokkos@5:",
        when="@:20251210",
        msg="LAMMPS is incompatible with Kokkos 5.x until @20260211",
    )

    # Add large potential files
    resource(
        name="C_10_10.mesocnt",
        url="https://download.lammps.org/potentials/C_10_10.mesocnt",
        sha256="923f600a081d948eb8b4510f84aa96167b5a6c3e1aba16845d2364ae137dc346",
        expand=False,
        placement={"C_10_10.mesocnt": "potentials/C_10_10.mesocnt"},
        when="+mesont",
    )

    root_cmakelists_dir = "cmake"

    def flag_handler(self, name, flags):
        wrapper_flags = []
        build_system_flags = []

        if self.spec.satisfies("+mpi+cuda") or self.spec.satisfies("+mpi+rocm"):
            if self.spec.satisfies("^[virtuals=mpi] cray-mpich"):
                gtl_lib = self.spec["cray-mpich"].package.gtl_lib
                build_system_flags.extend(gtl_lib.get(name) or [])
            # hipcc is not wrapped, we need to pass the flags via the build
            # system.
            build_system_flags.extend(flags)
        else:
            wrapper_flags.extend(flags)

        return (wrapper_flags, [], build_system_flags)

    def cmake_args(self):
        spec = self.spec

        args = [
            self.define_from_variant("BUILD_SHARED_LIBS", "lib"),
            self.define_from_variant("BUILD_MPI", "mpi"),
            self.define_from_variant("BUILD_OMP", "openmp"),
            self.define_from_variant("BUILD_TOOLS", "tools"),
            self.define("ENABLE_TESTING", self.run_tests),
            self.define("DOWNLOAD_POTENTIALS", False),
            self.define_from_variant("PKG_GPU", "gpu"),
        ]

        if spec.satisfies("+gpu"):
            if spec.satisfies("+cuda"):
                args.append(self.define("GPU_API", "cuda"))
                # The GPU package (cmake/Modules/Packages/GPU.cmake) uses
                # the classic find_package(CUDA) module (FindCUDA,
                # deprecated), which reads CUDA_HOST_COMPILER -- a
                # different variable from CMAKE_CUDA_HOST_COMPILER, the one
                # set by the modern enable_language(CUDA) path used for the
                # rest of the build. Because nothing in this recipe sets
                # CUDA_HOST_COMPILER, FindCUDA falls back to its own
                # detection instead of the compiler Spack actually selected
                # for the spec, and any attempt to steer the CUDA host
                # compiler via CMAKE_CUDA_HOST_COMPILER (e.g. to work
                # around a CUDA/GCC version incompatibility) silently has
                # no effect. Set it explicitly so the legacy module stays
                # consistent with the rest of the build.
                args.append(self.define("CUDA_HOST_COMPILER", self.compiler.cxx))
                args.append(self.define_from_variant("GPU_PREC", "gpu_precision"))
                cuda_arch = spec.variants["cuda_arch"].value
                if cuda_arch != "none":
                    if spec.satisfies("@develop"):
                        args.append(self.define("GPU_ARCH", f"{cuda_arch[0]}"))
                    else:
                        args.append(self.define("GPU_ARCH", f"sm_{cuda_arch[0]}"))
                args.append(self.define_from_variant("CUDA_MPS_SUPPORT", "cuda_mps"))
            elif spec.satisfies("+opencl"):
                # LAMMPS downloads and bundles its own OpenCL ICD Loader by default
                args.append(self.define("USE_STATIC_OPENCL_LOADER", False))
                args.append(self.define("GPU_API", "opencl"))
                args.append(self.define_from_variant("GPU_PREC", "gpu_precision"))
            elif spec.satisfies("+rocm"):
                args.append(self.define("GPU_API", "hip"))
                args.append(self.define_from_variant("GPU_PREC", "gpu_precision"))
                if spec.satisfies("@:20260330"):
                    args.append(self.define_from_variant("HIP_ARCH", "amdgpu_target"))
                else:
                    # HIP_ARCH deprecated, use GPU_ARCH instead
                    args.append(self.define_from_variant("GPU_ARCH", "amdgpu_target"))
                # HIP auto-detection can fail on machines without an attached GPU.
                args.append(self.define_from_variant("GPU_TARGETS", "amdgpu_target"))
                args.append(self.define("HIP_USE_DEVICE_SORT", False))

        if spec.satisfies("+kokkos"):
            args.append(self.define("EXTERNAL_KOKKOS", True))
            if spec.satisfies("@20240207: +kokkos+kspace"):
                args.append(self.define_from_variant("FFT_KOKKOS", "fft_kokkos"))

        if spec.satisfies("@20180629:+lib"):
            args.append(self.define("BUILD_LIB", True))

        if spec.satisfies("%aocc"):
            if spec.satisfies("+intel"):
                cxx_flags = (
                    "-O3 -m64 -ffast-math -fno-math-errno -fno-unroll-loops "
                    "-fveclib=AMDLIBM -muse-unaligned-vector-move"
                )
                if spec.satisfies("%aocc@4.1:4.2"):
                    cxx_flags += (
                        " -mllvm -force-gather-overhead-cost=50"
                        " -mllvm -enable-masked-gather-sequence=false"
                    )
                elif spec.satisfies("%aocc@5.0:"):
                    if spec.satisfies("%aocc@5.1:"):
                        cxx_flags += " -mllvm -enable-vector-gathers"
                    else:
                        cxx_flags += " -mllvm -enable-aggressive-gather"
                    if spec.target >= "zen5":
                        cxx_flags += (
                            " -fenable-restrict-based-lv"
                            " -mllvm -vectorizer-maximize-bandwidth=true"
                        )

                # add -fopenmp-simd if OpenMP not already turned on
                if spec.satisfies("~openmp"):
                    cxx_flags += " -fopenmp-simd"
                cxx_flags += " -DLMP_SIMD_COMPILER -DUSE_OMP_SIMD -DLMP_INTEL_USELRT"
            else:
                cxx_flags = "-O3 -mfma -fvectorize -funroll-loops"
            args.append(self.define("CMAKE_CXX_FLAGS_RELEASE", cxx_flags))
            args.append(self.define("CMAKE_CXX_FLAGS_RELWITHDEBINFO", cxx_flags))

        if spec.satisfies("+openmp %apple-clang"):
            args.extend(
                [
                    "-DOpenMP_CXX_LIB_NAMES=" + self.spec["llvm-openmp"].libs.names[0],
                    "-DOpenMP_C_LIB_NAMES=" + self.spec["llvm-openmp"].libs.names[0],
                    "-DOpenMP_CXX_LIBRARIES=" + self.spec["llvm-openmp"].libs[0],
                    "-DOpenMP_CXX_INCLUDE_DIR=" + self.spec["llvm-openmp"].headers.directories[0],
                    "-DOpenMP_omp_LIBRARY=" + self.spec["llvm-openmp"].libs[0],
                ]
            )

        # Overwrite generic cpu tune option
        args.append(self.define("CMAKE_TUNE_FLAGS", microarchitecture_flags(self.spec, "c")))

        args.append(self.define_from_variant("LAMMPS_SIZES", "lammps_sizes"))

        args.append(self.define_from_variant("WITH_JPEG", "jpeg"))
        args.append(self.define_from_variant("WITH_PNG", "png"))
        args.append(self.define_from_variant("WITH_FFMPEG", "ffmpeg"))
        args.append(self.define_from_variant("WITH_CURL", "curl"))

        for pkg, params in self.supported_packages.items():
            if "when" not in params or spec.satisfies(params["when"]):
                opt = "PKG_{0}".format(pkg.replace("-package", "").upper())
                args.append(self.define(opt, "+{0}".format(pkg) in spec))

        if spec.satisfies("+kspace"):
            args.append(self.define_from_variant("FFT", "fft"))
            args.append(self.define_from_variant("FFT_USE_HEFFTE", "heffte"))
            if spec.satisfies("fft=fftw3 ^armpl-gcc") or spec.satisfies("fft=fftw3 ^acfl"):
                args.append(self.define("FFTW3_LIBRARY", self.spec["fftw-api"].libs[0]))
                args.append(
                    self.define("FFTW3_INCLUDE_DIR", self.spec["fftw-api"].headers.directories[0])
                )
            # Using the -DFFT_SINGLE setting trades off a little accuracy
            # for reduced memory use and parallel communication costs
            # for transposing 3d FFT data.
            args.append(self.define("FFT_SINGLE", spec.satisfies("fftw_precision=single")))

        if spec.satisfies("+adios"):
            args.append(self.define("ADIOS2_DIR", self.spec["adios2"].prefix))
        if spec.satisfies("+plumed"):
            args.append(self.define("DOWNLOAD_PLUMED", False))
            if "+shared" in self.spec["plumed"]:
                args.append(self.define("PLUMED_MODE", "shared"))
            else:
                args.append(self.define("PLUMED_MODE", "static"))
        if spec.satisfies("+machdyn"):
            args.append(self.define("DOWNLOAD_EIGEN3", False))
            args.append(self.define("EIGEN3_INCLUDE_DIR", self.spec["eigen"].prefix.include))
        if spec.satisfies("+ml-hdnnp"):
            args.append(self.define("DOWNLOAD_N2P2", False))
            args.append(self.define("N2P2_DIR", self.spec["n2p2"].prefix))

        if spec.satisfies("+rocm"):
            args.append(self.define("CMAKE_CXX_COMPILER", spec["hip"].hipcc))
            args.append(self.define("HIP_PATH", spec["hip"].prefix))

        return args

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        if self.spec.satisfies("+intel %aocc"):
            env.append_flags("LDFLAGS", "-lalm -lm")

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        env.set("LAMMPS_POTENTIALS", self.prefix.share.lammps.potentials)
        if self.spec.satisfies("+python"):
            if self.spec.platform == "darwin":
                env.prepend_path("DYLD_FALLBACK_LIBRARY_PATH", self.prefix.lib)
                env.prepend_path("DYLD_FALLBACK_LIBRARY_PATH", self.prefix.lib64)
            else:
                env.prepend_path("LD_LIBRARY_PATH", self.prefix.lib)
                env.prepend_path("LD_LIBRARY_PATH", self.prefix.lib64)
        if self.spec.satisfies("+plugin"):
            env.prepend_path("LAMMPS_PLUGIN_PATH", self.prefix.lib.lammps.plugins)
            env.prepend_path("LAMMPS_PLUGIN_PATH", self.prefix.lib64.lammps.plugins)

    @run_after("install")
    def make_plugins_directories(self):
        os.makedirs(self.prefix.lib.lammps.plugins, exist_ok=True)
        os.makedirs(self.prefix.lib64.lammps.plugins, exist_ok=True)

    @run_after("install")
    def install_python(self):
        # do LAMMPS Python package installation using pip
        if self.spec.satisfies("@20230328: +python"):
            with working_dir("python"):
                os.environ["LAMMPS_VERSION_FILE"] = join_path(
                    self.stage.source_path, "src", "version.h"
                )
                pip(*PythonPipBuilder.std_args(), f"--prefix={self.prefix}", ".")
