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
    version("14.0.1", tag="release/shs-14.0.1", commit="bb11c8594e4cffb90f83f687c6c339a5e2e67045")
    version("14.0.0", tag="release/shs-14.0.0", commit="021715bc84423aa552e811299bcbefba68f87bec")
    version("13.1.0", tag="release/shs-13.1.0", commit="a1d91b2b0cca3782b7587dadfe7f660e326b53cb")
    version("13.0.0", tag="release/shs-13.0.0", commit="f62ae06d0b05774eb8dc4d8f347b4eb881ae35cb")
    version("12.0.2", tag="release/shs-12.0.2", commit="27f7be52e4b1ee6e8ce0c5674352a60869c02105")
    version("12.0.1", tag="release/shs-12.0.1", commit="d1ebe2db2ad311cc7bcae5b6ae11da1d82d198b2")
    version("12.0.0", tag="release/shs-12.0.0", commit="af5d2ed4114134ea4eaf095d16af619573729045")

    def install(self, spec, prefix):
        with working_dir(self.stage.source_path):
            copy_tree("include", prefix.include)
