# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Geode(Package):
    """
    Apache Geode is a data management platform that provides real-time,
    consistent access to data-intensive applications throughout widely
    distributed cloud architectures.
    """

    homepage = "https://geode.apache.org/"
    url = "https://archive.apache.org/dist/geode/1.9.2/apache-geode-1.9.2.tgz"
    list_url = "https://archive.apache.org/dist/geode/"
    list_depth = 1

    license("Apache-2.0")

    version("1.15.1", sha256="2668970982d373ef42cff5076e7073b03e82c8e2fcd7757d5799b2506e265d57")
    version("1.14.3", sha256="5efb1c71db34ba3b7ce1004579f8b9b7a43eae30f42c37837d5abd68c6d778bd")
    version("1.13.8", sha256="b5fc105ce0a16aaf7ba341668e022d458b18d6d2c44705a8c79c42077c6d8229")

    depends_on("java", type="run")

    def install(self, spec, prefix):
        install_tree(".", prefix)
