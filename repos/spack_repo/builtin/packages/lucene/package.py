# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Lucene(Package):
    """
    Apache Lucene is a high-performance, full featured text search engine
    library written in Java.
    """

    homepage = "https://lucene.apache.org/"
    url = "https://archive.apache.org/dist/lucene/java/8.3.1/lucene-8.3.1.tgz"
    list_url = "https://archive.apache.org/dist/lucene/java/"
    list_depth = 1

    license("Apache-2.0", checked_by="wdconinc")

    version("10.0.0", sha256="b40c29039c363a9479947acfbc41efb381af7868233446412d625a197436a243")
    version(
        "9.12.0",
        sha256="8d7c698e7bdee7580950c4323f091b996afb1b14c91d6d6e4e150ccff883c6c5",
        preferred=True,
    )

    # build.gradle minJavaVersion or versions.toml minJava
    depends_on("java@11:", type="run", when="@9:")
    depends_on("java@21:", type="run", when="@10:")

    def install(self, spec, prefix):
        install_tree(".", prefix)
