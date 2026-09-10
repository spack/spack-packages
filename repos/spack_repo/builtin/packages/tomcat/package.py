# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Tomcat(Package):
    """
    The Apache Tomcat software is an open source implementation of the
    Java Servlet, JavaServer Pages, Java Expression Language and Java
    WebSocket technologies.
    """

    homepage = "https://tomcat.apache.org/"
    url = (
        "https://archive.apache.org/dist/tomcat/tomcat-11/v11.0.0/bin/apache-tomcat-11.0.0.tar.gz"
    )

    license("Apache-2.0")

    version("11.0.0", sha256="d0ca319af349838f59009a9c5ed3709f02344201059dbc26dce4313ee969cd20")
    version("10.1.31", sha256="06f6e2e11ef5afb435a4b27e1e264ebcdbafd95389f5ee37e425dc135ed325d4")
    version(
        "9.0.96",
        sha256="bf4ad04955457ad663157876461015437a7479546aec9a38840d736b3d70151f",
        preferred=True,
    )

    # https://tomcat.apache.org/whichversion.html
    depends_on("java@8:", type="run", when="@9:")
    depends_on("java@11:", type="run", when="@10:")
    depends_on("java@17:", type="run", when="@11:")

    def url_for_version(self, version):
        return f"https://archive.apache.org/dist/tomcat/tomcat-{version.up_to(1)}/v{version}/bin/apache-tomcat-{version}.tar.gz"

    def install(self, spec, prefix):
        install_tree(".", prefix)
