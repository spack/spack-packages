# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class RankRun(CMakePackage):
    """rank-run is an application that executes serial jobs in parallel where each rank
    runs a given command or script."""

    homepage = "https://github.com/RRFSx/rank_run"
    git = "https://github.com/RRFSx/rank_run.git"
    url = "https://github.com/RRFSx/rank_run/archive/refs/tags/v1.0.0.tar.gz"

    maintainers("climbfuji")

    license("GPL-3.0-only")

    version("1.0.0", sha256="77cd9e8587566d414b2862d9022e44b3cdbcd5bd4b51915505cc4accdec9fe6b")

    depends_on("c", type="build")

    depends_on("mpi")
