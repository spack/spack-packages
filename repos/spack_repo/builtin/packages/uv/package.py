# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import re

from spack_repo.builtin.build_systems.cargo import CargoPackage

from spack.package import *


class Uv(CargoPackage):
    """An extremely fast Python package and project manager, written in Rust."""

    homepage = "https://docs.astral.sh/uv/"
    url = "https://github.com/astral-sh/uv/archive/refs/tags/0.11.19.tar.gz"
    supplier = "Organization: Astral"

    maintainers("mcmehrtens")
    license("Apache-2.0 OR MIT", checked_by="mcmehrtens", when="@0.0.5:")

    version("0.11.19", sha256="316a5fb9fca079064265a8007979e0057b68317b6a6693e15554d3d9112cce9c")

    executables = ["^uv$"]

    variant(
        "performance",
        default=True,
        description="Build with the high-performance jemalloc/mimalloc memory allocator",
    )

    depends_on("rust@1.94:", type="build")
    # C compiler needed for Cargo dependencies
    depends_on("c", type="build")
    # tikv-jemalloc-sys builds bundled jemalloc with `./configure && make`
    depends_on("gmake", type="build", when="+performance")

    build_directory = "crates/uv"

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
        uv = Executable(self.prefix.bin.uv)
        out = uv("--version", output=str, error=str)
        assert self.spec.version.string in out
