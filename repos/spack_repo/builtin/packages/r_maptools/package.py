# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RMaptools(RPackage):
    """Tools for Handling Spatial Objects.

    Set of tools for manipulating and reading geographic data, in particular
    ESRI shapefiles; C code used from shapelib. It includes binary access to
    GSHHG shoreline files. The package also provides interface wrappers for
    exchanging spatial objects with packages such as PBSmapping, spatstat,
    maps, RArcInfo, Stata tmap, WinBUGS, Mondrian, and others."""

    cran = "maptools"

    version("1.1-8", sha256="5e8579e3f559161935f1dde622ece703eefa2a28a677ce553d7f27611e66e0f7")

    depends_on("c", type="build")  # generated

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-sp@1.0-11:", type=("build", "run"))
    depends_on("r-foreign@0.8:", type=("build", "run"))
    depends_on("r-lattice", type=("build", "run"))
