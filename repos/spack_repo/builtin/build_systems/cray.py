# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack.package import InstallError, Package, depends_on, requires


class CrayExternal(Package):
    """Specialization of Package that takes care of setting common metadata for Cray software
    that must be used only as an external package.
    """

    has_code = False  # Skip attempts to fetch a source that is not available

    # Allows attaching compilers to externals in packages.yaml
    depends_on("c", type="build")

    requires("platform=linux", msg="Cray software is only available on linux")

    def install(self, spec, prefix):
        raise InstallError(
            self.spec.format(
                "{name} is not installable, you need to specify "
                "it as an external package in packages.yaml"
            )
        )
