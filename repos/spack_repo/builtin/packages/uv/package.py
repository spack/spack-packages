# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import re

from spack_repo.builtin.build_systems.cargo import CargoPackage
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class Uv(PythonPackage, CargoPackage):
    """An extremely fast Python package and project manager, written in Rust."""

    homepage = "https://docs.astral.sh/uv/"
    url = "https://github.com/astral-sh/uv/archive/refs/tags/0.11.19.tar.gz"
    supplier = "Organization: Astral"

    maintainers("mcmehrtens", "johnwparent", "adamjstewart")
    license("Apache-2.0 OR MIT", checked_by="mcmehrtens")

    version("0.11.24", sha256="0f1700c98068b9238544102fb9c4106352201f844b935b74947acd8cdb13b568")
    version("0.11.23", sha256="8bbb236ae5ab7fc72261d600f79f8efd0e306acb130669371d7c11db5eb6747b")
    version("0.11.22", sha256="315cb03d1b293bc78ac6a8c1124cf4be6877509ae75a1ee25dc120ff292338b4")
    version("0.11.21", sha256="12316609d3cd474a67d9b7e08991db7ec19390395ba03f56e79d39c6afbb723a")
    version("0.11.20", sha256="18146330b729dded1cbccc739eb15f9d4750dd226913afa00f2638dd5dfa4e48")
    version("0.11.19", sha256="316a5fb9fca079064265a8007979e0057b68317b6a6693e15554d3d9112cce9c")

    executables = ["^uv$"]

    # PythonPackage builds via maturin and preserves the `python -m uv` entry point;
    # CargoPackage builds the bare Rust binary as an alternative
    build_system("python_pip", "cargo", default="python_pip")

    variant(
        "performance",
        default=True,
        description="Build with the high-performance jemalloc/mimalloc memory allocator",
        when="build_system=cargo",
    )

    # Both build systems compile the Rust sources (maturin shells out to cargo),
    # and the bundled `-sys` crates need a C compiler
    depends_on("rust@1.94:", type="build")
    depends_on("c", type="build")

    with when("build_system=python_pip"):
        depends_on("py-maturin@1", type="build")
        # tikv-jemalloc-sys builds bundled jemalloc with `./configure && make`
        depends_on("gmake", type="build")

    with when("build_system=cargo"):
        depends_on("gmake", type="build", when="+performance")

    @property
    def build_directory(self):
        # The maturin manifest at the repo root drives the Python build; the bare
        # Cargo build targets the `uv` binary crate directly.
        if self.spec.satisfies("build_system=cargo"):
            return "crates/uv"
        return self.stage.source_path

    @property
    def build_args(self):
        # uv's default features include network-dependent `test-*` gates; so,
        # we drop them with --no-default-features and then re-enable only the
        # features we want
        features = ["uv-distribution/static"]
        if self.spec.satisfies("+performance"):
            features.append("performance")
        return ["--locked", "--no-default-features", "--features", ",".join(features)]

    @classmethod
    def determine_version(cls, exe):
        output = Executable(exe)("--version", output=str, error=str)
        match = re.match(r"uv (\S+)", output)
        return match.group(1) if match else None

    def test_version(self):
        """Verify uv executable outputs version"""
        uv = Executable(self.prefix.bin.uv)
        out = uv("--version", output=str, error=str)
        assert self.spec.version.string in out
