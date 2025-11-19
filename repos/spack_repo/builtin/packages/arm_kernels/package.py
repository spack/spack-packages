# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class ArmKernels(MakefilePackage):
    """This is a suite of simple Arm assembly kernels for testing
    the performance and functionality of Arm CPUs.
    """

    homepage = "https://github.com/NVIDIA/arm-kernels"
    git = "https://github.com/NVIDIA/arm-kernels.git"

    maintainers("green-br")

    license("BSD-3-Clause")

    version("main", branch="main")

    requires("target=aarch64:", msg="package is only available on aarch64")

    depends_on("cxx", type="build")

    def patch(self):
        filter_file(r"CXX = .*", "", "config.mk")
        filter_file(r"CXXFLAGS = .*", "", "config.mk")
        target = self.spec.target
        if "sve" not in target.features:
            filter_file(r"^.*_sve_.*\.x.*", "	\\", "arithmetic/Makefile")
        if "fphp" not in target.features:
            filter_file(r"^.*fp16_.*\.x.*", "	\\", "arithmetic/Makefile")

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install("arithmetic/*.x", prefix.bin)
