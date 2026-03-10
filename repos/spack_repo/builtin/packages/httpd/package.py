# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Httpd(AutotoolsPackage):
    """The Apache HTTP Server is a powerful and flexible HTTP/1.1 compliant
    web server."""

    homepage = "https://httpd.apache.org/"
    url = "https://archive.apache.org/dist/httpd/httpd-2.4.43.tar.bz2"

    license("Apache-2.0", checked_by="wdconinc")

    version("2.4.62", sha256="674188e7bf44ced82da8db522da946849e22080d73d16c93f7f4df89e25729ec")

    depends_on("c", type="build")
    depends_on("m4", type="build")
    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("apr")
    depends_on("apr-util")
    depends_on("pcre")

    def configure_args(self):
        spec = self.spec
        config_args = [
            f"--with-apr={spec['apr'].prefix}",
            f"--with-apr-util={spec['apr-util'].prefix}",
        ]
        return config_args
