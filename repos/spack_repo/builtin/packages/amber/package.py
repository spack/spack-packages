# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import shutil

from spack_repo.builtin.build_systems import cmake, generic
from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Amber(CMakePackage, Package, CudaPackage):
    """Amber is a suite of biomolecular simulation programs.

    A manual download is required: Amber is distributed under a license
    agreement (https://ambermd.org/GetAmber.php), so Spack cannot fetch the
    sources itself. Spack will search your current directory for the download
    files. Alternatively, add the files to a mirror so that Spack can find
    them. For instructions on how to set up a mirror, see
    https://spack.readthedocs.io/en/latest/mirrors.html

    * ``Amber18.tar.bz2`` (+ ``AmberTools19.tar.bz2``)
    * ``Amber20.tar.bz2`` (+ ``AmberTools21.tar.bz2``)
    * ``pmemd26_tar.bz2``

    Note: Only certain versions of ambertools are compatible with amber.
    Only the latter version of ambertools for each amber version is supported."""

    homepage = "https://ambermd.org/"
    manual_download = True

    def url_for_version(self, version):
        if version >= Version("26"):
            return "file://{0}/pmemd{1}.tar.bz2".format(os.getcwd(), version)
        return "file://{0}/Amber{1}.tar.bz2".format(os.getcwd(), version)

    maintainers("hseara")

    # The Amber license does not allow redistribution of the sources or of
    # binaries built from them.
    redistribute(source=False, binary=False)

    # Amber26: PMEMD-only source distribution. The archive is named
    # ``pmemd26_tar.bz2``; Spack would otherwise treat it as a bare bzip2 file
    # instead of a tarball, so spell out the extension.
    version(
        "26",
        sha256="0478ccce892f3525e995e9c85458d552c6060b73dd28acd03c366e61ecf23a14",
        extension="tar.bz2",
    )
    version("20", sha256="a4c53639441c8cc85adee397933d07856cc4a723c82c6bea585cd76c197ead75")
    version("18", sha256="2060897c0b11576082d523fb63a51ba701bc7519ff7be3d299d5ec56e8e6e277")

    build_system(
        conditional("cmake", when="@26:"),
        conditional("generic", when="@:20"),
        default="cmake",
    )

    for ver, ambertools_ver, ambertools_checksum in (
        # (version amber, version ambertools, sha256sum)
        (
            "20",
            "21",
            "f55fa930598d5a8e9749e8a22d1f25cab7fcf911d98570e35365dd7f262aaafd",
        ),
        (
            "18",
            "19",
            "0c86937904854b64e4831e047851f504ec45b42e593db4ded92c1bee5973e699",
        ),
    ):
        resource(
            when="@{0}".format(ver),
            name="AmberTools",
            url="file://{0}/AmberTools{1}.tar.bz2".format(os.getcwd(), ambertools_ver),
            sha256=ambertools_checksum,
            destination="",
            placement="ambertools_tmpdir",
        )

    for ver, num, checksum in (
        ("20", "1", "10780cb91a022b49ffdd7b1e2bf4a572fa4edb7745f0fc4e5d93b158d6168e42"),
        ("20", "2", "9c973e3f8f33a271d60787e8862901e8f69e94e7d80cda1695f7fad7bc396093"),
        ("20", "3", "acb359dc9b1bcff7e0f1965baa9f3f3dc18eeae99c49f1103c1e2986c0bbeed8"),
        ("20", "4", "fd93c74f5ec80689023648cdd12b2c5fb21a3898c81ebc3fa256ef244932562a"),
        ("20", "5", "8e46d5be28c002f560050a71f4851b01ef45a3eb66ac90d7e23553fae1370e68"),
        ("20", "6", "8cf9707b3d08ad9242326f02d1861831ad782c9bfb0c46e7b1f0d4640571d5c1"),
        ("20", "7", "143b6a09f774aeae8b002afffb00839212020139a11873a3a1a34d4a63fa995d"),
        ("20", "8", "a6fc6d5c8ba0aad3a8afe44d1539cc299ef78ab53721e28244198fd5425d14ad"),
        ("20", "9", "5ce6b534bab869b1e9bfefa353d7f578750e54fa72c8c9d74ddf129d993e78cf"),
        (
            "20",
            "10",
            "76a683435be7cbb860f5bd26f09a0548c2e77c5a481fc6d64b55a3a443ce481d",
        ),
        (
            "20",
            "11",
            "f40b3612bd3e59efa2fa1ec06ed6fd92446ee0f1d5d99d0f7796f66b18e64060",
        ),
        (
            "20",
            "12",
            "194119aed03f80677c4bab78a20fc09b0b3dc17c41a57c5eb3c912b2d73b18ab",
        ),
        ("18", "1", "3cefac9a24ece99176d5d2d58fea2722de3e235be5138a128428b9260fe922ad"),
        ("18", "2", "3a0707a9a59dcbffa765dcf87b68001450095c51b96ec39d21260ba548a2f66a"),
        ("18", "3", "24c2e06f71ae553a408caa3f722254db2cbf1ca4db274542302184e3d6ca7015"),
        ("18", "4", "51de613e8fda20cc92979265cf7179288df8c1af4202f02794ad7327fda2657b"),
        ("18", "5", "c70354bfa312603e4819efce11a242ddcc3830895453d9424f0c83f7ae98bc5b"),
        ("18", "6", "3450433a8697b27e43172043be68d31515a7c7c00b2b248f84043dd70a2f59a8"),
        ("18", "7", "10ba41422b7a3eb5b32bc6453231100544cf620c764ab8332c629a3b9fc749d4"),
        ("18", "8", "73968dc0fd99bcbd5eae2223bd54f414879c062ac933948ba6b8b67383dc6a53"),
        ("18", "9", "e7d72fa31560f1e8ea572b8c73259d9fe512f56fbeb1b58ae014c43b9b5b6290"),
        (
            "18",
            "10",
            "1bee419a3b0b686a729aa12515b0f96a9a8f43478ca2c01ea1661cc1698c6266",
        ),
        (
            "18",
            "11",
            "926557f0c137ea8dbf99a0487b25e131b12dfd39977d3e515f01f49187e6a09c",
        ),
        (
            "18",
            "12",
            "7e2645d539d257f7064808308048622818c9083dedfa4ac0a958cd15181231ac",
        ),
        (
            "18",
            "13",
            "95d2e33d0d05b8f9b6d8091d1c804271ec3a69e9aef792cc3b1ab8a2165eca3e",
        ),
        (
            "18",
            "14",
            "a1adfb072f60ffcb67adb589df7c5578629441bee4ccb89ab635a6e8d7a35277",
        ),
        (
            "18",
            "15",
            "4deb3df329c05729561dcc7310e49059eaddc504c4210ad31fad11dc70f61742",
        ),
        (
            "18",
            "16",
            "cf02f9b949127363bad1aa700ab662a3c7cf9ce0e2e4750e066d2204b9500a99",
        ),
        (
            "18",
            "17",
            "480300f949e0dd6402051810a9714adb388cf96e454a55346c76954cdd69413d",
        ),
    ):
        patch_url_str = "https://ambermd.org/bugfixes/{0}.0/update.{1}"
        patch(
            patch_url_str.format(ver, num),
            sha256=checksum,
            level=0,
            when="@{0}".format(ver),
        )

    # Patch to move the namelist sebomd after the variable declarations
    # Taken from http://archive.ambermd.org/202105/0098.html
    patch("sebomd_fix.patch", when="@20")

    # Patch to add ppc64le in config.guess
    patch("ppc64le.patch", when="@18:20 target=ppc64le:")

    # Patch to add aarch64 in config.guess
    patch("aarch64.patch", when="@18:20 target=aarch64:")

    # Workaround to modify the AmberTools script when using the NVIDIA
    # compilers
    patch("nvhpc.patch", when="@18:20 %nvhpc")

    # Workaround to use NVIDIA compilers to build the bundled Boost
    patch("nvhpc-boost.patch", when="@18:20 %nvhpc")

    variant("mpi", description="Build MPI executables", default=True)
    variant("openmp", description="Use OpenMP pragmas to parallelize", default=False)
    variant("x11", description="Build programs that require X11", default=False, when="@:20")
    variant(
        "update",
        description="Update the sources prior compilation",
        default=False,
        when="@:20",
    )
    variant(
        "nccl",
        default=False,
        when="@26: +cuda",
        description="Use NCCL for inter-GPU communication in pmemd.cuda.MPI",
    )
    variant(
        "plumed",
        default=False,
        when="@26:",
        description="Link PLUMED for enhanced-sampling / free-energy methods",
    )
    variant(
        "mkl",
        default=False,
        when="@26:",
        description="Use Intel MKL for BLAS/LAPACK and for the CPU X-ray restraint FFT "
        "(without it, X-ray restraints are disabled in the CPU pmemd)",
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")

    depends_on("zlib-api")
    depends_on("bzip2")
    depends_on("flex", type="build")
    depends_on("bison", type="build")
    depends_on("netcdf-fortran")
    # Potential issues with openmpi 4
    # (http://archive.ambermd.org/201908/0105.html)
    depends_on("mpi", when="+mpi")

    # Amber 18 / 20
    depends_on("parallel-netcdf", when="@20")  # when='AmberTools@21:'
    depends_on("tcsh", type=("build"), when="@20")  # when='AmberTools@21:'
    # Cuda dependencies
    # /AmberTools/src/configure2:1329
    depends_on("cuda@:11.1", when="@20+cuda")  # when='AmberTools@21:'
    depends_on("cuda@:10.2.89", when="@18+cuda")
    depends_on("gmake", type="build", when="@:20")

    # Amber 26+
    depends_on("cmake@3.8.1:", type="build", when="@26:")
    depends_on("netcdf-c", when="@26:")
    # MKL replaces BLAS/LAPACK when enabled.
    depends_on("blas", when="@26: ~mkl")
    depends_on("lapack", when="@26: ~mkl")
    depends_on("mkl", when="+mkl")
    # Amber's CudaConfig.cmake only knows how to configure CUDA 7.5 - 12.8
    # (and hard-codes the -gencode list per CUDA version). Anything older than
    # 11.0 lacks the targets Amber26 expects.
    depends_on("cuda@11.0:12.8", when="@26:+cuda")
    depends_on("nccl", when="+nccl")
    for _arch in CudaPackage.cuda_arch_values:
        depends_on(f"nccl cuda_arch={_arch}", when=f"+nccl cuda_arch={_arch}")
    # PLUMED >= 2.5 is required for build-time linking.
    depends_on("plumed@2.5:", when="+plumed")

    conflicts(
        "+x11",
        when="@:20 platform=cray",
        msg="x11 amber applications not available for cray",
    )
    conflicts("+openmp", when="@:20 %clang", msg="OpenMP not available for the clang compiler")
    conflicts(
        "+openmp",
        when="@:20 %apple-clang",
        msg="OpenMP not available for the Apple clang compiler",
    )
    conflicts(
        "+openmp",
        when="@26: ~mpi",
        msg="Amber26 only builds an OpenMP pmemd together with MPI (pmemd.OMP.MPI)",
    )

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        env.set("AMBER_PREFIX", self.prefix)
        env.set("AMBERHOME", self.prefix)
        if self.spec.satisfies("@:20 +cuda"):
            env.prepend_path("LD_LIBRARY_PATH", self.spec["cuda"].prefix.lib)


class CMakeBuilder(cmake.CMakeBuilder):
    """Amber 26+ (PMEMD-only source distribution)."""

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        spec = self.pkg.spec
        if spec.satisfies("+nccl"):
            # FindNCCL.cmake looks in $NCCL_HOME/{include,lib}
            env.set("NCCL_HOME", spec["nccl"].prefix)
        if spec.satisfies("+mkl"):
            # FindMKL.cmake picks the MKL root up from the environment
            env.set("MKLROOT", spec["mkl"].prefix)

    def _compiler_id(self):
        spec = self.pkg.spec
        if spec.satisfies("%gcc"):
            return "GNU"
        if spec.satisfies("%oneapi") or spec.satisfies("%intel-oneapi-compilers"):
            return "ONEAPI"
        if spec.satisfies("%intel"):
            return "INTEL"
        if spec.satisfies("%nvhpc"):
            return "PGI"
        if spec.satisfies("%cce"):
            return "CRAY"
        if spec.satisfies("%clang") or spec.satisfies("%apple-clang"):
            return "CLANG"
        return "AUTO"

    def cmake_args(self):
        spec = self.pkg.spec
        netcdf_f = spec["netcdf-fortran"]

        args = [
            "-Wno-dev",
            self.define("COMPILER", self._compiler_id()),
            self.define("PMEMD_ONLY", True),
            self.define("BUILD_PYTHON", False),
            self.define("BUILD_PERL", False),
            self.define("BUILD_GUI", False),
            self.define("DOWNLOAD_MINICONDA", False),
            self.define("CHECK_UPDATES", False),
            self.define("INSTALL_TESTS", False),
            self.define("PGM", False),
            self.define("USE_FFT", False),
            self.define_from_variant("MPI", "mpi"),
            self.define_from_variant("OPENMP", "openmp"),
            self.define("PMEMD_OMP_MPI", spec.satisfies("+mpi+openmp")),
            self.define_from_variant("CUDA", "cuda"),
        ]

        external = ["netcdf", "netcdf-fortran"]

        args.append(self.define("NetCDF_INCLUDES_F90", netcdf_f.prefix.include))
        args.append(self.define("NetCDF_LIBRARIES_F90", netcdf_f.libs[0]))

        if spec.satisfies("+mkl"):
            external.append("mkl")
            args.append(self.define("MKL_MULTI_THREADED", False))
            args.append(self.define("PMEMD_XRAY_CPU_FFT_BACKEND", "MKL"))
        else:
            external += ["blas", "lapack"]
            args.append(self.define("BLAS_LIBRARIES", spec["blas"].libs.joined(";")))
            args.append(self.define("LAPACK_LIBRARIES", spec["lapack"].libs.joined(";")))
            args.append(self.define("PMEMD_XRAY_CPU_FFT_BACKEND", "NONE"))

        if spec.satisfies("+plumed"):
            external.append("plumed")
        else:
            args.append(self.define("FORCE_DISABLE_LIBS", "plumed"))

        args.append(self.define("FORCE_EXTERNAL_LIBS", ";".join(external)))

        if spec.satisfies("+cuda"):
            args.append(self.define("NCCL", spec.satisfies("+nccl")))

        return args


class GenericBuilder(generic.GenericBuilder):
    """Amber 18 / 20 (classic Amber + AmberTools ``./configure`` build)."""

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        pkg = self.pkg
        amber_src = pkg.stage.source_path
        env.set("AMBERHOME", amber_src)

        env.prepend_path("CPATH", pkg.spec["bzip2"].prefix.include)

        if pkg.spec.satisfies("+cuda"):
            env.set("CUDA_HOME", pkg.spec["cuda"].prefix)

    def install(self, pkg, spec, prefix):
        install_tree("ambertools_tmpdir", ".")
        shutil.rmtree(join_path(pkg.stage.source_path, "ambertools_tmpdir"))

        if spec.satisfies("%gcc@14:"):
            filter_file(
                r"static void delete_punctuation\(\);",
                "static void delete_punctuation(char *obuf, char *ibuf, int *bufLen);",
                "AmberTools/src/cifparse/cifparse.l",
            )

        if spec.satisfies("%cce"):
            compiler = "cray"
        elif spec.satisfies("%gcc"):
            compiler = "gnu"
        elif spec.satisfies("%intel"):
            compiler = "intel"
        elif spec.satisfies("%nvhpc"):
            compiler = "pgi"
        elif spec.satisfies("%clang"):
            compiler = "clang"
        else:
            raise InstallError("Unknown compiler, exiting!!!")

        filter_file(
            r"-x /bin/csh",
            "command -v csh &> /dev/null/",
            "AmberTools/src/configure2",
            string=True,
        )

        conf = Executable("./configure")
        base_args = ["--skip-python", "--with-netcdf", spec["netcdf-fortran"].prefix]
        if spec.satisfies("~x11"):
            base_args += ["-noX11"]

        if spec.satisfies("+update"):
            update = Executable("./update_amber")
            update(*(["--update"]))
        else:
            base_args += ["--no-updates"]

        if spec.target.family != "x86_64":
            base_args += ["-nosse"]

        conf(*(base_args + [compiler]))
        make("install", parallel=False)

        if spec.satisfies("+cuda"):
            conf(*(base_args + ["-cuda", compiler]))
            make("install", parallel=False)

        if spec.satisfies("+mpi"):
            conf(*(base_args + ["-mpi", compiler]))
            make("install", parallel=False)

        if spec.satisfies("+openmp"):
            make("clean", parallel=False)
            conf(*(base_args + ["-openmp", compiler]))
            make("openmp", parallel=False)

        if spec.satisfies("+cuda") and spec.satisfies("+mpi"):
            make("clean", parallel=False)
            conf(*(base_args + ["-cuda", "-mpi", compiler]))
            make("install", parallel=False)

        install_tree(".", prefix)
