# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage

from spack.package import *


class TorchScatter(CMakePackage, CudaPackage):
    """Torch Extension Library of Optimized Scatter Operations.

    This version of the package is consumable by downstream users via CMake
    """

    homepage = "https://github.com/rusty1s/pytorch_scatter"
    git = "https://github.com/rusty1s/pytorch_scatter"
    url = "https://github.com/rusty1s/pytorch_scatter/archive/refs/tags/2.1.2.tar.gz"

    license("MIT")

    version("master", branch="master")
    version("2.1.2", sha256="6f375dbc9cfe03f330aa29ea553e9c7432e9b040d039b041f08bf05df1a8bf37")

    variant("python", default=False, description="Also ensure python bindings are available")

    depends_on("cxx", type="build")
    depends_on("c", type="build")

    depends_on("py-torch")
    depends_on("py-torch +cuda", when="+cuda")

    depends_on("py-torch-scatter@master", when="@master +python")
    depends_on("py-torch-scatter@2.1.2", when="@2.1.2 +python")

    conflicts("py-torch@2.1:", when="@:2.1.2")

    def cmake_args(self):
        args = [
            self.define_from_variant("WITH_CUDA", "cuda"),
            self.define("CMAKE_CXX_STANDARD", "20"),
            self.define("WITH_PYTHON", False),
        ]
        return args
