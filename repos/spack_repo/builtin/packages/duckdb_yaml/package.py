# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import (
    DuckdbCommunityExtensionPackage,
    published_binaries,
)

from spack.package import *


class DuckdbYaml(DuckdbCommunityExtensionPackage):
    """Adds support for reading YAML files, and a YAML type."""

    homepage = "https://github.com/teaguesterling/duckdb_yaml"

    license("MIT")

    with when("link_dependencies=static"):
        depends_on("yaml-cpp~shared+pic", type="build")
    with when("link_dependencies=shared"):
        depends_on("yaml-cpp+shared", type="link")

    published_binaries(
        "yaml",
        "2.0.0",
        {
            "linux_amd64": "677d787157ab784243b013dc25dd3978e713dfcc26ceb75db18e8221e863516c",
            "linux_arm64": "b08afa1cc84940c4f156f0748f1004413b76e806a2f7865dcdff5279f4833ffb",
            "osx_amd64": "eeedc71f59b209c4368272ab0c9127d02c1fdab13325cbbb9c0a9b80bc649558",
            "osx_arm64": "5a84b1e95a2092f67ec3739b6033661b721356f7159f5462ef74b566d529ac3a",
        },
        repository="community",
    )

    resource(
        name="extension_source",
        git="https://github.com/teaguesterling/duckdb_yaml.git",
        commit="0c4bb9048be18b08db271b87e82b868f0a25f196",
        placement="extension_source",
        when="@2.0.0 ~prebuilt",
    )
