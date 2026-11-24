# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Sparse(MakefilePackage):
    """An open source sparse linear equation solver."""

    homepage = "https://sparse.sourceforge.net/"
    url = "https://downloads.sourceforge.net/project/sparse/sparse/sparse1.4b/sparse1.4b.tar.gz"

    maintainers("wortiz")

    license("MIT")

    version("1.4b", sha256="63e6646244fd8f4d89f7f70fbf4cfd46b7688d21b22840a0ce57d294a7496d28")

    variant("pic", default=True, description="Build with position independent code")

    # Remove implicit usage of time() for newer compilers
    patch(
        "spTest_time_patch.patch",
        sha256="e10ee8e790bfbc198ba065bf3f9b4b4526b61997dfc238c922c8e5c429043657",
    )

    depends_on("c", type="build")  # generated

    def edit(self, spec, prefix):
        with working_dir("./src"):
            makefile = FileFilter("Makefile")
            makefile.filter(
                "CFLAGS = .*",
                f"CFLAGS = -O2 {self.compiler.c99_flag} "
                + (self.compiler.cc_pic_flag if spec.satisfies("+pic") else ""),
            )
            makefile.filter("CC = .*", "CC = {0}".format(spack_cc))
            makefile.filter("LIBRARY = .*", "LIBRARY = ../lib/libsparse.a")

    def build(self, spec, prefix):
        with working_dir("./src"):
            make()

    def install(self, spec, prefix):
        mkdir(prefix.include)
        install_tree("lib", prefix.lib)
        install_tree("bin", prefix.bin)
        install("src/*.h", prefix.include)
