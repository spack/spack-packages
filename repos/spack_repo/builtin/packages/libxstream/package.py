# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems import cmake, makefile
from spack_repo.builtin.build_systems.cmake import CMakePackage, generator
from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Libxstream(MakefilePackage, CMakePackage):
    """LIBXSTREAM is a library to work with streams, events, and code regions
    that are able to run asynchronous while preserving the usual stream
    conditions."""

    build_system(
        conditional("cmake", when="@1:"),
        conditional("makefile", when="@0.9.0:0.9.1"),
        default="cmake",
    )

    homepage = "https://github.com/hfp/libxstream"
    url = "https://github.com/hfp/libxstream/archive/0.9.0.tar.gz"
    git = "https://github.com/hfp/libxstream.git"

    maintainers("mtaillefumier")

    license("BSD-3-Clause")

    version(
        "0.9.0",
        sha256="03365f23b337533b8e5a049a24bc5a91c0f1539dd042ca5312abccc8f713b473",
    )
    version("main", branch="main")
    version("20260622", commit="64913491c84ce7244b5cd585302d35934277c47f")
    generator("ninja")

    variant("shared", default=True, description="Build shared libraries")
    variant("pic", default=True, description="Enable position independent code")
    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated
    depends_on("fortran", type="build")  # generated
    depends_on("gmake", type="build", when="@0.9.0:0.9.1")

    depends_on("opencl")
    depends_on("libxs", when="@1:")
    depends_on("libxs+shared", when="+shared")


class MakefileBuilder(makefile.MakefileBuilder):
    def patch(self):
        kwargs = {"ignore_absent": False, "backup": True, "string": True}
        makefile = FileFilter("Makefile.inc")

        makefile.filter("CC =", "CC ?=", **kwargs)
        makefile.filter("CXX =", "CXX ?=", **kwargs)
        makefile.filter("FC =", "FC ?=", **kwargs)

    def install(self, spec, prefix):
        make()
        install_tree("lib", prefix.lib)
        install_tree("include", prefix.include)
        install_tree("documentation", prefix.share + "/libxstream/doc/")


class CMakeBuilder(cmake.CMakeBuilder):
    def cmake_args(self):
        args = [
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define_from_variant("CMAKE_POSITION_INDEPENDENT_CODE", "pic"),
        ]
        return args
