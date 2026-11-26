# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Cfp(CMakePackage):
    """The Command File Processor (CFP) runs command files in parallel with MPI."""

    homepage = "https://github.com/NOAA-MDL/cfp"
    url = "https://github.com/NOAA-MDL/cfp/archive/refs/tags/v2.1.0.tar.gz"
    git = "https://github.com/NOAA-MDL/cfp"

    maintainers("EricEngle-NOAA")

    version("main", branch="main")
    version("2.1.0", sha256="89f512fe1c8ab73f859a6458efa174552fdf0a2706f69cce0185e85b07c58945")

    depends_on("fortran", type="build")

    depends_on("cmake@3.18:", type="build")
    depends_on("mpi")
