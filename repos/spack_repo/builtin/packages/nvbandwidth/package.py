# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage

from spack.package import *


class Nvbandwidth(CMakePackage, CudaPackage):
    """
    nvbandwidth: A tool for bandwidth measurements on NVIDIA GPUs.
    """

    git = "https://github.com/NVIDIA/nvbandwidth"

    license("Apache-2.0")

    version("main", branch="main")

    version(
        "v0.9",
        url="https://github.com/NVIDIA/nvbandwidth/archive/refs/tags/v0.9.tar.gz",
        sha256="552e7b2595c4b95ab1da86ba002f239185d247b2fb9929ed3cb9dc7f57bcd67c",
        preferred=True,
    )

    version(
        "v0.8",
        url="https://github.com/NVIDIA/nvbandwidth/archive/refs/tags/v0.8.tar.gz",
        sha256="b3622945eb7fce2b4e1aea7d13de04f415f4d998db602893201a904320cf2d39",
    )

    version(
        "v0.4",
        url="https://github.com/NVIDIA/nvbandwidth/archive/refs/tags/v0.4.tar.gz",
        sha256="c87eda04d5909d26c0d8756dd1a66ab048cf015dbb0d2719971dee182aa69212",
    )

    version(
        "v0.3",
        url="https://github.com/NVIDIA/nvbandwidth/archive/refs/tags/v0.3.tar.gz",
        sha256="744bcf9fbd007f4f71f7b5c2295aa223fe39eb5f048e6b1b6a3d0f942a19b3cc",
    )

    version(
        "v0.2",
        url="https://github.com/NVIDIA/nvbandwidth/archive/refs/tags/v0.2.tar.gz",
        sha256="d41a45dc03dd2baf37b6c4ecdbca442c5e9f6f989fd3ffa90852e50ba9ded26c",
    )

    version(
        "v0.1",
        url="https://github.com/NVIDIA/nvbandwidth/archive/refs/tags/v0.1.tar.gz",
        sha256="ce164f91e35d1b28ebb1f83b22f38199e430d18ebfb8e21fa8c5e53c38d82daf",
    )

    depends_on("cxx", type="build")  # generated

    depends_on("boost@1.66.0:+program_options")

    requires("+cuda")

    def install(self, spec, prefix):
        # We have no `make install` target, so move the files over explicitly
        mkdirp(prefix.bin)
        install(join_path(self.build_directory, "nvbandwidth"), join_path(prefix.bin))
