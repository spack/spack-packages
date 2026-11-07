# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import (
    DuckdbCommunityExtensionPackage,
    published_binaries,
)

from spack.package import *


class DuckdbDuckTails(DuckdbCommunityExtensionPackage):
    """Adds support for querying git history."""

    homepage = "https://github.com/teaguesterling/duck_tails"

    license("Apache-2.0")

    published_binaries(
        "duck_tails",
        "2.0.0",
        {
            "linux_amd64": "5024c8744bd3f66407f27eeb7968158750c3d39470fe1296b97d578654f2860b",
            "linux_arm64": "203421bb416e1a20a1f88988a5153b80cd20113d64a981e8e81229d585140ffa",
            "osx_arm64": "8323ca4088e1d01f4a5ef2184a31213ba243b95ebf173d5e2c210a6d20edb8f6",
        },
        repository="community",
    )

    resource(
        name="extension_source",
        git="https://github.com/teaguesterling/duck_tails.git",
        commit="2b20b7d21c864817538e347e82f70fed76598f4d",
        placement="extension_source",
        when="@2.0.0 +site_signed",
    )
