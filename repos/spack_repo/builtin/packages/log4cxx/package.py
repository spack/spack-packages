# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Log4cxx(CMakePackage):
    """A C++ port of Log4j"""

    homepage = "https://logging.apache.org/log4cxx/latest_stable/"
    url = "https://dlcdn.apache.org/logging/log4cxx/0.12.0/apache-log4cxx-0.12.0.tar.gz"

    maintainers("nicmcd")

    license("Apache-2.0", checked_by="wdconinc")

    version("1.2.0", sha256="09f4748aa5675ef5c0770bedbf5e00488668933c5a935a43ac5b85be2436c48a")

    variant(
        "cxxstd", default="20", description="C++ standard", values=("11", "17", "20"), multi=False
    )

    depends_on("cmake@3.13:", type="build")

    depends_on("apr-util")
    depends_on("apr")
    depends_on("boost+thread+system", when="cxxstd=11")
    depends_on("expat")
    depends_on("zlib-api")
    depends_on("zip")
    depends_on("c", type="build")
    depends_on("cxx", type="build")

    def cmake_args(self):
        return [
            self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"),
            self.define("BUILD_TESTING", "off"),
        ]
