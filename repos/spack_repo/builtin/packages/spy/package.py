# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Spy(CMakePackage):
    """SPY - C++20 compile-time detection of compilers, operating systems, architectures
    and SIMD extensions."""

    homepage = "https://jfalcou.github.io/spy/"
    url = "https://github.com/jfalcou/spy/archive/refs/tags/2.0.0.tar.gz"
    git = "https://github.com/jfalcou/spy.git"

    maintainers("jfalcou")

    license("BSL-1.0")

    version("main", branch="main")
    version("2.0.0", sha256="a2ab9dc30356defa319f104f4e180b08438dbea0e904864510c532b1299b7fff")

    depends_on("cxx", type="build")
    depends_on("cmake@3.22:", type="build")
    # The build is written with copacabana, which CPM fetches at configure time; the
    # prefix installed here is handed to CPM instead, see cmake_args.
    depends_on("copacabana", type="build")

    def cmake_args(self):
        return [
            self.define("CPM_COPACABANA_SOURCE", self.spec["copacabana"].prefix),
            self.define("CPM_LOCAL_PACKAGES_ONLY", True),
            self.define("SPY_BUILD_TEST", self.run_tests),
            self.define("SPY_BUILD_DOCUMENTATION", False),
        ]

    def check(self):
        # `all` builds nothing in a header-only library; the unit tests hang off the
        # aggregate target copacabana defines for the project.
        with working_dir(self.build_directory):
            cmake("--build", ".", "--target", "spy-test", "--parallel", str(make_jobs))
            ctest("--output-on-failure", "--parallel", str(make_jobs))
