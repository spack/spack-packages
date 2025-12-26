# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class LibmetatomicTorch(CMakePackage):
    """TorchScript/C++ bindings to metatomic"""

    homepage = "https://docs.metatensor.org/metatomic"
    url = "https://github.com/metatensor/metatomic/releases/download/metatomic-torch-v0.0.0/metatomic-torch-cxx-0.0.0.tar.gz"
    git = "https://github.com/metatensor/metatomic.git"

    maintainers("HaoZeke", "Luthaf", "RMeli")
    license("BSD-3-Clause", checked_by="HaoZeke")

    version("0.1.6", sha256="4cb9b7bb530a98119186167c31fb00ea7ef3bcc45d593e449e7670e9313e5327")
    version("0.1.5", sha256="8ecd1587797fe1cf6b2162ddc10cc84c558fdfd55ab225bc5de4fe15ace8fc3d")
    version("0.1.4", sha256="385ec8b8515d674b6a9f093f724792b2469e7ea2365ca596f574b64e38494f94")
    version("0.1.3", sha256="01a49e64e6c23d269fe935a557a60ae40092f4aad145fb6201caef26a9e0898b")

    depends_on("cmake@3.16:", type="build")
    depends_on("cxx", type="build")
    depends_on("c", type="build")
    depends_on("libmetatensor-torch@0.8.0:0.8", when="@0.1.4:")
    depends_on("libmetatensor-torch@0.7.6:0.7", when="@0.1.3")
    depends_on("py-torch@2.1.0:")
