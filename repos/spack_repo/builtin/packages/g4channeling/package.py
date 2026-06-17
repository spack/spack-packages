# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.packages.geant4_data.package import Geant4DataPackage

from spack.package import *


class G4channeling(Package, Geant4DataPackage):
    """Geant4 data for solid state crystal channeling"""

    homepage = "https://geant4.web.cern.ch"
    url = Geant4DataPackage.datasets_url + "/G4CHANNELING.1.0.tar.gz"

    tags = ["hep"]

    maintainers("drbenmorgan")

    # Only versions relevant to Geant4 releases built by spack are added
    version("2.0", sha256="662159288644e07b79d7fe091efbebba52b59546b3dc6f5d285b976ad12f2d06")
    version("1.0", sha256="203e3c69984ca09acd181a1d31a9b0efafad4bc12e6c608f0b05e695120d67f2")

    #: G4-prefixed environment variable
    g4envvar = "G4CHANNELINGDATA"

    #: Directory name inside 'share' before version is appended
    g4dirname = "G4CHANNELING"
