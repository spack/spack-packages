# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySphinxBookTheme(PythonPackage):
    """Lightweight Sphinx theme designed to mimic the look-and-feel of an interactive book."""

    homepage = "https://sphinx-book-theme.readthedocs.io/en/latest"
    pypi = "sphinx_book_theme/sphinx_book_theme-1.0.1.tar.gz"

    license("BSD-3-Clause")

    version("1.1.4", sha256="73efe28af871d0a89bd05856d300e61edce0d5b2fbb7984e84454be0fedfe9ed")
    version("1.1.3", sha256="1f25483b1846cb3d353a6bc61b3b45b031f4acf845665d7da90e01ae0aef5b4d")
    version("1.1.2", sha256="7f3abcd146ca82e6f39d6db53711102b1c1d328d12f65e3e47ad9bf842614a49")
    version("1.1.1", sha256="e4d1058dbcc2b693c8dfa76110fa122c8219a81b3fb35c6929f23d5da9befd3e")
    version("1.1.0", sha256="ad4f92998e53e24751ecd0978d3eb79fdaa59692f005b1b286ecdd6146ebc9c1")
    version("1.0.1", sha256="927b399a6906be067e49c11ef1a87472f1b1964075c9eea30fb82c64b20aedee")

    depends_on("python@3.7:", type=("build", "run"))

    depends_on("py-sphinx-theme-builder@0.2.0a7:", type="build")

    depends_on("py-sphinx@4:6", type=("build", "run"), when="@:1.0")
    depends_on("py-pydata-sphinx-theme@0.13.3:", type=("build", "run"), when="@:1.0")

    depends_on("py-sphinx@5:", type=("build", "run"), when="@1.1.0:")
    depends_on("py-pydata-sphinx-theme@0.14:", type=("build", "run"), when="@1.1.0:")
    depends_on("py-pydata-sphinx-theme@0.15.2:", type=("build", "run"), when="@1.1.3:")
    depends_on("py-pydata-sphinx-theme@0.15.4", type=("build", "run"), when="@1.1.4:")

    # https://github.com/executablebooks/sphinx-book-theme/issues/865
    conflicts(
        "py-pydata-sphinx-theme@0.16:",
        msg="Known bug that prevents sidebar from collapsing properly",
    )
