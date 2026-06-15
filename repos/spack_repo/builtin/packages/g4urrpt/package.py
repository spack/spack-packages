# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.packages.geant4_data.package import Geant4DataPackage

from spack.package import *


class G4urrpt(Geant4DataPackage):
    """Geant4 data for evaluated particle cross-sections on
    natural composition of elements"""

    homepage = "https://geant4.web.cern.ch"
    url = Geant4DataPackage.datasets_url + "/G4URRPT.1.0.tar.gz"

    tags = ["hep"]

    maintainers("drbenmorgan")

    # Only versions relevant to Geant4 releases built by spack are added
    version("1.1", sha256="6a3432db80bc088aee19c504b9c0124913005d6357ea14870451400ab20d9c11")
    version("1.0", sha256="278eb6c4086e919d2c2a718eb44d4897b7e06d2a32909f6ed48eb8590b3f9977")

    #: G4-prefixed environment variable
    g4envvar = "G4URRPTDATA"

    #: Directory name inside 'share' before version is appended
    g4dirname = "G4URRPT"
