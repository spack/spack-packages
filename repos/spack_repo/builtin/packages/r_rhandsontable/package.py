# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class RRhandsontable(RPackage):
    """An R interface to the 'Handsontable' JavaScript library, which is a
    minimalist Excel-like data grid editor."""

    homepage = "http://jrowen.github.io/rhandsontable/"
    url = "https://github.com/jrowen/rhandsontable/archive/refs/tags/v0.3.8.tar.gz"

    license("MIT")

    version("0.3.8", sha256="8dacdc5b95467b0537cb9690bd7c01dd07191d00216dc15ce295fc75a8976042")
    version("0.3.7", sha256="85129e9a6a59536333447e2a797732a751d08cb5534046600af4394f7a9136df")
    version("0.3.6", sha256="5c18216b75b452d7a87e893005fdcf2adf339c26c2cbccb95b8d9b147b51aefe")
    version("0.3.5", sha256="6dfc428294d583a35516815f47a0ba8b5db109c3c3c487fbb4cf5321925c9243")
    version("0.3.4", sha256="e459b2c5b03fe45a7e9bb6d3bcebc70271a59459b30d46e08200fcdd48df83a5")
    version("0.3.3", sha256="ec0e70a9a71799e3ada5652aa4d8048d29347da60a33cc2bbd41fdb733f11b1d")
    version("0.3.2", sha256="f60da3c872c0891e12ba3bcd6a48c86dabd80c666697f1c1619980d5ea7faceb")
    version("0.3.1", sha256="a1701d2ea9225c72d169bb6d3f9ec89760106cbae2e78aa337bb2c72629fd52b")
    version("0.3", sha256="8202da46674a99018b6f077b66941786248b8b610fa47d2ca52d1bdc2563c89a")
    version("0.2.1", sha256="9062444d5a0e0326894a1597333f28ee50f5169dee205dd417bfe3823f36cb49")

    depends_on("r-jsonlite", type=("build", "run"))
    depends_on("r-htmlwidgets@0.3.3:", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
