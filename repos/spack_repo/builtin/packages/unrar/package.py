# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Unrar(MakefilePackage):
    """RAR archive extraction utility"""

    homepage = "https://www.rarlab.com"
    url = "https://www.rarlab.com/rar/unrarsrc-5.9.4.tar.gz"

    version("7.0.9", sha256="505c13f9e4c54c01546f2e29b2fcc2d7fabc856a060b81e5cdfe6012a9198326")

    depends_on("cxx", type="build")  # generated

    def edit(self, spec, prefix):
        makefile = FileFilter("makefile")
        makefile.filter("LIBFLAGS=-fPIC", "LIBFLAGS={0}".format(self.compiler.cxx_pic_flag))
        makefile.filter("DESTDIR=/usr", "DESTDIR={0}".format(self.prefix))

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install("unrar", prefix.bin.unrar)
