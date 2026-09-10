# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Minio(MakefilePackage):
    """MinIO is a High Performance Object Storage released under Apache
    License v2.0. It is API compatible with Amazon S3 cloud storage
    service. Use MinIO to build high performance infrastructure for
    machine learning, analytics and application data workloads."""

    homepage = "https://min.io/"
    url = "https://github.com/minio/minio/archive/RELEASE.2020-07-13T18-09-56Z.tar.gz"

    license("AGPL-3.0-or-later")

    version(
        "2024-10-13T13-34-11Z",
        sha256="53301a6822f8466da88e3b24252d2551c37e7f96e9d37a36121d0616a69af1dd",
    )

    depends_on("go", type="build")

    def url_for_version(self, version):
        return "https://github.com/minio/minio/archive/RELEASE.{0}.tar.gz".format(version)

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install("minio", prefix.bin)
