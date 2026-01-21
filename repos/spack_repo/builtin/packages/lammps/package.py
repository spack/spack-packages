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
    version("20251210", sha256="175afc62a7314970d56e93b54745f4e6132e8f688155fff3dd70b298ec077c0e")
    version("20250910", sha256="475d5cda1b289ca3b3dcc97c1ee199f67fa6ad736951213e9b6ec08069d70f0c")
    version(
        "20250722.2",
        sha256="fede484269cdb22f1cb738b4cd118a9bf9cb4bd3c85667f1e6a73a9fa5c2de6b",
        preferred=True,
    )
    version(
        "20250722.1",
        sha256="4ba3648fae360ea1d3106e08bce13e21f856318196f4965f2a09fd812d572928",
        deprecated=True,
    )
    version(
        "20250722",
        sha256="38d7ab508433f33a53e11f0502aa0253945ce45d5595baf69665961c0a76da26",
        deprecated=True,
    )
    version(
        "20250612",
        sha256="b3fe6dc57115edb89d022879fe676503ec88b4e12cfee3488cc2f43cb0957ba7",
        deprecated=True,
    )
    version(
        "20250402",
        sha256="5087ebd6b00cd44a7d73303d49685668f6effa76dc375912f7f75db558b39bca",
        deprecated=True,
    )
    version(
        "20250204",
        sha256="a4cb0a58451d47ac31ee3e1f148d92f445298d6e27f2d06f161b9b4168d79eb1",
        deprecated=True,
    )
    version(
        "20240829.4", sha256="e7d6d60b94ada5acc2e1e9966ae12547fd550d6967d4511b8655c77e24878728"
    )
    version(
        "20230802.4", sha256="6eed007cc24cda80b5dd43372b2ad4268b3982bb612669742c8c336b79137b5b"
    )
    version(
        "20220623.4", sha256="42541b4dbd0d339d16ddb377e76d192bc3d1d5712fdf9e2cdc838fc980d0a0cf"
    )
    version(
        "20210929.3", sha256="e4c274f0dc5fdedc43f2b365156653d1105197a116ff2bafe893523cdb22532e"
    )
    version("20201029", sha256="759705e16c1fedd6aa6e07d028cc0c78d73c76b76736668420946a74050c3726")
    version("20200303", sha256="a1a2e3e763ef5baecea258732518d75775639db26e60af1634ab385ed89224d1")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    # ml-quip require Fortran, but not available in Spack
    for fc_pkg in ("kim", "scafacos"):
        depends_on("fortran", type="build", when=f"+{fc_pkg}")

    stable_versions = {
        "20250722.2",
        "20250722.1",
        "20250722",
        "20240829.4",
        "20230802.4",
        "20220623.4",
        "20210929.3",
        "20201029",
        "20200303",
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
        "cg-sdk": {"when": "@20210702:20220623"},
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
        "h5md": {"when": "@20210702:"},
        "intel": {"when": "@20210702:"},
        "interlayer": {"when": "@20210728:"},
        "kim": {},
        "kokkos": {"when": "@20201029:"},
        "kspace": {"default": True},
        "latboltz": {"when": "@20210702:"},
        "latte": {"when": "@20170922:20230328"},
        "lepton": {"when": "@20230208:"},
        "machdyn": {"when": "@20210702:"},
        "manifold": {"when": "@20210702:"},
        "manybody": {"default": True},
        "mc": {},
        "mdi": {"when": "@20210702:"},
        "meam": {"when": "@:20181212,20210702:"},
        "mesont": {"when": "@20210702:"},
        "mgpt": {"when": "@20210702:"},
        "misc": {},
        "ml-hdnnp": {"when": "@20210702:"},
        "ml-iap": {"when": "@20210702:"},
        "ml-pace": {"when": "@20210702:"},
        "ml-pod": {"when": "@20221222:"},
        "ml-rann": {"when": "@20210702:"},
        "ml-snap": {"when": "@20210702:"},
        "ml-uf3": {"when": "@20240627:"},
        "mliap": {"when": "@20200630:20210527"},
        "mofff": {"when": "@20210702:"},
        "molecule": {"default": True},
        "molfile": {"when": "@20210702:"},
        "mpiio": {"when": "@:20230802.1"},
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
        "reaction": {"when": "@20210702:"},
        "reax": {"when": "@:20181212"},
        "reaxff": {"when": "@20210702:"},
        "rheo": {"when": "@20240829:"},
        "replica": {},
        "rigid": {"default": True},
        "scafacos": {"when": "@20210702:"},
        "shock": {},
        "smtbq": {"when": "@20210702:"},
        "snap": {"when": "@:20210527"},
        "sph": {"when": "@20210702:"},
        "spin": {"when": "@20180629:"},
        "srd": {},
        "tally": {"when": "@20210702:"},
        "uef": {"when": "@20210702:"},
        "user-adios": {"when": "@20190228:20210527"},
        "user-atc": {"when": "@:20210527"},
        "user-awpmd": {"when": "@:20210527"},
        "user-bocs": {"when": "@20180511:20210527"},
        "user-brownian": {"when": "@20210514:20210527"},
        "user-cgsdk": {"when": "@20170504:20210527"},
        "user-colvars": {"when": "@:20210527"},
        "user-diffraction": {"when": "@:20210527"},
        "user-dpd": {"when": "@:20210527"},
        "user-drude": {"when": "@:20210527"},
        "user-eff": {"when": "@:20210527"},
        "user-fep": {"when": "@:20210527"},
        "user-h5md": {"when": "@:20210527"},
        "user-hdnnp": {"when": "@20210527"},
        "user-intel": {"when": "@:20210527"},
        "user-lb": {"when": "@:20210527"},
        "user-manifold": {"when": "@:20210527"},
        "user-meamc": {"when": "@20170706:20210527"},
        "user-mesodpd": {"when": "@20200319:20210527"},
        "user-mesont": {"when": "@20200615:20210527"},
        "user-mgpt": {"when": "@:20210527"},
        "user-misc": {"when": "@:20210702"},
        "user-mofff": {"when": "@20180205:20210527"},
        "user-molfile": {"when": "@:20210527"},
        "user-netcdf": {"when": "@20170504:20210527"},
        "user-omp": {"when": "@:20210527"},
        "user-phonon": {"when": "@:20210527"},
        "user-plumed": {"when": "@20181109:20210527"},
        "user-ptm": {"when": "@20181010:20210527"},
        "user-qtb": {"when": "@:20210527"},
        "user-rann": {"when": "@20210527"},
        "user-reaction": {"when": "@20200319:20210527"},
        "user-reaxc": {"when": "@:20210527"},
        "user-sdpd": {"when": "@20181109:20210527"},
        "user-smd": {"when": "@:20210527"},
        "user-smtbq": {"when": "@:20210527"},
        "user-sph": {"when": "@:20210527"},
        "user-tally": {"when": "@:20210527"},
        "user-uef": {"when": "@20171023:20210527"},
        "user-vtk": {"when": "@20210527"},
        "user-yaff": {"when": "@20190201:20210527"},
        "voronoi": {},
        "vtk": {"when": "@20210702:"},
        "yaff": {"when": "@20210702:"},
        # "ml-quip": {"when": "@20210702:"}, no quip package
        # "user-quip": {"when": "@20190201:20210527"}, no quip package
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
        "exceptions",
        default=False,
        description="Build with lammps exceptions",
        when="@:20230802.1",
    )
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
    variant(
        "gpu_precision",
        default="mixed",
        when="~kokkos",
        description="Select GPU precision (used by GPU package)",
        values=("double", "mixed", "single"),
        multi=False,
    )
    variant("tools", default=False, description="Build LAMMPS tools (msi2lmp, binary2txt, chain)")

    depends_on("cmake@3.16:", when="@20231121:", type="build")
    depends_on("cmake@3.20:", when="@20250910:", type="build")
    depends_on("mpi", when="+mpi")
    depends_on("mpi", when="+mpiio")
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
    depends_on("netcdf-c+mpi", when="+user-netcdf")
    depends_on("netcdf-c+mpi", when="+netcdf")
    depends_on("blas", when="+user-atc")
    depends_on("blas", when="+atc")
    depends_on("lapack", when="+user-atc")
    depends_on("lapack", when="+atc")
    depends_on("opencl", when="+opencl")
    depends_on("latte@1.0.1", when="@:20180222+latte")
    depends_on("latte@1.1.1:", when="@20180316:20180628+latte")
    depends_on("latte@1.2.1:", when="@20180629:20200505+latte")
    depends_on("latte@1.2.2:", when="@20200602:20230328+latte")
    depends_on("blas", when="+latte")
    depends_on("lapack", when="+latte")
    depends_on("python", when="+python")
    depends_on("python@3.6:", when="@20250402: +python")
    depends_on("mpi", when="+user-lb")
    depends_on("mpi", when="+latboltz")
    depends_on("mpi", when="+user-h5md")
    depends_on("mpi", when="+h5md")
    depends_on("hdf5", when="+user-h5md")
    depends_on("hdf5", when="+h5md")
    depends_on("jpeg", when="+jpeg")
    depends_on("kim-api", when="+kim")
    depends_on("curl", when="@20190329:+kim")
    depends_on("curl", when="+curl")
    depends_on("libpng", when="+png")
    depends_on("ffmpeg", when="+ffmpeg")
    depends_on("kokkos+shared@3.1:", when="@20200505:+kokkos")
    depends_on("kokkos@3.7.01:", when="@20230208: +kokkos")
    depends_on("kokkos@4.3.00:", when="@20240417: +kokkos")
    depends_on("kokkos@4.3.01:", when="@20240627: +kokkos")
    depends_on("kokkos@4.4.01:", when="@20241119: +kokkos")
    depends_on("kokkos@4.5.01:", when="@20250204: +kokkos")
    depends_on("kokkos@4.6.00:", when="@20250402: +kokkos")
    depends_on("kokkos@4.6.02:", when="@20250722: +kokkos")
    depends_on("kokkos@4.7.01:", when="@20251210: +kokkos")
    depends_on("adios2", when="+user-adios")
    depends_on("adios2", when="+adios")
    depends_on("plumed", when="+user-plumed")
    depends_on("plumed", when="+plumed")
    depends_on("eigen@3", when="+user-smd")
    depends_on("eigen@3", when="+machdyn")
    depends_on("pace", when="+ml-pace")
    depends_on("py-cython", when="+mliap+python", type="build")
    depends_on("py-cython", when="+ml-iap+python", type="build")
    depends_on("py-mdi", when="+mdi", type=("build", "run"))
    depends_on("py-pip", when="+python", type="build")
    depends_on("py-wheel", when="+python", type="build")
    depends_on("py-build", when="+python", type="build")
    depends_on("py-numpy", when="+python", type=("build", "run"))
    depends_on("py-mpi4py", when="+python+mpi", type=("build", "run"))
    depends_on("py-setuptools@42:", when="@20220217:+python", type=("build", "run"))
    for _n2p2_cond in ("+user-hdnnp", "+ml-hdnnp"):
        with when(_n2p2_cond):
            depends_on("n2p2@2.1.4:")
            depends_on("n2p2+shared", when="+lib")
    depends_on("scafacos", when="+scafacos")
    depends_on("scafacos cflags=-fPIC cxxflags=-fPIC fflags=-fPIC", when="+scafacos+lib")
    depends_on("vtk", when="+user-vtk")
    depends_on("vtk", when="+vtk")
    depends_on("hipcub", when="~kokkos +rocm")
    depends_on("hipcub@:6", when="@:20250722 ~kokkos +rocm")
    depends_on("llvm-amdgpu ", when="+rocm", type="build")
    depends_on("rocm-openmp-extras", when="+rocm +openmp", type="build")
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
    conflicts("+body", when="+poems@:20180628")
    conflicts("+python", when="~lib")
    conflicts("+qeq", when="~manybody")
    conflicts("+user-atc", when="~manybody")
    conflicts("+atc", when="~manybody")
    conflicts("+user-misc", when="~manybody")
    conflicts("+user-phonon", when="~kspace")
    conflicts("+phonon", when="~kspace")
    conflicts("%gcc@9:", when="@:20200303+openmp")
    conflicts("+dielectric", when="~kspace")
    conflicts("+dielectric", when="@:20210702~user-misc")
    conflicts("+dielectric", when="@20210728:~extra-pair")
    conflicts("+electrode", when="~kspace")
    conflicts("+mliap", when="~snap")
    conflicts("+ml-iap", when="~ml-snap")
    conflicts(
        "+user-adios +mpi",
        when="^adios2~mpi",
        msg="With +user-adios, mpi setting for adios2 and lammps must be the same",
    )
    conflicts(
        "+user-adios ~mpi",
        when="^adios2+mpi",
        msg="With +user-adios, mpi setting for adios2 and lammps must be the same",
    )
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
    conflicts(
        "~kokkos+rocm",
        when="@:20220602",
        msg="ROCm builds of the GPU package not maintained prior to version 20220623",
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

    # Backport of https://github.com/lammps/lammps/pull/3726
    conflicts("+kokkos+rocm+kspace", when="@:20210929.3")
    patch(
        "https://github.com/lammps/lammps/commit/ebb8eee941e52c98054fdf96ea78ee4d5f606f47.patch?full_index=1",
        sha256="3dedd807f63a21c543d1036439099f05c6031fd98e7cb1ea7825822fc074106e",
        when="@20220623.3:20230208 +kokkos +rocm +kspace",
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

    # Older LAMMPS does not compile with Kokkos 4.x
    conflicts(
        "^kokkos@4:",
        when="@:20230802.1",
        msg="LAMMPS is incompatible with Kokkos 4.x until @20230802.1",
    )

    patch("lib.patch", when="@20170901")
    patch("660.patch", when="@20170922")
    patch("gtest_fix.patch", when="@:20210310 %aocc@3.2.0")

    # This patch merged to LAMMPS trunk at 20221222 and backported to
    # stable version 20220623.4. We still patch all other affected
    # versions here
    patch("intel-aocc.patch", when="@20220324:20220623.3,20220803:20221103 +intel %aocc")

    patch(
        "https://github.com/lammps/lammps/commit/562300996285fdec4ef74542383276898555af06.patch?full_index=1",
        sha256="e6f1b62bbfdc79d632f4cea98019202d0dd25aa4ae61a70df1164cb4f290df79",
        when="@20200721 +cuda",
    )
    patch("hip_cmake.patch", when="@20220623:20221222 ~kokkos+rocm")

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

        mpi_prefix = "ENABLE"
        pkg_prefix = "ENABLE"
        if spec.satisfies("@20180629:"):
            mpi_prefix = "BUILD"
            pkg_prefix = "PKG"

        args = [
            self.define_from_variant("BUILD_SHARED_LIBS", "lib"),
            self.define_from_variant("LAMMPS_EXCEPTIONS", "exceptions"),
            self.define_from_variant("{}_MPI".format(mpi_prefix), "mpi"),
            self.define_from_variant("BUILD_OMP", "openmp"),
            self.define_from_variant("BUILD_TOOLS", "tools"),
            self.define("ENABLE_TESTING", self.run_tests),
            self.define("DOWNLOAD_POTENTIALS", False),
        ]
        if spec.satisfies("~kokkos"):
            # LAMMPS can be build with the GPU package OR the KOKKOS package
            # Using both in a single build is discouraged.
            # +cuda only implies that one of the two is used
            # by default it will use the GPU package if kokkos wasn't enabled
            if spec.satisfies("+cuda"):
                args.append(self.define("PKG_GPU", True))
                args.append(self.define("GPU_API", "cuda"))
                args.append(self.define_from_variant("GPU_PREC", "gpu_precision"))
                cuda_arch = spec.variants["cuda_arch"].value
                if cuda_arch != "none":
                    args.append(self.define("GPU_ARCH", "sm_{0}".format(cuda_arch[0])))
                args.append(self.define_from_variant("CUDA_MPS_SUPPORT", "cuda_mps"))
            elif spec.satisfies("+opencl"):
                # LAMMPS downloads and bundles its own OpenCL ICD Loader by default
                args.append(self.define("USE_STATIC_OPENCL_LOADER", False))
                args.append(self.define("PKG_GPU", True))
                args.append(self.define("GPU_API", "opencl"))
                args.append(self.define_from_variant("GPU_PREC", "gpu_precision"))
            elif spec.satisfies("+rocm"):
                args.append(self.define("PKG_GPU", True))
                args.append(self.define("GPU_API", "hip"))
                args.append(self.define_from_variant("GPU_PREC", "gpu_precision"))
                args.append(self.define_from_variant("HIP_ARCH", "amdgpu_target"))
            else:
                args.append(self.define("PKG_GPU", False))
        else:
            args.append(self.define("EXTERNAL_KOKKOS", True))
            if spec.satisfies("@20240207: +kokkos+kspace"):
                args.append(self.define_from_variant("FFT_KOKKOS", "fft_kokkos"))

        if spec.satisfies("@20180629:+lib"):
            args.append(self.define("BUILD_LIB", True))

        if spec.satisfies("%aocc"):
            if spec.satisfies("+intel"):
                cxx_flags = (
                    "-O3 -fno-math-errno -fno-unroll-loops "
                    "-fveclib=AMDLIBM -muse-unaligned-vector-move"
                )
                if spec.satisfies("%aocc@4.1:4.2"):
                    cxx_flags += (
                        " -mllvm -force-gather-overhead-cost=50"
                        " -mllvm -enable-masked-gather-sequence=false"
                    )
                elif spec.satisfies("%aocc@5.0:"):
                    cxx_flags += " -mllvm -enable-aggressive-gather"
                    if spec.target >= "zen5":
                        cxx_flags += " -fenable-restrict-based-lv"

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
                opt = "{0}_{1}".format(pkg_prefix, pkg.replace("-package", "").upper())
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

        if spec.satisfies("+user-adios") or spec.satisfies("+adios"):
            args.append(self.define("ADIOS2_DIR", self.spec["adios2"].prefix))
        if spec.satisfies("+user-plumed") or spec.satisfies("+plumed"):
            args.append(self.define("DOWNLOAD_PLUMED", False))
            if "+shared" in self.spec["plumed"]:
                args.append(self.define("PLUMED_MODE", "shared"))
            else:
                args.append(self.define("PLUMED_MODE", "static"))
        if spec.satisfies("+user-smd") or spec.satisfies("+machdyn"):
            args.append(self.define("DOWNLOAD_EIGEN3", False))
            args.append(self.define("EIGEN3_INCLUDE_DIR", self.spec["eigen"].prefix.include))
        if spec.satisfies("+user-hdnnp") or spec.satisfies("+ml-hdnnp"):
            args.append(self.define("DOWNLOAD_N2P2", False))
            args.append(self.define("N2P2_DIR", self.spec["n2p2"].prefix))

        if spec.satisfies("+rocm"):
            args.append(self.define("CMAKE_CXX_COMPILER", spec["hip"].hipcc))
            if spec.satisfies("@:20231121"):
                if spec.satisfies("^hip@:5.4"):
                    args.append(self.define("HIP_PATH", f"{spec['hip'].prefix}/hip"))
                elif spec.satisfies("^hip@5.5:"):
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
                pip(*PythonPipBuilder.std_args(self), f"--prefix={self.prefix}", ".")
