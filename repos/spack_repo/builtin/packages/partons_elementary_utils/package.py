# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class PartonsElementaryUtils(CMakePackage):
    """Utility methods for the PARTONS project."""

    homepage = "https://3d-partons.github.io/partons"
    url = "https://github.com/3d-partons/elementary-utils/archive/refs/tags/v5.0.0.tar.gz"
    git = "https://github.com/3d-partons/elementary-utils.git"

    tags = ["hep"]

    maintainers("wdconinc")

    license("GPL-3.0", checked_by="wdconinc")

    version("5.0.0", sha256="0611b0614e3efdc60893080e0f35de408fef08671076d8f42ffdeda4ab4a366f")

    depends_on("cxx", type="build")
    depends_on("cmake@3.5:", type="build")

    depends_on("sfml@:2")
