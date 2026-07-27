# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySnakemakeInterfaceStoragePlugins(PythonPackage):
    """This package provides a stable interface for interactions between Snakemake and its storage
    plugins."""

    homepage = "https://github.com/snakemake/snakemake-interface-storage-plugins"
    pypi = "snakemake_interface_storage_plugins/snakemake_interface_storage_plugins-3.3.0.tar.gz"
    maintainers("w8jcik")

    license("MIT")

    version("4.2.3", sha256="95be93d1aa1c56c189d9ff661930a6475e847a79a74013822c9570c0ef691755")
    version("4.1.0", sha256="9f1466b68abda3b4e602133318973d02c15404709d24eaeb02f23e713691aaf0")
    version("4.0.1", sha256="6703b6effb68b86d9f9fe95497efdb3139473e63a523084a27bb7bfefe379cbd")
    version("3.5.0", sha256="88ee1dde95f9d5abb03113c52fb8cfa78ee502cce9ec788c161b3c09076fc075")
    version("3.4.0", sha256="7e1289bda0f693640dc1257815c35168fe4996be977621bcc1671b58217c69ae")
    version("3.3.0", sha256="203d8f794dfb37d568ad01a6c375fa8beac36df8e488c0f9b9f75984769c362a")
    version("3.2.4", sha256="a44b99339f369703e3cfa5f21f3f513ca2000c8790c364be0e5df7d03fb264d3")
    version("3.1.0", sha256="26e95be235ef2a9716b890ea96c3a9a2e62061c5d72fbb89c2fad2afada87304")

    depends_on("py-wrapt@1.15:", when="@4.2:", type=("build", "run"))
    depends_on("py-wrapt@1.15:1", when="@:4.1", type=("build", "run"))
    depends_on("py-reretry@0.11.8:", when="@4.2:", type=("build", "run"))
    depends_on("py-reretry@0.11.8:0.11", when="@:4.1", type=("build", "run"))
    depends_on("py-throttler@1.2.2:", when="@4.2:", type=("build", "run"))
    depends_on("py-throttler@1.2.2:1", when="@:4.1", type=("build", "run"))
    depends_on("py-humanfriendly@10:", type=("build", "run"), when="@3.6:4.1")

    depends_on("py-snakemake-interface-common@1.12:", when="@4.2:", type=("build", "run"))
    depends_on("py-snakemake-interface-common@1.12:1", when="@:4.1", type=("build", "run"))

    depends_on("python@3.11:3", type=("build", "run"))
    depends_on("py-poetry-core", type="build")
