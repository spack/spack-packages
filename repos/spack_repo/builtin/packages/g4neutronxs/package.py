# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.packages.geant4_data.package import Geant4DataPackage

from spack.package import *


class G4neutronxs(Package, Geant4DataPackage):
    """Geant4 data for evaluated neutron cross-sections on natural composition
    of elements"""

    homepage = "https://geant4.web.cern.ch"
    url = Geant4DataPackage.datasets_url + "/G4NEUTRONXS.1.4.tar.gz"

    tags = ["hep"]

    maintainers("drbenmorgan")

    # Only versions relevant to Geant4 releases built by spack are added
    # Dataset not used after Geant4 10.4.x
    version("1.4", sha256="57b38868d7eb060ddd65b26283402d4f161db76ed2169437c266105cca73a8fd")

    #: G4-prefixed environment variable
    g4envvar = "G4NEUTRONXSDATA"

    #: Directory name inside 'share' before version is appended
    g4dirname = "G4NEUTRONXS"
