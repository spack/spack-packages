# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.packages.geant4_data.package import Geant4DataPackage

from spack.package import *


class G4tendl(Geant4DataPackage):
    """Optional Geant4 data for incident particles."""

    homepage = "https://geant4.web.cern.ch"

    tags = ["hep"]

    maintainers("drbenmorgan")

    # Only versions relevant to Geant4 releases built by spack are added
    version("1.4", sha256="4b7274020cc8b4ed569b892ef18c2e088edcdb6b66f39d25585ccee25d9721e0")
    version("1.3.2", sha256="3b2987c6e3bee74197e3bd39e25e1cc756bb866c26d21a70f647959fc7afb849")
    version("1.3", sha256="52ad77515033a5d6f995c699809b464725a0e62099b5e55bf07c8bdd02cd3bce")

    #: G4-prefixed environment variable
    g4envvar = "G4PARTICLEHPDATA"

    #: Directory name inside 'share' before version is appended
    g4dirname = "G4TENDL"
