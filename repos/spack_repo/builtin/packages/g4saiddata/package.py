# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.generic import Package
from spack_repo.builtin.packages.geant4_data.package import Geant4DataPackage

from spack.package import *


class G4saiddata(Package, Geant4DataPackage):
    """Geant4 data from evaluated cross-sections in SAID data-base"""

    homepage = "https://geant4.web.cern.ch"

    tags = ["hep"]

    maintainers("drbenmorgan")

    # Only versions relevant to Geant4 releases built by spack are added
    version("2.0", sha256="1d26a8e79baa71e44d5759b9f55a67e8b7ede31751316a9e9037d80090c72e91")
    version("1.1", sha256="a38cd9a83db62311922850fe609ecd250d36adf264a88e88c82ba82b7da0ed7f")

    #: G4-prefixed environment variable
    g4envvar = "G4SAIDXSDATA"

    #: Directory name inside 'share' before version is appended
    g4dirname = "G4SAIDDATA"
