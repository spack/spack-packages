# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.pipx import PipxPackage

from spack.package import *


class PipxS3cmd(PipxPackage):
    """
    S3cmd (s3cmd) is a free command line tool and client for uploading,
    retrieving and managing data in Amazon S3 and other cloud storage
    service providers that use the S3 protocol, such as Google Cloud
    Storage or DreamHost DreamObjects. It is best suited for power
    users who are familiar with command line programs.
    """

    homepage = "https://github.com/s3tools/s3cmd"
    url = "https://github.com/s3tools/s3cmd/releases/download/v2.3.0/s3cmd-2.3.0.tar.gz"

    maintainers("ebagrenrut")

    license("GPL-2.0")

    version("2.4.0", sha256="6b567521be1c151323f2059c8feec85ded96b6f184ff80535837fea33798b40b")
    version("2.3.0", sha256="15330776e7ff993d8ae0ac213bf896f210719e9b91445f5f7626a8fa7e74e30b")
