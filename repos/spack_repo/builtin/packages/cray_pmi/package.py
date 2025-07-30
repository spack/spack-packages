# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack.package import *


class CrayPmi(Package):
    """Cray's Process Management Interface library"""

    homepage = "https://docs.nersc.gov/development/compilers/wrappers/"

    maintainers("haampie")

    version("5.0.17")
    version("5.0.16")
    version("5.0.11")

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

    @property
    def headers(self):
        return find_headers("pmi", self.prefix.include, recursive=True)

    @property
    def libs(self):
        return find_libraries(["libpmi"], root=self.prefix, recursive=True)
