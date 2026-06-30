# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySphinxcontribSvg2pdfconverter(PythonPackage):
    """Sphinx SVG to PDF or PNG converter extension.

    Provides the ``sphinxcontrib.rsvgconverter`` (using rsvg-convert) and
    ``sphinxcontrib.inkscapeconverter`` (using Inkscape) extensions, which
    convert SVG images to PDF or PNG when building non-HTML documentation.
    The corresponding converter binary (rsvg-convert or inkscape) must be
    available on the PATH at run time."""

    homepage = "https://github.com/missinglinkelectronics/sphinxcontrib-svg2pdfconverter"
    pypi = "sphinxcontrib-svg2pdfconverter/sphinxcontrib_svg2pdfconverter-2.1.0.tar.gz"

    license("BSD-2-Clause")

    version("2.1.0", sha256="9756e82d5f3bf11629ffcbafb1f8a1092d3bb4789e33494032cdce9a9c8459d3")
    version("2.0.0", sha256="ab9c8f1080391e231812d20abf2657a69ee35574563b1014414f953964a95fa3")

    depends_on("python@3.6:", when="@2:", type=("build", "run"))
    depends_on("py-setuptools@61:", when="@2:", type="build")
    depends_on("py-setuptools", type="build")
    depends_on("py-sphinx@1.6.3:", type=("build", "run"))
