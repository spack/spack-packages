# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyXlsxwriter(PythonPackage):
    """XlsxWriter is a Python module for writing files in the Excel 2007+ XLSX
    file format."""

    pypi = "xlsxwriter/xlsxwriter-1.0.2.tar.gz"

    license("BSD-2-Clause")

    version("3.2.9", sha256="254b1c37a368c444eac6e2f867405cc9e461b0ed97a3233b2ac1e574efb4140c")
    version("3.1.7", sha256="353042efb0f8551ce72baa087e98228f3394fcb380e8b96313edf1eec8d50823")
    version("3.0.3", sha256="e89f4a1d2fa2c9ea15cde77de95cd3fd8b0345d0efb3964623f395c8c4988b7f")
    version("1.4.3", sha256="641db6e7b4f4982fd407a3f372f45b878766098250d26963e95e50121168cbe2")
    version("1.2.2", sha256="5a5e2195a4672d17db79839bbdf1006a521adb57eaceea1c335ae4b3d19f088f")
    version("1.0.2", sha256="a26bbbafff88abffce592ffd5dfaa4c9f08dc44ef4afbf45c70d3e270325f856")

    depends_on("py-setuptools", type="build")

    def url_for_version(self, version):
        url = "https://files.pythonhosted.org/packages/source/X/XlsxWriter/XlsxWriter-{}.tar.gz"
        if version >= Version("3.2.2"):
            url = url.lower()
        return url.format(version)
