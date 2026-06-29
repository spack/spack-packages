# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.packages.geant4_data.package import Geant4DataPackage

from spack.package import *


class G4particlexs(Package, Geant4DataPackage):
    """Geant4 data for evaluated particle cross-sections on
    natural composition of elements"""

    homepage = "https://geant4.web.cern.ch"

    tags = ["hep"]

    maintainers("drbenmorgan")

    # Only versions relevant to Geant4 releases built by spack are added
    version("4.2", sha256="c52bbf86aaa589b78aba80b16ab0adf1041ea300de5395865b97fcee6eb55851")
    version("4.1", sha256="07ae1e048e9ac8e7f91f6696497dd55bd50ccc822d97af1a0b9e923212a6d7d1")
    version("4.0", sha256="9381039703c3f2b0fd36ab4999362a2c8b4ff9080c322f90b4e319281133ca95")
    version("3.1.1", sha256="66c17edd6cb6967375d0497add84c2201907a25e33db782ebc26051d38f2afda")
    version("3.1", sha256="404da84ead165e5cccc0bb795222f6270c9bf491ef4a0fd65195128b27f0e9cd")
    version("2.1", sha256="094d103372bbf8780d63a11632397e72d1191dc5027f9adabaf6a43025520b41")
    version("1.1", sha256="100a11c9ed961152acfadcc9b583a9f649dda4e48ab314fcd4f333412ade9d62")

    #: G4-prefixed environment variable
    g4envvar = "G4PARTICLEXSDATA"

    #: Directory name inside 'share' before version is appended
    g4dirname = "G4PARTICLEXS"
