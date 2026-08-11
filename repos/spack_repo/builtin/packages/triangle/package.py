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

    depends_on("libx11", type="link")
    depends_on("gmake", type="build")

    def install(self, spec, prefix):
        # triangle 1.6's own makefile hardcodes CSWITCHES with -DLINUX
        # unconditionally, regardless of the actual build platform. triangle.c
        # only consults that macro (alongside the mutually-exclusive -DCPU86)
        # to twiddle the legacy x87 FPU's precision-control register on old
        # x86 hardware -- irrelevant on Apple Silicon (no x87 unit) and
        # unnecessary on modern x86_64 (doubles use SSE by default), but the
        # macro also gates an unconditional `#include <fpu_control.h>`, a
        # glibc/Linux-only header that doesn't exist on macOS at all. Building
        # with the stock makefile there fails outright with "fatal error:
        # 'fpu_control.h' file not found". Override CSWITCHES on Darwin to
        # drop -DLINUX (and skip the header/precision tweak entirely, since
        # neither alternative macro applies here); Linux builds are
        # unaffected and keep the upstream makefile's own default.
        cswitches = "-O -I/usr/X11R6/include -L/usr/X11R6/lib"
        if spec.satisfies("platform=darwin"):
            make("CSWITCHES=" + cswitches)
        else:
            make()
        mkdirp(prefix.bin)

        install("triangle", prefix.bin)
        install("showme", prefix.bin)

        # This package previously only installed the CLI executables above,
        # nothing a dependent could compile/link against -- but consumers
        # like proteus link directly against triangle's C API (a single
        # object file, triangle.o, built from triangle.c with -DTRILIBRARY
        # per the upstream makefile's own "trilibrary" target) rather than
        # shelling out to the CLI. Without an installed header+library,
        # proteus's own build fails with "fatal error: 'triangle.h' file not
        # found" (confirmed via a real `spack install py-proteus` build).
        # Build and install both, matching what proteus's config/default.py
        # expects: $TRIANGLE_DIR/include/triangle.h and
        # $TRIANGLE_DIR/lib/libtri.a.
        make("CSWITCHES=" + cswitches, "trilibrary")
        mkdirp(prefix.include)
        mkdirp(prefix.lib)
        install("triangle.h", prefix.include)
        ar = which("ar", required=True)
        ar("rcs", "libtri.a", "triangle.o")
        install("libtri.a", prefix.lib)
