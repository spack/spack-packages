# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RRgeos(RPackage):
    """Interface to Geometry Engine - Open Source ('GEOS').

    Interface to Geometry Engine - Open Source ('GEOS') using the C 'API' for
    topology operations on geometries. The 'GEOS' library is external to the
    package, and, when installing the package from source, must be correctly
    installed first. Windows and Mac Intel OS X binaries are provided on
    'CRAN'. ('rgeos' >= 0.5-1): Up to and including 'GEOS' 3.7.1, topological
    operations succeeded with some invalid geometries for which the same
    operations fail from and including 'GEOS' 3.7.2. The 'checkValidity='
    argument defaults and structure have been changed, from default FALSE to
    integer default '0L' for 'GEOS' < 3.7.2 (no check), '1L' 'GEOS' >= 3.7.2
    (check and warn). A value of '2L' is also provided that may be used,
    assigned globally using 'set_RGEOS_CheckValidity(2L)', or locally using the
    'checkValidity=2L' argument, to attempt zero-width buffer repair if invalid
    geometries are found. The previous default (FALSE, now '0L') is fastest and
    used for 'GEOS' < 3.7.2, but will not warn users of possible problems
    before the failure of topological operations that previously succeeded.
    From 'GEOS' 3.8.0, repair of geometries may also be attempted using
    'gMakeValid()', which may, however, return a collection of geometries of
    different types."""

    cran = "rgeos"

    version("0.6-4", sha256="9d03c4de96fd3fad55ff8d1ff8113dcaaa00f15d9d0588e54c9f91751bcede11")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("r@3.3.0:", type=("build", "run"))
    depends_on("r-sp@1.1-0:", type=("build", "run"))
    depends_on("geos@3.2.0:3.8.0", when="@:0.5-1")
    depends_on("geos@3.2.0:")
