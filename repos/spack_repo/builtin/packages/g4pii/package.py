# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.packages.geant4_data.package import Geant4DataPackage

from spack.package import *


class G4pii(Geant4DataPackage):
    """Geant4 data for shell ionisation cross-sections"""

    homepage = "https://geant4.web.cern.ch"

    tags = ["hep"]

    maintainers("drbenmorgan")

    # Only versions relevant to Geant4 releases built by spack are added
    version("1.3", sha256="6225ad902675f4381c98c6ba25fc5a06ce87549aa979634d3d03491d6616e926")

    #: G4-prefixed environment variable
    g4envvar = "G4PIIDATA"

    #: Directory name inside 'share' before version is appended
    g4dirname = "G4PII"
