# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Cppcheck(CMakePackage):
    """A tool for static C/C++ code analysis."""

    homepage = "https://cppcheck.sourceforge.net/"
    url = "https://github.com/danmar/cppcheck/archive/2.17.0.tar.gz"

    maintainers("white238")

    license("GPL-3.0-or-later")

    version("2.18.0", sha256="dc74e300ac59f2ef9f9c05c21d48ae4c8dd1ce17f08914dd30c738ff482e748f")
    version("2.17.1", sha256="bfd681868248ec03855ca7c2aea7bcb1f39b8b18860d76aec805a92a967b966c")

    variant("rules", default=False, description="Enable rules (requires PCRE)")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("pcre", when="+rules", type="build")
    depends_on("py-pygments", type="run")
    extends("python")

    def cmake_args(self):
        return [
            self.define("BUILD_TESTS", self.run_tests),
            self.define_from_variant("HAVE_RULES", "rules"),
        ]
