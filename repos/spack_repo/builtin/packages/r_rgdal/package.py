# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RRgdal(RPackage):
    """Bindings for the 'Geospatial' Data Abstraction Library.

    Provides bindings to the 'Geospatial' Data Abstraction Library ('GDAL') (>=
    1.11.4) and access to projection/transformation operations from the 'PROJ'
    library. Use is made of classes defined in the 'sp' package. Raster and
    vector map data can be imported into R, and raster and vector 'sp' objects
    exported. The 'GDAL' and 'PROJ' libraries are external to the package, and,
    when installing the package from source, must be correctly installed first;
    it is important that 'GDAL' < 3 be matched with 'PROJ' < 6. From 'rgdal'
    1.5-8, installed with to 'GDAL' >=3, 'PROJ' >=6 and 'sp' >= 1.4, coordinate
    reference systems use 'WKT2_2019' strings, not 'PROJ' strings. 'Windows'
    and 'macOS' binaries (including 'GDAL', 'PROJ' and their dependencies) are
    provided on 'CRAN'."""

    cran = "rgdal"

    version("1.6-7", sha256="555cedfdadb05db90b061d4b056f96d8b7010c00ea54bc6c1bbcc7684fadae33")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("r@3.3.0:", type=("build", "run"))
    depends_on("r@3.5.0:", type=("build", "run"), when="@1.5:")
    depends_on("r-sp@1.1-0:", type=("build", "run"))
    depends_on("gdal@1.11.4:")
    depends_on("proj@4.8.0:5", when="@:1.3-9")
    depends_on("proj@4.8.0:", when="@1.4-2:")

    conflicts("^proj@:5", when="^gdal@3:")
    conflicts("^proj@6:", when="^gdal@:2")
