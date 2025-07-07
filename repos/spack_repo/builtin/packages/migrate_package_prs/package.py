# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class MigratePackagePrs(Package):
    """A command-line tool to copy open package pull requests from spack/spack to
    spack/spack-packages."""

    homepage = "https://github.com/spack/migrate-package-prs"
    url = "https://github.com/spack/migrate-package-prs/releases/download/v1.0.0/migrate-package-prs-1.0.0.tar.gz"

    maintainers("haampie")

    version("1.0.0", sha256="b9a64459d8ef9ecd750c9678578f19c0a5e9bceb94d2bde4a2bf7e233e1d73e7")

    depends_on("gh", type="run")
    depends_on("jq", type="run")

    def install(self, spec, prefix):
        install_tree(".", prefix)
