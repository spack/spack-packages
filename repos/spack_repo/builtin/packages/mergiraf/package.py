# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cargo import CargoPackage

from spack.package import *


class Mergiraf(CargoPackage):
    """A syntax-aware git merge driver for a growing collection of programming
    languages and file formats.
    """

    homepage = "https://mergiraf.org/"
    url = "https://codeberg.org/mergiraf/mergiraf/archive/v0.6.0.tar.gz"
    list_url = "https://codeberg.org/mergiraf/mergiraf/releases"

    maintainers("alecbcs")

    license("GPL-3.0-only")

    version("0.16.3", sha256="c2f3f6b50496cbadb7d9caeb6cfc4e0dab8f99aaed5d9a560b30208cb68108f0")
    version("0.15.0", sha256="75f553935df38dd84679727fe3b3232d54ed4a9fe6ca214e3fd54ac714d0fae3")
    version("0.14.0", sha256="61738fea60d15ffb223d4af2e52fd02b0abddbbd0d9f58f7a33acd49fe4d4f9b")
    version("0.13.0", sha256="8b3851bac8ebac3c973c0f82fcaf1e4cc7a68d4effe3a4d727963b3824972909")
    version("0.12.1", sha256="5006c72d446e2b634e41d6d760661773ad449fed93154a8c8d461ad91461f997")
    version("0.8.1", sha256="b9f76cd133dbd60382a00705e4bed67727b94082f6c6a72d43fd6b7593a18595")
    version("0.6.0", sha256="548b0ae3d811d6410beae9e7294867c7e6d791cf9f68ddda5c24e287f7978030")

    depends_on("rust@1.89:", type="build", when="@0.12:")
