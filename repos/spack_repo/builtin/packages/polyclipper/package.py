# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Polyclipper(CMakePackage):
    """Library for polyhedral clipping planes."""

    homepage = "https://github.com/llnl/PolyClipper"
    url = "https://github.com/llnl/PolyClipper/archive/refs/tags/v1.2.6.tar.gz"
    git = "https://github.com/llnl/PolyClipper.git"

    maintainers("jmikeowen")
    license("BSD-3-Clause")

    version(
        "1.2.6",
        sha256="ffce2fe36fb888b7aaf93d4b3591b0875909573537ca39c0730b7d85bbc5558c"
    )

    with default_args(type="build"):
        depends_on("blt")
        depends_on("cmake@3.20:")
        depends_on("cxx")
        depends_on("c")

    def cmake_args(self):
        args = []
        args.append(self.define("BLT_SOURCE_DIR", self.spec["blt"].prefix))
        args.append(self.define("POLYCLIPPER_BLT_DIR", self.spec["blt"].prefix))
        args.append(self.define("ENABLE_CXXONLY", "ON"))
        args.append(self.define("POLYCLIPPER_ENABLE_PYTHON", "OFF"))
        args.append(self.define("POLYCLIPPER_ENABLE_TESTS", "OFF"))
        return args
