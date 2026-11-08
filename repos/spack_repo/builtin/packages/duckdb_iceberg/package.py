# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import (
    DuckdbExtensionPackage,
    published_binaries,
)

from spack.package import *


class DuckdbIceberg(DuckdbExtensionPackage):
    """Adds support for Apache Iceberg."""

    homepage = "https://github.com/duckdb/duckdb-iceberg"

    license("MIT")

    published_binaries(
        "iceberg",
        "2.0.0",
        {
            "linux_amd64": "ddc8e8f4af60e6e3accffa1b38043c328c810db91215d6299f29cc933655bf1a",
            "linux_arm64": "dc5fc010b24a044ec2dc34294d8d251f481560cfbd5819c22f1fb1b6cc0032ae",
            "osx_amd64": "799cb44a897b22ff0ec31129250efb73df48cf3a08658649c54ebd358f06a442",
            "osx_arm64": "11db9cb14ca5391eb59838055a3c5c5a5d83c827f7b15a255ac5f6d3187bc414",
        },
    )

    # The iceberg extension loads avro when it initializes
    for _when in ("@2.0.0", "@latest", "+prebuilt", "~prebuilt ~site_signed", "+site_signed"):
        depends_on(f"duckdb-avro{_when}", type=("build", "run"), when=_when)

    resource(
        name="extension_source",
        git="https://github.com/duckdb/duckdb-iceberg.git",
        commit="4c0c0874c48ec82a3e29910554891d04bcc0e988",
        placement="extension_source",
        when="@2.0.0 ~prebuilt",
    )
