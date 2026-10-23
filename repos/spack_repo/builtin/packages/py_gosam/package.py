# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.meson import MesonPackage
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyGosam(MesonPackage, PythonPackage):
    """The package GoSam allows for the automated calculation of
    one-loop amplitudes for multi-particle processes in renormalizable
    quantum field theories."""

    homepage = "https://github.com/gudrunhe/gosam"
    git = "https://github.com/gudrunhe/gosam.git"

    tags = ["hep"]

    extends("python")

    license("GPL-3.0-only")

    version(
        "3.0.3",
        url="https://github.com/gudrunhe/gosam/releases/download/v3.0.3/GoSam-3.0.3-e5cfdb6.tar.xz",
        sha256="da0a9fc713536451785282c48e157eb67852949cafe63f9a6c75d9c303662ccd",
    )
    version(
        "2.1.2",
        url="https://github.com/gudrunhe/gosam/releases/download/2.1.2/gosam-2.1.2+c307997.tar.gz",
        sha256="53601ab203c3d572764439018f976baff9c83b87abe1fcbbe15c07caf174680c",
    )
    version(
        "2.1.1",
        url="https://github.com/gudrunhe/gosam/releases/download/2.1.1/gosam-2.1.1-4b98559.tar.gz",
        sha256="4a2b9160d51e3532025b9579a4d17d0e0f8a755b8481aeb8271c1f58eb97ab01",
    )

    build_system(
        conditional("meson", when="@3:"),
        conditional("python_pip", when="@:2"),
        default="meson",
    )

    resource(
        name="avh-olo",
        url="https://bitbucket.org/hameren/oneloop/get/v3.7.2.tar.gz",
        sha256="d4efd039292f95ff150dadcd428163d643c6e48c97388eee4a753e57fa002db5",
        placement="subprojects/avh_olo",
        when="@3:",
    )
    resource(
        name="ninja-integral-reduction",
        url="https://github.com/peraro/ninja/releases/download/v1.2.0/ninja-latest.tar.gz",
        sha256="8907b22454f96fea3ebeeb85f8c17c0d0cc21c281c1b6603f16c7b1583226a62",
        placement="subprojects/ninja-1.2.0",
        when="@3:",
    )
    resource(
        name="form",
        url="https://github.com/vermaseren/form/releases/download/v4.2.1/form-4.2.1.tar.gz",
        sha256="f2722d6d4ccb034e01cf786d55342e1c21ff55b182a4825adf05d50702ab1a28",
        placement="subprojects/form-4.2.1",
        when="@3:",
    )

    patch("gosam-v3-build.patch", when="@3:")
    patch(
        "https://raw.githubusercontent.com/gudrunhe/gosam/v3.0.3/subprojects/packagefiles/avh_olo/create.py.patch",
        sha256="0a2ae9dd3138c29b1dc37cde2f2d99a569965a0f99e438151789167044d73137",
        working_dir="subprojects/avh_olo",
        when="@3:",
    )

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    depends_on("meson@1.4:", type="build", when="@3:")
    depends_on("ninja", type="build", when="@3:")
    depends_on("python@3.9:", type=("build", "run"), when="@3:")

    depends_on("form", type="run", when="@:2")
    depends_on("qgraf", type="run", when="@:2")
    depends_on("gosam-contrib", type="link", when="@:2")
    depends_on("python@3:", type=("build", "run"), when="@:2")
    depends_on("py-setuptools", type="build", when="@:2")

    @run_before("meson")
    def add_v3_subproject_build_files(self):
        for source, destination in (
            ("avh_olo", "avh_olo"),
            ("ninja", "ninja-1.2.0"),
            ("form", "form-4.2.1"),
        ):
            copy_tree(
                join_path("subprojects", "packagefiles", source),
                join_path("subprojects", destination),
            )

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        if self.spec.satisfies("@:2"):
            gosam_contrib_lib_dir = self.spec["gosam-contrib"].prefix.lib
            env.prepend_path("LD_LIBRARY_PATH", gosam_contrib_lib_dir)
