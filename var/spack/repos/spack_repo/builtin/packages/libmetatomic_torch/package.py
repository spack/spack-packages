# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class LibmetatomicTorch(CMakePackage):
    """TorchScript/C++ bindings to metatomic"""

    homepage = "https://docs.metatensor.org/metatomic"
    url = "https://github.com/metatensor/metatomic/releases/download/metatomic-torch-v0.1.2/metatomic_torch-0.1.2.tar.gz"
    git = "https://github.com/metatensor/metatomic.git"

    maintainers("HaoZeke", "luthaf", "rmeli")
    license("BSD-3-Clause", checked_by="HaoZeke")

    version("0.1.2", sha256="0d793b16b3d6eee915c89e9b1a385143ec2dbb6dc451bed8feee3a2445b3f63e")

    depends_on("cmake@3.16:", type="build")
    depends_on("cxx", type="build")
    depends_on("c", type="build")
    depends_on("libmetatensor-torch@0.7.6:", type=("build", "run"))
    depends_on("py-torch@2.1.0:2.7.0")

    def cmake_args(self):
        args = []
        return args
