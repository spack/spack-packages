# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RRvest(RPackage):
    """Easily Harvest (Scrape) Web Pages.

    Wrappers around the 'xml2' and 'httr' packages to make it easy to download,
    then manipulate, HTML and XML."""

    cran = "rvest"

    license("MIT")

    version("1.0.5", sha256="1e7c34a0b4467887195b1cd66388919989e82ca096d08df283c675d87e53bc00")
    version("1.0.4", sha256="7d707c6b2994cf7b6c1d665bec872d2ef5c55f30e7c343c447a8a386a6049ca6")
    version("1.0.3", sha256="a465ef7391afaa3c26eebe8c61db02314ac04c4d8de5aa53f090716763d21c1e")
    version("1.0.2", sha256="89bb477e0944c80298a52ccf650db8f6377fd7ed3c1bc7034d000f695fdf05a4")
    version("0.3.6", sha256="6a2ee3a25d2d738031edbc1b5e2410f2a4538dfbb9705af145f9039504b902fa")
    version("0.3.4", sha256="413e171b9e89b7dc4e8b41165027cf19eb97cd73e149c252237bbdf0d0a4254a")
    version("0.3.3", sha256="b10a87fa2d733f7c0fc567242ef0ab10a1a77d58d51796996cc0fd81381a556f")
    version("0.3.2", sha256="0d6e8837fb1df79b1c83e7b48d8f1e6245f34a10c4bb6952e7bec7867e4abb12")

    with default_args(type=("build", "run")):
        depends_on("r@4.1:", when="@1.0.5:")
        depends_on("r@3.6:", when="@1.0.4:")
        depends_on("r@3.2:", when="@0.3.4:")
        depends_on("r@3.1:", when="@0.3.3")
        depends_on("r@3.0.1:")

        depends_on("r-cli", when="@1.0.3:")
        depends_on("r-glue", when="@1.0.3:")
        depends_on("r-httr@0.5:")
        depends_on("r-lifecycle@1.0.3:", when="@1.0.4:")
        depends_on("r-lifecycle@1.0.0:", when="@1:")
        depends_on("r-magrittr")
        depends_on("r-rlang@1.1.0:", when="@1.0.4:")
        depends_on("r-rlang@1.0.0:", when="@1.0.3:")
        depends_on("r-rlang@0.4.10:", when="@1:")
        depends_on("r-selectr")
        depends_on("r-tibble", when="@1:")
        depends_on("r-xml2@1.4:", when="@1.0.5:")
        depends_on("r-xml2@1.3:", when="@1:")
        depends_on("r-xml2")

        # Historical dependencies
        depends_on("r-withr", when="@1.0.3")
