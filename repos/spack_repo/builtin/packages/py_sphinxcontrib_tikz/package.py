# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySphinxcontribTikz(PythonPackage):
    """
    This package contains the tikz Sphinx extension, which enables the use
    of the PGF/TikZ LaTeX package to draw nice pictures.
    """

    homepage = "https://sphinxcontrib-tikz.readthedocs.io"
    pypi = "sphinxcontrib-tikz/sphinxcontrib-tikz-0.4.20.tar.gz"

    version("0.4.20", sha256="2ee3bd1f9ca2f349c0823a4f3507d91c410e7f96be20f051fef7af1665f341ca")

    all_suites = ["pdf2svg", "netpbm", "imagemagick", "ghostscript"]

    default_suite = "pdf2svg"

    variant(
        "suite",
        default=default_suite,
        description="Conversion suite used to convert pdfs to various image formats",
        values=all_suites,
        multi=True,
    )

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-sphinx", type=("build", "run"))

    for suite in ["netpbm", "imagemagick"]:
        depends_on("poppler", when="suite=" + suite, type="run")

    depends_on("texlive", type="run")
    depends_on("pdf2svg", when="suite=pdf2svg", type="run")
    depends_on("netpbm", when="suite=netpbm", type="run")
    depends_on("imagemagick", when="suite=imagemagick", type="run")
    depends_on("ghostscript", when="suite=ghostscript", type="run")
