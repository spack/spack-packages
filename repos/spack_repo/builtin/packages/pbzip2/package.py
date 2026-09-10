# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Pbzip2(MakefilePackage):
    """PBZIP2 is a parallel implementation of the bzip2 block-sorting file
    compressor that uses pthreads and achieves near-linear speedup on SMP
    machines. The output of this version is fully compatible with bzip2 v1.0.2
    or newer (ie: anything compressed with pbzip2 can be decompressed with
    bzip2). PBZIP2 should work on any system that has a pthreads compatible C++
    compiler (such as gcc)."""

    homepage = "http://compression.great-site.net/pbzip2/"
    url = "https://launchpad.net/pbzip2/1.1/1.1.13/+download/pbzip2-1.1.13.tar.gz"

    maintainers("Markus92")

    license("bzip2-1.0.6", checked_by="Markus92")

    version("1.1.13", sha256="8fd13eaaa266f7ee91f85c1ea97c86d9c9cc985969db9059cdebcb1e1b7bdbe6")

    depends_on("cxx", type="build")
    depends_on("bzip2 +shared", type=("build", "run"))

    def edit(self, spec, prefix):
        makefile = FileFilter("Makefile")
        makefile.filter("PREFIX = .*", f"PREFIX = {prefix}")

        # This Makefile assigns CXXFLAGS/LDFLAGS with plain `=`, so neither
        # depends_on-provided include paths nor flag_handler()-injected
        # flags reach the compiler - patch the Makefile text directly
        # instead, the same way PREFIX is handled above.
        extra_cxxflags = ""
        # bzip2's include path is never seen otherwise ("bzlib.h file not found").
        bzip2_prefix = spec["bzip2"].prefix
        extra_cxxflags += f" -I{bzip2_prefix.include}"
        # pbzip2 uses C99 PRIuMAX macros without the C++11-required space
        # (e.g. "%"PRIuMAX). Clang-based compilers treat this as an error.
        if (
            self.spec.satisfies("%cxx=clang")
            or self.spec.satisfies("%cxx=apple-clang")
            or self.spec.satisfies("%cxx=oneapi")
            or self.spec.satisfies("%cxx=aocc")  # AMD's compiler is clang-based too
        ):
            extra_cxxflags += " -Wno-reserved-user-defined-literal"

        makefile.filter(r"^CXXFLAGS = -O2$", f"CXXFLAGS = -O2{extra_cxxflags}")
        makefile.filter(r"^LDFLAGS =$", f"LDFLAGS = -L{bzip2_prefix.lib}")
