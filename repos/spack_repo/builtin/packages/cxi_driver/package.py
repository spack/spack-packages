# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class CxiDriver(Package):
    """This are the Linux driver headers for the Cray/HPE Cassini 1 and 2
    high-speed network interconnect (aka. Slingshot), and its Ethernet driver."""

    homepage = "https://github.com/HewlettPackard/shs-cxi-driver"
    git = "https://github.com/HewlettPackard/shs-cxi-driver.git"

    license("GPL-2.0")

    version("main", branch="main")
    version("13.1.0", tag="release/shs-13.1.0")
    version("13.0.0", tag="release/shs-13.0.0")
    version("12.0.1", tag="release/shs-12.0.1")
    version("12.0.0", tag="release/shs-12.0.0")

    def install(self, spec, prefix):
        with working_dir(self.stage.source_path):
            copy_tree("include", prefix.include)
