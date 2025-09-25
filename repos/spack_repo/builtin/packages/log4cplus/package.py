# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Log4cplus(CMakePackage):
    """log4cplus is a simple to use C++ logging API
    providing thread-safe, flexible, and arbitrarily
    granular control over log management and configuration."""

    homepage = "https://github.com/log4cplus/log4cplus"
    url = "https://github.com/log4cplus/log4cplus/releases/download/REL_2_1_2/log4cplus-2.1.2.tar.bz2"

    license("Apache-2.0 AND BSD-2-Clause")

    version("2.1.2", sha256="2450dfbb4ab35dd2c9e64d8c750c514bf7293b81d8f32af7ab124417f70adfad")
    version("2.0.8", sha256="ca36aa366036d1c61fc0366a9ffbcf32bad55d74878b2c36a9c34dcc00b8a0ca")
    version("1.2.2", sha256="853efd919f9ca76c518c0944e6b0ced1174523a86b6db046ed4f23fe695167bd")

    depends_on("c", type="build")
    depends_on("cxx", type="build")  # generated

    def url_for_version(self, version):
        # log4cplus tags use REL_X_Y_Z
        rel = "REL_{0}".format(str(version).replace(".", "_"))
        return f"https://github.com/log4cplus/log4cplus/releases/download/{rel}/log4cplus-{version}.tar.bz2"
