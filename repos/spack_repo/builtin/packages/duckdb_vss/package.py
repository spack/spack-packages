# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import (
    DuckdbExtensionPackage,
    published_binaries,
)

from spack.package import *


class DuckdbVss(DuckdbExtensionPackage):
    """Adds indexing support to accelerate Vector Similarity Search."""

    homepage = "https://github.com/duckdb/duckdb-vss"

    license("MIT")

    published_binaries(
        "vss",
        "2.0.0",
        {
            "linux_amd64": "02d1ae4508e00cf0dae89f713683f4bf0622774eaa4154398945b77134fdfc3a",
            "linux_arm64": "e4bf5cb45febe9ecaf14fd2daea914d8c8f197e37a58338e3c9db0868064a267",
            "osx_amd64": "b4b4785d221bfde3f48ab9aaf7decf7561d05f4266bb4ec713dcaea990290681",
            "osx_arm64": "4d24e0543efb77376e58297aba11054abefd726207eb98dd57ef112bca146456",
        },
    )

    resource(
        name="extension_source",
        git="https://github.com/duckdb/duckdb-vss.git",
        commit="3685131eacaf0d467d430be5c4e5e7d1d483437a",
        placement="extension_source",
        when="@2.0.0 ~prebuilt",
    )
