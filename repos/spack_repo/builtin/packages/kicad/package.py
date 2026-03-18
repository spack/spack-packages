# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.packages.boost.package import Boost

from spack.package import *


class Kicad(CMakePackage):
    """KiCad is an open source software suite for Electronic Design
    Automation (EDA). The programs handle Schematic Capture, and PCB
    Layout with Gerber output."""

    homepage = "https://kicad.org"
    url = "https://gitlab.com/kicad/code/kicad/-/archive/5.1.8/kicad-5.1.8.tar.gz"
    maintainers("aweits")

    license("GPL-3.0-or-later")

    version("7.0.2", sha256="8df56648226061c91ddd1d2ca970c66190fc70c7ace23c99cc28c209713e4dfc")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("wxwidgets")
    depends_on("python@3:", type=("build", "run"))
    # py-wxpython needs work
    # depends_on('py-wxpython', type=('build', 'run'))
    depends_on("glew")
    depends_on("gl")
    depends_on("glm")
    depends_on("boost@1.56:")

    # TODO: replace this with an explicit list of components of Boost,
    # for instance depends_on('boost +filesystem')
    # See https://github.com/spack/spack/pull/22303 for reference
    depends_on(Boost.with_default_variants)
    depends_on("opencascade")
    depends_on("unixodbc")
    depends_on("swig", type="build")
    depends_on("curl")
    depends_on("pkgconfig")
    depends_on("git", type=("build", "run"))
    depends_on("ngspice")
    depends_on("hicolor-icon-theme", type=("build", "run"))
    depends_on("adwaita-icon-theme", type=("build", "run"))
    depends_on("gsettings-desktop-schemas", type=("build", "run"))

    extends("python")

    resource_list = [
        # version, resource, sha256sum
        (
            "7.0.2",
            "footprints",
            "81ba4e1a48a4a741e3860d2e6b305a1002aea41c9ce168db13f9c7650198e374",
        ),
        (
            "7.0.2",
            "packages3D",
            "a436414b9466db3aacfbe3efedfc784bcec2d2839789234fc65414069a9e470d",
        ),
        ("7.0.2", "symbols", "d0f9aed81172e14da899d90e2ead6ef8c4d515da3a3847a26bab22db4a7e4528"),
        ("7.0.2", "templates", "2ca6de284aa6d1567173d3d5ef10bb7f416cc919b7a9cae438ebb36ced15df74"),
    ]

    for ver, lib, checksum in resource_list:
        resource(
            when="@{0}".format(ver),
            name=lib,
            url="https://gitlab.com/kicad/libraries/kicad-{0}/-/archive/{1}/kicad-{0}-{1}.tar.bz2".format(
                lib, ver
            ),
            sha256=checksum,
            destination="",
        )

    def setup_dependent_build_environment(
        self, env: EnvironmentModifications, dependent_spec: Spec
    ) -> None:
        env.prepend_path("XDG_DATA_DIRS", self.prefix.share)

    def setup_dependent_run_environment(
        self, env: EnvironmentModifications, dependent_spec: Spec
    ) -> None:
        env.prepend_path("XDG_DATA_DIRS", self.prefix.share)

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.prepend_path("XDG_DATA_DIRS", self.prefix.share)

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        env.prepend_path("XDG_DATA_DIRS", self.prefix.share)

    def cmake_args(self):
        args = []
        args.append("-DKICAD_SCRIPTING_PYTHON3=ON")
        args.append("-DKICAD_SCRIPTING_WXPYTHON=OFF")
        if self.spec.satisfies("^opencascade"):
            args.append(
                "-DOCC_INCLUDE_DIR={0}".format(self.spec["opencascade"].prefix.include.opencascade)
            )
        return args

    @run_after("install")
    def install_libraries(self):
        for ver, lib, checksum in self.resource_list:
            if self.spec.version == Version(ver):
                with working_dir("kicad-{0}-{1}".format(lib, ver)):
                    cmake(*self.std_cmake_args)
                    make("install")
