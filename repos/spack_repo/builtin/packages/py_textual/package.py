# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTextual(PythonPackage):
    """Textual is a Rapid Application Development framework for Python."""

    homepage = "https://github.com/Textualize/textual"
    pypi = "textual/textual-0.47.1.tar.gz"

    version("5.3.0", sha256="1b6128b339adef2e298cc23ab4777180443240ece5c232f29b22960efd658d4d")
    version("5.2.0", sha256="6d4a77fddde7aa659acc25c3e14ed27ff75e125c6730c6f57263cf91b60e0d50")
    version("5.1.1", sha256="8df8830155046660592c8926e18d43c712dfe4e8a1351a98b1138f9b64ec14dc")
    version("5.1.0", sha256="28e3833c8bef2319ab09483077c9812da422cecdeaa673319ba00f0523921e67")
    version("5.0.1", sha256="c6e20489ee585ec3fa43b011aa575f52e4fafad550e040bff9f53a464897feb6")
    version("5.0.0", sha256="44f507a1e264bab753b436c55245d8a957c348b3cada37f12a7782b5ccfbb1da")
    version("0.47.1", sha256="4b82e317884bb1092f693f474c319ceb068b5a0b128b121f1aa53a2d48b4b80c")

    depends_on("python@3.8:3", type=("build", "run"))

    depends_on("py-poetry-core@1.2.0:", type="build")
    depends_on("py-rich@13.3.3:", type=("build", "run"))
    depends_on("py-markdown-it-py+linkify@2.1.0:", type=("build", "run"))
    depends_on("py-mdit-py-plugins", type=("build", "run"))
    # Depending on py-mdit-py-plugins rather than on py-markdown-it-py+plugins,
    # because py-markdown-it-py+plugins would cause a circular dependency
    depends_on("py-typing-extensions@4.4.0:4", type=("build", "run"))
