# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import platform

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class PypyBootstrap(Package):
    """Binary build of PyPy 2 for bootstrapping source build of PyPy 3."""

    homepage = "https://www.pypy.org/"
    url = "https://downloads.python.org/pypy/pypy2.7-v8.0.0-linux64.tar.gz"

    maintainers("adamjstewart")

    license("MIT")

    if platform.system() == "Linux":
        if platform.machine() == "x86_64":
            version(
                "2.7-v8.0.0", "714e8c41608d0d66588c3ba48fb788dc33a1e8a865168d165585d1660beade0d"
            )
            version(
                "2.7-v7.3.12", "1a61a2574b79466f606010f2999a2b995bd96cd085f91a78ebdd3d5c2c40e81d"
            )
        elif platform.machine() == "aarch64":
            version(
                "2.7-v8.0.0", "9ece5a6f575514ed38dde663e7f54e59de01c35b2df6d1ef83e25490d6b7c7b8"
            )
            version(
                "2.7-v7.3.12", "e04dcb6286a7b4724ec3f0e50d3cc1ba8583301dd1658c06d7f37599e4201c59"
            )
    elif platform.system() == "Darwin":
        if platform.machine() == "arm64":
            version(
                "2.7-v8.0.0", "167966aa205ca29b8d3ac6994e3d0d1741f3bf03e9e300737ed591304347c7b0"
            )
            version(
                "2.7-v7.3.12", "6b747aa076ae8597e49603c5dec4ca5935a1a0a132d7404a559be96a260d9bf7"
            )
        elif platform.machine() == "x86_64":
            version(
                "2.7-v8.0.0", "4e4f27669b27a7ff950058eb07e22687f5a04ba04220bb3df24411f07d5c0340"
            )
            version(
                "2.7-v7.3.12", "6e89ffdd15537ce4ffce3145b65ee57c2e9c952892bd95b934012d2f009f503b"
            )
    elif platform.system() == "Windows":
        version("2.7-v8.0.0", "185abbe3186e44966a771adcb7f652e2d1710b52202ee38edc8577152216da43")
        version("2.7-v7.3.12", "84cd3b98812d47a1ddb36f3417cc96b3dbdfa32c2b4e16438f205e1253f7ccea")

    def url_for_version(self, version):
        url = "https://downloads.python.org/pypy/pypy{}-{}.{}"
        if version >= Version("2.7-v8"):
            ext = "tar.gz"
        else:
            ext = "tar.bz2"
        if platform.system() == "Linux":
            if platform.machine() == "x86_64":
                arch = "linux64"
            elif platform.machine() == "aarch64":
                arch = "aarch64"
        elif platform.system() == "Darwin":
            arch = "macos_" + platform.machine()
        elif platform.system() == "Windows":
            arch = "win64"
            ext = "zip"
        return url.format(version, arch, ext)

    def install(self, spec, prefix):
        install_tree(".", prefix)

    @property
    def command(self):
        return Executable(self.prefix.bin.pypy)

    def setup_dependent_package(self, module, dependent_spec):
        module.pypy = self.command
