# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Mui(CMakePackage):
    """Multiscale Universal Interface: A Concurrent Framework for Coupling Heterogeneous Solvers"""

    homepage = "https://mxui.github.io/"
    git = "https://github.com/MxUI/MUI.git"
    url = "https://github.com/MxUI/MUI/archive/refs/tags/2.0.tar.gz"

    maintainers("blairSmcc03")

    license("GPL-3.0 OR Apache-2.0", checked_by="blairSmcc03")

    version("2.0", sha256="fdddd4ffe72c22356eb53707567622a9bfb8d17836a9677a980f035e87e1b295")
    version("master", branch="master")

    depends_on("cmake@3.18:")
    depends_on("mpi")
    depends_on("cxx", type="build")

    def cmake_args(self):
        return []
