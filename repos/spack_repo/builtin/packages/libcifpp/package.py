# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Libcifpp(CMakePackage):
    """Library containing code to manipulate mmCIF and PDB files."""

    homepage = "https://github.com/PDB-REDO/libcifpp"
    url = "https://github.com/PDB-REDO/libcifpp/archive/refs/tags/v9.0.6.tar.gz"

    license("BSD-2-Clause", checked_by="snehring")

    version("10.0.3", sha256="1f151165cdfc23a7acdc728e86db21ba6ad5470c582bc856c06226eb7884ee35")
    version("9.0.6", sha256="e6263a63404762671d6875de385e0c7ad869b0fe3fae41808003e00c94e7ed8c")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("pkgconfig", type="build")
    # just using headers apparently
    depends_on("eigen@3", type="build")
    depends_on("fmt", when="@:9.0.6")
    depends_on("pcre2")
    depends_on("zlib-api")

    with when("@10:"):
        conflicts("%gcc@:12", msg="libcifpp requires gcc@13:")
        conflicts("%clang@:13", msg="libcifpp requires clang@14:")

    def patch(self):
        # include<format> not actually available until gcc13 or clang 14
        if self.spec.satisfies("@:9.0.6 %gcc@:12"):
            files = [
                join_path("include", "cif++", "format.hpp"),
                join_path("include", "cif++", "point.hpp"),
                join_path("src", "model.cpp"),
                join_path("src", "utilities.cpp"),
            ]
            for f in files:
                filter_file("std::format", "fmt::format", f, string=True)
            # would a crazy person do this!?
            for f in [files[i] for i in [1, 3]]:
                filter_file("#include <format>", "#include <fmt/format.h>", f)
            filter_file(r"(find_package\(Threads\))", "\\1\nfind_package(fmt)", "CMakeLists.txt")
            filter_file(r"(PUBLIC Threads::Threads .*>)", "\\1 fmt::fmt", "CMakeLists.txt")
            filter_file(
                r"(find_dependency\(Threads\))",
                "\\1\nfind_dependency(fmt)",
                join_path("cmake", "cifpp-config.cmake.in"),
            )
