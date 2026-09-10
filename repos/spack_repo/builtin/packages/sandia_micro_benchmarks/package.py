# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class SandiaMicroBenchmarks(MakefilePackage):
    """Sandia Micro Benchmarks test HPC networking, including messaging rate performance, across
    several different HPC networking protocols, including MPI, RMA, and SHMEM. There is also a test
    for MPI implementation overhead."""

    maintainers("nhanford", "mdosanjh")

    license("GPL-2.0-or-later", checked_by="nhanford")

    homepage = "https://github.com/sandialabs/SMB"
    git = "https://github.com/sandialabs/SMB.git"
    version("master", branch="master")

    variant(name="shmem", default=False, description="Build the SHMEM benchmark.")

    depends_on("mpi")
    depends_on("sos", when="+shmem")

    @property
    def build_targets(self):
        targets = ["mpi_overhead", "msgrate", "rma_mt_mpi"]
        if self.spec.satisfies("+shmem"):
            targets.append("shmem_mt")
        return targets

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        for target in self.build_targets:
            make(target)
            install(target, prefix.bin)
