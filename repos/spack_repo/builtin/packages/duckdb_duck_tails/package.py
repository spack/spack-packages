# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbCommunityExtensionPackage

from spack.package import *


class DuckdbDuckTails(DuckdbCommunityExtensionPackage):
    """Adds support for querying git history."""

    homepage = "https://github.com/teaguesterling/duck_tails"

    license("Apache-2.0")

    checksums = {
        "2.0.0": {
            "linux_amd64": "b0a7518c444195b7ba2df1f944e801afa919035bd6f3ffb8253a7b9d845a89f2",
            "linux_arm64": "70c8bad6dd8df69883aa3267a809fb5aa141a1e3933cb4aa5399fb4dfce8c237",
            "osx_arm64": "f8ede0448462318286777f971cfe02b403214ca77ff8f283612665ada06b6c2d",
        }
    }
