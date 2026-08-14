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
    # Xlib.h itself #includes X11/X.h (protocol constants), which libx11
    # doesn't re-export -- it comes from xproto, already pulled in
    # transitively as one of libx11's own build deps, but that isn't enough
    # to put its prefix on this package's own include path below; depend on
    # it directly so spec["xproto"] is guaranteed available here too
    # (confirmed needed via a real build: showme failed with "X11/X.h: No
    # such file or directory" once Xlib.h's own location was fixed).
    depends_on("xproto", type="build")
    depends_on("gmake", type="build")

    def install(self, spec, prefix):
        # triangle 1.6's own makefile hardcodes CSWITCHES to
        # "-O -DLINUX -I/usr/X11R6/include -L/usr/X11R6/lib" unconditionally,
        # regardless of the actual build platform, and CSWITCHES must be
        # overridden on every platform (not just Darwin) for two independent
        # reasons:
        #  - showme.c #includes X11/Xlib.h directly, and the hardcoded
        #    -I/usr/X11R6/include is a legacy path that doesn't exist once
        #    X11 comes from Spack's own libx11 dependency rather than a
        #    system install (confirmed via a real build: showme failed with
        #    "X11/Xlib.h: No such file or directory" even with libx11 built
        #    as a dependency above -- the generic build system used here
        #    doesn't auto-inject dependency include/lib paths the way
        #    AutotoolsPackage/CMakePackage do, so they must be wired up
        #    explicitly here).
        #  - -DLINUX gates an unconditional `#include <fpu_control.h>` in
        #    triangle.c (used to twiddle the legacy x87 FPU's
        #    precision-control register on old x86 hardware -- irrelevant on
        #    Apple Silicon, unnecessary on modern x86_64 where doubles use
        #    SSE by default) via a glibc/Linux-only header that doesn't
        #    exist on macOS at all; keep it on Linux, drop it on Darwin.
        #  - triangle.c/showme.c are K&R-style C (old-style function
        #    definitions, no prototypes in scope at call sites) -- harmless
        #    under GCC's old implicit-int/implicit-declaration defaults, but
        #    a sufficiently modern GCC (confirmed reproducing on 15.2.0;
        #    apparently not triggered on whatever GCC version/platform this
        #    fix was originally verified against) defaults to a C standard
        #    that treats a call to an as-yet-undeclared function as
        #    returning int with no parameters, then reports a hard "too many
        #    arguments" error once it reaches that function's own
        #    (parameter-bearing) K&R definition later in the file, rather
        #    than the warning older defaults gave. PETSc's own Triangle.py
        #    package hits the identical failure and works around it exactly
        #    this way -- add -std=gnu17 (old enough to keep implicit
        #    declarations as a warning, not an error) unconditionally.
        x11 = spec["libx11"].prefix
        xproto = spec["xproto"].prefix
        cswitches = "-O -std=gnu17 -I{0} -I{1} -L{2}".format(x11.include, xproto.include, x11.lib)
        if not spec.satisfies("platform=darwin"):
            cswitches = "-DLINUX " + cswitches
        make("CSWITCHES=" + cswitches)
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
