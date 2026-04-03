# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPropcache(PythonPackage):
    """Fast property caching"""

    homepage = "https://github.com/aio-libs/propcache"
    pypi = "propcache/propcache-0.3.1.tar.gz"

    license("Apache-2.0")

    version("0.4.1", sha256="f48107a8c637e80362555f37ecf49abe20370e557cc4ab374f04ec4423c97c3d")
    version("0.3.2", sha256="20d7d62e4e7ef05f221e0db2856b979540686342e7dd9973b815599c7057e168")
    version("0.3.1", sha256="40d980c33765359098837527e18eddefc9a24cea5b45e078a7f3bb5b032c6ecf")

    depends_on("py-setuptools@47:", type="build")
    depends_on("py-expandvars", type="build")
    depends_on("py-tomli", when="^python@:3.10", type="build")
    depends_on("py-cython", type="build")

    depends_on("python@3.9:", when="@0.2.1:", type=("build", "run"))
