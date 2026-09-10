# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class UnitsLlnl(CMakePackage):
    """A C++ library for handling physical units and conversions between them."""

    homepage = "https://github.com/LLNL/units"
    git = "https://github.com/LLNL/units.git"

    maintainers("phlptp")

    license("BSD-3-Clause", checked_by="cmelone")

    version("main", branch="main")

    variant("shared", default=False, description="Build shared instead of static library")
    variant("header_only", default=False, description="Expose the units library as header-only")
    variant("converter", default=True, description="Build a unit converter app")
    variant("non_english", default=True, description="Enable non-English unit names")
    variant("extra_standards", default=True, description="Enable extra unit standards (X12, R20)")

    depends_on("cmake@3.22:", type="build")
    depends_on("c", type="build")
    depends_on("cxx", type="build")

    def cmake_args(self):
        args = [
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define_from_variant("UNITS_HEADER_ONLY", "header_only"),
            self.define_from_variant("UNITS_BUILD_CONVERTER_APP", "converter"),
            self.define(
                "UNITS_DISABLE_NON_ENGLISH_UNITS", not self.spec.satisfies("+non_english")
            ),
            self.define(
                "UNITS_DISABLE_EXTRA_UNIT_STANDARDS", not self.spec.satisfies("+extra_standards")
            ),
            self.define("UNITS_ENABLE_TESTS", self.run_tests),
        ]
        return args
