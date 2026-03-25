# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cargo import CargoPackage

from spack.package import *


class Uv(CargoPackage):
    """An extremely fast Python package and project manager, written in Rust."""

    homepage = "https://github.com/astral-sh/uv"
    git = "https://github.com/astral-sh/uv.git"
    url = "https://github.com/astral-sh/uv/archive/refs/tags/0.11.0.tar.gz"

    license("MIT OR Apache-2.0")
    maintainers("johnwparent", "adamjstewart")

    build_directory = "crates/uv"

    executables = ["^uv$"]

    version("0.11.0", sha256="d61c168d4a3b0dad3c2c2a73c591fe7a2bbad96ea5a5e15f857d03308e15ca50")
    version("0.10.12", sha256="73c256e80ac1b6e030aeb0643a80d84c32f327fbe09450ff39069103503f46c9")
    version("0.9.30", sha256="c89f7d66c6aa8324e14f6b07b35af64e37368d6cb4e2b93d8bb7fdd2159f78f6")
    version("0.8.24", sha256="33f4ad5c8fe980e35c2eb79d9d3bfbada3d1a1ef63f0aa7c8ce0d3affce79617")

    with default_args(type="build"):
        depends_on("c")

        # from Cargo.toml
        depends_on("rust@1.92:", when="@0.10.12:")
        depends_on("rust@1.91:", when="@0.10.7:")
        depends_on("rust@1.88:", when="@0.7.22:")
        depends_on("rust@1.86:", when="@0.7.16:")
        depends_on("rust@1.85:", when="@0.7.6:")
        depends_on("rust@1.84:", when="@0.6.13:")
        depends_on("rust@1.83:", when="@0.5.9:")
        depends_on("rust@1.81:")

        depends_on("gmake")

        # Historical dependencies
        depends_on("cmake", when="@:0.6.3")

    @when("@:0.6.3")
    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.set("CMAKE", self.spec["cmake"].prefix.bin.cmake)
