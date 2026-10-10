# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.cargo import CargoPackage

from spack.package import *


class AsciinemaAgg(CargoPackage):
    """agg (asciinema gif generator) produces high-quality, lightweight animated GIF
    files from asciicast terminal recordings. It supports custom color themes, fonts,
    rendering speed adjustments, and idle-time compression.
    """

    homepage = "https://docs.asciinema.org/manual/agg/"
    url = "https://github.com/asciinema/agg/archive/refs/tags/v1.9.0.tar.gz"
    git = "https://github.com/asciinema/agg.git"

    license("GPL-3.0-or-later")

    version("1.9.0", sha256="8170119502ad2c1c697e5cd4d050d87c425ecee726c5f6c3c2140703bcb31bb3")
    version("1.8.1", sha256="9a2a7e6ca2748befb6a4c1c3eff437ae6029fde99ec882a951b3671aa30eacdb")
    version("1.8.0", sha256="31e0d54b6abc2c7545464bef0b5b9603d851c186c4ecfcd52f08a30d7bfa2781")
    version("1.7.0", sha256="8927e2f3b1db53feed2e74319497ddc8404ac7989cb592099c402fbd05d94aa4")
    version("1.6.0", sha256="541bdc7e7ec148d2146c8033e58a9046d9d3587671e8f375c9e606b5a24d3f82")
    version("1.5.0", sha256="4bfbd0cc02f416ce868f0209b659a87e333de8f0b5edad19810e152ac6e7fc55")
    version("1.4.3", sha256="1089e47a8e6ca7f147f74b2347e6b29d94311530a8b817c2f30f19744e4549c1")

    depends_on("c", type="build")
    depends_on("rust@1.85.0:", type="build", when="@1.7.0:")
    depends_on("rust@1.75.0:", type="build", when="@1.6.0")
    depends_on("rust@1.70.0:", type="build", when="@:1.5.0")

    @run_after("install")
    def symlink_asciinema_agg(self):
        with working_dir(self.prefix.bin):
            if os.path.exists("agg") and not os.path.exists("asciinema-agg"):
                symlink("agg", "asciinema-agg")

    def test_version(self):
        """Check agg can run and report its version."""
        agg = which(self.prefix.bin.join("agg"))
        out = agg("--version", output=str.split, error=str.split)
        assert str(self.spec.version) in out
