# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import re

from spack_repo.builtin.build_systems.cargo import CargoPackage

from spack.package import *


class AstGrep(CargoPackage):
    """ast-grep(sg) is a CLI tool for code structural search, lint, and rewriting."""

    homepage = "https://ast-grep.github.io"
    url = "https://github.com/ast-grep/ast-grep/archive/refs/tags/0.43.0.tar.gz"
    git = "https://github.com/ast-grep/ast-grep.git"
    supplier = "Organization: ast-grep"

    executables = ["^ast-grep$"]

    maintainers("mcmehrtens")

    license("MIT", checked_by="mcmehrtens")

    version("main", branch="main")
    version("0.44.0", sha256="1cc8d5d6a759c6d99c676bcec09fbf1fc72e023804e54480146fd62b300fce95")
    version("0.43.0", sha256="1fb6c32a5ae96254d54df7c4358f664e5c6bebdd7754c8b9a3a7db079fe4d525")

    # https://github.com/ast-grep/ast-grep/blob/0.44.0/Cargo.toml#L20
    depends_on("rust@1.85:", type="build", when="@0.44:")
    # https://github.com/ast-grep/ast-grep/blob/0.43.0/Cargo.toml#L20
    depends_on("rust@1.79:", type="build", when="@0.43")

    # The default "builtin-parser" feature pulls in tree-sitter-* grammar
    # crates, whose build.rs each compile C parsers via the cc crate:
    # https://github.com/ast-grep/ast-grep/blob/0.43.0/crates/language/Cargo.toml#L48-L84
    # e.g. https://docs.rs/crate/tree-sitter-rust/0.24.2/source/bindings/rust/build.rs
    depends_on("c", type="build", when="@0.43:")

    build_directory = "crates/cli"

    build_args = ["--locked"]

    @classmethod
    def determine_version(cls, exe):
        output = Executable(exe)("--version", output=str, error=str)
        match = re.search(r"ast-grep ([0-9.]+)", output)
        return match.group(1) if match else None

    def test_version(self):
        """Check ast-grep can run and report its version."""
        ast_grep = which(self.prefix.bin.join("ast-grep"))
        out = ast_grep("--version", output=str.split, error=str.split)
        assert str(self.spec.version) in out
