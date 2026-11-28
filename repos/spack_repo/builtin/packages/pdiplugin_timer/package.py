# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *

from ..pdi.package import Pdi


class PdipluginTimer(CMakePackage):
    """The timer plugin for the PDI library measures the time spent by PDI and
    its plugins, between user-defined start and stop events."""

    homepage = "https://pdi.dev"
    git = "https://github.com/pdidev/pdi.git"
    url = "https://github.com/pdidev/pdi/archive/refs/tags/1.12.0.tar.gz"

    license("BSD-3-Clause")

    maintainers("jbigot")

    for v in Pdi.versions:
        if v >= Version("1.12.0"):
            version(str(v), **Pdi.versions[v])

    variant("tests", default=False, description="Build tests")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("cmake@3.22.1:", type=("build"))
    # @= (an exact version) only exists from spack 0.20 on
    exact = "@="
    for v in Pdi.versions:
        if v >= Version("1.12.0"):
            depends_on("pdi" + exact + str(v), type=("link", "run"), when=exact + str(v))
    depends_on("pkgconfig", type=("build"))

    root_cmakelists_dir = "plugins/timer"

    def cmake_args(self):
        return [
            "-DINSTALL_PDIPLUGINDIR:PATH={:s}".format(self.prefix.lib),
            self.define_from_variant("BUILD_TESTING", "tests"),
        ]

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        env.prepend_path("PDI_PLUGIN_PATH", self.prefix.lib)
