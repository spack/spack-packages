# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Zookeeper(Package):
    """
    Apache ZooKeeper is an effort to develop and maintain an open-source
    server which enables highly reliable distributed coordination.
    """

    homepage = "https://archive.apache.org"
    url = "https://archive.apache.org/dist/zookeeper/zookeeper-3.8.4/apache-zookeeper-3.8.4-bin.tar.gz"

    license("Apache-2.0")

    version("3.8.4", sha256="284cb4675adb64794c63d95bf202d265cebddc0cda86ac86fb0ede8049de9187")

    depends_on("java")

    def install(self, spec, prefix):
        install_tree(".", prefix)

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        env.set("ZOOBINDIR", self.prefix.bin)
        env.set("ZOOCFGDIR", ".")
        env.set("ZOO_LOG_DIR", ".")
