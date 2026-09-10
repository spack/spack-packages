# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPygrib(PythonPackage):
    """Python interface for reading and writing GRIB data."""

    homepage = "https://jswhit.github.io/pygrib"
    pypi = "pygrib/pygrib-2.1.6.tar.gz"

    version("2.1.6", sha256="047980aeb010ef457999950bcc8e46556910316cb77fe78c0bd1b3520aa920f0")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("py-setuptools@61:", type="build")
    depends_on("py-cython@0.29:", type="build")
    depends_on("python@3.9:", type=("build", "run"))

    depends_on("py-packaging", type=("build", "run"))
    depends_on("py-pyproj", type=("build", "run"))
    depends_on("py-numpy@2:", type=("build", "run"))
    depends_on("eccodes", type=("build", "run"))

    # See: https://github.com/jswhit/pygrib/pull/269
    patch("fix-cython-3.1.patch", when="@2.1.6 ^py-cython@3.1:")

    def setup_build_environment(self, env):
        env.set("ECCODES_DIR", self.spec["eccodes"].prefix)
