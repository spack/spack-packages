# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.aocl_lapack.package import (  # noqa: F401
    AoclLapack,
    AutotoolsBuilder,
    CMakeBuilder,
)

from spack.package import *


class Amdlibflame(AoclLapack):
    """libFLAME (AMD Optimized version).

    This package has been renamed to ``aocl-lapack`` to match the upstream
    AOCL naming. It is kept as a thin, fully deprecated alias so existing specs
    that reference ``amdlibflame`` continue to resolve. Build logic is
    inherited from :class:`AoclLapack`; use ``aocl-lapack`` for new work.
    """

    _name = "amdlibflame"

    # Redeclare every AoclLapack version as deprecated. A hand-copied list would
    # miss a version added only to the canonical package, and Spack would then
    # expose it here without deprecated=True.
    for v, vargs in AoclLapack.versions.items():
        version(str(v), **dict(vargs, deprecated=True))
