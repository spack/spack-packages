# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
import os

from spack_repo.builtin.build_systems.cmake import CMakePackage, generator

from spack.package import *


class Gplates(CMakePackage):
    """GPlates is desktop software for the interactive visualisation of plate tectonics.

    GPlates offers a novel combination of interactive plate tectonic reconstructions,
    geographic information system (GIS) functionality and raster data visualisation.
    GPlates enables both the visualisation and the manipulation of plate tectonic
    reconstructions and associated data through geological time.
    """

    homepage = "https://www.gplates.org"
    url = "file://{}/gplates_2.3.0_src.zip".format(os.getcwd())
    manual_download = True

    version("2.3.0", sha256="7d4be9d524d1fcbb6a81de29bd1d4b13133082db23f0808965c5efe30e9538ab")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.5:", type="build")
    depends_on("gl")
    depends_on("glu")
    depends_on("glew")
    depends_on("python@2:3")
    depends_on("boost@1.35:1.75+program_options+python+system+thread")
    depends_on("qt@5.6:+opengl")
    depends_on("gdal@1.3.2:")
    depends_on("cgal@4.7:")
    depends_on("proj@4.6:")
    depends_on("qwt@6.0.1:")
    depends_on("zlib-api")

    # When built in parallel, headers are not generated before they are used
    # (specifically, ViewportWindowUi.h) with the Makefiles generator.
    generator("ninja")
