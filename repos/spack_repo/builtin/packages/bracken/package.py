# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Bracken(Package):
    """Bracken (Bayesian Reestimation of Abundance with KrakEN) is a highly
    accurate statistical method that computes the abundance of species in DNA
    sequences from a metagenomics sample."""

    homepage = "https://ccb.jhu.edu/software/bracken"
    url = "https://github.com/jenniferlu717/Bracken/archive/v2.7.tar.gz"

    license("GPL-3.0-only")

    version("2.9", sha256="b8fd43fc396a2184d9351fb4a459f95ae9bb5865b195a18e22436f643044c788")
    version("2.8", sha256="b0c8a803cc020b7d1cbca47b53e71e874d9688b836911e4a4b71b0e4b826b61a")
    version("2.7", sha256="1795ecd9f9e5582f37549795ba68854780936110a2f6f285c3e626d448cd1532")

    depends_on("cxx", type="build")

    depends_on("python", type="run")
    depends_on("kraken2", type="run")

    parallel = False
    
    def install(self, spec, prefix):
        # Create install directories
        mkdirp(prefix.bin)
        mkdirp(join_path(prefix.bin, "src"))

        # Ensure installer is executable
        chmod = which("chmod", required=True)
        chmod("+x", "install_bracken.sh")

        # Run installer to build kmer2read_distr
        installer = Executable("./install_bracken.sh")
        installer(self.stage.source_path)

        # Install primary executables
        install("bracken", prefix.bin)
        install("bracken-build", prefix.bin)

        # Install compiled helper binary
        install("./src/kmer2read_distr", prefix.bin)

        # Install analysis helper script
        install("./analysis_scripts/combine_bracken_outputs.py", prefix.bin)

        chmod("+x", join_path(prefix.bin, "combine_bracken_outputs.py"))

        # Install Python helper scripts into bin/src
        helper_scripts = ("est_abundance.py", "generate_kmer_distribution.py")

        for script in helper_scripts:
            src_path = join_path("src", script)

            if os.path.isfile(src_path):
                install(src_path, join_path(prefix.bin, "src"))

                symlink(join_path(prefix.bin, "src", script), join_path(prefix.bin, script))
