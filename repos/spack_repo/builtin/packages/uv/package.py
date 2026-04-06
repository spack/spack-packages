# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cargo import CargoPackage
from spack_repo.builtin.build_system.python import PythonPackage

from spack.package import *


class Uv(CargoPackage, PythonPackage):
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

    variant("python", default=False, description="Build and install ruff as a wheel")

    build_system("cargo", conditional("python_pip", when="+python"), default="cargo")

    with when("+python"):
        build_system("python_pip")
        depends_on("python@3.8:", type=("build", "run"))
        depends_on("py-maturin@1", type="build")

    with default_args(type="build"):
        depends_on("c")
        depends_on("gmake")

        # from Cargo.toml
        depends_on("rust@1.92:", when="@0.10.12:")
        depends_on("rust@1.91:", when="@0.10.7:")
        depends_on("rust@1.88:", when="@0.7.22:")
