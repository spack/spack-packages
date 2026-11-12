# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RCollections(RPackage):
    """Provides high performance container data types such as queues, stacks, deques, dicts
    and ordered dicts."""

    cran = "collections"

    license("MIT")

    version("0.3.12", sha256="60e63ee65bc1889e54a008410f53cb5b643f2fffdb926c3ed12316094709c60d")

    depends_on("c", type="build")
