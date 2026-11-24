# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyReportlab(PythonPackage):
    """The ReportLab Toolkit. An Open Source Python library for generating
    PDFs and graphics."""

    homepage = "https://www.reportlab.com"
    pypi = "reportlab/reportlab-3.4.0.tar.gz"

    license("BSD-3-Clause")

    version("4.4.10", sha256="5cbbb34ac3546039d0086deb2938cdec06b12da3cdb836e813258eb33cd28487")
    version("4.4.9", sha256="7cf487764294ee791a4781f5a157bebce262a666ae4bbb87786760a9676c9378")
    version("4.4.4", sha256="cb2f658b7f4a15be2cc68f7203aa67faef67213edd4f2d4bdd3eb20dab75a80d")
    version("4.0.4", sha256="7f70b3b56aff5f11cb4136c51a0f5a56fe6e4c8fbbac7b903076db99a8ef31c1")
    version("3.6.12", sha256="b13cebf4e397bba14542bcd023338b6ff2c151a3a12aabca89eecbf972cb361a")
    version("3.4.0", sha256="5beaf35e59dfd5ebd814fdefd76908292e818c982bd7332b5d347dfd2f01c343")

    depends_on("python@3.9:3", type=("build", "run"), when="@4.4.4:")
    depends_on("python@3.7:3", type=("build", "run"), when="@3.6.9:4.4.3")
    # version restictions were taken over from release 3.4.0 setup.py
    depends_on("py-setuptools@2.2:", type="build")
    depends_on("py-pip@1.4.1:", type="build")

    depends_on("pil@9:", type=("build", "run"), when="@3.6.10:")
    depends_on("pil@2.4.0:", type=("build", "run"), when="@3.4")
    depends_on("py-charset-normalizer", type=("build", "run"), when="@4.4.2:")

    depends_on("freetype")

    @when("@:3")
    def patch(self):
        filter_file(
            "[FREETYPE_PATHS]",
            "[FREETYPE_PATHS]\n"
            + "lib={}\n".format(self.spec["freetype"].libs.directories[0])
            + "inc={}\n".format(self.spec["freetype"].headers.directories[0]),
            "setup.cfg",
            string=True,
        )
