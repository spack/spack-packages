# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.aocl_libm.package import AoclLibm

from spack.package import *


class Amdlibm(AoclLibm):
    """AMD LibM (AMD Optimized math library).

    This package has been renamed to ``aocl-libm`` to match the upstream AOCL
    naming. It is kept as a thin, fully deprecated alias so existing specs that
    reference ``amdlibm`` continue to resolve. Build logic is inherited
    from :class:`AoclLibm`; use ``aocl-libm`` for new work.
    """

    _name = "amdlibm"

    # Redeclare every AoclLibm version as deprecated. A hand-copied list would
    # miss a version added only to the canonical package, and Spack would then
    # expose it here without deprecated=True.
    for v, vargs in AoclLibm.versions.items():
        version(str(v), **dict(vargs, deprecated=True))
