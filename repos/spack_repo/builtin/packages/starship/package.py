# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.cargo import CargoPackage

from spack.package import *


class Starship(CargoPackage):
    """The minimal, blazing-fast, and infinitely customizable prompt for
    any shell!"""

    homepage = "https://starship.rs/"
    url = "https://github.com/starship/starship/archive/v1.24.1.tar.gz"

    maintainers("ebagrenrut")

    license("ISC")

    version("1.25.0", sha256="e77f3c23683eb544f6dae7171e3c80676aefc66329225bdcd58e40846bb6445f")
    version("1.24.2", sha256="b7ab0ef364f527395b46d2fb7f59f9592766b999844325e35f62c8fa4d528795")
    version("1.24.1", sha256="4f2ac4181c3dea66f84bf8c97a3cb39dd218c27c8e4ade4de149d3834a87c428")

    depends_on("c", type="build")
    depends_on("cmake", type="build")
    depends_on("rust@1.90:", type="build", when="@1.24.2:")
    depends_on("rust@1.89:", type="build")

    @property
    def build_args(self):
        return ["--locked"]

    @run_after("install")
    def install_completions(self):
        starship = Executable(self.prefix.bin.starship)

        bash_comp_path = bash_completion_path(self.prefix)
        mkdirp(bash_comp_path)
        with open(bash_comp_path / self.name, "w") as file:
            starship("completions", "bash", output=file)

        fish_comp_path = fish_completion_path(self.prefix)
        mkdirp(fish_comp_path)
        with open(fish_comp_path / f"{self.name}.fish", "w") as file:
            starship("completions", "fish", output=file)

        zsh_comp_path = zsh_completion_path(self.prefix)
        mkdirp(zsh_comp_path)
        with open(zsh_comp_path / f"_{self.name}", "w") as file:
            starship("completions", "zsh", output=file)
