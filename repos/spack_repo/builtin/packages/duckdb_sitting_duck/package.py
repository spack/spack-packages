# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import (
    DuckdbCommunityExtensionPackage,
    published_binaries,
)

from spack.package import *


class DuckdbSittingDuck(DuckdbCommunityExtensionPackage):
    """Adds parsing of source code ASTs with tree-sitter grammars."""

    homepage = "https://github.com/teaguesterling/sitting_duck"

    license("Apache-2.0")

    published_binaries(
        "sitting_duck",
        "2.0.0",
        {
            "linux_amd64": "69f6aa09aa24af322d2d42f4c162a3fc26a236ce15c29fec58fb505a7f1f9c97",
            "linux_arm64": "f0c92308d351411fa7298cba56912b111bfc5e85bd481145d00206af1e7a2ea5",
            "osx_amd64": "32977556386fb9f79bda0adec28448df8a17c3e6266e81a4d738e60fd10dc057",
            "osx_arm64": "81e689174ba82820b032e96824754e5debea411ea9b04ad78a9d93681ffa6e29",
        },
        repository="community",
    )

    resource(
        name="extension_source",
        git="https://github.com/teaguesterling/sitting_duck.git",
        commit="cee95ef6eeb33aa6c25527769d3ebf97898aa994",
        submodules=lambda package: ["third_party/tree-sitter"],
        placement="extension_source",
        when="@2.0.0 ~prebuilt",
    )
