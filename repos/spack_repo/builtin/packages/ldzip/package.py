# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Ldzip(MakefilePackage):
    """LDZip compresses PLINK2 linkage disequilibrium (LD) matrices into the
    .ldzip format, and supports random access to the compressed data."""

    homepage = "https://github.com/23andMe/LDZip"
    git = "https://github.com/23andMe/LDZip.git"

    maintainers("teaguesterling")

    # cpp/external/CLI11.hpp, which the binary compiles in, is BSD-3-Clause
    license("MIT AND BSD-3-Clause")

    version("main", branch="main")
    # The project has no tags or releases
    version("2026-08-10", commit="f8e363af03b2101b04e56b142595a16a060856b6")

    variant("r", default=True, description="Also install the LDZipMatrix R package")

    depends_on("cxx", type="build")
    depends_on("zstd")

    with when("+r"):
        extends("r")
        depends_on("r-rcpp@1.0.8:", type=("build", "run"))
        depends_on("r-rsqlite", type=("build", "run"))
        depends_on("r-dbi", type=("build", "run"))

    build_directory = "cpp"

    sanity_check_is_file = ["bin/ldzip"]

    @property
    def build_targets(self):
        return ["build", f"CXX={spack_cxx}", f"ZSTD_PREFIX={self.spec['zstd'].prefix}"]

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install(join_path(self.build_directory, "bin", "ldzip"), prefix.bin)

        if spec.satisfies("+r"):
            r = self.module.R
            mkdirp(self.module.r_lib_dir)
            # The project does not commit the files that Rcpp generates
            with working_dir("R"):
                r("--vanilla", "-e", "Rcpp::compileAttributes()")
            r("--vanilla", "CMD", "INSTALL", f"--library={self.module.r_lib_dir}", "R")
