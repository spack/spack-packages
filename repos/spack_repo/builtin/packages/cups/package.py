# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Cups(AutotoolsPackage):
    """CUPS is the standards-based, open source printing system developed by
    Apple Inc. for macOS and other UNIX-like operating systems. CUPS uses the
    Internet Printing Protocol (IPP) to support printing to local and network
    printers. This provides the core CUPS libraries, not a complete CUPS
    install."""

    homepage = "https://www.cups.org/"
    url = (
        "https://github.com/OpenPrinting/cups/releases/download/v2.4.10/cups-2.4.10-source.tar.gz"
    )

    license("Apache-2.0", checked_by="wdconinc")

    version("2.4.14", sha256="660288020dd6f79caf799811c4c1a3207a48689899ac2093959d70a3bdcb7699")
    version("2.4.13", sha256="8255ecf037be72660de24a73bcada042fc5bf509fc87bc8ad16cd0675735c1a8")
    version("2.4.12", sha256="b1dde191a4ae2760c47220c82ca6155a28c382701e6c1a0159d1054990231d59")
    version("2.4.11", sha256="9a88fe1da3a29a917c3fc67ce6eb3178399d68e1a548c6d86c70d9b13651fd71")
    version("2.4.10", sha256="d75757c2bc0f7a28b02ee4d52ca9e4b1aa1ba2affe16b985854f5336940e5ad7")
    version("2.4.9", sha256="38fbf4535a10554113e013d54fedda03ee88007ea6a9761d626a04e1e4489e8c")
    version("2.4.8", sha256="75c326b4ba73975efcc9a25078c4b04cdb4ee333caaad0d0823dbd522c6479a0")
    version("2.4.7", sha256="dd54228dd903526428ce7e37961afaed230ad310788141da75cebaa08362cf6c")
    version("2.4.6", sha256="58e970cf1955e1cc87d0847c32526d9c2ccee335e5f0e3882b283138ba0e7262")
    version("2.4.5", sha256="9a404de55f74525b0a6851df0cfdebfa1215aec0e7c2f7be6b9b09b6916fb000")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("pkgconfig", type="build")

    depends_on("gnutls")

    def configure_args(self):
        args = ["--enable-gnutls", "--with-components=core"]
        return args
