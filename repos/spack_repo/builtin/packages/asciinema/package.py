# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.cargo import CargoPackage

from spack.package import *


class Asciinema(CargoPackage):
    """Terminal session recorder, streamer, and player."""

    homepage = "https://asciinema.org"
    url = "https://github.com/asciinema/asciinema/archive/refs/tags/v3.2.1.tar.gz"
    git = "https://github.com/asciinema/asciinema.git"

    license("GPL-3.0-or-later")

    version("3.2.1", sha256="e7e49a09c664a76afc5bc25ca09871eb090bfbe68a2ddbc72750d3cb215d36f1")
    version("3.2.0", sha256="247c7c87481f38d7788c1fb1be12021c778676c0d0ab37e529ec528f87f487ce")
    version("3.1.0", sha256="d07d22d9531fa98d2999dfc2ef27651efc3a4f5e5f46a78c3c306b69c466af8b")
    version("3.0.1", sha256="612ecb265ccb316f07c9825bacd7301fd21f03a72b516edd370b0d3aa1adf2bb")
    version("3.0.0", sha256="f44feaa1bc150e7964635dc4714fd86089a968587fed81dccf860ee7b64617ca")

    depends_on("c", type="build")
    depends_on("rust@1.82.0:", type="build")

    def setup_build_environment(self, env):
        env.set("ASCIINEMA_GEN_DIR", os.path.join(self.stage.source_path, "gen"))

    @run_after("install")
    def install_completions_and_man(self):
        gen_dir = os.path.join(self.stage.source_path, "gen")
        comp_dir = os.path.join(gen_dir, "completion")
        man_dir = os.path.join(gen_dir, "man")

        if os.path.isdir(comp_dir):
            bash_comp = bash_completion_path(self.prefix)
            mkdirp(bash_comp)
            for f in os.listdir(comp_dir):
                if f.endswith(".bash"):
                    install(os.path.join(comp_dir, f), os.path.join(bash_comp, "asciinema"))

            zsh_comp = zsh_completion_path(self.prefix)
            mkdirp(zsh_comp)
            for f in os.listdir(comp_dir):
                if f.startswith("_"):
                    install(os.path.join(comp_dir, f), zsh_comp)

            fish_comp = fish_completion_path(self.prefix)
            mkdirp(fish_comp)
            for f in os.listdir(comp_dir):
                if f.endswith(".fish"):
                    install(os.path.join(comp_dir, f), fish_comp)

        if os.path.isdir(man_dir):
            man1_dir = os.path.join(self.prefix.share.man, "man1")
            mkdirp(man1_dir)
            for manpage in os.listdir(man_dir):
                if manpage.endswith(".1"):
                    install(os.path.join(man_dir, manpage), man1_dir)

    def test_version(self):
        """Check asciinema can run and report its version."""
        asciinema = which(self.prefix.bin.join("asciinema"))
        out = asciinema("--version", output=str.split, error=str.split)
        assert str(self.spec.version) in out
