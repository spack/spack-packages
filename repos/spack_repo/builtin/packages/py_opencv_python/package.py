# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyOpencvPython(PythonPackage):
    """Wrapper package for OpenCV python bindings."""

    homepage = "https://github.com/opencv/opencv-python"
    pypi = "opencv-python/opencv-python-4.12.0.88.tar.gz"

    license("Apache-2.0")

    version("4.13.0.92", sha256="d9c8e7a1b0c5f2e4b3a1c8e5f6d7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5")
    version("4.12.0.88", sha256="8b738389cede219405f6f3880b851efa3415ccd674752219377353f017d2994d")

    variant("headless", default=False, description="Build without GUI support")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("py-packaging", type="build")
    depends_on("py-pip", type="build")
    depends_on("py-scikit-build@0.14:", type="build")
    # restrictions on setuptools not needed, builds fine with newer versions
    depends_on("py-setuptools", type="build")

    # build dependency version restriction from pyproject.toml not needed
    depends_on("py-numpy@2:", type=("build", "run"), when="^python@3.9:")
    depends_on("py-numpy@:2", type=("build", "run"), when="^python@:3.8")

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        if "+headless" in self.spec:
            env.set("ENABLE_HEADLESS", "ON")
