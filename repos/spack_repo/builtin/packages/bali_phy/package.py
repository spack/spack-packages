# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import tempfile
from pathlib import Path

from spack_repo.builtin.build_systems.meson import MesonPackage

from spack.package import (
    Executable,
    conflicts,
    depends_on,
    license,
    maintainers,
    version,
    which,
    working_dir,
)


class BaliPhy(MesonPackage):
    """Bayesian co-estimation of phylogenies and multiple sequence alignments."""

    homepage = "https://www.bali-phy.org"
    url = "https://github.com/bredelings/BAli-Phy/archive/refs/tags/4.3.tar.gz"
    maintainers("bredelings")
    license("GPL-2.0-or-later")

    version("4.3", sha256="02ea2f882ed55cd5cc1d4b15ceb56861c729f20f6302fbd3e65c8c61b848e3c6")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("meson@1.6:", type="build")
    depends_on("cmake", type="build")  # Discover Cereal and CLI11's CMake metadata.
    depends_on("pandoc", type="build")
    depends_on("boost@1.81: +program_options +random +chrono +json")
    depends_on("cli11@2.6.1:", type="build")
    depends_on("eigen@3.4:", type="build")
    depends_on("cereal", type="build")
    depends_on("fmt@12: ~shared")
    depends_on("xxhash")
    depends_on("zstd libs=static")
    depends_on("utf8proc")
    depends_on("cairo +pdf +png +svg +ft +fc")
    depends_on("python@3:", type=("build", "run"))
    depends_on("r", type="run")

    conflicts("%cxx=gcc@:12", msg="BAli-Phy requires C++23 support (GCC 13 or newer)")
    conflicts("%cxx=llvm@:17", msg="BAli-Phy requires Clang 18 or newer")
    conflicts("%cxx=apple-clang@:15", msg="BAli-Phy requires Apple Clang 16 or newer")

    def setup_build_environment(self, env):
        env.set("BOOST_ROOT", self.spec["boost"].prefix)

    # Meson treats Cairo as optional; require it so the package includes drawing tools.
    def meson_args(self):
        which("pkg-config", required=True)("--cflags", "--libs", "cairo")
        return ["-Db_ndebug=true", "-Dwith-mpi=false", "-Dextra-tools=true"]

    # Exercise installed model files and MCMC; --version alone misses incomplete installations.
    # Keep this small package smoke test alongside the upstream analysis tests.
    def test_analysis(self):
        """Run a short seeded analysis using the installed examples and model libraries."""
        with tempfile.TemporaryDirectory() as directory:
            with working_dir(directory):
                bali_phy = Executable(str(Path(self.prefix.bin) / "bali-phy"))
                bali_phy(
                    str(Path(self.prefix.share.doc) / "bali-phy/examples/5S-rRNA/5d.fasta"),
                    "--iterations=20",
                    "--seed=12345",
                )
                assert Path("5d-1/C1.log").is_file()
