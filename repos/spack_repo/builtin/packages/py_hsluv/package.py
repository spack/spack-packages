# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyHsluv(PythonPackage):
    """hsluv is a Python implementation of HSLuv, a human-friendly HSL color
    space. It can convert to/from hex and RGB."""

    homepage = "https://www.hsluv.org"
    pypi = "hsluv/hsluv-5.0.4.tar.gz"

    maintainers("Markus92")

    license("MIT", checked_by="Markus92")

    version("5.0.4", sha256="2281f946427a882010042844a38c7bbe9e0d0aaf9d46babe46366ed6f169b72e")

    depends_on("python@3.7:", type=("build", "run"))

    depends_on("py-setuptools@38.6.0:", type="build")
