# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cargo import CargoPackage
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class Ruff(CargoPackage, PythonPackage):
    """An extremely fast Python linter and code formatter, written in Rust."""

    homepage = "https://docs.astral.sh/ruff"
    git = "https://github.com/astral-sh/ruff.git"
    url = "https://github.com/astral-sh/ruff/archive/refs/tags/0.11.11.tar.gz"

    license("MIT")
    maintainers("adamjstewart")

    build_directory = "crates/ruff"

    version(
        "0.15.10", sha256="42f72c865e0484f490cce86441df2207f38f8da6334013c859c5840f0e69c395"
    )  # FIXME
    version("0.15.7", sha256="370003574c8bde1eef286ece925f33e43be4d3564c8eca8dfb4fb100a1dce797")
    version("0.14.14", sha256="6a6a952a0b273df14eadd4e5a61a48fcc02fa268d2b258062bf332e6b53d4090")
    version("0.13.0", sha256="1be5402b5ca6925725fcb73af70a07b515246009d7bbb14f17e7f5adacd8a307")
    version("0.12.0", sha256="3623e20815ae84254ca5dec780165e89c2f1947c73824167e3a44d41fde74f57")
    version("0.11.11", sha256="fcd8fdd349559421494b653e53a2fc6441a35e51d2992af035c5e5c84e060702")

    variant("python", default=False, description="Build and install ruff as a wheel")

    build_system("cargo", conditional("python_pip", when="+python"), default="cargo")

    with when("+python"):
        build_system("python_pip")
        depends_on("py-maturin@1.9:1", when="@0.12.7:", type="build")
        depends_on("py-maturin@1", type="build")

    with default_args(type="build"):
        depends_on("c")
        depends_on("gmake")

        # Found in Cargo.toml
        depends_on("rust@1.91:", when="@0.15.0:")
        depends_on("rust@1.90:", when="@0.14.10:")
        depends_on("rust@1.89:", when="@0.14.4:")
        depends_on("rust@1.88:", when="@0.12.0:")
        depends_on("rust@1.85:", when="@0.11.11:")
        depends_on("rust@1.84:", when="@0.11.4:")
