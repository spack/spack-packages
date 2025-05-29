# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Maxbin(MakefilePackage):
    """MaxBin is software for binning assembled metagenomic sequences based on an Expectation-Maximization algorithm."""

    homepage = "https://flowcraft.readthedocs.io/en/latest/user/components/maxbin2.html"
    url = "https://sourceforge.net/projects/maxbin2/files/MaxBin-2.2.7.tar.gz/download"

    license("BSD")

    version("2.2.7", sha256="cb6429e857280c2b75823c8cd55058ed169c93bc707a46bde0c4383f2bffe09e")

    depends_on("perl@5:", type=("build", "run"))
    depends_on("perl-libwww-perl", type=("build", "run"))
    depends_on("bowtie2", type=("build", "run"))
    depends_on("fraggenescan", type=("build", "run"))
    depends_on("hmmer@3", type=("build", "run"))
    depends_on("idba", type=("build", "run"))

    build_directory = "src"

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install_tree(".", prefix.bin)
        perl = which("perl")
        sed = which("sed")
        sed("-i", f's;#!/usr/bin/perl;#!{perl};', f"{prefix}/bin/run_MaxBin.pl")
        sed("-i", f's;my $tmpname =  "tmp_" . time();my $tmpname =  "/tmp/maxbin_tmp_" . time();', f"{prefix}/bin/run_MaxBin.pl")
