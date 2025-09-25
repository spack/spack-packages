# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Rocketmq(Package):
    """
    Apache RocketMQ is a distributed messaging and streaming platform
    with low latency, high performance and reliability, trillion-level
    capacity and flexible scalability.
    """

    homepage = "https://rocketmq.apache.org/"
    url = "https://archive.apache.org/dist/rocketmq/4.5.2/rocketmq-all-4.5.2-bin-release.zip"

    license("Apache-2.0", checked_by="wdconinc")

    version("5.3.1", sha256="251d7261fa26d35eaffef6a2fce30880054af7a5883d578dd31574bf908a8b97")

    depends_on("java@8:", type="run")

    # UseBiasedLocking deprecated in java@15:, removed in java@21:
    # https://openjdk.org/jeps/374, https://github.com/apache/rocketmq/pull/8809
    depends_on("java@:20", type="run")

    def install(self, spec, prefix):
        install_tree(".", prefix)
