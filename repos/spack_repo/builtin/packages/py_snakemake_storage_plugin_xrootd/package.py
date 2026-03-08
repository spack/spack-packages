# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySnakemakeStoragePluginXrootd(PythonPackage):
    """A Snakemake storage plugin to read and write from XRootD Storage."""

    homepage = "https://github.com/snakemake/snakemake-storage-plugin-xrootd"
    pypi = "snakemake_storage_plugin_xrootd/snakemake_storage_plugin_xrootd-0.1.4.tar.gz"

    maintainers("wdconinc")

    license("MIT", checked_by="wdconinc")

    version(
        "1.0.0", sha256="1f7675f6259b3aace99023b3cf65cbb62e00935b76cf10b6dbdbcbe35b6fbfff"
    )  # FIXME
    version("0.4.1", sha256="ccad9b12ae1ca73d858e0767cfb62c48fa21b6300a89da50337e38b7d632359c")
    version("0.4.0", sha256="f221ba5e8e83fe08248c1b9c0a8d202d159d3d4e3efd68d6ad054b93e56c6b55")
    version("0.3.2", sha256="1898d436b1f2c967d46304a708e271bac46e8b3e4b24d5fdba7cae2a8dee41ce")
    version("0.3.1", sha256="3b505932b1cf6e8e915992c21ce6d289dd8b4d056b1ef5b244131a717d94164e")
    version("0.3.0", sha256="7b21bc6bde036ac05731fca06dd5d055fc4b780dda8c5940a38cce8bd4b2450e")
    version("0.2.1", sha256="c841d4647f9802c9c41cbba73fce6ef82bcc275ba6dc8a6be25f1952f4a5edff")
    version("0.2.0", sha256="4fdb732ef129c2b4690706cdfc3067936b03abaa67784ce8630b835fd41494b3")
    version("0.1.4", sha256="61a48b2567fa7f35a29f00f0a74d1efd069a16c0ef7c9f7f440a46088d2c6dbc")

    depends_on("xrootd@5.6.4:5 +python", type=("build", "run"))

    depends_on("py-snakemake-interface-common@1.15:1", type=("build", "run"))
    depends_on(
        "py-snakemake-interface-storage-plugins@4.0.1:4", type=("build", "run"), when="@0.5:"
    )
    depends_on(
        "py-snakemake-interface-storage-plugins@3.3.0:3", type=("build", "run"), when="@:0.4"
    )

    depends_on("python@3.11:3", type=("build", "run"))
    depends_on("py-hatchling", type="build", when="@0.1.5:")
    depends_on("py-hatch-vcs", type="build", when="@0.1.5:")
    depends_on("py-poetry-core", type="build", when="@:0.1.4")

    depends_on("snakemake@8.18:8", type=("build", "run"), when="@:0.3")
