# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyIjson(PythonPackage):
    """Iterative JSON parser with standard Python iterator interfaces."""

    homepage = "https://github.com/ICRAR/ijson"
    pypi = "ijson/ijson-3.5.0.tar.gz"

    version("3.5.0", sha256="94688760720e3f5212731b3cb8d30267f9a045fb38fb3870254e7b9504246f31")

    depends_on("c", type="build")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools@77:", type="build")
