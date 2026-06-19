# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.packages.geant4_data.package import Geant4DataPackage

from spack.package import *


class G4realsurface(Geant4DataPackage):
    """Geant4 data for measured optical surface reflectance"""

    homepage = "https://geant4.web.cern.ch"

    tags = ["hep"]

    maintainers("drbenmorgan")

    # Only versions relevant to Geant4 releases built by spack are added
    version("2.2", sha256="9954dee0012f5331267f783690e912e72db5bf52ea9babecd12ea22282176820")
    version("2.1.1", sha256="90481ff97a7c3fa792b7a2a21c9ed80a40e6be386e581a39950c844b2dd06f50")
    version("2.1", sha256="2a287adbda1c0292571edeae2082a65b7f7bd6cf2bf088432d1d6f889426dcf3")
    version("1.0", sha256="3e2d2506600d2780ed903f1f2681962e208039329347c58ba1916740679020b1")

    #: G4-prefixed environment variable
    g4envvar = "G4REALSURFACEDATA"

    #: Directory name inside 'share' before version is appended
    g4dirname = "RealSurface"

    def url_for_version(self, version):
        """Handle version string."""
        datasets_url = Geant4DataPackage.datasets_url
        prefix = "G4" if version > Version("1.0") else ""
        return f"{datasets_url}/{prefix}RealSurface.{version}.tar.gz"
