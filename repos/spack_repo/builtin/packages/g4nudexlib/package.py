# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.packages.geant4_data.package import Geant4DataPackage

from spack.package import *


class G4nudexlib(Package, Geant4DataPackage):
    """Geant4 data for evaluated particle cross-sections on
    natural composition of elements"""

    homepage = "https://geant4.web.cern.ch"

    tags = ["hep"]

    maintainers("drbenmorgan")

    # Only versions relevant to Geant4 releases built by spack are added
    version("1.0", sha256="cac7d65e9c5af8edba2b2667d5822e16aaf99065c95f805e76de4cc86395f415")

    #: G4-prefixed environment variable
    g4envvar = "G4NUDEXLIBDATA"

    #: Directory name inside 'share' before version is appended
    g4dirname = "G4NUDEXLIB"
