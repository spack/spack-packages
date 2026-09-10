# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Preseq(MakefilePackage, AutotoolsPackage):
    """The preseq package is aimed at predicting and estimating the complexity
    of a genomic sequencing library, equivalent to predicting and
    estimating the number of redundant reads from a given sequencing depth
    and how many will be expected from additional sequencing using an
    initial sequencing experiment."""

    homepage = "https://github.com/smithlabcode/preseq"

    license("GPL-3.0-only")

    version("3.2.0", sha256="95b81c9054e0d651de398585c7e96b807ad98f0bdc541b3e46665febbe2134d9")
    version("2.0.3", sha256="747ddd4227515a96a45fcff0709f26130386bff3458c829c7bc1f3306b4f3d91")
    version("2.0.2", sha256="1d7ea249bf4e5826e09697256643e6a2473bc302cd455f31d4eb34c23c10b97c")

    build_system(
        conditional("makefile", when="@:2"),
        conditional("autotools", when="@3:"),
        default="autotools",
    )

    variant(
        "hts",
        default=False,
        description="Use HTSlib to support BAM to mapped read conversions",
        when="@3:",
    )

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    # As of 3.0, preseq does not link libefence
    depends_on("libefence", when="@:2")

    # As of 3.0.2, preseq does not use gsl
    depends_on("gsl", when="@:3.0.1")

    depends_on("htslib", when="+hts")

    conflicts("gcc@13:", when="+hts")

    def url_for_version(self, version):
        """
        preseq 2 tarball has an _ and is bzipped while preseq 3 tarball has a - and is
        gzipped
        """
        uri = f"https://github.com/smithlabcode/preseq/releases/download/v{version}"
        if version < Version("3.0"):
            return f"{uri}/preseq_v{version}.tar.bz2"
        else:
            return f"{uri}/preseq-{version}.tar.gz"

    @when("@:2")
    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.set("PREFIX", self.prefix)

    @when("+hts")
    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.set("CPPFLAGS", f"-I{self.spec['htslib'].prefix.include}")
        env.set("LDFLAGS", f"-L{self.spec['htslib'].prefix.lib}")

    @when("@:2")
    def configure(self, spec, prefix):
        return

    @when("+hts")
    def configure_args(self):
        return ["--enable-hts"]
