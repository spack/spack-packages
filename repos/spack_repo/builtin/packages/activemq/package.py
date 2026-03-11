# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Activemq(Package):
    """
    Apache ActiveMQ is a high performance Apache 2.0 licensed Message Broker
    and JMS 1.1 implementation.
    """

    homepage = "https://archive.apache.org/dist/activemq"
    url = "https://archive.apache.org/dist/activemq/5.14.0/apache-activemq-5.14.0-bin.tar.gz"

    license("Apache-2.0")

    version("6.1.3", sha256="cad14e816e990f1312709ebfc228f42895d8c54c652d3cd56f0b5145635dc794")
    version("5.18.6", sha256="b1363696e4e014423f6ab22f1ece4bf14ee32b80bfa5bdbae7dd4026a47ff03a")

    depends_on("cxx", type="build")  # generated

    depends_on("java")
    depends_on("java@11:", when="@5.17:")
    depends_on("java@17:", when="@6:")

    def install(self, spec, prefix):
        install_tree(".", prefix)
