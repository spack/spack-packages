# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Palp(MakefilePackage):
    """PALP (Package for Analyzing Lattice Polytopes) is a set of programs
    for calculations with lattice polytopes and applications to toric
    geometry, including the computation of normal forms, Hodge numbers of
    Calabi-Yau hypersurfaces and complete intersections, nef partitions,
    and Mori cones."""

    homepage = "https://hep.itp.tuwien.ac.at/~kreuzer/CY/CYpalp.html"
    url = "https://hep.itp.tuwien.ac.at/~kreuzer/CY/palp/palp-2.21.tar.gz"

    maintainers("d-torrance")

    license("GPL-3.0-only", checked_by="d-torrance")

    version("2.21", sha256="7e4a7bf219998a844c0bcce0a176e49d0743cb4b505a0e195329bf2ec196ddd7")

    depends_on("c", type="build")

    build_targets = ["all-dims"]

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        for program in find(".", "*.x", recursive=False):
            install(program, prefix.bin)
