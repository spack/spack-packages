# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.meson import MesonPackage

from spack.package import *


class Freebayes(MesonPackage):
    """Bayesian haplotype-based genetic polymorphism discovery and
    genotyping."""

    homepage = "https://github.com/ekg/freebayes"
    url = "https://github.com/freebayes/freebayes/releases/download/v1.3.5/freebayes-1.3.5-src.tar.gz"
    git = "https://github.com/ekg/freebayes.git"

    license("MIT")

    version("1.3.6", sha256="6016c1e58fdf34a1f6f77b720dd8e12e13a127f7cbac9c747e47954561b437f5")
    version("1.3.5", sha256="7e2635690e916ed85cec36b3263e6e5357413a4f2bf3035362d9749335e8a696")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("cmake", type="build")
    depends_on("zlib-api")

    depends_on("ninja", type="build")
    depends_on("pkgconfig", type="build")
    depends_on("htslib")
    depends_on("zlib-api")
    depends_on("xz")
    depends_on("parallel")
    depends_on("vcftools")
    depends_on("bc")
    depends_on("samtools")
    depends_on("gmake", type="build")

    parallel = False

    @property
    def vcflib_builddir(self):
        return join_path(self.build_directory, "vcflib")

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        if self.run_tests:
            env.prepend_path("PATH", self.vcflib_builddir)
            env.prepend_path("PATH", self.build_directory)

    def check(self):
        mkdir(self.vcflib_builddir)
        with working_dir(self.vcflib_builddir):
            cmake("../../vcflib")
            make()
        with working_dir(self.build_directory):
            ninja("test")
