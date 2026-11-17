# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.aocl_blas.package import AoclBlas

from spack.package import *


class Amdblis(AoclBlas):
    """AMD Optimized BLIS.

    This package has been renamed to ``aocl-blas`` to match the upstream AOCL
    naming. It is kept as a thin, fully deprecated alias so existing specs that
    reference ``amdblis`` continue to resolve. Build logic is inherited
    from :class:`AoclBlas`; use ``aocl-blas`` for new work.
    """

    _name = "amdblis"

    # Redeclare every AoclBlas version as deprecated. A hand-copied list would
    # miss a version added only to the canonical package, and Spack would then
    # expose it here without deprecated=True.
    for v, vargs in AoclBlas.versions.items():
        version(str(v), **dict(vargs, deprecated=True))
