# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class PartonsNuma(CMakePackage):
    """Numerical analysis routines for the PARTONS project."""

    homepage = "https://3d-partons.github.io/partons"
    url = "https://github.com/3d-partons/numa/archive/refs/tags/v5.0.0.tar.gz"
    git = "https://github.com/3d-partons/numa.git"

    tags = ["hep"]

    maintainers("wdconinc")

    license("GPL-3.0", checked_by="wdconinc")

    version("5.0.0", sha256="1ba38b59cf0b8b32ff418f52a63601c65817503b1bf7823860dc6d09782066b0")

    depends_on("cxx", type="build")
    depends_on("cmake@3.5:", type="build")

    depends_on("sfml@:2")
    depends_on("partons-elementary-utils")
    depends_on("eigen@3")
