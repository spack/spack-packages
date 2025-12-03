# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Ioapi(MakefilePackage):
    """Models-3/EDSS Input/Output Applications Programming Interface."""

    homepage = "https://www.cmascenter.org/ioapi/"
    git = "https://github.com/cjcoats/ioapi-3.2.git"

    maintainers("omsai")

    license("GPL-2.0-or-later", checked_by="omsai")

    # The two -develop versions below without date suffixes are "rolling
    # releases":
    # https://www.cmascenter.org/ioapi/documentation/all_versions/html/AVAIL.html#build
    # If you installed ioapi@3.2 previously it was a rolling release that
    # caused checksums to fail (#22633, #28247).  Until recently, upstream did
    # not freeze tarballs and now freezes them with a date suffix.
    version("4.0-develop", branch="ioapi-4.0")
    version("3.2-develop", branch="master")
    # Dated suffix versions are now pulled from GitHub.  The dates below are
    # based on the, the GitHub tag release date, because there is no other
    # reliable version:
    # 1. Most of upstream's tagged versions are missing a leading zero and are
    #    therefore not in ascending numerical order which break versioning
    #    relationships.
    # 2. The tarball VERSION.txt is not reliably updated.
    version("3.2.20200828", commit="ef5d5f4e112c249b593b19426421f25d79ae094b", preferred=True)
    version("3.2.20200714", commit="6ebb47e96db3b641af63ee5f853c943b596a1268")
    version("3.2.20200420", commit="4017280cc656993a5be50f0da9287a56166da22b")

    # MPI support is not yet well supported in this spack package and
    # may fail to build.
    variant("mpi", default=False, description="Enable MPI support")

    depends_on("c", type="build")
    depends_on("fortran", type="build")
    depends_on("sed", type="build")

    depends_on("mpi", when="+mpi")
    depends_on("netcdf-c@4.4.2: ~mpi +parallel-netcdf", when="+mpi")
    depends_on("netcdf-c@4.4.2: ~mpi", when="~mpi")
    depends_on("netcdf-fortran@4.4.2:")

    # Supporting compilers by mapping to their Makeinclude files
    # requires additional work and testing; the package naming scheme
    # is inconsistent perhaps because it's meant more for human
    # editing.
    conflicts("^intel-oneapi-compilers", msg="Update this spack package to support oneapi")
    conflicts("%nvhpc", msg="Update this spack package to support pgi")
    # There is no evidence of support for LLVM even on macOS.
    conflicts("%llvm", msg="IOAPI does not support LLVM")

    # Parallel build will fail with this error:
    #
    # Fatal Error: Cannot open module file 'm3utilio.mod' for reading at (1):
    # No such file or directory
    parallel = False

    def setup_build_environment(self, env):
        # The BIN environmental variables needs to be set in addition
        # to being written into the top-level Makefile.
        BIN = "Linux2_x86_64gfort"
        if self.spec.satisfies("+mpi"):
            BIN += "mpi"
        env.set("BIN", BIN)

    def edit(self, spec, prefix):
        # No default Makefile bundled; edit the template.
        symlink("Makefile.template", "Makefile")
        # The makefile uses stubborn assignments of = instead of ?= so
        # edit the makefile instead of using environmental variables.
        makefile = FileFilter("Makefile")
        makefile.filter(
            "(^VERSION.*)",
            """
CPLMODE = nocpl
\\1
        """.strip(),
        )
        BIN = "Linux2_x86_64gfort"
        if self.spec.satisfies("+mpi"):
            BIN += "mpi"
        makefile.filter(
            "^BASEDIR.*",
            (
                """
BASEDIR = """
                + self.build_directory
                + """
INSTALL = """
                + prefix
                + """
BININST = """
                + prefix.bin
                + """
LIBINST = """
                + prefix.lib
                + f"""
BIN = {BIN}
        """
            ).strip(),
        )
        # Fix circular dependency bug for generating subdirectory Makefiles.
        makefile.filter("^configure:.*", "configure:")
        # Fix hard-coded fortran mpi compiler.
        if self.spec.satisfies("+mpi"):
            makeinclude = FileFilter(f"ioapi/Makeinclude.{BIN}")
            makeinclude.filter("mpicc", f"{self.spec['mpi'].mpicc}")
            makeinclude.filter("mpif90", f"{self.spec['mpi'].mpifc}")
        # Generate the subdirectory Makefiles.
        make("configure")

    def flag_handler(self, name: str, flags: List[str]):
        if name == "fflags" and self.spec.satisfies("%fortran=gcc@10:"):
            flags.append("-fallow-argument-mismatch")
        return (flags, None, None)

    def install(self, spec, prefix):
        make("install")
        # Install the header files.
        mkdirp(prefix.include.fixed132)
        install("ioapi/*.EXT", prefix.include)
        # Install the header files for CMAQ and SMOKE in the
        # non-standard -ffixed-line-length-132 format.
        install("ioapi/fixed_src/*.EXT", prefix.include.fixed132)
