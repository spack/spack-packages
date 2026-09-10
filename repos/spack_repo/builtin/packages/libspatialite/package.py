# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Libspatialite(AutotoolsPackage):
    """SpatiaLite is an open source library intended to extend the
    SQLite core to support fully fledged Spatial SQL capabilities."""

    homepage = "https://www.gaia-gis.it"
    url = "https://www.gaia-gis.it/gaia-sins/libspatialite-sources/libspatialite-4.3.0a.tar.gz"

    license("MPL-1.1")

    version("5.1.0", sha256="43be2dd349daffe016dd1400c5d11285828c22fea35ca5109f21f3ed50605080")
    version("5.0.1", sha256="eecbc94311c78012d059ebc0fae86ea5ef6eecb13303e6e82b3753c1b3409e98")
    version("5.0.0", sha256="7b7fd70243f5a0b175696d87c46dde0ace030eacc27f39241c24bac5dfac6dac")

    depends_on("c", type="build")  # generated

    depends_on("pkgconfig", type="build")
    depends_on("freexl")
    depends_on("freexl@2:", when="@5.1:")
    depends_on("geos")
    depends_on("geos@:3.9", when="@:5.0.0")
    depends_on("iconv")
    depends_on("librttopo", when="@5.0.1:")

    # in libxml2 2.15+ http support is completely removed, so this will need
    # to be refined when libspatiallite is updated
    # https://www.gaia-gis.it/fossil/libspatialite/tktview?name=e8f33aa9d8
    # https://www.gaia-gis.it/fossil/libspatialite/tktview?name=ac85f0fca3
    depends_on("libxml2 +http")
    depends_on("minizip")
    depends_on("proj")
    depends_on("sqlite+rtree")
