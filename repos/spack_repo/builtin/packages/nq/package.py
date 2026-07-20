# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Nq(MakefilePackage):
    """
    Small utilities allowing the creation of very lightweight job queue systems which
    require no setup, maintenance, supervision, or any long-running processes.
    """

    homepage = "https://github.com/leahneukirchen/nq"
    url = "https://github.com/leahneukirchen/nq/archive/v1.0.tar.gz"

    maintainers("ebagrenrut")

    license("CC0-1.0")

    version("1.0", sha256="d5b79a488a88f4e4d04184efa0bc116929baf9b34617af70d8debfb37f7431f4")

    depends_on("c", type="build")

    @property
    def build_targets(self):
        targets = [f"PREFIX={self.prefix}", "all"]
        return targets

    @property
    def install_targets(self):
        targets = [f"PREFIX={self.prefix}", "install"]
        return targets
