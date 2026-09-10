# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyJsonschemaSpecifications(PythonPackage):
    """The JSON Schema meta-schemas and vocabularies, exposed as a Registry."""

    homepage = "https://jsonschema-specifications.readthedocs.io/"
    pypi = "jsonschema_specifications/jsonschema_specifications-2023.12.1.tar.gz"

    maintainers("wdconinc")

    license("MIT", checked_by="wdconinc")

    version("2025.9.1", sha256="b540987f239e745613c7a9176f3edb72b832a4ac465cf02712288397832b5e8d")
    version("2023.12.1", sha256="48a76787b3e70f5ed53f1160d2b81f586e4ca6d1548c5de7085d1682674764cc")

    depends_on("python@3.9:", type=("build", "run"), when="@2024:")
    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-hatchling@1.27.0:", type="build", when="@2025:")
    depends_on("py-hatchling", type="build")
    depends_on("py-hatch-vcs", type="build")

    depends_on("py-referencing@0.31.0:", type=("build", "run"))

    # Historical dependencies
    depends_on("py-importlib-resources@1.4.0:", type=("build", "run"), when="^python@:3.8")
