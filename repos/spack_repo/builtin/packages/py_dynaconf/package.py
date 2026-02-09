# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyDynaconf(PythonPackage):
    """Dynaconf is a dynamic configuration management package for Python projects"""

    homepage = "https://github.com/dynaconf/dynaconf"
    pypi = "dynaconf/dynaconf-3.2.2.tar.gz"

    license("MIT")

    version("3.2.9", sha256="a612a05c0307b826193b9f7e738f9497c537d5b2668aa2979da3538d7dcdd400")
    version("3.2.2", sha256="2f98ec85a2b8edb767b3ed0f82c6d605d30af116ce4622932a719ba70ff152fc")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools@38.6.0:", type="build")
