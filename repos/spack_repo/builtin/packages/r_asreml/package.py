# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RAsreml(RPackage):
    """ASReml-R is a statistical package that fits linear mixed models using
    Residual Maximum Likelihood (REML) in the R environment."""

    # NOTES
    # Annoyingly, this doesn't seem to be distributed well.
    # When you download a version of asreml-r you get a file named
    # the same regardless of the r version requested.
    # You're going to need to rename the archive to fit the
    # naming pattern below.

    homepage = "https://vsni.co.uk/software/asreml-r"

    manual_download = True
    license_required = True
    license_vars = ["vsni_LICENSE"]
    license_files = ["vsni.lic"]

    maintainers("snehring")

    license("UNKNOWN", checked_by="snehring")

    requires("target=x86_64: platform=linux", msg="r-asreml is only available for x86_64 linux")

    version(
        "4.2.0.393_R45", sha256="a180d47af2f21c09055c1bd0808515bc1b457e196d2f239e9984b38950643b11"
    )
    version(
        "4.2.0.393_R44", sha256="cc4e3385cb0195a85fd6a5d339a21ce80c7c6731f567d88780db53aeb11cca24"
    )
    version(
        "4.2.0.393_R43", sha256="8d5becb56a6a0a32d45cb14548833c861fc95d4ec8139129170193ea05ec1c44"
    )
    version(
        "4.2.0.302_R43", sha256="0a685521c80e3263ebb852886d3e1bd31213bd83507e7fffca34261ae18523f9"
    )

    with default_args(type=("build", "run")):
        depends_on("r@4.5", when="@4.2.0.393_R45")
        depends_on("r@4.4", when="@4.2.0.393_R44")
        depends_on("r@4.3", when="@4.2.0.302_R43:4.2.0.393_R43")
        depends_on("r-data-table")
        depends_on("r-ggplot2")
        depends_on("r-jsonlite")

    def url_for_version(self, version):
        return f"file://{os.getcwd()}//asreml_{version}_x86_64-pc-linux-gnu.tar.gz"

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        env.set("vsni_LICENSE", join_path(self.prefix, "vsni.lic"))
