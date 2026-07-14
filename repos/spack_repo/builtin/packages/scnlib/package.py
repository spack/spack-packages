# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Scnlib(CMakePackage):
    """scanf for modern C++"""

    homepage = "https://scnlib.dev"
    url = "https://github.com/eliaskosunen/scnlib/archive/refs/tags/v4.0.1.tar.gz"

    maintainers("pranav-sivaraman")

    license("Apache-2.0", checked_by="pranav-sivaraman")

    version("4.0.1", sha256="ece17b26840894cc57a7127138fe4540929adcb297524dec02c490c233ff46a7")
    version("3.0.1", sha256="bc8a668873601d00cce6841c2d0f2c93f836f63f0fbc77997834dea12e951eb1")

    variant("shared", default=True, description="Build shared libs")
    variant(
        "regex-backend",
        default="std",
        description="Regex backend to use",
        multi=False,
        values=("std", "Boost"),
    )
    variant(
        "icu",
        default=False,
        description="Use the ICU when using the Boost regex backend",
        when="regex-backend=Boost",
    )

    depends_on("cxx", type="build")
    depends_on("cmake@3.16:", type="build")

    depends_on("fast-float@5:6")

    depends_on("boost +regex cxxstd=17", when="regex-backend=Boost")
    depends_on("boost +icu", when="+icu")

    depends_on("googletest cxxstd=17", type="test")
    depends_on("python@3:", type="test")

    patch(
        url="https://github.com/eliaskosunen/scnlib/commit/39276cc436adcfc2544faf1de3991c2784c86ce3.patch?full_index=1",
        sha256="013a8a9466fadb3396af187da08057f4e79b1c26bf340da99b19fd47dd049795",
        when="@4",
    )

    def cmake_args(self):
        args = [
            self.define("SCN_TESTS", self.run_tests),
            self.define("SCN_BENCHMARKS", False),
            self.define("SCN_EXAMPLES", False),
            self.define("SCN_DOCS", False),
            self.define("SCN_USE_EXTERNAL_FAST_FLOAT", True),
            self.define("SCN_USE_EXTERNAL_GTEST", True),
            self.define("SCN_USE_EXTERNAL_BENCHMARK", True),
            self.define("SCN_USE_EXTERNAL_REGEX_BACKEND", True),
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define_from_variant("SCN_REGEX_BACKEND", "regex-backend"),
        ]

        return args
