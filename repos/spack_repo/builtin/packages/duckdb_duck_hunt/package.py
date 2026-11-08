# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import (
    DuckdbCommunityExtensionPackage,
    published_binaries,
)

from spack.package import *


class DuckdbDuckHunt(DuckdbCommunityExtensionPackage):
    """Adds parsing of test results, build outputs and CI logs."""

    homepage = "https://github.com/teaguesterling/duck_hunt"

    license("Apache-2.0")

    published_binaries(
        "duck_hunt",
        "2.0.0",
        {
            "linux_amd64": "f94c59f4c1958ee254ec862082cee140f04da0702f199c307d8a6adef15a1905",
            "linux_arm64": "50169ee6783ed7608df3b1faecfd416b90f43ebb0e1c53716666f8b7a04b2688",
            "osx_amd64": "e211c550696646ccec730c61914d7474f6ed05b85d91a6d7bd5630e2402cdd0f",
            "osx_arm64": "1afd7c2cdd84e3df4567f5497c62b04f2f3b42d6076c8a2517f2ad3b0bab121a",
        },
        repository="community",
    )

    resource(
        name="extension_source",
        git="https://github.com/teaguesterling/duck_hunt.git",
        commit="72149b4fdabdfbf4bb231c81123832c428cc93a3",
        submodules=lambda package: ["test/samples/ghalogs", "test/samples/loghub"],
        placement="extension_source",
        when="@2.0.0 +site_signed",
    )
