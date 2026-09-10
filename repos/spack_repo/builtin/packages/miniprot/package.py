# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Miniprot(Package):
    """Miniprot aligns a protein sequence against a genome with affine gap penalty,
    splicing and frameshift. It is primarily intended for annotating protein-coding
    genes in a new species using known genes from other speciesa.

    Miniprot is not optimized for mapping distant homologs because distant homologs
    are less informative to gene annotations. Nonetheless, it is still possible to
    tune seeding parameters to achieve higher sensitivity at the cost of
    performance."""

    homepage = "https://github.com/lh3/miniprot"
    url = "https://github.com/lh3/miniprot/archive/refs/tags/v0.18.tar.gz"

    license("MIT", checked_by="emwjacobson")

    version("0.18", sha256="e1b5c08571fa3a4aa225da8ec9c6e744cd116b4dc50d9e187114cffe336921ee")
    version("0.17", sha256="afdad05d18290756a7056ca7f67a91bd55d56006100653fd3dd956652206a415")
    version("0.16", sha256="1ec0290552a6c80ad71657a44c767c3a2a2bbcfe3c7cc150083de7f9dc4b3ed0")

    depends_on("c", type="build")
    depends_on("gmake", type="build")
    depends_on("zlib-api")

    def install(self, spec, prefix):
        filter_file("^CC=.*", "CC={0}".format(self.compiler.cc), "Makefile")
        make()

        mkdirp(prefix.bin)
        install("miniprot", join_path(prefix.bin, "miniprot"))
        set_executable(join_path(prefix.bin, "miniprot"))
        mkdirp(prefix.man.man1)
        install("miniprot.1", prefix.man.man1)
