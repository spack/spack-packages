# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RGoogledrive(RPackage):
    """An Interface to Google Drive.

    Manage Google Drive files from R."""

    cran = "googledrive"

    license("MIT")

    version("2.1.2", sha256="3809ea4d8333eb80e6ca4e780f198014f65b21c3cf4ec95a63aeb6772c8d94aa")
    version("2.1.1", sha256="0b8b4f74ba3630b0347249a32a80bc5fc2e8b63ad2952702f30162bd2d38fb82")
    version("2.1.0", sha256="0d70353bbf1bebc96d3987ebd9cbb2b0902e6ddc4cdccece3d07c2bb688c4b74")
    version("2.0.0", sha256="605c469a6a086ef4b049909c2e20a35411c165ce7ce4f62d68fd39ffed8c5a26")

    with default_args(type=("build", "run")):
        depends_on("r@4.1:", when="@2.1.2:")
        depends_on("r@3.6:", when="@2.1.1:")
        depends_on("r@3.5:", when="@2.1.0:")
        depends_on("r@3.3:")

        depends_on("r-cli@3.0.0:")
        depends_on("r-gargle@1.6.0:", when="@2.1.2:")
        depends_on("r-gargle@1.5.0:", when="@2.1.1:")
        depends_on("r-gargle@1.3.0:", when="@2.1.0:")
        depends_on("r-gargle@1.2.0:")
        depends_on("r-glue@1.4.2:")
        depends_on("r-httr")
        depends_on("r-jsonlite")
        depends_on("r-lifecycle")
        depends_on("r-magrittr")
        depends_on("r-pillar@1.9.0:", when="@2.1.1:")
        depends_on("r-pillar")
        depends_on("r-purrr@1.0.1:", when="@2.1.0:")
        depends_on("r-purrr@0.2.3:")
        depends_on("r-rlang@1.0.2:", when="@2.1.0:")
        depends_on("r-rlang@0.4.9:")
        depends_on("r-tibble@2.0.0:")
        depends_on("r-uuid")
        depends_on("r-vctrs@0.3.0:")
        depends_on("r-withr")
