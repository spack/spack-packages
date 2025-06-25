# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.bundle import BundlePackage
from spack.package import *


class CiKickPackage(BundlePackage):
    """Package for forcing a to run in CI"""

    homepage = "https://www.spack.io"

    maintainers("kwryankrattiger", "eugenewalker")

    variant("asdf", default=True, description="asdf")

    def install(self):
        """Force install failure to avoid this package ever existing in the build cache"""
        exit(1)
