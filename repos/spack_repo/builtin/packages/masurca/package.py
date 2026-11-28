# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
#
# MaSuRCA 4.1.4 does not compile with modern compilers (confirmed: AOCC and
# GCC 14 both fail here; the community reports the same with GCC 13, see
# references below). The vendored source code (MUMmer/PacBio/SuperReads/
# CA8, fairly old) is missing standard C++ includes (<cstdint>,
# <algorithm>) in a number of files -- older GCC tolerated this via
# transitive includes, modern compilers do not.
#
# Iteration history (kept as a comment so this isn't "simplified" back to
# something already known to fail):
# 1) Patching files one by one (the file list from issue 359) fixed the
#    first error, but more affected files kept turning up that issue
#    didn't cover (intervalList.H, overlapStoreBuild.C, likely others) --
#    enumerating files by hand doesn't scale.
# 2) Forcing <cstdint> and <algorithm> globally via CXXFLAGS (-include)
#    covers all affected files at once. <cstdint> globally caused no side
#    effects. <algorithm> globally caused one: "reference to 'prev' is
#    ambiguous" in metagenomics_ovl_analyses.C, which declares a
#    file-static "int prev;" that collides with std::prev once
#    <algorithm>/<iterator> brings it into scope (via a transitive "using
#    namespace std").
# 3) Final fix: keep both includes global (covers all affected files,
#    known or not), and rename that one file-static "prev" variable
#    (internal linkage, safe to rename) to resolve the only known
#    collision.
#
# References:
#   https://github.com/alekseyzimin/masurca/issues/370 (exact same error
#     reported independently with GCC 14)
#   https://github.com/alekseyzimin/masurca/issues/359 ("[Resolved]",
#     the community fix this was originally based on, file-by-file)
#   https://github.com/alekseyzimin/masurca/issues/352 (same problem
#     reported with GCC 13)

import re

from spack_repo.builtin.build_systems.generic import Package
from spack_repo.builtin.packages.boost.package import Boost

from spack.package import *

# File with the global "prev" variable that collides with std::prev once
# <algorithm> is forced (see note above). Path verified against the real
# tarball.
_PREV_CONFLICT_FILE = "CA8/src/AS_ENV/metagenomics_ovl_analyses.C"


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

        # Rename the "prev" variable in this one file (see note above) so
        # it doesn't collide with std::prev once <algorithm> is forced
        # globally. \b...\b word boundaries so "prevp"/"prevd" (distinct
        # variables that also exist in this file) are left untouched.
        f = join_path("global-1", _PREV_CONFLICT_FILE)
        with open(f, "r+", encoding="utf-8") as fh:
            content = fh.read()
            new_content = re.sub(r"\bprev\b", "prev_masurca_local", content)
            if new_content != content:
                fh.seek(0)
                fh.write(new_content)
                fh.truncate()

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        if self.spec.satisfies("@4:"):
            env.set("DEST", self.prefix)

        # <cstdint> and <algorithm> globally -- see note above the class
        # for why (upstream source is missing these includes in several
        # files, enumerating them individually doesn't scale). "-include
        # <header>" is a standard flag (gcc, clang/AOCC), injects it into
        # every compiled file without touching the source tree directly.
        # <algorithm> is C++-only, so it does not go in CFLAGS (would
        # break real .c file compilation).
        env.append_flags("CFLAGS", "-include stdint.h")
        env.append_flags("CXXFLAGS", "-include cstdint")
        env.append_flags("CXXFLAGS", "-include algorithm")

    def install(self, spec, prefix):
        installer = Executable("./install.sh")
        installer()
        if self.spec.satisfies("@:4"):
            install_tree(".", prefix)
