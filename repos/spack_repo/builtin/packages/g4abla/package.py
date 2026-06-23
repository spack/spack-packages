# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.generic import Package
from spack_repo.builtin.packages.geant4_data.package import Geant4DataPackage

from spack.package import *


class G4abla(Package, Geant4DataPackage):
    """Geant4 data for nuclear shell effects in INCL/ABLA hadronic mode"""

    homepage = "https://geant4.web.cern.ch"

    tags = ["hep"]

    maintainers("drbenmorgan")

    # Only versions relevant to Geant4 releases built by spack are added
    version("3.3", sha256="1e041b3252ee9cef886d624f753e693303aa32d7e5ef3bba87b34f36d92ea2b1")
    version("3.1", sha256="7698b052b58bf1b9886beacdbd6af607adc1e099fc730ab6b21cf7f090c027ed")
    version("3.0", sha256="99fd4dcc9b4949778f14ed8364088e45fa4ff3148b3ea36f9f3103241d277014")

    #: G4-prefixed environment variable
    g4envvar = "G4ABLADATA"

    #: Directory name inside 'share' before version is appended
    g4dirname = "G4ABLA"
