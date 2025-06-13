# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class LibmetatensorTorch(CMakePackage):
    """TorchScript/C++ bindings to metatensor"""

    homepage = "https://docs.metatensor.org"
    url = "https://github.com/metatensor/metatensor/releases/download/metatensor-torch-v0.7.6/metatensor-torch-cxx-0.7.6.tar.gz"
    git = "https://github.com/metatensor/metatensor.git"

    maintainers("HaoZeke", "luthaf")
    license("BSD-3-Clause", checked_by="HaoZeke")

    version("0.7.6", sha256="8dcc07c86094034facba09ebcc6b52f41847c2413737c8f9c88ae0a2990f8d41")

    depends_on("cmake@3.16:", type="build")
    depends_on("cxx", type="build")
    depends_on("c", type="build")
    depends_on("libmetatensor@0.1.13:", type=("build", "run"))
    conflicts("libmetatensor@0.2.0:")
    depends_on("py-torch@2.1.0:")
    conflicts("py-torch@2.7.0")

    def cmake_args(self):
        args = []
        return args
