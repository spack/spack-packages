# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.go import GoPackage

from spack.package import *


class Scorecard(GoPackage):
    """OpenSSF Scorecard - Security health metrics for Open Source"""

    homepage = "https://scorecard.dev/"
    url = "https://github.com/ossf/scorecard/archive/refs/tags/v5.2.1.tar.gz"

    maintainers("alecbcs", "tgamblin")

    license("Apache-2.0", checked_by="alecbcs")

    version("5.3.0", sha256="4fbcb442071d5e463c8d20f8bc8ac52502e874e06a395887469c84335f4b21fb")
    version("5.2.1", sha256="f73d5212de4f67f143258a64664af6906aa7fcad2188b66c3beabd46871e2f62")

    @run_after("install")
    def install_completions(self):
        scorecard = Executable(self.prefix.bin.scorecard)

        # Install bash completions
        mkdirp(bash_completion_path(self.prefix))
        with open(bash_completion_path(self.prefix) / "scorecard", "w") as file:
            scorecard("completion", "bash", output=file)

        # Install fish completions
        mkdirp(fish_completion_path(self.prefix))
        with open(fish_completion_path(self.prefix) / "scorecard.fish", "w") as file:
            scorecard("completion", "fish", output=file)

        # Install zsh completions
        mkdirp(zsh_completion_path(self.prefix))
        with open(zsh_completion_path(self.prefix) / "_scorecard", "w") as file:
            scorecard("completion", "zsh", output=file)
