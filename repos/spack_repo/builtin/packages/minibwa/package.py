# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import gzip

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Minibwa(MakefilePackage):
    """Align short and moderately long DNA reads to a reference using an FM index."""

    homepage = "https://github.com/lh3/minibwa"
    url = "https://github.com/lh3/minibwa/archive/refs/tags/v0.7.tar.gz"
    git = "https://github.com/lh3/minibwa.git"

    license("MIT AND Apache-2.0 AND HPND AND GPL-2.0-or-later", when="+gpl")
    license("MIT AND Apache-2.0", when="~gpl")

    version("0.7", sha256="8a1129bcba045e4af4b6fbf73b3fc6b42208afbab870c774c5f0cd2716d748ae")

    variant("openmp", default=True, description="Enable OpenMP for libsais index construction")
    variant("mimalloc", default=True, description="Enable the bundled mimalloc allocator")
    variant("gpl", default=True, description="Enable GPL-licensed low-memory index construction")

    depends_on("c", type="build")
    depends_on("zlib-api", type="link")

    # Upstream's SIMD kernels have SSE2 and AArch64 NEON implementations.
    requires("target=x86_64:", "target=aarch64:", policy="one_of")
    conflicts("%c=apple-clang", when="+openmp", msg="Apple Clang does not accept -fopenmp")

    @property
    def build_targets(self):
        # ARCH= lets Spack select the ISA. The SSE2 fallback handles baseline x86-64.
        # Use upstream's trimmed libsais and its static mimalloc allocator override.
        return [
            "minibwa",
            "CC={0}".format(spack_cc),
            "ARCH=",
            "omp={0}".format(int(self.spec.satisfies("+openmp"))),
            "mimalloc={0}".format(int(self.spec.satisfies("+mimalloc"))),
            "gpl={0}".format(int(self.spec.satisfies("+gpl"))),
        ]

    def install(self, spec, prefix):
        mkdirp(prefix.bin, prefix.man.man1, prefix.share.doc.minibwa)
        install("minibwa", prefix.bin)
        install("minibwa.1", prefix.man.man1)
        install("LICENSE.txt", prefix.share.doc.minibwa)

    def test_version(self):
        """Check that the installed executable reports the packaged version."""
        minibwa = Executable(self.prefix.bin.minibwa)
        version = minibwa("version", output=str).strip()
        assert version.split("-", 1)[0] == str(self.version), version

    def test_index_and_map(self):
        """Index a synthetic reference and check the SAM record for an exact match."""
        reference = (
            "AAGCCCAATAAACCACTCTGACTGGCCGAATAGGGATATAGGCAACGACATGTGCGGCGACCCTTGCGACAGTGACGCTTTC"
            "GCCGTTGCCTAAACCTATTTGAAGGAGTCTAGCAGCCGCAGTAAGGCACAATACCTCGTCCGTGTTACCAGACCAAACAAG"
            "ACGTCCTCTTCAATGTTTAAATGACCCTCTCGTCATA"
        )
        read = reference[40:140]
        with gzip.open("reference.fa.gz", "wt") as fasta:
            fasta.write(">ref\n{0}\n".format(reference))
        with open("read.fq", "w") as fastq:
            fastq.write("@read\n{0}\n+\n{1}\n".format(read, "I" * len(read)))

        minibwa = Executable(self.prefix.bin.minibwa)
        minibwa("index", "-t2", "reference.fa.gz", "reference")
        sam = minibwa("map", "-t2", "reference", "read.fq", output=str).splitlines()
        assert "@SQ\tSN:ref\tLN:{0}".format(len(reference)) in sam, sam
        records = [line.split("\t") for line in sam if not line.startswith("@")]
        assert len(records) == 1, records
        assert records[0][:4] == ["read", "0", "ref", "41"], records[0]
        assert records[0][5] == "100M" and records[0][9] == read, records[0]
