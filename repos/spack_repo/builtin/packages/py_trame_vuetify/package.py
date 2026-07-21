# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTrameVuetify(PythonPackage):
    """Vuetify widgets for trame"""

    homepage = "https://github.com/Kitware/trame-vuetify"
    git = "https://github.com/Kitware/trame-vuetify.git"
    pypi = "trame_vuetify/trame_vuetify-3.2.1.tar.gz"

    maintainers("LydDeb")

    license("MIT", checked_by="LydDeb")

    version("3.2.1", sha256="1578904a8fc5313ba8033076ea2d9338a050a26c68ceebb207fb6b15e18c0a45")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-trame-client@3.7:3", type=("build", "run"))
