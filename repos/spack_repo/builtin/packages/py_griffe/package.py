# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyGriffe(PythonPackage):
    """Signatures for entire Python programs. Extract the structure, the frame,
    the skeleton of your project, to generate API documentation or find
    breaking changes in your API."""

    homepage = "https://mkdocstrings.github.io/griffe/"
    pypi = "griffe/griffe-0.22.0.tar.gz"

    license("ISC")

    version("1.15.0", sha256="7726e3afd6f298fbc3696e67958803e7ac843c1cfe59734b6251a40cdbfb5eea")
    version("0.22.0", sha256="a3c25a2b7bf729ecee7cd455b4eff548f01c620b8f58a8097a800caad221f12e")

    depends_on("python@3.10:", type=("build", "run"), when="@1.15:")
    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-pdm-backend", type="build", when="@0.26:")
    depends_on("py-pdm-pep517", type="build", when="@:0.25")

    depends_on("py-colorama@0.4:", type=("build", "run"), when="@1.15.0:")
    depends_on("py-cached-property", type=("build", "run"), when="^python@:3.7")
