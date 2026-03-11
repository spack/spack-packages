# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Elasticsearch(Package):
    """Elasticsearch is a search engine based on Lucene. It provides a
    distributed, multitenant-capable full-text search engine with an HTTP web
    interface and schema-free JSON documents.
    """

    homepage = "https://www.elastic.co/"
    url = "https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.15.2-linux-x86_64.tar.gz"

    version("8.15.2", sha256="0b6905ede457be9d1d73d0b6be1c3a7c7c6220829846b532f2604ad30ba7308f")

    depends_on("java", type="run")

    def install(self, spec, prefix):
        dirs = ["bin", "config", "lib", "modules", "plugins"]

        for d in dirs:
            install_tree(d, join_path(prefix, d))
