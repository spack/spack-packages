# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyLogistro(PythonPackage):
    """Simple wrapper over logging for a couple basic features."""

    homepage = "https://github.com/geopozo/logistro"
    pypi = "logistro/logistro-1.1.0.tar.gz"

    license("MIT")

    version("2.0.1", sha256="8446affc82bab2577eb02bfcbcae196ae03129287557287b6a070f70c1985047")
    version("1.1.0", sha256="ad51f0efa2bc705bea7c266e8a759cf539457cf7108202a5eec77bdf6300d774")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools@65:", type="build")
    depends_on("py-setuptools-git-versioning", type="build")
