# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Drill(Package):
    """
    Apache Drill is a distributed MPP query layer that supports SQL and
    alternative query languages against NoSQL and Hadoop data storage
    systems.
    """

    homepage = "https://drill.apache.org/"
    url = "https://dist.apache.org/repos/dist/release/drill/1.17.0/apache-drill-1.17.0.tar.gz"
    git = "https://github.com/apache/drill.git"

    license("Apache-2.0", checked_by="wdconinc")

    version("1.21.2", sha256="77e2e7438f1b4605409828eaa86690f1e84b038465778a04585bd8fb21d68e3b")
    version("1.20.3", sha256="1520cd2524cf8e0ce45fcf02e8e5e3e044465c6dacad853f9fadf9c918863cad")

    # pom.xml, requireJavaVersion
    depends_on("java@8:", type="run")

    def install(self, spec, prefix):
        install_tree(".", prefix)
