# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Mille(CMakePackage):
    """Mille is the I/O component used by the Millepede-II package
    and supported by the GeneralBrokenLines track fitter."""

    homepage = "https://github.com/millepede-project/mille"
    url = "https://github.com/millepede-project/mille/archive/refs/tags/V01-00-05.tar.gz"
    git = "https://github.com/millepede-project/mille.git"

    license("LGPL-2.0-only", checked_by="paulgessinger")

    version("main", branch="main")
    version("01-01-04", sha256="40b4d702208b33683d390b4684ccc90f6df0805fd96a92e33fefa12b93387dfe")
    version("01-01-03", sha256="f8962ad6cedab87a45fe5d40341f29712bbabcddd33375414a89dc2b11ac86ad")
    version("01-01-02", sha256="b765224b516d2c1840c84905b9df697858564b5851fd6926b8fe1d2d8a063505")
    version("01-01-01", sha256="415da5f7da0c477985be6a807c175013a862f9685e568cb2632d533c37f246be")
    version("01-01-00", sha256="8535bf002453cc30a3719ca0347b07008c57a8d31a810c926c8c857539935fc9")
    version("01-00-05", sha256="2dec8402201938c7b2d7680db30aff19fd06dd06a420dbde45f57de2ce50d2ff")
    version("01-00-04", sha256="cfd9d87f45b78aa0fc43d128d8ba25a81d0123b705aea7dc666548e561ce3e74")
    version("01-00-03", sha256="ecfb238ededdc88785d20ecb913149796001fcf670f55200ca6c68e63026b7b2")
    version("01-00-02", sha256="b91af335c9797170ad3cebe4621532d16b72dc7c344ded47830eeea00ee0ad95")
    version("01-00-00", sha256="0da735a8948c26b4b3ad81ef0ff1515826a7f7a30186a09fb973981c8eef5172")

    requires("%gcc", msg="Mille hardcodes gcc/g++/gfortran", when="@:01-00-03")

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
