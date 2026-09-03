# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Raberu(CMakePackage):
    """RABERU - a C++20 library for named, typed and defaulted keyword arguments."""

    homepage = "https://jfalcou.github.io/raberu/"
    url = "https://github.com/jfalcou/raberu/archive/refs/tags/v1.1.tar.gz"
    git = "https://github.com/jfalcou/raberu.git"

    maintainers("jfalcou")

    license("BSL-1.0")

    version("main", branch="main")
    version("1.1", sha256="48a16761ba27493544b48c3550dc306c015443a0d12d725d73bf148ee97a49d8")

    depends_on("cxx", type="build")
    depends_on("cmake@3.12:", type="build")
    depends_on("cmake@3.22:", type="build", when="@main")
    # On main the build is written with copacabana, which CPM fetches at configure time;
    # the prefix installed here is handed to CPM instead, see cmake_args.
    depends_on("copacabana", type="build", when="@main")
    depends_on("tts", type="test", when="@main")

    def patch(self):
        if self.spec.satisfies("@1.1"):
            # The 1.1 tarball ships a single include/raberu.hpp; its install rule names
            # the include/raberu directory that only later versions have.
            filter_file(
                "install(DIRECTORY ${PROJECT_SOURCE_DIR}/include/raberu TYPE INCLUDE)",
                "install(FILES ${PROJECT_SOURCE_DIR}/include/raberu.hpp TYPE INCLUDE)",
                "CMakeLists.txt",
                string=True,
            )

    def cmake_args(self):
        args = [
            # The 1.1 test suite fetches TTS itself at configure time, so only main runs it.
            self.define("RABERU_BUILD_TEST", self.run_tests and self.spec.satisfies("@main")),
        ]
        if self.spec.satisfies("@main"):
            args += [
                self.define("CPM_COPACABANA_SOURCE", self.spec["copacabana"].prefix),
                self.define("CPM_LOCAL_PACKAGES_ONLY", True),
                self.define("RABERU_BUILD_DOCUMENTATION", False),
            ]
        return args

    def check(self):
        # `all` builds nothing in a header-only library; the unit tests hang off the
        # aggregate target copacabana defines for the project.
        if self.spec.satisfies("@1.1"):
            return
        with working_dir(self.build_directory):
            cmake("--build", ".", "--target", "raberu-test", "--parallel", str(make_jobs))
            ctest("--output-on-failure", "--parallel", str(make_jobs))
