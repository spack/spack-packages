# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack_repo.builtin.build_systems.sourceforge import SourceforgePackage

from spack.package import *


class HealpixCxx(AutotoolsPackage, SourceforgePackage):
    """Healpix-CXX is a C/C++ library for calculating
    Hierarchical Equal Area isoLatitude Pixelation of a sphere."""

    homepage = "https://healpix.sourceforge.io"
    sourceforge_mirror_path = "healpix/healpix_cxx-3.50.0.tar.gz"

    license("GPL-2.0-or-later")

    version("3.83.0", sha256="9d376402ee416175edd71cfae4623f3187c3762d1110c5aef84468480e3159a8")
    version("3.60.0", sha256="dc3be17ad982f7d882eb00d3b7218bc302db8267a55ae28ce9225eadcbe4202e")
    version("3.50.0", sha256="6538ee160423e8a0c0f92cf2b2001e1a2afd9567d026a86ff6e2287c1580cb4c")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("pkgconfig", type="build")

    depends_on("cfitsio@3", when="@:3.60.0")
    depends_on("cfitsio@4.5", when="@3.83.0:")

    depends_on("libsharp@2024-05-31 +openmp", when="@3.60.0:")

    def setup_build_environment(self, env):

        if self.spec.satisfies("@3.60.0:"):
            env.set("SHARP_CFLAGS", self.spec["libsharp"].headers.include_flags)
            env.set("SHARP_LIBS", self.spec["libsharp"].libs.link_flags)
