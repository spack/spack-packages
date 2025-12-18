# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.go import GoPackage

from spack.package import *


class Yamlfmt(GoPackage):
    """yamlfmt is an extensible command line tool or library to format yaml files."""

    homepage = "https://github.com/google/yamlfmt"
    url = "https://github.com/google/yamlfmt/archive/refs/tags/v0.20.0.tar.gz"

    maintainers("ebagrenrut")

    license("Apache-2.0")

    version("0.20.0", sha256="de6bc4373ba46c520d936dd4b60395868ec17aba338b9fd849594c1f41b6c057")

    depends_on("go@1.21:", type="build")

    @property
    def build_args(self):
        return [
            "-p",
            str(self.module.make_jobs),
            "-modcacherw",
            "-ldflags",
            f"-s -w -X main.version={self.version}",
            "-o",
            f"{self.name}",
            f"{join_path(self.build_directory, 'cmd', self.name)}",
        ]
