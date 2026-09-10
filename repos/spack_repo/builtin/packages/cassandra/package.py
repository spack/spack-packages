# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Cassandra(Package):
    """
    Apache Cassandra is a highly-scalable partitioned row store. Rows are
    organized into tables with a required primary key.
    """

    homepage = "https://cassandra.apache.org/"
    url = "https://archive.apache.org/dist/cassandra/4.0.1/apache-cassandra-4.0.1-bin.tar.gz"

    license("Apache-2.0", checked_by="wdconinc")

    version("5.0.1", sha256="73f4c807b0aa4036500d5dc54e30ef82bcf549ab1917eff2bbc7189b0337ea84")

    depends_on("java@11:", type=("build", "run"))

    def install(self, spec, prefix):
        install_tree(".", prefix)
