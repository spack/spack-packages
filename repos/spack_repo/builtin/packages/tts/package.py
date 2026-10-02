# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Tts(CMakePackage):
    """TTS - Tiny Test System, a C++20 unit test library for numerical code."""

    homepage = "https://jfalcou.github.io/tts/"
    url = "https://github.com/jfalcou/tts/archive/refs/tags/3.0.tar.gz"
    git = "https://github.com/jfalcou/tts.git"

    maintainers("jfalcou")

    license("BSL-1.0")

    version("main", branch="main")
    version("3.0", sha256="3954fb40a2d444bc935ecf2d439ed72d3c72eae9ec1b021fc99b469166bf57cd")

    depends_on("cxx", type="build")
    depends_on("cmake@3.22:", type="build")
    # The build is written with copacabana, which CPM fetches at configure time; the
    # prefix installed here is handed to CPM instead, see cmake_args.
    depends_on("copacabana", type="build")

    def cmake_args(self):
        return [
            self.define("CPM_COPACABANA_SOURCE", self.spec["copacabana"].prefix),
            self.define("CPM_LOCAL_PACKAGES_ONLY", True),
            self.define("TTS_BUILD_TEST", self.run_tests),
            self.define("TTS_BUILD_DOCUMENTATION", False),
        ]

    def check(self):
        # `all` builds nothing in a header-only library; the unit tests hang off the
        # aggregate target copacabana defines for the project.
        with working_dir(self.build_directory):
            cmake("--build", ".", "--target", "tts-test", "--parallel", str(make_jobs))
            ctest("--output-on-failure", "--parallel", str(make_jobs))
