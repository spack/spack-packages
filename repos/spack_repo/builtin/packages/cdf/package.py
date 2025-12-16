# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Cdf(MakefilePackage):
    """NASA CDF (Common Data Format) is a self-describing data format for the
    storage and manipulation of scalar and multidimensional data in a platform
    and discipline independent fashion."""

    homepage = "https://cdf.gsfc.nasa.gov/"
    url = "https://spdf.gsfc.nasa.gov/pub/software/cdf/dist/cdf39_1/cdf39_1-dist-cdf.tar.gz"

    maintainers("edhartnett")

    license("NASA-1.3")

    version("3.9.1", sha256="d548789117c52fcd4d08be5f432c86ae927e182d3876e800cd4ca98e5f7fa5e7")

    def edit(self, spec, prefix):
        """CDF build system doesn't require editing."""
        pass

    def build(self, spec, prefix):
        """Build CDF with custom Makefile parameters."""
        make("OS=linux", "ENV=gnu", "all")

    def install(self, spec, prefix):
        """Install CDF to specified prefix."""
        make("INSTALLDIR={0}".format(prefix), "install")
