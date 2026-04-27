# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTriton(PythonPackage):
    """A language and compiler for custom Deep Learning operations."""

    homepage = "https://github.com/triton-lang/triton"
    url = "https://github.com/triton-lang/triton/archive/refs/tags/v2.1.0.tar.gz"
    git = "https://github.com/triton-lang/triton.git"

    license("MIT")

    version("main", branch="main")
    version("3.4.0", sha256="a96e87a911794c907fab30e0c7a3f96ef4e9e8fdc8812cd8bbc6f0457619072f")
    version("3.3.1", sha256="9dc77d9205933bf2fc05eb054f4f1d92acd79a963826174d57fe9cfd58ba367b")
    version("3.2.0", sha256="04eb07e2ff1b87bf4b26e132d696177248bfb9c71cecd4864e561a9c103de9b3")
    version("2.1.0", sha256="4338ca0e80a059aec2671f02bfc9320119b051f378449cf5f56a1273597a3d99")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    with default_args(type="build"):
        # https://github.com/triton-lang/triton/blob/v3.3.1/python/requirements.txt
        depends_on("cmake@3.18:3")
        depends_on("ninja@1.11.1:")
        depends_on("py-setuptools@40.8.0:")
        depends_on("py-pybind11@2.13.1:")
        depends_on("py-lit")

    depends_on("py-setuptools@40.8.0:", type="run", when="@3.2.0")
    depends_on("py-filelock", type=("build", "run"))
    depends_on("zlib-api", type="link")
    conflicts("^openssl@3.3.0")

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        """Set environment variables used to control the build"""
        if self.spec.satisfies("%clang"):
            env.set("TRITON_BUILD_WITH_CLANG_LLD", "True")

    @property
    def build_directory(self):
        return "." if self.spec.satisfies("@3.4.0:") else "python"
