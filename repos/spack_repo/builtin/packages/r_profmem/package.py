# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RProfmem(RPackage):
    """Simple Memory Profiling for R."""

    cran = "profmem"

    license("LGPL-2.1-or-later AND LGPL-3.0-or-later")

    version("0.7.0", sha256="16efc5f13f4b78919c9d51c07acf62c051e0e3830ae3cc32c596f8daf569c3cb")
