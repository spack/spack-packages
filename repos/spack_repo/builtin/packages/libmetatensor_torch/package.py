# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class LibmetatensorTorch(CMakePackage):
    """TorchScript/C++ bindings to metatensor"""

    homepage = "https://docs.metatensor.org"
    url = "https://github.com/metatensor/metatensor/releases/download/metatensor-torch-v0.0.0/metatensor-torch-cxx-0.0.0.tar.gz"
    git = "https://github.com/metatensor/metatensor.git"

    maintainers("HaoZeke", "luthaf", "rmeli")
    license("BSD-3-Clause", checked_by="HaoZeke")

    version("0.8.0", sha256="61d383ce958deafe0e3916088185527680c9118588722b17ec5c39cfbaa6da55")
    version("0.8.1", sha256="9da124e8e09dc1859700723a76ff29aef7a216b84a19d38746cc45bf45bc599b")

    depends_on("cmake@3.16:", type="build")
    depends_on("cxx", type="build")
    depends_on("c", type="build")
    depends_on("libmetatensor@0.1.14:0.1")
    depends_on("py-torch@2.1.0:")
