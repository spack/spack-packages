# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.build_systems.cmake import CMakePackage

class Parafeed(CMakePackage):
    """Parafeed is a C++ library to parse and interact with the commandline."""

    homepage = "https://github.com/sanbee/parafeed"
    url      = "https://github.com/sanbee/parafeed/archive/refs/tags/v1.1.41.tar.gz"

    maintainers("preshanth", "sanbee", "sanbw")

    # TODO: Check actual license in project. Replace "UNKNOWN" with actual SPDX identifier.
    license("UNKNOWN", checked_by="sanbee")

    version("1.1.41", sha256="a5cb034914cab8b661469f2f1aae6af7d88045d54f3535da8ff004a04cd8abd3")
    version("1.1.4",  sha256="9ca767aa1139516926456fff14fec466890caba5646e46f0553c7b648bb5510e")
    version("1.1.2",  sha256="74eb62034b0c4cbfd9a4a05872c10d568b184e8cf7543405d460fc0c52001139")
    version("1.1.1",  sha256="757290ec76b3762febbaadca4c597f9d668be55767dbcfdba305ddc48cb07689")

    # Build-time and run-time dependencies
    depends_on("readline")
    depends_on("bison")
    depends_on("flex")
    depends_on("pkgconfig", type="build")
    depends_on("cmake@3.1:", type="build")

    # C++ standard variant
    variant(
        "cxxstd",
        default="11",
        values=("11", "14", "17", "20", "23"),
        description="C++ standard to use"
    )

    def cmake_args(self):
        args = [
            self.define("CMAKE_CXX_STANDARD", self.spec.variants["cxxstd"].value),
            self.define("CMAKE_CXX_STANDARD_REQUIRED", "ON"),
            self.define("CMAKE_CXX_EXTENSIONS", "OFF")
        ]
        return args
