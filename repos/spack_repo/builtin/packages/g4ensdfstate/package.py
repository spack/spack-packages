# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.packages.geant4_data.package import Geant4DataPackage

from spack.package import *


class G4ensdfstate(Package, Geant4DataPackage):
    """Geant4 data for nuclides properties"""

    homepage = "https://geant4.web.cern.ch"
    url = Geant4DataPackage.datasets_url + "/G4ENSDFSTATE.2.1.tar.gz"

    tags = ["hep"]

    maintainers("drbenmorgan")

    # Only versions relevant to Geant4 releases built by spack are added
    version("3.0", sha256="4bdc3bd40b31d43485bf4f87f055705e540a6557d64ed85c689c59c9a4eba7d6")
    version("2.3", sha256="9444c5e0820791abd3ccaace105b0e47790fadce286e11149834e79c4a8e9203")
    version("2.2", sha256="dd7e27ef62070734a4a709601f5b3bada6641b111eb7069344e4f99a01d6e0a6")
    version("2.1", sha256="933e7f99b1c70f24694d12d517dfca36d82f4e95b084c15d86756ace2a2790d9")
    version("1.0", sha256="4562e7476aa2df7204a1a77263e9d2331e9ffcdb591d11814dcc2d6b605021dd")

    #: G4-prefixed environment variable
    g4envvar = "G4ENSDFSTATEDATA"

    #: Directory name inside 'share' before version is appended
    g4dirname = "G4ENSDFSTATE"
