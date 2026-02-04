# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Malt(CMakePackage):
    """
    MALT is a memory profile tool to track mallocs in a C/C++ application and report
    allocation information (lifetime, sizes...) in a friendly web graphical interface
    by annotating the source code and proving charts.
    """

    # Project infos
    homepage = "https://memtt.github.io/malt"
    url = "https://github.com/memtt/malt/releases/download/v1.5.0/malt-1.5.0.tar.xz"
    maintainers("svalat")

    license("CECILL-C")

    # Versions XZ
    version("1.6.0", sha256="61a4a9f0c61057eb91ef4bca9f461469c2a8a57010c2e5011b321fcc8632fc73")
    version("1.5.0", sha256="da41f80855578d219079b8f0a7b333085706129e8310d8ad3f9c5b5721839bbc")

    # Version BZ2
    version(
        "1.4.1",
        sha256="9bd25c8a9f4d7004c32ff20cba6909e7b246c1f6c29307ef357809f4b4955d82",
        url="https://github.com/memtt/malt/releases/download/v1.4.1/malt-1.4.1.tar.bz2",
    )
    version(
        "1.3.1",
        sha256="9f3b22ace13e0a3bc773fed4044a5c19439aeb9111077582704382b3d1675194",
        url="https://github.com/memtt/malt/releases/download/v1.3.1/malt-1.3.1.tar.bz2",
    )
    version(
        "1.2.5",
        sha256="9660e42f92230e6acf5c19df5195f59a4c2d7d919eeab4410fe943507eee2c67",
        url="https://github.com/memtt/malt/releases/download/v1.2.5/malt-1.2.5.tar.bz2",
    )

    # Versions now deprecated
    with default_args(deprecated=True):
        version(
            "1.4.0",
            sha256="fb64e99eec9b9d3cb46b5f9cbd1e47b31354356ebc0502c27af101dfcff68b9f",
            url="https://github.com/memtt/malt/releases/download/v1.4.0/malt-1.4.0.tar.bz2",
        )
        version(
            "1.2.4",
            sha256="47068fe981b4cbbfe30eeff37767d9057992f8515106d7809ce090d3390a712f",
            url="https://github.com/memtt/malt/releases/download/v1.2.4/malt-1.2.4.tar.bz2",
        )
        version(
            "1.2.3",
            sha256="edba5d9e6a11308f82b9c8b61871e47a8ae18493bf8bff7b6ff4f4a4369428de",
            url="https://github.com/memtt/malt/releases/download/v1.2.3/malt-1.2.3.tar.bz2",
        )
        version(
            "1.2.2",
            sha256="543cace664203fd9eb6b7d4945c573a3e507a43da105b5dc7ac03c78e9bb1a10",
            url="https://github.com/memtt/malt/releases/download/v1.2.2/malt-1.2.2.tar.bz2",
        )
        version(
            "1.2.1",
            sha256="0e4c0743561f9fcc04dc83457386167a9851fc9289765f8b4f9390384ae3618a",
            url="https://github.com/memtt/malt/archive/v1.2.1.tar.gz",
        )

    # Variants up to 1.3.1
    variant(
        "nodejs",
        default=True,
        description="Enable the installation of the Web GUI based on NodeJS",
        when="@:1.3.1",
    )

    # Variants up to 1.2.5
    variant(
        "qt",
        default=False,
        when="+nodejs@:1.2.5",
        description="Build the viewer based on NodeJS + QT web toolkit (requires NodeJS too)",
    )

    # Dependencies
    depends_on("cxx", type="build")
    depends_on("c", type="build")

    # Old deps up to 1.3.1
    depends_on("node-js@18:", type=("build", "run"), when="+nodejs@:1.3.1")
    depends_on("qt", when="+qt@:1.3.1")

    # common deps
    depends_on("libelf")
    depends_on("libunwind")
    depends_on("binutils", type="run")

    # from 1.4.0 - 1.4.1
    depends_on("openssl", when="@1.4.0:1.4.1")

    # since 1.4.0
    depends_on("python@3:", when="@1.4.0:")

    # since 1.5.0
    depends_on("nlohmann-json", when="@1.5.0:")

    # configure options
    def cmake_args(self):
        if self.spec.satisfies("@1.5.0:"):
            return [f"-DPYTHON_PREFIX={self.spec['python'].prefix}", "-DLIBDIR=lib64"]
        elif self.spec.satisfies("@1.4.0:"):
            return [
                f"-DCRYPTO_PREFIX={self.spec['openssl'].prefix}",
                f"-DPYTHON_PREFIX={self.spec['python'].prefix}",
                "-DLIBDIR=lib64",
            ]
        else:
            return []
        return []
