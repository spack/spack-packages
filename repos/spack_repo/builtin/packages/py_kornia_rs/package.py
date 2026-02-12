# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyKorniaRs(PythonPackage):
    """Low level implementations for computer vision in Rust."""

    homepage = "http://www.kornia.org/"
    url = "https://github.com/kornia/kornia-rs/archive/refs/tags/v0.1.1.tar.gz"
    git = "https://github.com/kornia/kornia-rs.git"

    license("Apache-2.0")
    maintainers(
        "edgarriba",
        "ducha-aiki",
        "lferraz",
        "shijianjian",
        "cjpurackal",
        "johnnv1",
        "adamjstewart",
    )

    version("main", branch="main")
    version("0.1.10", sha256="b6f5dd6e1e25e2163648953476a5dada2f6a9e5d8e524f78d1680977152bb179")
    version("0.1.9", sha256="a9b8a6afa00d80c9b1b1e3e5ff650762dac9605829a4f768ff5aedf47649efc2")
    version("0.1.1", sha256="b9ac327fae6e982e6d7df9faeadd1d4f6453e65521819ae9ae5b90e9da0ed1a5")
    version("0.1.0", sha256="0fca64f901dddff49b72e51fc92a25f0a7606e9a1a72ef283606245ea6b4f90d")

    # PyO3 has tight coupling with CPython version
    # Assume Python versions aren't supported until wheels are available on PyPI
    with default_args(type=("build", "run")):
        depends_on("python@:3.14")
        depends_on("python@:3.13", when="@:0.1.9")
        depends_on("python@:3.12", when="@:0.1.7")
        depends_on("python@:3.11", when="@:0.1.0")

    with default_args(type="build"):
        # kornia-py/pyproject.toml
        depends_on("py-maturin@1", when="@0.1.6:")
        depends_on("py-maturin@1.3.2:", when="@:0.1.5")

        # kornia-py/Cargo.toml
        depends_on("rust@1.76:", when="@0.1.7:")

        # rav1e needs rustdoc
        depends_on("rust+dev")

        # pyo3 needs cmake
        depends_on("cmake")

        # turbojpeg-sys needs an assembly compiler
        depends_on("nasm")

    # dlpack-rs needs libclang
    depends_on("llvm+clang")

    # See https://github.com/kornia/kornia-rs/commit/93f768137814709b60767f7fc24a9b0184002aee
    patch("py-kornia-rs-pin-fast_image_resize.patch", when="@0.1.9")
    patch("py-kornia-rs-pin-circular_buffer.patch", when="@0.1.9")

    @property
    def build_directory(self):
        return "kornia-py" if self.spec.satisfies("@0.1.3:") else "py-kornia"
