# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbSittingDuck(DuckdbExtensionPackage):
    """Adds parsing of source code ASTs with tree-sitter grammars."""

    homepage = "https://github.com/teaguesterling/sitting_duck"

    license("Apache-2.0")

    repository = "community"

    checksums = {
        "2.0.0": {
            "linux_amd64": "dce8ff819775f9e47be7ab08052e5c18d43c33e09515a4d31ad99d888bf401a9",
            "linux_arm64": "68dee8b3f6dd9331507c0a16e30654e8972a06515ab34fbf1653a6017d658d9f",
            "osx_amd64": "e61ce8f183df643f13c55d26524715ad9f371d25d478667844eedc3c81379361",
            "osx_arm64": "55c4a46549cf9969807b55fe9b9472d2986bb744c293a2b1ccc5be302bae6cfc",
        }
    }
