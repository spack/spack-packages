# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbWebbed(DuckdbExtensionPackage):
    """Adds support for processing XML and HTML."""

    homepage = "https://github.com/teaguesterling/duckdb_webbed"

    license("MIT")

    repository = "community"

    checksums = {
        "2.0.0": {
            "linux_amd64": "7171dc2f308cd79fe78757891e7249b725614ac16076db375ee7380e74e90eb0",
            "linux_arm64": "e8d434933e47d5eebc3577655b3bcc54aab4a60919fcefca33969273c66fa3bb",
            "osx_amd64": "041f7e6ba0c8cf3b100a4ec8cc40d3b8f43b48fe8b6acef7efdd64545eeb8e8c",
            "osx_arm64": "9eff1f3488ad48245e7a7ff8fb23952a07a48ea2aeb081bf663d6a1695d261e6",
        }
    }
