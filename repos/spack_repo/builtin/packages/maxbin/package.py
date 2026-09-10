# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Maxbin(MakefilePackage):
    """MaxBin is software for binning assembled metagenomic sequences based on an
    Expectation-Maximization algorithm."""

    homepage = "https://flowcraft.readthedocs.io/en/latest/user/components/maxbin2.html"
    url = "https://sourceforge.net/projects/maxbin2/files/MaxBin-2.2.7.tar.gz/download"

    license("BSD")

    version("2.2.7", sha256="cb6429e857280c2b75823c8cd55058ed169c93bc707a46bde0c4383f2bffe09e")

    extends("perl")
    depends_on("perl@5:", type=("build", "run"))
    depends_on("perl-libwww-perl", type=("build", "run", "link"))
    depends_on("bowtie2", type=("build", "run"))
    depends_on("fraggenescan", type=("build", "run"))
    depends_on("hmmer@3", type=("build", "run"))
    depends_on("idba", type=("build", "run"))

    depends_on("cxx", type="build")

    build_directory = "src"

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install_tree(".", prefix.bin)
        perl = join_path(spec["perl"].prefix.bin, "perl")
        perl_libwww_perl = join_path(spec["perl-libwww-perl"].prefix.lib, "perl5")
        perl_http_message = join_path(spec["perl-http-message"].prefix.lib, "perl5")
        filter_file(
            r"#!/usr/bin/perl -w",
            f"#!{perl} -w -I {perl_libwww_perl} -I {perl_http_message}",
            f"{prefix}/bin/run_MaxBin.pl",
            string=True,
        )
        filter_file(
            r'my $tmpname =  "tmp_" . time();',
            'my $tmpname =  "/tmp/maxbin_tmp_" . time();',
            f"{prefix}/bin/run_MaxBin.pl",
            string=True,
        )
