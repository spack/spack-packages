# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.meson import MesonPackage

from spack.package import *


class BaliPhy(MesonPackage):
    """Bayesian co-estimation of phylogenies and multiple sequence alignments."""

    homepage = "https://www.bali-phy.org"
    url = "https://github.com/bredelings/BAli-Phy/archive/refs/tags/4.3.tar.gz"

    maintainers("bredelings")

    license("GPL-2.0-or-later")

    version("4.3", sha256="02ea2f882ed55cd5cc1d4b15ceb56861c729f20f6302fbd3e65c8c61b848e3c6")

    variant("doc", default=True, description="Require Pandoc for manual-page generation")
    variant("cairo", default=True, description="Require Cairo for drawing trees")
    variant(
        "r", default=True, description="Require R for convergence diagnostics and summary plots"
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("meson@1.6:", type="build")
    depends_on("cmake", type="build")  # Discover Cereal and CLI11's CMake metadata.
    depends_on("pandoc", type="build", when="+doc")
    depends_on("boost@1.81: +program_options +random +chrono +json")
    depends_on("cli11@2.6.1:", type="build")
    depends_on("eigen@3.4:", type="build")
    depends_on("cereal", type="build")
    depends_on("fmt@12:")
    depends_on("xxhash")
    depends_on("zstd")
    depends_on("utf8proc")
    depends_on("cairo +pdf +png +svg +ft +fc", when="+cairo")
    depends_on("python@3:", type=("build", "run"))
    depends_on("r", type="run", when="+r")

    conflicts("%cxx=gcc@:12", msg="BAli-Phy requires C++23 support (GCC 13 or newer)")
    conflicts("%cxx=llvm@:17", msg="BAli-Phy requires Clang 18 or newer")
    conflicts("%cxx=apple-clang@:15", msg="BAli-Phy requires Apple Clang 16 or newer")

    # Work around 4.3's static Zstd request, which can select a system archive over Spack's
    # shared library. Later versions containing the upstream fix do not need this patch.
    patch(
        "https://github.com/bredelings/BAli-Phy/commit/8d4d6482d602b6e4ec7c6a8383b23f87361727ea.patch?full_index=1",
        sha256="97389870cc327a69a16a43c2260e9f33d9e800815a57f6853583cdda8f01cc59",
        when="@4.3",
    )

    def setup_build_environment(self, env):
        env.set("BOOST_ROOT", self.spec["boost"].prefix)

    def meson_args(self):
        return ["-Dwith-mpi=false", "-Dextra-tools=true"]

    # Exercise installed model files and MCMC; --version alone misses incomplete installations.
    def test_analysis(self):
        """Run a short seeded analysis using the installed examples and model libraries."""
        bali_phy = which("bali-phy", path=self.prefix.bin, required=True)
        fasta = join_path(self.prefix.share.doc, "bali-phy", "examples", "5S-rRNA", "5d.fasta")
        bali_phy(fasta, "--iterations=20", "--seed=12345")
        assert os.path.isfile(join_path("5d-1", "C1.log"))
