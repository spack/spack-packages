# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyAlePy(PythonPackage):
    """The Arcade Learning Environment: a platform for AI research."""

    homepage = "https://github.com/Farama-Foundation/Arcade-Learning-Environment"
    pypi = "ale_py/ale_py-0.12.0.tar.gz"

    license("GPL-2.0-only")

    version("0.12.0", sha256="6030416b6a049d399bf95420ad2fdbf0ea8f83051b502774d27b477a06000dbc")

    variant("sdl", default=True, description="Enable SDL support")
    variant("vector", default=True, description="Build the vector interface")
    variant("xla", default=True, description="Build vector XLA support")

    depends_on("cxx", type="build")
    depends_on("cmake@3.14:", type="build")
    depends_on("sdl2", type=("build", "link"), when="+sdl")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-scikit-build-core@0.10:", type="build")
    depends_on("py-nanobind@2.5.0:", type="build")
    depends_on("py-jax@0.4.31:", type="build", when="platform=linux")
    depends_on("py-jax@0.4.31:", type="build", when="platform=windows")

    depends_on("py-numpy@1.20:", type=("build", "run"))
    depends_on("py-typing-extensions", type=("build", "run"), when="^python@:3.10")

    depends_on("py-gymnasium@1.1.0:", type=("build", "run"), when="+vector")
    depends_on("py-opencv-python@3.0:", type=("build", "run"), when="+vector")

    depends_on("py-gymnasium@1.1.0:", type=("build", "run"), when="+xla")
    depends_on("py-opencv-python@3.0:", type=("build", "run"), when="+xla")
    depends_on("py-jax@0.4.31:", type=("build", "run"), when="+xla platform=linux")
    depends_on("py-jax@0.4.31:", type=("build", "run"), when="+xla platform=windows")
    depends_on("py-chex", type=("build", "run"), when="+xla platform=linux")
    depends_on("py-chex", type=("build", "run"), when="+xla platform=windows")

    def config_settings(self, spec, prefix):
        sdl = "ON" if spec.satisfies("+sdl") else "OFF"
        vector = "ON" if spec.satisfies("+vector") else "OFF"
        xla = "ON" if spec.satisfies("+xla") else "OFF"

        return {
            "cmake.args": ";".join(
                [
                    f"-DSDL_SUPPORT={sdl}",
                    f"-DSDL_DYNLOAD={sdl}",
                    "-DBUILD_CPP_LIB=OFF",
                    "-DBUILD_PYTHON_LIB=ON",
                    f"-DBUILD_VECTOR_LIB={vector}",
                    f"-DBUILD_VECTOR_XLA_LIB={xla}",
                ]
            )
        }
