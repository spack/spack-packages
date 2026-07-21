# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Kcov(CMakePackage):
    """Code coverage tool for compiled programs, Python and Bash which uses
    debugging information to collect and report data without special
    compilation options"""

    homepage = "https://simonkagstrom.github.io/kcov/index.html"
    url = "https://github.com/SimonKagstrom/kcov/archive/refs/tags/v42.tar.gz"

    license("GPL-2.0-or-later")

    version("43", sha256="4cbba86af11f72de0c7514e09d59c7927ed25df7cebdad087f6d3623213b95bf")
    version("42", sha256="2c47d75397af248bc387f60cdd79180763e1f88f3dd71c94bb52478f8e74a1f8")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("cmake@2.8.4:", type="build")
    depends_on("zlib-api", type="link")
    depends_on("curl", type="link")
    depends_on("openssl", type="link")
    depends_on("libdwarf", when="platform=darwin", type="link")
    depends_on("elfutils", when="platform=linux", type="link")
    depends_on("binutils +libiberty", when="platform=linux", type="link")

    def cmake_args(self):
        # Necessary at least on macOS, fixes linking error to LLDB
        # https://github.com/Homebrew/homebrew-core/blob/master/Formula/kcov.rb
        return ["-DSPECIFY_RPATH=ON"]

    def test_kcov_help(self):
        """run installed kcov help"""
        kcov = Executable(self.prefix.bin.kcov)
        # The help message exits with an exit code of 1
        kcov("-h", ignore_errors=1)

    @run_after("install")
    @on_package_attributes(run_tests=True)
    def check_install(self):
        self.test_kcov_help()
