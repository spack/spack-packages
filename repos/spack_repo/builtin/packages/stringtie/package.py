# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Stringtie(MakefilePackage):
    """StringTie is a fast and highly efficient assembler of RNA-Seq alignments
    into potential transcripts."""

    homepage = "https://ccb.jhu.edu/software/stringtie"
    url = "https://github.com/gpertea/stringtie/archive/v1.3.3b.tar.gz"

    license("MIT")

    version("3.0.3", sha256="cb473760912a7a23b09232171902b57a973ca791510c526a7a60f23616008ec8")
    version("3.0.0", sha256="c8d66f7c76965df112de4d5fe24f558a63b4e72b3b2286b9172b13aa8f0aa9f5")
    version("2.2.1", sha256="19592aa37e293f4dcd684a4c6e0a1439ee34876d9f22944fb4edceba8c09631b")
    version("1.3.4d", sha256="0134c0adc264efd31a1df4301b33bfcf3b3fe96bd3990ce3df90819bad9af968")
    version("1.3.4a", sha256="6164a5fa9bf8807ef68ec89f47e3a61fe57fa07fe858f52fb6627f705bf71add")
    version("1.3.3b", sha256="30e8a3a29b474f0abeef1540d9b4624a827d8b29d7347226d86a38afea28bc0f")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("zlib-api")

    def build(self, spec, prefix):
        make("release")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install("stringtie", prefix.bin)
