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

    version("0.0.13", sha256="7a1d135a400ca076407ea30012d1f75419634160ed3b9cad96607bf2956b23b3")
    version("0.0.12", sha256="cd01810e106c3b652a01b8f784dd21741de9fdc47bd595d02c122a7d5cefeee7")
    version("0.0.11", sha256="ebcbc7d646847cb6610de1da4ffc849d8b800e29fd1e9ebb81ba8f3fbac88c25")
    version("0.0.10", sha256="0a1f9f7577e56cd508a8f93d0be2a502fdf33de6a7d65a328a4c80b784f4ac5f")
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
