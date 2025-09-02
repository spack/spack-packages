# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Openmx(MakefilePackage):
    """OpenMX (Open source package for Material eXplorer) is a software
    package for nano-scale material simulations based on density functional
    theories (DFT), norm-conserving pseudopotentials, and pseudo-atomic
    localized basis functions.
    """

    homepage = "http://www.openmx-square.org/index.html"
    url = "https://t-ozaki.issp.u-tokyo.ac.jp/openmx3.8.tar.gz"

    version("3.9", sha256="27bb56bd4d1582d33ad32108fb239b546bdd1bdffd6f5b739b4423da1ab93ae2")
    version("3.8", sha256="36ee10d8b1587b25a2ca1d57f110111be65c4fb4dc820e6d93e1ed2b562634a1")

    depends_on("c", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    resource(
        name="patch",
        url="http://www.openmx-square.org/bugfixed/18June12/patch3.8.5.tar.gz",
        sha256="d0fea2ce956d796a87a4bc9e9d580fb115ff2a22764650fffa78bb79a1b30468",
        placement="patch",
        when="@3.8",
    )

    resource(
        name="patch",
        url="http://www.openmx-square.org/bugfixed/21Oct17/patch3.9.9.tar.gz",
        sha256="20cccc4e3412a814a53568f400260e90f79f0bfb7e2bed84447fe071b26edd38",
        placement="patch",
        when="@3.9",
    )

    # Custom patch for clang: override Set_ProExpn_VNA.c
    # See https://www.openmx-square.org/forum/patio.cgi?mode=view&no=2955
    resource(
        name="set_proexpn_patch",
        url="https://gist.githubusercontent.com/Ncmexp2717/aaffd91eb1bc15e1909b057cc2e83c1f/raw/4e7dfd4a9346b82de69ce9b1d270042bebcd1610/Set_ProExpn_VNA.c",
        sha256="d33de4cbae9af19f39bdf880d33a487cb8fb65beb9fbaa40f4202315dc6ec87b",
        placement="set_proexpn_patch",
        when="@3.9",
        expand=False,
    )

    depends_on("mpi")
    depends_on("fftw-api@3")
    depends_on("blas")
    depends_on("lapack")
    depends_on("scalapack")
    depends_on("sse2neon", when="target=aarch64:")

    # Need OpenMP threaded BLAS libraries
    requires("^openblas threads=openmp", when="^[virtuals=blas] openblas")
    requires("^amdblis threads=openmp", when="^[virtuals=blas] amdblis")
    requires("^intel-oneapi-mkl threads=openmp", when="^[virtuals=blas] intel-oneapi-mkl")

    patch("for_aarch64.patch", when="@3.8 target=aarch64:")

    parallel = False

    build_directory = "source"

    def edit(self, spec, prefix):
        # Move contents to source/
        # http://www.openmx-square.org/bugfixed/18June12/README.txt
        copy_tree("patch", "source")
        # Move extra file for 3.9 patch
        # http://www.openmx-square.org/bugfixed/21Oct17/README.txt
        if spec.satisfies("@3.9"):
            copy(join_path("source", "kpoint.in"), "work")
            if "%aocc" in spec or "%llvm" in spec:
                copy("set_proexpn_patch/Set_ProExpn_VNA.c", "source/Set_ProExpn_VNA.c")
        filter_file(r"\bgcc\b", "$(CC)", "source/makefile")
        makefile = FileFilter("./source/makefile")
        makefile.filter("^DESTDIR.*$", "DESTDIR = {0}/bin".format(prefix))
        mkdirp(prefix.bin)

    @property
    def common_arguments(self):
        spec, common_option = self.spec, []
        lapack_blas_libs = spec["lapack"].libs + spec["blas"].libs + spec["scalapack"].libs
        cc_option = [
            spec["mpi"].mpicc,
            self.compiler.openmp_flag,
            spec["fftw-api"].headers.include_flags,
        ]
        fc_option = [spec["mpi"].mpifc, self.compiler.openmp_flag]
        lib_option = [
            spec["fftw-api"].libs.ld_flags,
            lapack_blas_libs.ld_flags,
            "-lmpi_mpifh",
            self.compiler.openmp_flag,
        ]
        if spec.satisfies("@3.8"):
            cc_option.append("-I$(LIBERIDIR)")
        if spec.satisfies("@3.9"):
            lib_option.extend(["-lmpi_usempif08"])
            lib_option.extend(["-lmpi_usempi_ignore_tkr"])

        if "%fj" in spec:
            common_option.append("-Dkcomp  -Kfast")
            cc_option.append("-Dnosse -Nclang")
            fc_option.extend([self.compiler.openmp_flag, "-Ccpp"])
        else:
            common_option.append("-O3")
            cc_option.extend(
                ["-Wno-error=implicit-function-declaration", "-Wno-error=implicit-int", "-fcommon"]
            )
            if "%gcc" in spec:
                lib_option.append("-lgfortran")
                if spec.satisfies("%gcc@10:"):
                    fc_option.append("-fallow-argument-mismatch")
            if "%llvm" in spec or "%aocc" in spec:
                lib_option.extend(["-lflang", "-lpgmath", "-lflangrti"])
            if "%oneapi" in spec:
                lib_option.extend(["-lifcore"])

        return [
            "CC={0} -Dscalapack {1} ".format(" ".join(cc_option), " ".join(common_option)),
            "FC={0} {1}".format(" ".join(fc_option), " ".join(common_option)),
            "LIB={0}".format(" ".join(lib_option)),
        ]

    @property
    def build_targets(self):
        return ["all"] + self.common_arguments

    @property
    def install_targets(self):
        return ["all"] + self.common_arguments
