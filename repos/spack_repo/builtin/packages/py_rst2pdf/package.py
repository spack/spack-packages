# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyRst2pdf(PythonPackage):
    """Convert reStructured Text to PDF via ReportLab.

    The usual way of creating PDF from reStructuredText is by going through
    LaTeX. This tool provides an alternative by producing PDF directly using
    the ReportLab library."""

    homepage = "https://rst2pdf.org/"
    pypi = "rst2pdf/rst2pdf-0.99.tar.gz"
    git = "https://github.com/rst2pdf/rst2pdf.git"

    license("MIT")

    version("0.105", sha256="857e8741014ec5015f7a00aafb5dccbb56378ef4c1da55a828d44bcf5ff3acdb")
    version("0.103.1", sha256="3ffe816d4b3275aee21b8ffdd08b2e6be4d7590cd88b189f733cbc6996d63786")
    version("0.100", sha256="664c3c16e6d3dea274e840a436eac4dba6cb50ab6af3162fc9d5716be3cb7b42")
    version("0.99", sha256="8fa23fa93bddd1f52d058ceaeab6582c145546d80f2f8a95974f3703bd6c8152")

    with default_args(type="build"):
        depends_on("py-setuptools@64:", when="@0.103:")
        depends_on("py-setuptools")
        depends_on("py-setuptools-scm@8:", when="@0.103:")
        depends_on("py-setuptools-scm")

    with default_args(type=("build", "run")):
        depends_on("python@3.10:", when="@0.104:")
        depends_on("python@3.9:", when="@0.103:")
        depends_on("python@3.8:", when="@0.100:0.102")

        # ignore upper bound restrictions, because they seem to be too strict
        depends_on("py-docutils@0.21.2:", when="@0.103:")
        depends_on("py-docutils")
        depends_on("py-jinja2@3:", when="@0.103:")
        depends_on("py-jinja2")
        depends_on("py-packaging@26:", when="@0.105:")
        depends_on("py-packaging@24:", when="@0.103:")
        depends_on("py-packaging")
        depends_on("py-pygments@2:", when="@0.103:")
        depends_on("py-pygments")
        depends_on("py-pyyaml@6.0.1:", when="@0.105:")
        depends_on("py-pyyaml@6:", when="@0.103:")
        depends_on("py-pyyaml")
        depends_on("py-reportlab@4:", when="@0.103:")
        depends_on("py-reportlab")

        # Historical dependencies
        depends_on("py-importlib-metadata@8:", when="@0.103")
        depends_on("py-importlib-metadata", when="@:0.103")
        depends_on("py-smartypants@2:", when="@0.103")
        depends_on("py-smartypants", when="@:0.103")
