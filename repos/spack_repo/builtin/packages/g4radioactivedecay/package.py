# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.generic import Package
from spack_repo.builtin.packages.geant4_data.package import Geant4DataPackage

from spack.package import *


class G4radioactivedecay(Package, Geant4DataPackage):
    """Geant4 data files for radio-active decay hadronic processes"""

    homepage = "https://geant4.web.cern.ch"

    tags = ["hep"]

    maintainers("drbenmorgan")

    # Only versions relevant to Geant4 releases built by spack are added
    version("6.1.2", sha256="a40d7e3ebc64d35555c4a49d0ff1e0945cd605d84354d053121293914caea13a")
    version("5.6", sha256="3886077c9c8e5a98783e6718e1c32567899eeb2dbb33e402d4476bc2fe4f0df1")
    version("5.4", sha256="240779da7d13f5bf0db250f472298c3804513e8aca6cae301db97f5ccdcc4a61")
    version("5.3", sha256="5c8992ac57ae56e66b064d3f5cdfe7c2fee76567520ad34a625bfb187119f8c1")
    version("5.2", sha256="99c038d89d70281316be15c3c98a66c5d0ca01ef575127b6a094063003e2af5d")
    version("5.1.1", sha256="f7a9a0cc998f0d946359f2cb18d30dff1eabb7f3c578891111fc3641833870ae")
    version("4.0", sha256="ed2053bddee507920a29a27db4364fbef255b951597686b0410d5458e9b38cb5")

    #: G4-prefixed environment variable
    g4envvar = "G4RADIOACTIVEDATA"

    #: Directory name inside 'share' before version is appended
    g4dirname = "RadioactiveDecay"

    def url_for_version(self, version):
        """Handle version string."""
        datasets_url = Geant4DataPackage.datasets_url
        prefix = "G4"
        return f"{datasets_url}/{prefix}{self.g4dirname}.{version}.tar.gz"
