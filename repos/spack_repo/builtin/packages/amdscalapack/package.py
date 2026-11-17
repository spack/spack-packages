# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.aocl_scalapack.package import AoclScalapack

from spack.package import *


class Amdscalapack(AoclScalapack):
    """ScaLAPACK (AMD Optimized version).

    This package has been renamed to ``aocl-scalapack`` to match the upstream
    AOCL naming. It is kept as a thin, fully deprecated alias so existing specs
    that reference ``amdscalapack`` continue to resolve. Build logic is
    inherited from :class:`AoclScalapack`; use ``aocl-scalapack`` for new work.
    """

    _name = "amdscalapack"

    # Redeclare every AoclScalapack version as deprecated. A hand-copied list would
    # miss a version added only to the canonical package, and Spack would then
    # expose it here without deprecated=True.
    for v, vargs in AoclScalapack.versions.items():
        version(str(v), **dict(vargs, deprecated=True))
