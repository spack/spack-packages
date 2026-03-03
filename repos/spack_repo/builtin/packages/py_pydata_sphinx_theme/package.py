# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPydataSphinxTheme(PythonPackage):
    """A clean, three-column, Bootstrap-based Sphinx theme by and for the PyData community."""

    homepage = "https://pydata-sphinx-theme.readthedocs.io/en/stable"
    pypi = "pydata_sphinx_theme/pydata_sphinx_theme-0.14.1.tar.gz"

    license("BSD-3-Clause")

    version("0.16.1", sha256="a08b7f0b7f70387219dc659bff0893a7554d5eb39b59d3b8ef37b8401b7642d7")
    version("0.16.0", sha256="721dd26e05fa8b992d66ef545536e6cbe0110afb9865820a08894af1ad6f7707")
    version("0.15.4", sha256="7762ec0ac59df3acecf49fd2f889e1b4565dbce8b88b2e29ee06fdd90645a06d")
    version("0.15.3", sha256="f26ed9b676f61d1b2ae9289f3d7e496e8678dd56f2568b27a66fa4ad1f164efd")
    version("0.15.2", sha256="4243fee85b3afcfae9df64f83210a04e7182e53bc3db8841ffff6d21d95ae320")
    version("0.15.1", sha256="4606f7d59765ae06ff7cb5e07dead4286ea2ff2164deeee63922481eddf1083c")
    version("0.14.4", sha256="f5d7a2cb7a98e35b9b49d3b02cec373ad28958c2ed5c9b1ffe6aff6c56e9de5b")
    version("0.14.3", sha256="bd474f347895f3fc5b6ce87390af64330ee54f11ebf9660d5bc3f87d532d4e5c")
    version("0.14.2", sha256="53860c95686f2b4fd8823ff977116a0dd654cceb01ff63c415cfeb5f19736753")
    version("0.14.1", sha256="d8d4ac81252c16a002e835d21f0fea6d04cf3608e95045c816e8cc823e79b053")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("python@3.9:", type=("build", "run"), when="@0.15.0:")

    depends_on("py-sphinx-theme-builder", type="build")

    depends_on("py-sphinx@5:", type=("build", "run"))
    depends_on("py-sphinx@6.1:", type=("build", "run"), when="@0.16.0:")
    depends_on("py-beautifulsoup4", type=("build", "run"))
    depends_on("py-docutils@:0.16,0.17.1:", type=("build", "run"))
    depends_on("py-packaging", type=("build", "run"), when="@:0.15")
    depends_on("py-babel", type=("build", "run"))
    depends_on("py-pygments@2.7:", type=("build", "run"))
    depends_on("py-accessible-pygments", type=("build", "run"))
    depends_on("py-typing-extensions", type=("build", "run"))
