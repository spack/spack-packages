# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Lyra(CMakePackage):
    """A simple to use, composable, header-only command-line parser for C++11 and beyond."""

    homepage = "https://github.com/bfgroup/Lyra"
    url = "https://github.com/bfgroup/Lyra/releases/download/1.7.0/lyra-1.7.0.tar.bz2"
    license("BSL-1.0")

    version("1.8.0", sha256="7f70c230f0bbcdf77a653f982343c87028cf8a0d4196f6ac79ad376697ed1c1a")

    depends_on("cmake@3.12:", type="build")

    def test(self):
        test_src = join_path(self.package_dir, "test")
        test_dir = self.test_suite.current_test_data_dir

        install_tree(test_src, test_dir)

        with working_dir(test_dir):
            cmake = which("cmake")
            cmake(
                "-S",
                ".",
                "-B",
                "build",
                "-DCMAKE_PREFIX_PATH={0}".format(self.prefix),
                "-DCMAKE_CXX_STANDARD=11",
                "-DCMAKE_CXX_STANDARD_REQUIRED=ON",
            )
            cmake("--build", "build")

            Executable("./build/test_lyra")()
