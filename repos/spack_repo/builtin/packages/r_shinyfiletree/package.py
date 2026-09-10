# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RShinyfiletree(RPackage):
    """This creates a widget with a shiny file tree."""

    homepage = "https://github.com/fbreitwieser/shinyFileTree"
    url = "https://github.com/fbreitwieser/shinyFileTree/tarball/76c44e744c930c3908a98d4a055a5bff7fba1e0c"

    license("GPL-3.0")

    version(
        "0.0.0.9000",
        sha256="3df3d52798287b506613acf65eb07d9a535d55af97da0726f1b8ef202bd498df",
        url="https://github.com/fbreitwieser/shinyFileTree/tarball/76c44e744c930c3908a98d4a055a5bff7fba1e0c",
    )

    depends_on("r@3.2.3:", type=("build", "run"))
    depends_on("r-htmlwidgets", type=("build", "run"))
