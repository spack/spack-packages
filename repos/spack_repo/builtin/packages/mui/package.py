# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Mui(CMakePackage):
    """Multiscale Universal Interface: A Concurrent Framework for Coupling Heterogeneous Solvers"""

    homepage = "https://mxui.github.io/"
    git = "https://github.com/MxUI/MUI.git"

    maintainers("Wendi-L", "SLongshaw")

    license("Apache-2.0", checked_by="blairSmcc03")

    version("2.0", branch="master")

    depends_on("cmake@3.27:")
    depends_on("mpi")

    def cmake_args(self):
        """Map Spack variants to the project's CMake options."""
        args = []

        return args
