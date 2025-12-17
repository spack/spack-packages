# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTy(PythonPackage):
    """An extremely fast Python type checker, written in Rust."""

    homepage = "https://github.com/astral-sh/ty/"
    pypi = "ty/ty-0.0.1a29.tar.gz"

    license("MIT")
    maintainers("adamjstewart")

    version("0.0.2", sha256="e02dc50b65dc58d6cb8e8b0d563833f81bf03ed8a7d0b15c6396d486489a7e1d")
    version(
        "0.0.1a29",
        sha256="43bb55fd467a057880d62ad4bbb048223fd4fba7d8e4d7d5372a0f4881da83fe",
        deprecated=True,
    )

    # ruff/Cargo.toml
    depends_on("rust@1.90:", when="@0.0.2:")
    depends_on("rust@1.89:")

    depends_on("py-maturin@1", type="build")
