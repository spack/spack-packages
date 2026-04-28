# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RWk(RPackage):
    """Lightweight Well-Known Geometry Parsing.

    Provides a minimal R and C++ API for parsing well-known binary and
    well-known text representation of geometries to and from R-native formats.
    Well-known binary is compact and fast to parse; well-known text is
    human-readable and is useful for writing tests. These formats are only
    useful in R if the information they contain can be accessed in R, for which
    high-performance functions are provided here."""

    cran = "wk"

    license("MIT")

    version("0.9.4", sha256="b973dd5fa9aed94efc7ea4027146e804ba54df818a71278d6a5b7df0ae9e348b")
    version("0.9.2", sha256="33675edd9baedb09bf69a3a55fec3190e2bf57a5f4f63f94bc06861b5e83e5f8")
    version("0.7.2", sha256="6f8b72f54e2efea62fda8bc897124b43a39b81cffa9569103d06d95f946eab2f")
    version("0.7.0", sha256="e24327d38f2ff2d502c67c60eba3b4e44079a64ed8b805df64f231dc4712a2de")
    version("0.6.0", sha256="af2c2837056a6dcc9f64d5ace29601d6d668c95769f855ca0329648d7326eaf5")
    version("0.4.1", sha256="daa7351af0bd657740972016906c686f335b8fa922ba10250e5000ddc2bb8950")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("r@2.10:", type=("build", "run"), when="@0.7.0:")
    depends_on("r-cpp11", type=("build", "run"), when="@:0.6.0")
