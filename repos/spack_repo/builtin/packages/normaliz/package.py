# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Normaliz(AutotoolsPackage):
    """Normaliz is an open-source tool for computations in discrete convex
    geometry, including affine monoids, rational and algebraic cones, and
    polyhedra. It supports tasks such as convex hulls, lattice point
    enumeration, Hilbert bases, Ehrhart series, and Gröbner bases of lattice
    and toric ideals. Normaliz provides both a command-line interface and a C++
    library (libnormaliz) for integrating its algorithms into other
    software."""

    homepage = "https://www.normaliz.uni-osnabrueck.de/"
    url = "https://github.com/Normaliz/Normaliz/releases/download/v3.10.5/normaliz-3.10.5.tar.gz"

    maintainers("d-torrance")

    license("GPL-3.0-or-later", checked_by="d-torrance")

    version("3.11.1", sha256="9a00d590f0fdcad847e2189696d2842d97ed896ed36c22421874a364047f76e8")
    version("3.11.0", sha256="14441981afce3546c1c0f12b490714da3564af7a60d12ac0a494f9d2382d1a01")
    version("3.10.5", sha256="58492cfbfebb2ee5702969a03c3c73a2cebcbca2262823416ca36e7b77356a44")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("diffutils", type="build")

    depends_on("gmp")

    variant(
        "nauty",
        default=False,
        description="Enable nauty support for computing automorphism groups",
    )
    depends_on("nauty", when="+nauty")

    variant("flint", default=False, description="Enable flint support for algebraic polyhedra")
    depends_on("flint", when="+flint")

    # TODO: cocoalib & e-antic variants
