# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Spooles(MakefilePackage):
    """SPOOLES is a library for solving sparse real and complex linear systems
    of equations, written in C and using object-oriented design. It is a build
    dependency of the CalculiX finite-element solver and its preCICE adapter."""

    homepage = "https://www.netlib.org/linalg/spooles/spooles.2.2.html"
    url = "https://www.netlib.org/linalg/spooles/spooles.2.2.tgz"

    # SPOOLES is distributed under its own permissive, BSD-like terms (see the
    # "Internet Public License" notice shipped in the archive). It has no SPDX
    # identifier, so no license() directive is declared here.

    maintainers("failed33")

    version("2.2", sha256="a84559a0e987a1e423055ef4fdf3035d55b65bbe4bf915efaa1a35bef7f8c5dd")

    depends_on("c", type="build")

    # The 2.2 archive expands into the current directory (no top-level folder);
    # Make.inc and the top-level "makefile" therefore sit at the source root.
    build_directory = "."

    # The global archive build (`make global`) drives sequential sub-makes and
    # is not safe under `make -j`.
    parallel = False

    build_targets = ["global"]

    def edit(self, spec, prefix):
        # Point the bundled Make.inc at the active compiler, force -fPIC (the
        # static archive is linked into CalculiX and the preCICE adapter), and
        # restore ranlib (upstream ships the no-op "RANLIB = echo").
        makeinc = FileFilter("Make.inc")
        makeinc.filter(r"^\s*CC\s*=.*$", "  CC = " + spack_cc)
        # SPOOLES is 1999-era C: modern gcc (>= 14) and clang promote
        # int-conversion / implicit-function / implicit-int to hard errors, so
        # downgrade them to warnings (no-ops on the gcc 11 we validated with).
        makeinc.filter(
            r"^\s*CFLAGS\s*=.*$",
            "  CFLAGS = -O2 -fPIC -D_DEFAULT_SOURCE -Wno-error=int-conversion "
            "-Wno-error=implicit-function-declaration -Wno-error=implicit-int",
        )
        makeinc.filter(r"^\s*RANLIB\s*=.*$", "  RANLIB = ranlib")

        # Build the multithreaded (MT) objects into the global archive: the
        # preCICE adapter compiles CalculiX with -DUSE_MT and needs those
        # symbols. Upstream comments the MT entry out of the `global` target.
        filter_file(r"^#cd MT/src", "\tcd MT/src", "makefile")

        # Tree/src/makeGlobalLib references a stale "drawTree.c"; the real source
        # in the 2.2 tarball is "draw.c".
        filter_file("drawTree.c", "draw.c", join_path("Tree", "src", "makeGlobalLib"))

    def install(self, spec, prefix):
        mkdirp(prefix.lib)
        install("spooles.a", join_path(prefix.lib, "libspooles.a"))

        # Install every header, preserving SPOOLES' in-tree layout, so that a
        # downstream "-I<prefix.include>" resolves both the entry-point includes
        # (e.g. "FrontMtx/FrontMtx.h") and the relative cross-includes between
        # SPOOLES modules.
        for root, _dirs, files in os.walk("."):
            for name in files:
                if name.endswith(".h"):
                    src = join_path(root, name)
                    dst = join_path(prefix.include, os.path.relpath(src, "."))
                    mkdirp(os.path.dirname(dst))
                    install(src, dst)
