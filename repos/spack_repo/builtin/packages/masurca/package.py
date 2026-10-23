# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package
from spack_repo.builtin.packages.boost.package import Boost

from spack.package import *


class Masurca(Package):
    """MaSuRCA is whole genome assembly software. It combines the efficiency
    of the de Bruijn graph and Overlap-Layout-Consensus (OLC)
    approaches."""

    homepage = "https://www.genome.umd.edu/masurca.html"
    url = "https://github.com/alekseyzimin/masurca/releases/download/v3.3.1/MaSuRCA-3.3.1.tar.gz"

    license("GPL-3.0-only")

    version("4.1.4", sha256="6112d742bac326917a57d02f71494e5de4c6a67c6bbef8de54f842b9d5873d7d")
    version("4.1.1", sha256="8758f6196bf7f57e24e08bda84abddfff08feb4cea204c0eb5e1cb9fe8198573")
    version("4.1.0", sha256="15078e24c79fe5aabe42748d64f95d15f3fbd7708e84d88fc07c4b7f2e4b0902")
    version("4.0.9", sha256="a31c2f786452f207c0b0b20e646b6c85b7357dcfd522b697c1009d902d3ed4cf")
    version("4.0.5", sha256="db525c26f2b09d6b359a2830fcbd4a3fdc65068e9a116c91076240fd1f5924ed")
    version("4.0.1", sha256="68628acaf3681d09288b48a35fec7909b347b84494fb26c84051942256299870")
    version("3.3.1", sha256="587d0ee2c6b9fbd3436ca2a9001e19f251b677757fe5e88e7f94a0664231e020")
    version("3.2.9", sha256="795ad4bd42e15cf3ef2e5329aa7e4f2cdeb7e186ce2e350a45127e319db2904b")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("gmake", type="build")

    depends_on("perl", type=("build", "run"))
    depends_on(Boost.with_default_variants)
    depends_on("zlib-api")
    patch("arm.patch", when="target=aarch64:")

    def patch(self):
        filter_file("#include <sys/sysctl.h>", "", "global-1/CA8/src/AS_BAT/memoryMappedFile.H")
        if self.spec.target.family == "aarch64":
            for makefile in "Makefile.am", "Makefile.in":
                m = join_path("global-1", "prepare", makefile)
                filter_file("-minline-all-stringops", "", m)
                m = join_path("global-1", makefile)
                filter_file("-minline-all-stringops", "", m)

            filter_file(
                r"make -C ${MINIMAP2_DIR}",
                r"make -C ${MINIMAP2_DIR} arm_neon=1 aarch64=1",
                join_path("Flye", "Makefile"),
                string=True,
                ignore_absent=True,
            )

        if self.spec.satisfies("%gcc@13:"):
            for misc in ("SuperReads", "PacBio"):
                filter_file(
                    "#include <algorithm>",
                    "#include <algorithm>\n#include <cstdint>",
                    join_path("global-1", misc, "include", "misc.hpp"),
                    string=True,
                    ignore_absent=True,
                )

            filter_file(
                '#include "const_iterator_traits.hpp"',
                "#include <cstdint>\n#include <iterator>\n#include <type_traits>\n"
                '#include "const_iterator_traits.hpp"',
                join_path("global-1", "MUMmer", "include", "mummer", "48bit_iterator.hpp"),
                string=True,
                ignore_absent=True,
            )

            for src in (
                "getSuperReadInsertCountsFromReadPlacementFile.cc",
                "getSuperReadInsertCountsFromReadPlacementFileTwoPasses.cc",
            ):
                filter_file(
                    r"bool operator()(const char *s1, const char *s2) {",
                    r"bool operator()(const char *s1, const char *s2) const {",
                    join_path("global-1", "SuperReads", "src2", src),
                    string=True,
                    ignore_absent=True,
                )

            hashfn = join_path("global-1", "SOAPdenovo2", "standardPregraph", "hashFunction.c")
            x86 = "#if defined(__x86_64__) || defined(__i386__)"
            filter_file(
                r"static uint32_t cpuid ( uint32_t functionInput )",
                x86 + "\nstatic uint32_t cpuid ( uint32_t functionInput )",
                hashfn,
                string=True,
                ignore_absent=True,
            )
            filter_file(
                r"static inline int crc32cTable (",
                "#endif\n\nstatic inline int crc32cTable (",
                hashfn,
                string=True,
                ignore_absent=True,
            )
            filter_file(
                r"uint32_t ecx = cpuid ( 1 );",
                x86 + "\n\tuint32_t ecx = cpuid ( 1 );\n#else\n\tuint32_t ecx = 0;\n#endif",
                hashfn,
                string=True,
                ignore_absent=True,
            )

            filter_file(
                r"inline int * update_posmap(",
                r"static inline int * update_posmap(",
                join_path("global-1", "samtools", "padding.c"),
                string=True,
                ignore_absent=True,
            )

            for header in (
                join_path("src", "sequence", "sequence_container.h"),
                join_path("src", "polishing", "subs_matrix.h"),
            ):
                filter_file(
                    "#pragma once",
                    "#pragma once\n\n#include <cstdint>",
                    join_path("Flye", header),
                    string=True,
                    ignore_absent=True,
                )

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        if self.spec.satisfies("@4:"):
            env.set("DEST", self.prefix)

        env.append_flags(
            "CFLAGS",
            "-std=gnu17 "
            "-Wno-error=implicit-function-declaration "
            "-Wno-error=implicit-int "
            "-Wno-error=int-conversion "
            "-Wno-error=incompatible-pointer-types",
        )

    def install(self, spec, prefix):
        installer = Executable("./install.sh")
        installer()
        # For @4: install.sh installs straight into $DEST (= prefix), so only
        # older versions need the source tree copied over.
        if self.spec.satisfies("@:3"):
            install_tree(".", prefix)
