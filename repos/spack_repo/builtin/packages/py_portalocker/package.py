# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPortalocker(PythonPackage):
    """Portalocker is a library to provide an easy API to file locking."""

    homepage = "https://github.com/WoLpH/portalocker"
    pypi = "portalocker/portalocker-2.5.1.tar.gz"

    license("BSD-3-Clause")

    version("3.2.0", sha256="1f3002956a54a8c3730586c5c77bf18fae4149e07eaf1c29fc3faf4d5a3f89ac")
    version("2.5.1", sha256="ae8e9cc2660da04bf41fa1a0eef7e300bb5e4a5869adfb1a6d8551632b559b2b")
    version("1.6.0", sha256="4013e6d17123560178a5ba28cb6fdf13fd3079dee18571ff824e05b7abc97b94")

    depends_on("python@3.5:", when="@2:", type=("build", "run"))
    depends_on("python@3.9:", when="@3:", type=("build", "run"))
    depends_on("py-setuptools@38.3.0:", type="build")
    depends_on("py-setuptools-scm", type="build", when="@3.2.0:")
    depends_on("py-pywin32@226:", type=("build", "run"), when="platform=windows")
