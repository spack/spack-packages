# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage, generator

from spack.package import *


class NanomsgNg(CMakePackage):
    """Nanomsg NG (nng) is a rewrite of the Scalability Protocols
    library known as nanomsg, and adds significant new capabilities,
    while retaining compatibility with the original."""

    homepage = "https://nng.nanomsg.org/"
    url = "https://github.com/nanomsg/nng/archive/refs/tags/v2.1.0.tar.gz"
    git = "https://github.com/nanomsg/nng.git"

    maintainers("yahooguntu")

    license("MIT", checked_by="yahooguntu")

    version("main", branch="main")
    version("2.1.0", sha256="e2fdcdf126b530e331b4727812b710629cdb5d90d230ce8f080e2eb520299d8d")

    generator("ninja")

    # note: wolfssl is also supported, but there isn't a recipe for it
    variant(
        "tls_engine",
        default="none",
        values=("openssl", "mbed", "none"),
        description="TLS support"
    )

    depends_on("c", type="build")
    depends_on("cmake@3.15:", type="build")

    depends_on("mbedtls@3.6: libs=shared", when="tls_engine=mbed")
    depends_on("openssl@3.5:", when="tls_engine=openssl")

    def cmake_args(self):
        # avoid the need for a c++ compiler by turning off compilation of tests
        args = [self.define("NNG_TESTS", "OFF")]

        if not self.spec.satisfies("tls_engine=none"):
            args.append(self.define("NNG_ENABLE_TLS", True))
            args.append(self.define_from_variant("NNG_TLS_ENGINE", "tls_engine"))
        return args

    def test_nngcat(self):
        nngcat = which(self.prefix.bin.nngcat)
        if nngcat is None:
            raise SkipTest("nngcat was not built or installed")

        out = nngcat("--version", output=str, error=str)
        assert out, "nngcat --version returned empty output"
