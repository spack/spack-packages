# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.cargo import CargoPackage

from spack.package import *


class Pueue(CargoPackage):
    """Pueue is a command-line task management tool for sequential and parallel execution of
    long-running tasks."""

    homepage = "https://github.com/Nukesor/pueue"
    url = "https://github.com/Nukesor/pueue/archive/refs/tags/v4.0.1.tar.gz"

    maintainers("ebagrenrut")

    license("Apache-2.0 AND MIT")

    version("4.0.2", sha256="059ee9688cb8b1ce46284f5ad58de21911b6af50098d29598085d2b9dbd432ab")
    version("4.0.1", sha256="7bbe552700041b2e9cd360b69c328d6932ad57d0e0a480a8992fab3a2737cdf8")

    depends_on("c", type="build")
    depends_on("rust@1.85:", type="build")

    @property
    def build_directory(self):
        return f"{join_path(super().build_directory, self.name)}"

    @run_after("install")
    def install_completions(self):
        pueue = Executable(self.prefix.bin.pueue)

        bash_comp_path = bash_completion_path(self.prefix)
        mkdirp(bash_comp_path)
        pueue("completions", "bash", f"{bash_comp_path}")

        fish_comp_path = fish_completion_path(self.prefix)
        mkdirp(fish_comp_path)
        pueue("completions", "fish", f"{fish_comp_path}")

        zsh_comp_path = zsh_completion_path(self.prefix)
        mkdirp(zsh_comp_path)
        pueue("completions", "zsh", f"{zsh_comp_path}")
