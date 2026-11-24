# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPymupdf(PythonPackage):
    """
    A high performance Python library for data extraction, analysis, conversion & manipulation of
    PDF (and other) documents.
    """

    homepage = "https://pymupdf.readthedocs.io"
    git = "https://github.com/pymupdf/PyMuPDF.git"
    pypi = "pymupdf/pymupdf-1.27.2.2.tar.gz"

    maintainers("LydDeb")

    license("AGPL-3.0-only", checked_by="LydDeb")

    version("1.27.2.2", sha256="ea8fdc3ab6671ca98f629d5ec3032d662c8cf1796b146996b7ad306ac7ed3335")

    # These dependencies were added gradually during build testing.
    with default_args(type="build"):
        depends_on("c")
        depends_on("cxx")
        depends_on("py-libclang")
        depends_on("swig")
    # These dependencies were identified by scanning the source code using the 'pipreqs' command.
    with default_args(type=("build", "run")):
        depends_on("py-fonttools")
        depends_on("py-pandas")
        depends_on("py-pillow")
        depends_on("py-pymupdf-fonts")

    # This URL is Hard coded in setup.py
    resource(
        when="@1.27.2.2",
        name="mupdf",
        url="https://mupdf.com/downloads/archive/mupdf-1.27.2-source.tar.gz",
        sha256="553867b135303dc4c25ab67c5f234d8e900a0e36e66e8484d99adc05fe1e8737",
        destination="mupdf",
        placement="archive",
        expand=True,
    )

    # Set the build environment is not enough
    patch("setup_get_mupdf_internal.patch")

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.set("PYMUPDF_SETUP_MUPDF_TGZ", join_path(self.stage.source_path, "mupdf/archive"))
