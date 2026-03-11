# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPydanticCore(PythonPackage):
    """Core functionality for Pydantic validation and serialization"""

    homepage = "https://github.com/pydantic/pydantic-core"
    pypi = "pydantic_core/pydantic_core-2.18.4.tar.gz"

    license("MIT", checked_by="qwertos")

    version("2.41.5", sha256="08daa51ea16ad373ffd5e7606252cc32f07bc72b28284b6bc9c6df804816476e")
    version("2.41.4", sha256="70e47929a9d4a1905a67e4b687d5946026390568a8e952b92824118063cee4d5")
    version("2.27.1", sha256="62a763352879b84aa31058fc931884055fd75089cccbd9d58bb6afd01141b235")
    version("2.23.2", sha256="95d6bf449a1ac81de562d65d180af5d8c19672793c81877a2eda8fde5d08f2fd")
    version("2.18.4", sha256="ec3beeada09ff865c344ff3bc2f427f5e6c26401cc6113d77e372c3fdac73864")

    with default_args(type="build"):
        # Cargo.toml
        depends_on("rust@1.75:", when="@2.27:")
        depends_on("rust@1.76:", when="@2.18")

        # pyproject.toml
        depends_on("py-maturin@1.9.4:1", when="@2.41:")
        depends_on("py-maturin@1")

    with default_args(type=("build", "run")):
        # Based on PyPI wheel availability
        depends_on("python@:3.14")
        depends_on("python@:3.13", when="@:2.27")
        depends_on("python@:3.12", when="@:2.19")

        depends_on("py-typing-extensions@4.14.1:", when="@2.41:")
        depends_on("py-typing-extensions@4.6:")

    conflicts("py-typing-extensions@4.7.0")
