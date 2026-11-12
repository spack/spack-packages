# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Xad(CMakePackage):
    """XAD is a high-performance C++ automatic differentiation library."""

    homepage = "https://auto-differentiation.github.io/"
    url = "https://github.com/auto-differentiation/xad/archive/refs/tags/v2.1.0.tar.gz"

    maintainers("JohnyMarley")

    license("AGPL-3.0-or-later", checked_by="JohnyMarley")

    version("2.1.0", sha256="110729586b1a097c9e4a7ec34c48e60f3aec7ec61ef192a417ce0774cc32be43")

    depends_on("cmake@3.15:", type="build")
    depends_on("cxx", type="build")
    depends_on("c", type="build")
