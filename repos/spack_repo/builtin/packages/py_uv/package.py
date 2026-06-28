# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import re

from spack_repo.builtin.build_systems.cargo import CargoPackage
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyUv(PythonPackage, CargoPackage):
    """An extremely fast Python package and project manager, written in Rust."""

    homepage = "https://github.com/astral-sh/uv"
    pypi = "uv/uv-0.10.1.tar.gz"
    supplier = "Organization: Astral"

    license("Apache-2.0 OR MIT", checked_by="mcmehrtens")
    maintainers("adamjstewart", "mcmehrtens")

    executables = ["^uv$"]

    version("0.11.25", sha256="458e731778e7b5cc870710397859c23e766703e7bc0695f23b3eb15080745ba6")
    version("0.11.24", sha256="8602a1b6300a3a948afacc62e1cb933c8394c27966db85ed7e29483300b69dc4")
    version("0.11.23", sha256="f2476dda35866ea3ded3a5905759da2d32dfac36dfd5b3428191a99a8ce15b02")
    version("0.11.22", sha256="32e31cb70bada3ad03d99614ead365cd36b2ac9455a6fc232f6d50b619a964e1")
    version("0.11.21", sha256="083882c73373a16de4c136d54e3386a52388dead5048a07505e25578b157182f")
    version("0.11.20", sha256="a246f30931cbc93d0a39d0cfc75be045fddd45773a734ddf8afa869aabc46c63")
    version("0.11.19", sha256="f56f5bf853626a30423052d7ee00bf5cc940a08347d6ee7ede96862d084054a5")
    version("0.11.18", sha256="61f2bc99898383f9bf04e24b984e42e19cde378dd79192935ca21d75563368a8")
    version("0.11.17", sha256="1d1be74deec997db1dda05a7e67541c904d65cbfd72e455d3c0a2a1e4bf2cddf")
    version("0.11.16", sha256="4b435fcb0af8f34833dcc1903a8a223856437efd0d515c2160a2871def221238")
    version("0.11.15", sha256="755f959ec6a2fd8ccb6ee76ad90ab759d2eb1f4797444078645dd1ee4bca92d6")
    version("0.11.14", sha256="0ea006a117b586b2681b6dfd9703a540d2ad2a136ec0f48d272767e599cc3dfb")
    version("0.11.13", sha256="c30889b6a4417f94a0315371ec5bf8af151f062406ad3fb4b2cbf13d645d825c")
    version("0.11.12", sha256="2d85d1fe06bafddf9632ec5c8ac24f86bd6eb7ec21e650be8c3565b600b502c9")
    version("0.11.11", sha256="2ba46a912a1775957c579a1a42c8c8b480418502326b72427b1cad972c8f659f")
    version("0.11.10", sha256="9b3a2ce56c4a22065462473acee0b729140370650974de4e781a5273f49371fa")
    version("0.11.9", sha256="43edb4b3eb43a9780f9232110dfbcc0bed9367ce5b24d37a315817d3faf3c913")
    version("0.11.8", sha256="bb2cf302b8503629aab6f0090a05551e6f8cfc2d687ca059cad7ec9e11214335")
    version("0.11.7", sha256="46d971489b00bdb27e0aa715e4a5cd4ef2c28ea5b6ef78f2b67bf861eb44b405")
    version("0.11.6", sha256="e3b21b7e80024c95ff339fcd147ac6fc3dd98d3613c9d45d3a1f4fd1057f127b")
    version("0.10.1", sha256="c89e7fd708fb3474332d6fc54beb2ea48313ebdc82c6931df92a884fcb636d9d")
    with default_args(deprecated=True):
        # https://www.cvedetails.com/cve/CVE-2025-13327/
        version(
            "0.7.22", sha256="f5cf159907d594e33433f14737d1ee843dc8799edfcf57b5b8c0f282d1117051"
        )
        version(
            "0.7.15", sha256="c608cd2d89db7482ab40fc6e7de27afc87b20595e145ed81a2a8702e9a0d7e2d"
        )
        version("0.7.5", sha256="ae2192283eb645ccab189b1dfd8b13d3264eae631469a903c0e0f2dffce65e3b")
        version("0.6.8", sha256="45ecd70cfe42132ff84083ecb37fe7a8d2feac3eacd7a5872e7a002fb260940f")
        version(
            "0.4.27", sha256="c13eea45257362ecfa2a2b31de9b62fbd0542e211a573562d98ab7c8fc50d8fc"
        )
        version(
            "0.4.17", sha256="01564bd760eff885ad61f44173647a569732934d1a4a558839c8088fbf75e53f"
        )
        version(
            "0.4.16", sha256="2144995a87b161d063bd4ef8294b1e948677bd90d01f8394d0e3fca037bb847f"
        )
        version(
            "0.4.15", sha256="8e36b8e07595fc6216d01e729c81a0b4ff029a93cc2ef987a73d3b650d6d559c"
        )

    # PythonPackage builds via maturin and preserves the `python -m uv` entry
    # point; CargoPackage builds the bare Rust binary as an alternative. The
    # cargo build needs the `uv-distribution/static` feature, which is absent
    # before 0.7.5, so the cargo build system is only offered for @0.7.5:.
    build_system(
        "python_pip",
        conditional("cargo", when="@0.7.5:"),
        default="python_pip",
    )

    with default_args(type="build"):
        # Both build systems compile the Rust sources (maturin shells out to cargo),
        # and the bundled `-sys` crates need a C compiler
        depends_on("c")

        # the bundled jemalloc allocator builds its C sources with `./configure && make`
        depends_on("gmake")

        # Minimum Rust toolchain, from Cargo.toml
        depends_on("rust@1.94:", when="@0.11.18:")
        depends_on("rust@1.93:", when="@0.11.8:")
        depends_on("rust@1.92:", when="@0.10.10:")
        depends_on("rust@1.91:", when="@0.9.27:")
        depends_on("rust@1.89:", when="@0.9.8:")
        depends_on("rust@1.88:", when="@0.8.19:")
        depends_on("rust@1.87:", when="@0.8.14:")
        depends_on("rust@1.86:", when="@0.7.16:")
        depends_on("rust@1.85:", when="@0.7.6:")
        depends_on("rust@1.84:", when="@0.6.13:")
        depends_on("rust@1.83:", when="@0.5.9:")
        depends_on("rust@1.81:")

    with when("build_system=python_pip"):
        # maturin builds against the Python interpreter; every release sets
        # requires-python = ">=3.8" in pyproject.toml
        depends_on("python@3.8:", type=("build", "run"))

        with default_args(type="build"):
            depends_on("py-maturin@1")

            # Historical dependencies
            depends_on("cmake", when="@:0.6.3")

    @when("@:0.6.3")
    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.set("CMAKE", self.spec["cmake"].prefix.bin.cmake)

    @property
    def build_directory(self):
        # The maturin manifest at the repo root drives the Python build; the
        # bare Cargo build targets the `uv` binary crate directly.
        if self.spec.satisfies("build_system=cargo"):
            return "crates/uv"
        return self.stage.source_path

    @property
    def build_args(self):
        # uv's `default` feature set bundles `test-defaults` (integration tests
        # against live crates.io/PyPI/Git/R2); drop it via --no-default-features
        # and re-enable only the two release features we want
        features = "uv-distribution/static,performance"
        return ["--locked", "--no-default-features", "--features", features]

    @classmethod
    def determine_version(cls, exe):
        output = Executable(exe)("--version", output=str, error=str)
        match = re.match(r"uv (\S+)", output)
        return match.group(1) if match else None

    def test_imports(self):
        """import the uv module (python_pip build only)"""
        if self.spec.satisfies("build_system=python_pip"):
            super().test_imports()

    def test_version(self):
        """verify uv executable outputs version"""
        uv = Executable(self.prefix.bin.uv)
        out = uv("--version", output=str, error=str)
        assert self.spec.version.string in out
