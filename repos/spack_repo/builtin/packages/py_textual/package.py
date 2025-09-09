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
    version("0.47.1", sha256="4b82e317884bb1092f693f474c319ceb068b5a0b128b121f1aa53a2d48b4b80c")

    depends_on("python@3.8:3", type=("build", "run"))

    depends_on("py-poetry-core@1.2.0:", type="build")
    depends_on("py-rich@13.3.3:", type=("build", "run"))
    depends_on("py-markdown-it-py+linkify@2.1.0:", type=("build", "run"))
    depends_on("py-mdit-py-plugins", type=("build", "run"))
    # Depending on py-mdit-py-plugins rather than on py-markdown-it-py+plugins,
    # because py-markdown-it-py+plugins would cause a circular dependency
    depends_on("py-typing-extensions@4.4.0:4", type=("build", "run"))
    depends_on("py-platformdirs@3.6:4", when="@5.3:")
