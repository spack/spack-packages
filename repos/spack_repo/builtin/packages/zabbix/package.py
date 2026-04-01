# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Zabbix(AutotoolsPackage):
    """Real-time monitoring of IT components and services,
    such as networks, servers, VMs, applications and the cloud."""

    homepage = "https://www.zabbix.com"
    url = "https://github.com/zabbix/zabbix/archive/refs/tags/5.0.3.tar.gz"

    license("AGPL-3.0-only", when="@7:", checked_by="wdconinc")
    license("GPL-2.0-or-later", when="@:6", checked_by="wdconinc")

    version("7.0.4", sha256="73aa6b47bd4078587589b30f09671fb30c7743f5b57e81ea8e9bd5a7c5f221c7")
    version("6.0.34", sha256="e60558911230d27ffad98850e414b46e318c9d41591a6ff65a255c0810cfcb8b")
    version("5.0.44", sha256="f8ee86fd21f0f57e7fad68387271b995c1e5cc402d517cd7df5d5221fd6129fd")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("autoconf", type="build")
    depends_on("autoconf-archive", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")
    depends_on("pkgconfig", type="build")
    depends_on("mysql-client")
    # Older versions of mysql use openssl-1.x, causing build issues:
    depends_on("mysql@8.0.35:", when="^[virtuals=mysql-client] mysql")
    depends_on("libevent")
    depends_on("pcre")
    depends_on("go")

    def autoreconf(self, spec, prefix):
        Executable("./bootstrap.sh")()

    def configure_args(self):
        mysql_prefix = self.spec["mysql-client"].prefix
        if self.spec.satisfies("^[virtuals=mysql-client] mysql"):
            mysql_config = mysql_prefix.bin.mysql_config
        else:
            mysql_config = mysql_prefix.bin.mariadb_config

        args = [
            "--enable-server",
            "--enable-proxy",
            "--enable-agent",
            "--enable-agent2",
            f"--with-mysql={mysql_config}",
            f"--with-libevent={self.spec['libevent'].prefix}",
            f"--with-libpcre={self.spec['pcre'].prefix}",
        ]

        return args

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        env.prepend_path("PATH", self.prefix.sbin)
