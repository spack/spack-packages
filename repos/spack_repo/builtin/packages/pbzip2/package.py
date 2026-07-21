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

    def flag_handler(self, name: str, flags: List[str]):
        if name == "cxxflags":
            # pbzip2 uses C99 PRIuMAX macros without the C++11-required space
            # between the string literal and the macro (e.g., "%"PRIuMAX).
            # Clang-based compilers (including Intel oneAPI icpx) treat this
            # as an error. Suppress it since the code is functionally correct.
            if (
                self.spec.satisfies("%cxx=clang")
                or self.spec.satisfies("%cxx=apple-clang")
                or self.spec.satisfies("%cxx=oneapi")
            ):
                flags.append("-Wno-reserved-user-defined-literal")
        return (flags, None, None)
