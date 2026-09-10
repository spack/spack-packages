# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Solr(Package):
    """Solr is highly reliable, scalable and fault tolerant, providing distributed
    indexing, replication and load-balanced querying, automated failover and
    recovery,centralized configuration and more. Solr powers the search and
    navigation features of many of the world's largest internet sites."""

    homepage = "https://solr.apache.org/"
    url = "https://archive.apache.org/dist/solr/solr/7.7.3/solr-7.7.3.tgz"
    list_url = "https://archive.apache.org/dist/solr/solr"
    list_depth = 1

    license("Apache-2.0", checked_by="wdconinc")

    version("9.7.0", sha256="38548b86fa4e3c87883875952da124bf7d742cb8f7b25d37a1176833588e8552")
    version("8.11.4", sha256="163fbdf246bbd78910bc36c3257ad50cdf31ccc3329a5ef885c23c9ef69e0ebe")

    depends_on("java", type="run")

    def url_for_version(self, version):
        if self.spec.satisfies("@9:"):
            return f"https://archive.apache.org/dist/solr/solr/{version}/solr-{version}.tgz"
        else:
            return f"https://archive.apache.org/dist/lucene/solr/{version}/solr-{version}.tgz"

    def install(self, spec, prefix):
        install_tree(".", prefix)
