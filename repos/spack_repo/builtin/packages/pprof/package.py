# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.go import GoPackage

from spack.package import *


class Pprof(GoPackage):
    """pprof is a tool for visualization and analysis of profiling data."""

    homepage = "https://github.com/google/pprof"
    git = "https://github.com/google/pprof.git"

    maintainers("mcmehrtens")
    license("Apache-2.0", checked_by="mcmehrtens")

    # pprof doesn't have tagged releases
    version("main", branch="main", get_full_repo=True)

    # pprof's go.mod requires go 1.24; Go supports the two most recent
    # major releases, so this will need updating with new Go releases.
    depends_on("go@1.24:", type="build")

    variant(
        "graphviz",
        default=True,
        description="Enable graphic visualization of profiles (SVG, PDF, etc.)",
    )

    depends_on("graphviz", type="run", when="+graphviz")

    @property
    def sanity_check_is_file(self):
        return [join_path("bin", "pprof")]
