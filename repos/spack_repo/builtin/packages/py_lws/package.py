# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyLws(PythonPackage):
    """Fast spectrogram phase recovery using Local Weighted Sums"""

    homepage = "https://pypi.org/project/lws/"
    pypi = "lws/lws-1.2.6.tar.gz"

    license("Apache-2.0")

    version("1.2.8", sha256="aaaf86c4f040bc33f81981333fb37c280cd82ec338b8a421a5f74ba3c6f64d06")
    version("1.2.6", sha256="ac94834832aadfcd53fcf4a77e1d95155063b39adbce14c733f8345bdac76e87")

    depends_on("cxx", type="build")  # generated

    depends_on("python@3:", type=("build", "run"))
    depends_on("py-cython", type="build")
    depends_on("py-setuptools", type="build")
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.set("LWS_USE_CYTHON", "1")
