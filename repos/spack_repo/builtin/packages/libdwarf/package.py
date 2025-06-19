# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import sys

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *

class Libdwarf(CMakePackage):
    """The DWARF Debugging Information Format is of interest to
    programmers working on compilers and debuggers (and any one
    interested in reading or writing DWARF information). It was
    developed by a committee (known as the PLSIG at the time)
    starting around 1991. Starting around 1991 SGI developed the
    libdwarf and dwarfdump tools for internal use and as part of
    SGI IRIX developer tools. Since that time dwarfdump and
    libdwarf have been shipped (as an executable and archive
    respectively, not source) with every release of the SGI
    MIPS/IRIX C compiler."""

    homepage = "https://www.prevanders.net/dwarf.html"
    url = "https://www.prevanders.net/libdwarf-0.10.1.tar.xz"
    list_url = homepage

    license("LGPL-2.1-only")

    version("2.0.0", sha256="c3d1db72a979e14ee60b93010f0698d30fc1bca4eb1341006783d4e9c9ec7e72")
    version("0.12.0", sha256="444dc1c5176f04d3ebc50341552a8b2ea6c334f8f1868a023a740ace0e6eae9f")
    version("0.11.0", sha256="846071fb220ac1952f9f15ebbac6c7831ef50d0369b772c07a8a8139a42e07d2")
    version("0.10.1", sha256="b511a2dc78b98786064889deaa2c1bc48a0c70115c187900dd838474ded1cc19")

    variant("shared", default=True, description="Build shared libs")
    variant("examples", default=False, description="Build examples")
    variant("pic", default=True, description="Build with position independent code")
    variant("dwarfdump", default=True, description="Build dwarfdump")
    variant("dwarfgen", default=False, description="Build dwarfgen")
    variant(
        "decompression",
        default=True,
        description="Enables support for compressed debug sections",
    )

    conflicts("+shared ~pic")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("cmake@3.5:", type="build", when="@0.10:")
    depends_on("cmake@3.10:", type="build", when="@0.12:")

    with when("+decompression"):
        depends_on("zlib-api")
        depends_on("zstd")

    def url_for_version(self, version):
        if version < Version("20130126"):
            return super().url_for_version(version)
        return f"https://www.prevanders.net/libdwarf-{version}.tar.gz"

    def cmake_args(self):
        args = [
            self.define_from_variant("BUILD_SHARED", "shared"),
            self.define_from_variant("BUILD_DWARFEXAMPLE", "examples"),
            self.define_from_variant("PIC_ALWAYS", "pic"),
            self.define_from_variant("BUILD_DWARFDUMP", "dwarfdump"),
            self.define_from_variant("BUILD_DWARFGEN", "dwarfgen"),
            self.define_from_variant("ENABLE_DECOMPRESSION", "decompression"),
            self.define("BUILD_NON_SHARED", self.spec.satisfies("~shared")),
            self.define("DO_TESTING", self.run_tests),
        ]

        return args
