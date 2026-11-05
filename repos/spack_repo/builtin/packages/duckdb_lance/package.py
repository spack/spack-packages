# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbLance(DuckdbExtensionPackage):
    """Adds support for querying Lance datasets."""

    homepage = "https://github.com/lance-format/lance-duckdb"

    license("Apache-2.0")

    checksums = {
        "2.0.0": {
            "linux_amd64": "8bf758fc1e2465958f2e245bf0ceb4896342c30543ee24c191539df6dae53385",
            "linux_arm64": "0b2ba3542e539ac7f2eaceea2943baf7fa2c9887b9367d7ae076ebaf57ac356c",
            "osx_arm64": "c2d9df566bf927a34acbcf7c0ef30432f6ff5021b5aa709339554319b9376577",
        }
    }
