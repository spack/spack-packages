# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RPkgbuild(RPackage):
    """Find Tools Needed to Build R Packages.

    Provides functions used to build R packages. Locates compilers needed to
    build R packages on various platforms and ensures the PATH is configured
    appropriately so R can use them."""

    cran = "pkgbuild"

    license("MIT")

    version("1.4.8", sha256="2e4259202ce90fc452f31ff36cfe14ff21a38e9fd71c3015e25018b9079924cb")
    version("1.4.4", sha256="5972843cd43654715cdbdd28f50af013fa3d1c213146654992b2b5f39ed0e2a8")
    version("1.4.0", sha256="357f3c40c99650eaa8a715991ff1355a553acb165f217ed204712f698ba55ed6")
    version("1.3.1", sha256="7c6a82d1e6b19e136a7d16095743c50cd7b6340eeda594e4a8e14d74972ddb48")
    version("1.2.0", sha256="2e19308d3271fefd5e118c6d132d6a2511253b903620b5417892c72d2010a963")
    version("1.0.8", sha256="b149fcf3e98ef148945ff9f4272512cd03e21408c235ec6c0548167fd41219a1")
    version("1.0.4", sha256="2934efa5ff9ccfe1636d360aedec36713f3bb3128a493241dbb728d842ea3b5f")
    version("1.0.3", sha256="c93aceb499886e42bcd61eb7fb59e47a76c9ba5ab5349a426736d46c8ce21f4d")

    depends_on("c", type="build")  # generated

    with default_args(type=("build", "run")):
        depends_on("r@3.5:", when="@1.4.3:")
        depends_on("r@3.4:", when="@1.4.0:")
        depends_on("r@3.1:")

        depends_on("r-callr@3.2.0:", when="@1.0.4:")
        depends_on("r-callr@2.0.0:")
        depends_on("r-cli@3.4.0:", when="@1.4.0:")
        depends_on("r-cli")
        depends_on("r-desc")
        depends_on("r-processx", when="@1.4.0:")
        depends_on("r-r6")

        # Historical dependencies
        depends_on("r-crayon", when="@:1.4.2")
        depends_on("r-prettyunits", when="@:1.4.2")
        depends_on("r-rprojroot", when="@:1.4.2")
        depends_on("r-withr@2.3.0:", when="@1.3.1:1.4.0")
        depends_on("r-withr@2.1.2:", when="@:1.4.0")
