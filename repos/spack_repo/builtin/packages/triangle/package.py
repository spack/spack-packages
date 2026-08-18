# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Triangle(Package):
    """Triangle is a two-dimensional mesh generator and Delaunay
    triangulator. Triangle generates exact Delaunay triangulations,
    constrained Delaunay triangulations, conforming Delaunay
    triangulations, Voronoi diagrams, and high-quality triangular
    meshes."""

    homepage = "https://www.cs.cmu.edu/~quake/triangle.html"
    url = "https://www.netlib.org/voronoi/triangle.zip"

    maintainers("justinh2002")

    license("Unlicense")

    version("1.6", sha256="1766327add038495fa3499e9b7cc642179229750f7201b94f8e1b7bee76f8480")

    depends_on("libx11", type=("build", "link"))
    depends_on("xproto", type="build")
    depends_on("gmake", type="build")

    def install(self, spec, prefix):
        x11 = spec["libx11"].prefix
        xproto = spec["xproto"].prefix
        cswitches = "-O -std=gnu17 -I{0} -I{1} -L{2}".format(x11.include, xproto.include, x11.lib)
        if not spec.satisfies("platform=darwin"):
            cswitches = "-DLINUX " + cswitches
        make("CSWITCHES=" + cswitches)
        mkdirp(prefix.bin)

        install("triangle", prefix.bin)
        install("showme", prefix.bin)

        make("CSWITCHES=" + cswitches, "trilibrary")
        mkdirp(prefix.include)
        mkdirp(prefix.lib)
        install("triangle.h", prefix.include)
        ar = which("ar", required=True)
        ar("rcs", "libtri.a", "triangle.o")
        install("libtri.a", prefix.lib)
