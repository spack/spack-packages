# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbUrlpattern(DuckdbExtensionPackage):
    """Adds the WHATWG URLPattern API for matching URLs."""

    homepage = "https://github.com/teaguesterling/duckdb_urlpattern"

    license("MIT")

    repository = "community"

    checksums = {
        "2.0.0": {
            "linux_amd64": "0f0ffd0f37ba2c1714c99c26d1c90eb1a8ad819b0b50374fe4f949c66906d04a",
            "linux_arm64": "64ed2ffd114803aef3e05c53dc570379d27e928918b3af02a0140786f68909e1",
            "osx_amd64": "2da915b091262fa085733d27c5190d8837613fe8c4db1816539d6de234aa4d1d",
            "osx_arm64": "86f71f9504e803f8d47bfce5dbc0fa48e043a689bbb0cb8b4ddd58e4c7ca1a54",
        }
    }
