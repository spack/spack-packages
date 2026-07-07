# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.packages.geant4_data.package import Geant4DataPackage

from spack.package import *


class G4incl(Package, Geant4DataPackage):
    """Geant4 data for evaluated particle cross-sections on natural
    composition of elements"""

    homepage = "https://geant4.web.cern.ch"

    tags = ["hep"]

    maintainers("drbenmorgan")

    # Only versions relevant to Geant4 releases built by spack are added
    version("1.3", sha256="e4b3dbe52acef53536454e22443091212843821bd23628eed846d299599f3bf9")
    version("1.2", sha256="f880b16073ee0a92d7494f3276a6d52d4de1d3677a0d4c7c58700396ed0e1a7e")
    version("1.1", sha256="5d82e71db5f5a1b659937506576be58db7de7753ec5913128141ae7fce673b44")
    version("1.0", sha256="716161821ae9f3d0565fbf3c2cf34f4e02e3e519eb419a82236eef22c2c4367d")

    #: G4-prefixed environment variable
    g4envvar = "G4INCLDATA"

    #: Directory name inside 'share' before version is appended
    g4dirname = "G4INCL"
