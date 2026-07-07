# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Hammer(CMakePackage):
    """HAMMER — Helicity Amplitude Module for Matrix Element Reweighting.

    A tool for reweighting Monte Carlo simulations for semileptonic B-decays.
    """

    homepage = "https://hammer.physics.lbl.gov"
    url = "https://hammer.physics.lbl.gov/Hammer-1.4.1-Source.tar.gz"
    git = "https://gitlab.com/mpapucci/Hammer.git"

    maintainers("wdconinc")

    license("GPL-3.0", checked_by="wdconinc")

    version("1.4.1", sha256="0d225a7fd3ff0dea25532cb3fceaa38e27ce338eae6d17c65db519f8d2fe28cd")

    variant("root", default=False, description="Build with ROOT support")
    variant("python", default=True, description="Build with Python bindings")
    variant("examples", default=False, description="Install and build Hammer examples")

    depends_on("cxx", type="build")
    depends_on("cmake@3.2:3", type="build")  # @:3 for use of TestEndianess.c.in

    depends_on("boost@1.50: +thread")
    depends_on("yaml-cpp@0.6:")

    depends_on("root", when="+root")
    depends_on("python", when="+python")
    depends_on("hepmc3", when="+examples")

    def cmake_args(self):
        return [
            self.define("BUILD_SHARED_LIBS", True),
            self.define("BUILD_DOCUMENTATION", False),
            self.define("ENABLE_TESTS", self.run_tests),
            self.define("INSTALL_EXTERNAL_DEPENDENCIES", False),
            self.define_from_variant("WITH_ROOT", "root"),
            self.define_from_variant("WITH_PYTHON", "python"),
            self.define_from_variant("WITH_EXAMPLES", "examples"),
            self.define_from_variant("WITH_EXAMPLES_EXTRA", "examples"),
        ]
