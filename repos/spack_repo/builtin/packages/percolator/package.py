# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Percolator(CMakePackage):
    """Semi-supervised learning for peptide identification from shotgun proteomics datasets"""

    homepage = "http://percolator.ms/"
    url = "https://github.com/percolator/percolator/archive/refs/tags/rel-3-08.tar.gz"

    license("Apache-2.0")

    version("3.8", sha256="24b67632f11b74104c153715e123906ed71dc62178c2f8df71de82f2240bf6c0")
    version("3.7.1", sha256="f1c9833063cb4e99c51a632efc3f80c6b8f48a43fd440ea3eb0968af5c84b97a")
    version("3.6.5", sha256="e386998046f59c34be01b1b0347709751d92f3a98e9a0079f8e7c5af5e2dcc8f")

    def url_for_version(self, version):
        chunks = str(version).split(".")

        if len(chunks) == 3:
            major, minor, patch = chunks
            tag = f"rel-{major}-{int(minor):02}-{int(patch):02}"
        elif len(chunks) == 2:
            major, minor = chunks
            tag = f"rel-{major}-{int(minor):02}"
        else:
            tag = f"rel-{version}"

        return f"https://github.com/percolator/percolator/archive/refs/tags/{tag}.tar.gz"

    variant("xml", default=True, description="Enables XML parsing (pepXML support)")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("cmake@3.5:", type="build", when="@3.8:")
    depends_on("cmake@2.8.11:", type="build", when="@3.6:3.7")
    depends_on("boost@1.70:", type="build", when="@3.8:")
    depends_on("boost@1.46:", type="build", when="@3.6:3.7")
    depends_on("boost+system+filesystem", type="build")

    depends_on("xerces-c transcoder=none netaccessor=none", when="+xml")
    depends_on("xsd", when="+xml")
    depends_on("libtirpc@1.2:", when="+xml")

    depends_on("zlib")
    depends_on("sqlite")

    def cmake_args(self):
        return [self.define_from_variant("XML_SUPPORT", "xml")]
