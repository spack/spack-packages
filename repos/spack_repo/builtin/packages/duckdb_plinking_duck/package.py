# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbPlinkingDuck(DuckdbExtensionPackage):
    """Adds support for PLINK 2 genomics file formats."""

    homepage = "https://github.com/teaguesterling/plinking_duck"

    license("MIT")

    repository = "community"

    checksums = {
        "2.0.0": {
            "linux_amd64": "ce705843d05860074df02e746647400e44fa72375a195049f56d7f578934a03b",
            "linux_arm64": "1e9a82624daf2d139e02b3bc8f41fd3ae30811d2eed3aa5c26f52ecabe2df043",
            "osx_amd64": "e6a58d2decd7e074a329d565116e4774e153bdc9fffdc33c4a67d9ac991320f3",
            "osx_arm64": "4279234264362a0d24d286ba03a81d82bb972cdf058d6137b9cfa0b8c11c84ab",
        }
    }
