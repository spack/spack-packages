# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from glob import glob

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class DiaUmpireSe(Package):
    """Computational analysis for mass spectrometry-based proteomics data."""

    homepage = "https://diaumpire.nesvilab.org/"
    url = "https://github.com/Nesvilab/DIA-Umpire/archive/refs/tags/v2.2.8.tar.gz"
    git = "https://github.com/Nesvilab/DIA-Umpire.git"

    maintainers("w8jcik")

    license("GPL-3.0")

    version("2.3.4", commit="68b73feeec6b4ef4812b5b3a7c410270e609b1ad")
    version("2.2.9", commit="255e0fec1d3775fd9616c2e4c40e137ca1766476")
    version("2.2.8", sha256="94113ea5c088189a28afc88ccfd1e0e4435755a3f499beb1dab10df0fb927282")

    depends_on("java@11:15", type=("build", "run"), when="@2.3.4:")
    depends_on("java@9:15", type=("build", "run"), when="@2.2.9:2.3.3")
    depends_on("java@1.7:15", type=("build", "run"), when="@:2.2.8")

    def install(self, spec, prefix):
        if spec.satisfies("@2.2.9:"):
            batmass_jars = []

            with working_dir("lib"):
                for jar in glob("batmass-io-*.jar"):
                    batmass_jars.append(jar)

            build_gradle = FileFilter("DIA_Umpire_SE/build.gradle")

            build_gradle.filter(
                r"implementation project\(':DIA-Umpire'\)",
                f"implementation project(':DIA-Umpire')\n    implementation name: \"{batmass_jars[0].rstrip('.jar')}\"",  # noqa
            )

        with working_dir("DIA_Umpire_SE"):
            gradlew = Executable("./gradlew")
            gradlew("clean", "build", "--no-daemon")

        mkdirp(prefix.lib)

        with working_dir("DIA_Umpire_SE/build/libs"):
            for jar in glob("*"):
                install(jar, prefix.lib)

        if spec.satisfies("^openjdk@11:"):
            silence_java_warnings_params = (
                "--add-opens=java.base/java.lang=ALL-UNNAMED "
                "--add-opens=java.base/java.math=ALL-UNNAMED "
                "--add-opens=java.base/java.net=ALL-UNNAMED "
                "--add-opens=java.base/java.text=ALL-UNNAMED "
                "--add-opens=java.base/java.util=ALL-UNNAMED "
                "--add-opens=java.base/java.util.concurrent=ALL-UNNAMED "
            )

            launcher_script = FileFilter("DIA_Umpire_SE/build/scripts/DIA_Umpire_SE")
            launcher_script.filter(r"\$JAVA_OPTS", f"{silence_java_warnings_params} $JAVA_OPTS")

        mkdirp(prefix.bin)
        install("DIA_Umpire_SE/build/scripts/DIA_Umpire_SE", prefix.bin)
