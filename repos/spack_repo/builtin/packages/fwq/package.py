# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os.path

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Fwq(MakefilePackage):
    """FWQ is the Fixed Work Quanta benchmark designed to test system noise on HPC systems."""

    homepage = "https://github.com/LLNL/system-noise"
    git = "https://github.com/LLNL/system-noise.git"

    maintainers("eleon", "nhanford")

    license("MIT", checked_by="nhanford")

    version("main", branch="main")

    variant("mpi", default=False, description="Build MPI-dependent benchmarks.")

    depends_on("mpi", when="+mpi")
    depends_on("gcc")
    depends_on("py-pandas")

    build_directory = "fwq"

    @property
    def build_targets(self):
        targets = ["single", "thread"]
        if self.spec.satisfies("+mpi"):
            targets.append("mpi")
        return targets

    @property
    def install_targets(self):
        targets = ["fwq", "fwq-th"]
        if self.spec.satisfies("+mpi"):
            targets.append("fwq-mpi")
        return targets

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        with working_dir(self.build_directory):
            for target in self.install_targets:
                install(target, prefix.bin)
        install(os.path.join("scripts", "fwq-stats.py"), prefix.bin)
