# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Metabat(CMakePackage):
    """MetaBAT, an efficient tool for accurately reconstructing single
    genomes from complex microbial communities."""

    homepage = "https://bitbucket.org/berkeleylab/metabat"
    url = "https://bitbucket.org/berkeleylab/metabat/get/v2.12.1.tar.gz"

    license("BSD-3-Clause-LBNL")

    version("2.15", sha256="550487b66ec9b3bc53edf513d00c9deda594a584f53802165f037bde29b4d34e")
    version("2.14", sha256="d43d5e91afa8f2d211a913739127884669516bfbed870760597fcee2b513abe2")
    version("2.13", sha256="aa75a2b62ec9588add4c288993821bab5312a83b1259ff0d508c215133492d74")

    depends_on("c", type="build")
    depends_on("cxx", type="build")  # generated

    depends_on("autoconf", type="build")
    depends_on("cmake", type="build")

    depends_on(
        "boost@1.55:1.82+program_options+filesystem+system+graph+serialization+iostreams\
                cxxstd=11",
        type=("build", "run"),
    )
    depends_on("perl", type="run")
    depends_on("zlib-api", type="link")
    depends_on("ncurses", type="link")

    def patch(self):
        filter_file(r"(autoconf)", r"autoreconf -i && \1", join_path("cmake", "htslib.cmake"))
        filter_file(
            "./configure",
            (
                f"./configure --host={self.spec.build_spec.target.family.name}-linux-gnu"
                f" --without-libdeflate "
            ),
            join_path("cmake", "htslib.cmake"),
        )

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.set("BOOST_ROOT", self.spec["boost"].prefix)

    def install_args(self, spec, prefix):
        return ["PREFIX={0}".format(prefix)]

    @run_after("build")
    def fix_perl_scripts(self):
        filter_file(r"#!/usr/bin/perl", "#!/usr/bin/env perl", "aggregateBinDepths.pl")

        filter_file(r"#!/usr/bin/perl", "#!/usr/bin/env perl", "aggregateContigOverlapsByBin.pl")
