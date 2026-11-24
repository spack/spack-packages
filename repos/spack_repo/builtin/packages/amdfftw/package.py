# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.aocl_fftw.package import AoclFftw

from spack.package import *


class Amdfftw(AoclFftw):
    """FFTW (AMD Optimized version).

    This package has been renamed to ``aocl-fftw`` to match the upstream AOCL
    naming. It is kept as a thin, fully deprecated alias so existing specs that
    reference ``amdfftw`` continue to resolve. Build logic is inherited
    from :class:`AoclFftw`; use ``aocl-fftw`` for new work.
    """

    _name = "amdfftw"

    # Redeclare every AoclFftw version as deprecated. A hand-copied list would
    # miss a version added only to the canonical package, and Spack would then
    # expose it here without deprecated=True.
    for v, vargs in AoclFftw.versions.items():
        version(str(v), **dict(vargs, deprecated=True))
