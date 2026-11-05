# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbInet(DuckdbExtensionPackage):
    """Adds support for IP-related data types and functions."""

    homepage = "https://github.com/duckdb/duckdb-inet"

    license("MIT")

    checksums = {
        "2.0.0": {
            "linux_amd64": "b1e8776d27d351eceec714c958304eb9011b27a181a4f182e9370a12b939d2c6",
            "linux_arm64": "33bc81e01599926266940ff51593093b875c9f7a910fcfce3b4ae804e93838c7",
            "osx_amd64": "59f38bb9c67b3dcb677e7d156a60f709a3619999dda36a29852733456c7bf9a0",
            "osx_arm64": "9bbb02e869f93042f784234806332bdeed99f80f176e45ddb67c3f9a8ca6a315",
        }
    }
