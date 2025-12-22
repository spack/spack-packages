# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *

# Necessary to pin each version to py-mdanalysis
VERSIONS = {
    "2.10.0": "286b8678e19195093a19b57b26d76b8274415d33ac23fc872355639fcb49beef",
    "2.9.0": "8e4942ec3aaef5e93aeb39690293764ab9995550135ff1bd0df2f40cb95c0626",
    "2.8.0": "a611dfa060088cc11e582c90dbd37bd1142d65423f7de6e304d3d694655aee0b",
    "2.7.0": "326d65d7f14da8d1b047aab87ca312a68459a5fd18ddf6d8cb9ac9c3ca51d9e5",
    "2.6.1": "043f7451f4d9c42ea9e6609a81a6002948e2c74fd268282e0831416789b22e5e",
    "2.6.0": "16fdd10e5240b606e8f9210b7cbd9e4be110e6b8d79bb6e72ce6250c4731a817",
    "2.5.0": "a15b53b7f8bed67900a2bf542bbb3cab81dc71674fa6cddb3248dd11880e4c9d",
    "2.4.3": "6fbdeccdbfb249f76520ee3605d007cd70292187e3754d0184c71e5afe133abb",
    "2.4.2": "6e8fb210a4268691c77717ea5157e82d85874a4f7ee0f8f177718451a44ee793",
}


class PyMdanalysistests(PythonPackage):
    """Test suite for MDAnalysis"""

    homepage = "https://www.mdanalysis.org"
    pypi = "MDAnalysisTests/MDAnalysisTests-2.4.2.tar.gz"

    maintainers("RMeli")

    license("GPL-3.0-or-later")

    # Version need to match MDAnalysis'
    for mdanalysistests_version, sha in VERSIONS.items():
        version(mdanalysistests_version, sha256=sha)
        depends_on(
            f"py-mdanalysis@{mdanalysistests_version}",
            when=f"@{mdanalysistests_version}",
            type=("build", "run"),
        )

    depends_on("python@3.11:", when="@2.10.0:", type=("build", "run"))
    depends_on("python@3.10:", when="@2.8.0:", type=("build", "run"))
    depends_on("python@3.9:", when="@2.5.0:", type=("build", "run"))
    depends_on("python@3.8:", type=("build", "run"))

    depends_on("py-pytest@3.3.0:", type=("build", "run"))
    depends_on("py-hypothesis", type=("build", "run"))

    depends_on("py-setuptools@40.9.0:", when="@2.8.0:", type="build")
    depends_on("py-setuptools", type="build")

    def url_for_version(self, version):
        """
        From version 2.8.0 onwards, the archive named changed
        to 'mdanalysistests-{version}.tar.gz from 'MDAnalysistests-{version}.tar.gz
        """
        if version >= Version("2.8.0"):
            return f"https://files.pythonhosted.org/packages/source/m/mdanalysistests/mdanalysistests-{version}.tar.gz"
