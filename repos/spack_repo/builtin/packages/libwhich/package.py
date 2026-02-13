# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Libwhich(MakefilePackage):
    """
    Libwhich: the functionality of which for libraries.
    """

    homepage = "https://github.com/vtjnash/libwhich"
    url = "https://github.com/vtjnash/libwhich/archive/refs/tags/v1.1.0.tar.gz"
    git = "https://github.com/vtjnash/libwhich.git"

    maintainers("dmageeLANL")

    license("MIT")

    version("master", branch="master")
    version("1.3.0", sha256="853e843824ee8b20b0192d45bf9837c860ef41cce4a10bd14c59860753e5fa0b")

    with default_args(deprecated=True):
        version("1.2.0", sha256="aa13017310f3f9b008267283c155992bb7e0f6002dafaf82e6f0dbd270c18b0a")
        version("1.1.0", sha256="f1c30bf7396859ad437a5db74e9e328fb4b4e1379457121e28a3524b1e3a0b3f")
        version("1.0.0", sha256="61d5d643d4cbd4b340b9b48922e1b4fd2a35729b7cfdcc7283aab82a6f742a6c")

    depends_on("c", type="build")

    def install(self, spec, prefix):
        if spec.satisfies("@1.2:"):
            make("install", f"prefix={prefix}")
        else:
            mkdir(prefix.bin)
            install("libwhich", prefix.bin)
