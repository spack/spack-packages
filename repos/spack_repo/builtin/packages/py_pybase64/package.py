# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPybase64(PythonPackage):
    """Fast Base64 encoding/decoding."""

    homepage = "https://github.com/mayeut/pybase64"
    pypi = "pybase64/pybase64-1.4.3.tar.gz"

    version("1.4.3", sha256="c2ed274c9e0ba9c8f9c4083cfe265e66dd679126cd9c2027965d807352f3f053")

    depends_on("c", type="build")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools@80:", type="build")
