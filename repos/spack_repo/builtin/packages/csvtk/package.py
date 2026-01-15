# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.go import GoPackage

from spack.package import *


class Csvtk(GoPackage):
    """csvtk is a cross-platform, efficient and practical CSV/TSV toolkit."""

    homepage = "https://bioinf.shenwei.me/csvtk/"
    url = "https://github.com/shenwei356/csvtk/archive/refs/tags/v0.36.0.tar.gz"

    maintainers("ebagrenrut")

    license("MIT")

    version("0.36.0", sha256="0acea7e49c8af12ed76b11ec562ffc05a2fff28cb3c4e7b032e9271f13599ec8")

    depends_on("go@1.24:", type="build")

    @property
    def build_directory(self):
        return f"{join_path(super().build_directory, self.name)}"

    @run_after("install")
    def install_completions(self):
        csvtk = Executable(self.prefix.bin.csvtk)

        bash_comp_path = bash_completion_path(self.prefix)
        mkdirp(bash_comp_path)
        csvtk("genautocomplete", "--shell=bash", f"--file={join_path(bash_comp_path, self.name)}")

        fish_comp_path = fish_completion_path(self.prefix)
        mkdirp(fish_comp_path)
        csvtk(
            "genautocomplete",
            "--shell=fish",
            f"--file={join_path(fish_comp_path, self.name)}.fish",
        )

        zsh_comp_path = zsh_completion_path(self.prefix)
        mkdirp(zsh_comp_path)
        csvtk(
            "genautocomplete", "--shell=zsh", f"--file={join_path(zsh_comp_path, f'_{self.name}')}"
        )
