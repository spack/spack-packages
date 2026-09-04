# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Graph500(MakefilePackage):
    """Graph500 reference implementations."""

    homepage = "https://graph500.org"
    url = "https://github.com/graph500/graph500/archive/graph500-3.0.0.tar.gz"

    maintainers("juntangc")

    license("BSL-1.0")

    version("3.0.0", sha256="887dcff56999987fba4953c1c5696d50e52265fe61b6ffa8bb14cc69ff27e8a0")

    variant(
        "procs_not_power_of_two",
        default=False,
        description="Enable support for non-power-of-two ranks and nodes",
    )

    depends_on("c", type="build")
    depends_on("mpi@2.0:")

    build_directory = "src"

    @property
    def build_targets(self):
        cflags = [
            "-O3",
            "-Drestrict=__restrict__",
            "-DGRAPH_GENERATOR_MPI",
            "-DREUSE_CSR_FOR_VALIDATION",
            "-I../aml",
            "-I../generator",
            "-I.",
        ]
        if self.spec.satisfies("%gcc@10:"):
            cflags.append("-fcommon")
        if self.spec.satisfies("%gcc@14:"):
            cflags.extend(
                [
                    "-fgnu89-inline",
                    "-std=gnu99",
                    "-Wno-error=implicit-function-declaration",
                    "-Wno-error=incompatible-pointer-types",
                    "-Wno-error=int-conversion",
                ]
            )
        if "+procs_not_power_of_two" in self.spec:
            cflags.append("-DPROCS_PER_NODE_NOT_POWER_OF_TWO")
        return [f"CFLAGS={' '.join(cflags)}"]

    def edit(self, spec, prefix):
        makefile = FileFilter(join_path(self.build_directory, "Makefile"))
        makefile.filter(r"^MPICC\s*=.*", f"MPICC={spec['mpi'].mpicc}")

        if "+procs_not_power_of_two" in spec:
            filter_file(
                r"^#\s*define\s+SIZE_MUST_BE_POWER_OF_TWO",
                "/* #define SIZE_MUST_BE_POWER_OF_TWO */",
                join_path(self.build_directory, "common.h"),
            )

    def install(self, spec, prefix):
        with working_dir(self.build_directory):
            mkdirp(prefix.bin)
            install("graph500_reference_bfs", prefix.bin)
            install("graph500_reference_bfs_sssp", prefix.bin)
            install("graph500_custom_bfs", prefix.bin)
            install("graph500_custom_bfs_sssp", prefix.bin)
