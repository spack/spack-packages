# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Mille(CMakePackage):
    """Mille is the I/O component used by the Millepede-II package
    and supported by the GeneralBrokenLines track fitter."""

    homepage = "https://gitlab.desy.de/millepede/mille"
    url = "https://gitlab.desy.de/millepede/mille/-/archive/V01-00-00/mille-V01-00-00.tar.gz"
    git = "https://gitlab.desy.de/millepede/mille.git"

    license("LGPL-2.0-only", checked_by="paulgessinger")

    version("main", branch="main")
    version("01-00-03", sha256="1953e2a341fed3a1c431c954d6e8f1c823926bc2886bdc209d859d2cb9dac6d8")
    version("01-00-02", sha256="bb232672003a8f13f848635e49a261acb79de26634e4ba76347358f209b5de05")
    version("01-00-00", sha256="ae4bf37de8d835aa8adc2960bb795a2080233a4c8af3d4b55adf395e20df0f3e")

    variant("zlib", default=True, description="Enable zlib support")
    variant("root", default=False, description="Enable ROOT support")

    _cxxstd_values = ["17", "20", "23"]
    variant(
        "cxxstd",
        default="20",
        values=_cxxstd_values,
        multi=False,
        description="Use the specified C++ standard when building.",
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")

    depends_on("zlib-api", when="+zlib")

    for cxxstd in _cxxstd_values:
        depends_on(f"root cxxstd={cxxstd}", when=f"+root cxxstd={cxxstd}")

    def cmake_args(self):
        args = [
            self.define_from_variant("SUPPORT_ZLIB", "zlib"),
            self.define_from_variant("SUPPORT_ROOT", "root"),
            self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"),
            "-DBUILD_TESTS=OFF",
        ]
        return args
