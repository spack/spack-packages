# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.packages.geant4_data.package import Geant4DataPackage

from spack.package import *


class G4ndl(Geant4DataPackage):
    """Geant4 Neutron data files with thermal cross sections"""

    homepage = "https://geant4.web.cern.ch"
    url = Geant4DataPackage.datasets_url + "/G4NDL.4.5.tar.gz"

    tags = ["hep"]

    maintainers("drbenmorgan")

    version("4.7.1", sha256="d3acae48622118d2579de24a54d533fb2416bf0da9dd288f1724df1485a46c7c")
    version("4.7", sha256="7e7d3d2621102dc614f753ad928730a290d19660eed96304a9d24b453d670309")
    version("4.6", sha256="9d287cf2ae0fb887a2adce801ee74fb9be21b0d166dab49bcbee9408a5145408")
    version("4.5", sha256="cba928a520a788f2bc8229c7ef57f83d0934bb0c6a18c31ef05ef4865edcdf8e")
    version("4.4", sha256="e9fe8800566a83ccaf9b5229a1fa1d2cd24530bbd2e9fcb96eb6b5b117233071")

    #: G4-prefixed environment variable
    g4envvar = "G4NEUTRONHPDATA"

    #: Directory name inside 'share' before version is appended
    g4dirname = "G4NDL"
