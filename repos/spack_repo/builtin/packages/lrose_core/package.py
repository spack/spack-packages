# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class LroseCore(CMakePackage):
    """The overall goal of the project is to provide high-quality, open source
    software to the community of scientists, researchers, educators, and
    operational organizations using atmospheric lidars, radars, and
    profilers."""

    homepage = "https://www.eol.ucar.edu/content/lidar-radar-open-software-environment"
    url = "https://github.com/NCAR/lrose-core/archive/lrose-core-20250105.tar.gz"
    git = "https://github.com/NCAR/lrose-core.git"

    maintainers("vanderwb")

    license("Apache-2.0")

    version("20250811", sha256="e53995e4291c536d7d310d4c84793e414c732428c1b177c841ea6813e36bd9ba")
    version("20250105", sha256="c91938a1fa022359d2cd3c447a1ea777c70d456344967db768b3b0d2a08bd53b")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    variant("fractl", default=True, description="Install fractl applications")
    variant("samurai", default=True, description="Install samurai applications")
    variant("vortrac", default=False, description="Install vortrac applications")

    depends_on("cmake@3.7:", type="build")
    depends_on("libx11")
    depends_on("netcdf-c")
    depends_on("qt@5:")
    depends_on("fftw@3:")

    depends_on("armadillo", when="+vortrac")

    root_cmakelists_dir = "codebase"

    resource(name="lrose-displays", git="https://github.com/NCAR/lrose-displays", branch="master")

    resource(
        name="fractl", git="https://github.com/mmbell/fractl", branch="master", when="+fractl"
    )

    resource(
        name="samurai", git="https://github.com/mmbell/samurai", branch="master", when="+samurai"
    )

    resource(
        name="vortrac", git="https://github.com/mmbell/vortrac", branch="master", when="+vortrac"
    )

    def build_and_install_extra_utility(self, component):
        with working_dir(f"spack-build-{component}", create=True):
            cmake_args = [f"../{component}"] + self.std_cmake_args
            cmake_args.append("-DLROSE_PREFIX=" + self.spec.prefix)
            cmake(*cmake_args)
            make()
            make("install")

    @run_after("install")
    def add_extra_components(self):
        # These components are optional add-ons but are included by default in RPM releases
        for component in ("fractl", "samurai", "vortrac"):
            if self.spec.satisfies(f"+{component}"):
                self.build_and_install_extra_utility(component)

        # The CMake install does not install these components, and the color_scales needed by
        # HawkEye do not come with the source code at all!
        prefix = self.prefix
        install_tree("docs", "{}/docs".format(prefix))
        install_tree("release_notes", "{}/release_notes".format(prefix))
        install_tree("lrose-displays/color_scales", "{}/share/color_scales".format(prefix))
