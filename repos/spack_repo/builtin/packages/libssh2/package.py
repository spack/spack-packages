# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems import autotools, cmake
from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Libssh2(AutotoolsPackage, CMakePackage):
    """libssh2 is a client-side C library implementing the SSH2 protocol"""

    homepage = "https://www.libssh2.org/"
    url = "https://www.libssh2.org/download/libssh2-1.7.0.tar.gz"

    license("BSD-3-Clause")

    version("1.11.1", sha256="d9ec76cbe34db98eec3539fe2c899d26b0c837cb3eb466a56b0f109cabf658f7")

    build_system("autotools", "cmake", default="autotools")

    variant(
        "crypto",
        default="openssl",
        description="The backend to use for cryptography",
        values=("openssl", "mbedtls"),
    )
    variant("shared", default=True, description="Build shared libraries")

    depends_on("c", type="build")

    with when("build_system=cmake"):
        depends_on("cmake@2.8.11:", type="build")
        # on macOS ensure CMP0042 is on (default in cmake 3.0+)
        depends_on("cmake@3:", type="build", when="platform=darwin")

    with when("crypto=openssl"):
        depends_on("openssl")

    depends_on("mbedtls@:2 +pic", when="crypto=mbedtls")
    depends_on("zlib-api")
    depends_on("xz")


class CMakeBuilder(cmake.CMakeBuilder):
    def cmake_args(self):
        args = [
            self.define("BUILD_TESTING", False),
            self.define("RUN_DOCKER_TESTS", False),
            self.define("BUILD_EXAMPLES", False),
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
        ]

        crypto = self.spec.variants["crypto"].value

        if crypto == "openssl":
            args.append(self.define("CRYPTO_BACKEND", "OpenSSL"))
        elif crypto == "mbedtls":
            args.append(self.define("CRYPTO_BACKEND", "mbedTLS"))

        return args


class AutotoolsBuilder(autotools.AutotoolsBuilder):
    def configure_args(self):
        crypto = self.spec.variants["crypto"].value
        return [
            "--disable-tests",
            "--disable-docker-tests",
            "--disable-examples-build",
            "--without-libgcrypt",
            "--without-wincng",
            *self.enable_or_disable("shared"),
            f"--with-crypto={crypto}",
        ]
