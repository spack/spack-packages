# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyFreetypePy(PythonPackage):
    """Freetype Python provides bindings for the FreeType library. Only the
    high-level API is bound."""

    homepage = "https://https://freetype-py.readthedocs.io/en/latest/"
    pypi = "freetype-py/freetype-py-2.5.1.zip"

    maintainers("Markus92")

    license("BSD-3-Clause", checked_by="Markus92")

    version("2.5.1", sha256="cfe2686a174d0dd3d71a9d8ee9bf6a2c23f5872385cf8ce9f24af83d076e2fbd")

    depends_on("py-setuptools@42:", type="build")
    depends_on("py-setuptools-scm@3.4: +toml", type="build")

    depends_on("freetype", type=("build", "run"))
