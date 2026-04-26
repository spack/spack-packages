# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import sys

from spack_repo.builtin.build_systems import autotools, cmake
from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Expat(AutotoolsPackage, CMakePackage):
    """Expat is an XML parser library written in C."""

    homepage = "https://libexpat.github.io/"
    url = "https://github.com/libexpat/libexpat/releases/download/R_2_2_9/expat-2.2.9.tar.bz2"

    license("MIT")
    version("2.8.0", sha256="586494499ac3ad46d87f3beda7b1f770c1c8026a9b60e151593f8b29089a52ca")
    # deprecate all releases before 2.8.0 because of various security issues
    version(
        "2.7.5",
        sha256="386a423d40580f1e392e8b512b7635cac5083fe0631961e74e036b0a7a830d77",
        deprecated=True,
    )
    version(
        "2.7.4",
        sha256="e6af11b01e32e5ef64906a5cca8809eabc4beb7ff2f9a0e6aabbd42e825135d0",
        deprecated=True,
    )
    version(
        "2.7.3",
        sha256="59c31441fec9a66205307749eccfee551055f2d792f329f18d97099e919a3b2f",
        deprecated=True,
    )
    version(
        "2.7.2",
        sha256="976f6c2d358953c22398d64cd93790ba5abc62e02a1bbc204a3a264adea149b8",
        deprecated=True,
    )
    version(
        "2.7.1",
        sha256="45c98ae1e9b5127325d25186cf8c511fa814078e9efeae7987a574b482b79b3d",
        deprecated=True,
    )
    version(
        "2.7.0",
        sha256="10f3e94896cd7f44de566cafa2e0e1f35e8df06d119b38d117c0e72d74a4b4b7",
        deprecated=True,
    )

    build_system("autotools", "cmake", default="autotools")

    # Version 2.2.2 introduced a requirement for a high quality
    # entropy source.  "Older" linux systems (aka CentOS 7) do not
    # support get_random so we'll provide a high quality source via
    # libbsd.
    variant(
        "libbsd",
        default=sys.platform == "linux",
        description="Use libbsd (for high quality randomness)",
    )

    variant(
        "shared",
        default=True,
        description="Build expat as shared if true, static if false",
        when="build_system=cmake",
    )

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("libbsd", when="+libbsd")

    def url_for_version(self, version):
        url = "https://github.com/libexpat/libexpat/releases/download/R_{0}/expat-{1}.tar.bz2"
        return url.format(version.underscored, version.dotted)


class AutotoolsBuilder(autotools.AutotoolsBuilder):
    def configure_args(self):
        spec = self.spec
        args = ["--without-docbook", "--enable-static"]
        if spec.satisfies("+libbsd"):
            args.append("--with-libbsd")
        return args


class CMakeBuilder(cmake.CMakeBuilder):
    def cmake_args(self):
        args = [
            self.define("EXPAT_BUILD_DOCS", False),
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
        ]

        if self.spec.satisfies("+libbsd"):
            args.append(self.define_from_variant("EXPAT_WITH_LIBBSD", "libbsd"))

        return args
