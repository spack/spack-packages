# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RQuickjsr(RPackage):
    """An 'R' interface to the 'QuickJS' portable 'JavaScript' engine.
    The engine and all 'R' to 'JavaScript' interoperability is bundled
    within the package, requiring no dependencies beyond a 'C' compiler."""

    homepage = "https://bellard.org/quickjs/"
    cran = "QuickJSR"

    license("MIT", checked_by="wdconinc")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    version("1.9.2", sha256="f0ab99048cfb520d818401da99fbcac844a83c3f27f085f91d8fd8a17f319de0")
    version("1.8.1", sha256="dd4cf107016d659991cdbd313908209e3998ea8b093f3632d8b3a84dea435e0f")
    version("1.3.1", sha256="10559d6e84a838ec97acdbc6028a59e2121811d4a20e83c95cdb8fb4ce208fd1")
