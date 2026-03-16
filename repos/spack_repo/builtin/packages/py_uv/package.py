# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyUv(PythonPackage):
    """An extremely fast Python package and project manager, written in Rust."""

    homepage = "https://github.com/astral-sh/uv"
    pypi = "uv/uv-0.10.1.tar.gz"

    license("APACHE 2.0 or MIT")

    version("0.10.1", sha256="c89e7fd708fb3474332d6fc54beb2ea48313ebdc82c6931df92a884fcb636d9d")
    version("0.7.22", sha256="f5cf159907d594e33433f14737d1ee843dc8799edfcf57b5b8c0f282d1117051")
    version("0.7.15", sha256="c608cd2d89db7482ab40fc6e7de27afc87b20595e145ed81a2a8702e9a0d7e2d")
    version("0.7.5", sha256="ae2192283eb645ccab189b1dfd8b13d3264eae631469a903c0e0f2dffce65e3b")
    version("0.6.8", sha256="45ecd70cfe42132ff84083ecb37fe7a8d2feac3eacd7a5872e7a002fb260940f")
    version("0.4.27", sha256="c13eea45257362ecfa2a2b31de9b62fbd0542e211a573562d98ab7c8fc50d8fc")
    version("0.4.17", sha256="01564bd760eff885ad61f44173647a569732934d1a4a558839c8088fbf75e53f")
    version("0.4.16", sha256="2144995a87b161d063bd4ef8294b1e948677bd90d01f8394d0e3fca037bb847f")
    version("0.4.15", sha256="8e36b8e07595fc6216d01e729c81a0b4ff029a93cc2ef987a73d3b650d6d559c")

    # from Cargo.toml
    depends_on("rust@1.86:", type=("build", "run"), when="@0.7.16:")
    depends_on("rust@1.85:", type=("build", "run"), when="@0.7.6:")
    depends_on("rust@1.84:", type=("build", "run"), when="@0.6.13:")
    depends_on("rust@1.83:", type=("build", "run"), when="@0.5.9:")
    depends_on("rust@1.81:", type=("build", "run"))

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-maturin@1", type="build")

    depends_on("gmake", type="build")

    # Historical dependencies
    depends_on("cmake", type="build", when="@:0.6.3")

    @when("@:0.6.3")
    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.set("CMAKE", self.spec["cmake"].prefix.bin.cmake)

    executables = ["^uv$"]
