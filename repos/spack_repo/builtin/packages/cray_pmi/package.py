# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cray import CrayPackage

from spack.package import *


class CrayPmi(CrayPackage):
    """Cray's Process Management Interface library"""

    homepage = "https://docs.nersc.gov/development/compilers/wrappers/"

    maintainers("haampie")

    version("5.0.17")
    version("5.0.16")
    version("5.0.11")

    @property
    def headers(self):
        return find_headers("pmi", self.prefix.include, recursive=True)

    @property
    def libs(self):
        return find_libraries(["libpmi"], root=self.prefix, recursive=True)
