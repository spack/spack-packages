# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPymupdfFonts(PythonPackage):
    """Collection of font binaries for use in PyMuPDF"""

    homepage = "https://github.com/pymupdf/pymupdf-fonts"
    git = "https://github.com/pymupdf/pymupdf-fonts.git"
    pypi = "pymupdf_fonts/pymupdf_fonts-1.0.5.tar.gz"

    maintainers("LydDeb")

    license("OFL-1.1", checked_by="LydDeb")

    version("1.0.5", sha256="ac12e3ec4affa35e9a0aca29135ef41c23bdbe5758c3355dac236986309e6bc6")

    with default_args(type="build"):
        depends_on("py-setuptools")
