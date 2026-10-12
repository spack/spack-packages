# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Graph500(MakefilePackage):
    """Graph500 reference implementations."""

    homepage = "https://graph500.org"
    url = "https://github.com/graph500/graph500/archive/graph500-3.0.0.tar.gz"

    maintainers("juntangc")

    license("BSL-1.0")

    version("3.0.0", sha256="887dcff56999987fba4953c1c5696d50e52265fe61b6ffa8bb14cc69ff27e8a0")

    variant(
        "procs_not_power_of_two",
        default=False,
        description="Enable support for non-power-of-two ranks and nodes",
    )

    depends_on("c", type="build")
    depends_on("mpi@2.0:")

    # graph500 3.0.0 relies on implicit declarations of memset() and
    # isisolated(), which GCC 14 promoted from a warning to an error.
    # Upstream's last release was in 2017, so fix the sources directly.
    patch("graph500-gcc14-implicit-decls.patch")

    build_directory = "src"

    def flag_handler(self, name, flags):
        if name == "cflags":
            # GCC 10 defaults to -fno-common, but 'column' and 'weights' are
            # tentative definitions in a shared header.
            if self.spec.satisfies("%gcc@10:"):
                flags.append("-fcommon")
            # Several functions are defined as bare 'inline' with no external
            # definition anywhere (send_visit in src/bfs_reference.c,
            # aml_poll_intra and friends in aml/aml.c). Under C99 semantics
            # that links only because the upstream -O3 inlines every call, so
            # any lower optimization level fails with undefined references.
            # Restore GNU89 inline semantics, which emit an external
            # definition, so user-supplied flags like -O0 still build.
            if self.spec.satisfies("%gcc"):
                flags.append("-fgnu89-inline")
            # common.h guards SIZE_MUST_BE_A_POWER_OF_TWO behind an #ifndef on
            # this macro, so defining it is enough to switch VERTEX_OWNER and
            # friends from bitmask arithmetic to modulo arithmetic.
            if self.spec.satisfies("+procs_not_power_of_two"):
                flags.append("-DPROCS_PER_NODE_NOT_POWER_OF_TWO")

        # MakefilePackage does not implement flags_to_build_system_args, so
        # everything has to be injected through the compiler wrapper.
        return (flags, None, None)

    def edit(self, spec, prefix):
        makefile = FileFilter(join_path(self.build_directory, "Makefile"))
        makefile.filter(r"^MPICC\s*=.*", f"MPICC={spec['mpi'].mpicc}")

    def install(self, spec, prefix):
        with working_dir(self.build_directory):
            mkdirp(prefix.bin)
            install("graph500_reference_bfs", prefix.bin)
            install("graph500_reference_bfs_sssp", prefix.bin)
            install("graph500_custom_bfs", prefix.bin)
            install("graph500_custom_bfs_sssp", prefix.bin)
