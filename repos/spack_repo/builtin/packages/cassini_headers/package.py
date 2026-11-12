# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class CassiniHeaders(Package):
    """This package provides hardware definitions and C headers for use by the
    Linux driver and by user-space applications for the Cassini/Slingshot
    +high-speed network interconnect made by HPE (formerly Cray)"""

    homepage = "https://github.com/HewlettPackard/shs-cassini-headers"
    git = "https://github.com/HewlettPackard/shs-cassini-headers.git"

    license("GPL-2.0-only or BSD-2-Clause")

    version("main", branch="main")
    version("14.0.1", tag="release/shs-14.0.1", commit="125b3d00d0d65029a21aa139f8dce88d845491c5")
    version("14.0.0", tag="release/shs-14.0.0", commit="96e971c9cf26c8fa3aa2f33be55fc36f25055b14")
    version("13.1.0", tag="release/shs-13.1.0", commit="2f6e60a44367ff7439dbb2315531b73fcf5dc4c8")
    version("13.0.0", tag="release/shs-13.0.0", commit="144056ff2143b99ec08b3f1cd07c5e3ae176878d")
    version("12.0.2", tag="release/shs-12.0.2", commit="b3f65f01296e4f486bb41fafed7ff6ee686cee8f")
    version("12.0.1", tag="release/shs-12.0.1", commit="b3f65f01296e4f486bb41fafed7ff6ee686cee8f")
    version("12.0.0", tag="release/shs-12.0.0", commit="b3f65f01296e4f486bb41fafed7ff6ee686cee8f")

    def install(self, spec, prefix):
        with working_dir(self.stage.source_path):
            copy_tree("include", prefix.include)
            copy_tree("share", prefix.share)
