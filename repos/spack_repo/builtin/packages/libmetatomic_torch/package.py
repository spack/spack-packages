# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class LibmetatomicTorch(CMakePackage):
    """TorchScript/C++ bindings to metatomic"""

    homepage = "https://docs.metatensor.org/metatomic"
    url = "https://github.com/metatensor/metatomic/releases/download/metatomic-torch-v0.1.4/metatomic-torch-cxx-0.1.4.tar.gz"
    git = "https://github.com/metatensor/metatomic.git"

    maintainers("HaoZeke", "luthaf", "rmeli")
    license("BSD-3-Clause", checked_by="HaoZeke")

    version("0.1.4", sha256="385ec8b8515d674b6a9f093f724792b2469e7ea2365ca596f574b64e38494f94")

    depends_on("cmake@3.16:", type="build")
    depends_on("cxx", type="build")
    depends_on("c", type="build")
    depends_on("libmetatensor-torch@0.8.0:")
    depends_on("py-torch@2.1.0:2.7.0")
