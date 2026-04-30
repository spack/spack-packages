# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Ant(Package):
    """Apache Ant is a Java library and command-line tool whose mission is to
    drive processes described in build files as targets and extension points
    dependent upon each other
    """

    homepage = "https://ant.apache.org/"
    url = "https://archive.apache.org/dist/ant/source/apache-ant-1.9.7-src.tar.gz"

    license("Apache-2.0")

    version("1.10.14", sha256="9a5fe31f44d1eb62590cbe38e4fab25b25e2f68643b38a54b66498e0bf621b54")
    version("1.10.13", sha256="da006f4c888d41d0f3f213565e48aeff73e4d8a6196e494121d8da1e567a8406")

    depends_on("java")

    def install(self, spec, prefix):
        env["ANT_HOME"] = self.prefix
        bash = which("bash", required=True)
        bash("./build.sh", "install-lite")
