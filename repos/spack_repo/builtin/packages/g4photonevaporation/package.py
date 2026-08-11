# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.packages.geant4_data.package import Geant4DataPackage

from spack.package import *


class G4photonevaporation(Package, Geant4DataPackage):
    """Geant4 data for photon evaporation"""

    homepage = "https://geant4.web.cern.ch"

    tags = ["hep"]

    maintainers("drbenmorgan")

    # Only versions relevant to Geant4 releases built by spack are added
    version("6.1.2", sha256="02149c0ab91d88ee24e78532558777e39a068b9fcdd199136101ff58e635e742")
    version("6.1", sha256="5ffc1f99a81d50c9020186d59874af73c53ba24c1842b3b82b3188223bb246f2")
    version("5.7", sha256="761e42e56ffdde3d9839f9f9d8102607c6b4c0329151ee518206f4ee9e77e7e5")
    version("5.5", sha256="5995dda126c18bd7f68861efde87b4af438c329ecbe849572031ceed8f5e76d7")
    version("5.3", sha256="d47ababc8cbe548065ef644e9bd88266869e75e2f9e577ebc36bc55bf7a92ec8")
    version("5.2", sha256="83607f8d36827b2a7fca19c9c336caffbebf61a359d0ef7cee44a8bcf3fc2d1f")
    version("4.3.2", sha256="d4641a6fe1c645ab2a7ecee09c34e5ea584fb10d63d2838248bfc487d34207c7")
    version("3.0", sha256="c76a843672eca21110e97a274a6b5cd9a58b66f35235301c8e1b162926e0e7cb")

    #: G4-prefixed environment variable
    g4envvar = "G4LEVELGAMMADATA"

    #: Directory name inside 'share' before version is appended
    g4dirname = "PhotonEvaporation"

    def url_for_version(self, version):
        """Handle version string."""
        datasets_url = Geant4DataPackage.datasets_url
        prefix = "G4"
        return f"{datasets_url}/{prefix}{self.g4dirname}.{version}.tar.gz"
