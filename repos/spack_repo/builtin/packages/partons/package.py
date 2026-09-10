# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Partons(CMakePackage):
    """PARTONS is a software framework dedicated to the phenomenology
    of 3D hadron structure, in particular Generalized Parton Distributions
    (GPDs) and Transverse Momentum Dependent (TMDs) parton distribution
    functions."""

    homepage = "https://3d-partons.github.io/partons/"
    url = "https://github.com/3d-partons/partons/archive/refs/tags/v5.0.0.tar.gz"
    git = "https://github.com/3d-partons/partons.git"

    tags = ["hep"]

    maintainers("wdconinc")

    license("GPL-3.0", checked_by="wdconinc")

    version("5.0.0", sha256="6ac7b68890ce19a8dfd2515264201d7424d2aa809e4b8c2e714528a1f6234865")

    depends_on("cxx", type="build")
    depends_on("cmake@3.5:", type="build")

    depends_on("partons-elementary-utils")
    depends_on("partons-numa")
    depends_on("sfml@:2")
    depends_on("cln")
    depends_on("gsl")
    depends_on("apfelxx")
    depends_on("lhapdf")
    depends_on("libxml2")
