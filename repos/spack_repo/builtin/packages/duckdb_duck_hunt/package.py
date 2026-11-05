# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbDuckHunt(DuckdbExtensionPackage):
    """Adds parsing of test results, build outputs and CI logs."""

    homepage = "https://github.com/teaguesterling/duck_hunt"

    license("Apache-2.0")

    repository = "community"

    checksums = {
        "2.0.0": {
            "linux_amd64": "df27ddaddca1c9a725b0f043c9434f32f81b7371a3ece4da6a4df940ca9413bf",
            "linux_arm64": "bfc6ec28ec3490cfdcefb452103aa6b348095019b69510eb268e5864d1c2184a",
            "osx_amd64": "2bdb7855311fd1d8173562273525d9672071b96fe1e284878e7c15bbc8e10260",
            "osx_arm64": "090fcfd4b0755d5ee7a669ad660b9724fe5a2faea88b9e10c081394176db6153",
        }
    }
