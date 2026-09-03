# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Kumi(CMakePackage):
    """KUMI - C++20 Tuple & Tuple-base Algorithms Library."""

    homepage = "https://jfalcou.github.io/kumi/"
    url = "https://github.com/jfalcou/kumi/archive/refs/tags/v4.0.tar.gz"
    maintainers("jfalcou")
    git = "https://github.com/jfalcou/kumi.git"

    license("BSL-1.0")

    version("main", branch="main")
    version("4.0", sha256="f788ee60b814a07d2b2148dd86b5153261b582ac5a248905cbf3e19423a0f7cd")
    version("3.1", sha256="2c1c07e22ec6687d338dfb3f0586e9af186c00af047b496708401d2fce68e7b8")
    version("3.0", sha256="166b621e475935d2a3a195d13937a285060812c1fd7a95575a9c7b1dc425f2a1")
    version("2.1", sha256="34fc756780d463db35716e40eecd89b1505917926281262c74af425556a5260c")
    version("2.0", sha256="c9f2d2014d3513c57db4457c5a678c7adce1fa9bd061ee008847876f06dac355")
    version("1.0", sha256="d28be244e326b1c9f1651b47728af74bb6be80a7accd39f07441a246d49220f5")

    depends_on("cxx", type="build")  # generated
    depends_on("cmake@3.22:", type="build", when="@3.1:")
    depends_on("cmake@3.28:", type="build", when="@4.0:")
    # Since 3.1 the build is written with copacabana, which CPM fetches at configure
    # time; the prefix installed here is handed to CPM instead, see cmake_args.
    depends_on("copacabana", type="build", when="@3.1:")
    depends_on("tts", type="test", when="@3.1:")

    def cmake_args(self):
        args = [self.define("KUMI_BUILD_TEST", self.run_tests)]
        if self.spec.satisfies("@3.1:"):
            args += [
                self.define("CPM_COPACABANA_SOURCE", self.spec["copacabana"].prefix),
                self.define("CPM_LOCAL_PACKAGES_ONLY", True),
                self.define("KUMI_BUILD_DOCUMENTATION", False),
            ]
        return args

    def check(self):
        # `all` builds nothing in a header-only library; the unit tests hang off the
        # aggregate target copacabana defines for the project.
        with working_dir(self.build_directory):
            cmake("--build", ".", "--target", "kumi-test", "--parallel", str(make_jobs))
            ctest("--output-on-failure", "--parallel", str(make_jobs))
