# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbMarkdown(DuckdbExtensionPackage):
    """Adds support for reading and writing Markdown files."""

    homepage = "https://github.com/teaguesterling/duckdb_markdown"

    license("MIT")

    repository = "community"

    checksums = {
        "2.0.0": {
            "linux_amd64": "8d40ee075b3a19e95e2c64c7d600d5a50f323b0346549339f6a37f32ec869ab1",
            "linux_arm64": "e185d76b40aba95bd49929b5f0c04bcbc41174a8aa94f694c34e90818ea45a67",
            "osx_amd64": "48f316dd80d78e06a5d19ad885d9a2535eabf6182803c35154672c557d28c54c",
            "osx_arm64": "b926625c2d9f427908ac51c612595e46dcacea492583d0bb2645accd4f1565e4",
        }
    }
