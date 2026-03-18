# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.bundle import BundlePackage

from spack.package import *


class SmokeTest(BundlePackage):
    """This is a smoke-test package for use in CI to force pipelines to run re-build jobs.

    Note: This package requires that the builtin repo is also in the python path
    """

    homepage = "https://www.spack.io"

    maintainers("kwryankrattiger")

    # This package has the same license as Spack
    license("Apache-2.0 OR MIT")

    version("0.1.0")

    def install(self, *args):
        """This install method always fails. This ensures there is never a binary cache
        created so this package is guarenteed to rebuild in CI
        """
        raise InstallError("smoke-test")
