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

    version("3.50.0", sha256="6538ee160423e8a0c0f92cf2b2001e1a2afd9567d026a86ff6e2287c1580cb4c")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("cfitsio@3")
