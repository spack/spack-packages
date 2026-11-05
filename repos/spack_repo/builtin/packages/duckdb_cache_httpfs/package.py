# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbCommunityExtensionPackage

from spack.package import *


class DuckdbCacheHttpfs(DuckdbCommunityExtensionPackage):
    """Adds a read cache for the httpfs filesystem."""

    homepage = "https://github.com/dentiny/duck-read-cache-fs"

    license("MIT")

    checksums = {
        "2.0.0": {
            "linux_amd64": "93e8b6b761a19863e8a2f26b8fd9331baea030ade2fedf0d063f437923571f98",
            "linux_arm64": "d4377d563e7d6e0b5915b2e443792094e656a6ce61af79e2a39d2a1246c52b39",
            "osx_amd64": "b0ba90d45060adbab2991bb1ef4f674ca01f1eea9a459e02b50ecd990cd151f3",
            "osx_arm64": "04220e346112bdf9b7e99da7e256fa32880d063b8dc7f265299b4f3e1087e2bd",
        }
    }
