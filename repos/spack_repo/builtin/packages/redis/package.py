# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Redis(MakefilePackage):
    """Redis is an open source (BSD licensed), in-memory data structure store,
    used as a database, cache and message broker.
    It supports data structures such as strings, hashes, lists, sets, sorted
    sets with range queries, bitmaps, hyperloglogs, geospatial indexes with
    radius queries and streams. Redis has built-in replication, Lua scripting,
    LRU eviction, transactions and different levels of on-disk persistence,
    and provides high availability via Redis Sentinel and automatic
    partitioning with Redis Cluster
    """

    homepage = "https://redis.io"
    urls = [
        "https://download.redis.io/releases/redis-7.4.0.tar.gz",
        "https://github.com/redis/redis/archive/refs/tags/7.4.0.tar.gz",
    ]
    git = "https://github.com/redis/redis.git"

    maintainers("lpottier")

    license("BSD-3-Clause")

    version("7.4.0", sha256="57b47c2c6682636d697dbf5d66d8d495b4e653afc9cd32b7adf9da3e433b8aaf")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    variant("tls", default=False, when="@6:", description="Builds with TLS support")
    depends_on("openssl@1.1:", type=("build", "link"), when="+tls")

    variant(
        "systemd",
        default=False,
        description="Builds with systemd support (systemd development libraries required)",
    )

    @property
    def build_targets(self):
        use_tls = "yes" if "+tls" in self.spec else "no"
        use_systemd = "yes" if "+systemd" in self.spec else "no"
        return ["BUILD_TLS={0}".format(use_tls), "USE_SYSTEMD={0}".format(use_systemd)]

    @property
    def install_targets(self):
        return ["PREFIX={0}".format(self.spec.prefix), "install"]

    @run_after("install")
    def install_conf(self):
        mkdirp(self.prefix.conf)
        install("redis.conf", self.prefix.conf)
