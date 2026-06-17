# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Uriparser(CMakePackage):
    """uriparser is a strictly RFC 3986 compliant URI parsing and handling
    library written in C99."""

    homepage = "https://uriparser.github.io/"
    url = "https://github.com/uriparser/uriparser/releases/download/uriparser-0.9.3/uriparser-0.9.3.tar.gz"

    license("BSD-3-Clause")

    version(
        "1.0.2",
        sha256="963554c32d40fb6cba5644f1ba63e6dd7a182b2948bd71ee448c532f53b07f1e",
    )
    # deprecate all releases before 1.0.2 because of various security issues
    version(
        "1.0.1",
        sha256="5a3b7c491a1e9033d86b9c00a947bafc46407187938578daf799a4155cb7c88a",
        deprecated=True,
    )
    version(
        "0.9.7",
        sha256="11553b2abd2b5728a6c88e35ab08e807d0a0f23c44920df937778ce8cc4d40ff",
        deprecated=True,
    )
    version(
        "0.9.6",
        sha256="10e6f90d359c1087c45f907f95e527a8aca84422251081d1533231e031a084ff",
        deprecated=True,
    )

    variant("docs", default=False, description="Build API documentation")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("cmake@3.15:", type="build")
    depends_on("googletest@1.8.1", type="link")
    depends_on("doxygen", when="+docs", type="build")
    depends_on("graphviz", when="+docs", type="build")

    def cmake_args(self):
        args = []

        if self.run_tests:
            args.append("-DURIPARSER_BUILD_TESTS:BOOL=ON")
        else:
            args.append("-DURIPARSER_BUILD_TESTS:BOOL=OFF")

        if "+docs" in self.spec:
            args.append("-DURIPARSER_BUILD_DOCS:BOOL=ON")
        else:
            args.append("-DURIPARSER_BUILD_DOCS:BOOL=OFF")

        return args
