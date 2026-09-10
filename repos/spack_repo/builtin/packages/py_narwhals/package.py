# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyNarwhals(PythonPackage):
    """Extremely lightweight compatibility layer between dataframe libraries"""

    homepage = "https://github.com/narwhals-dev/narwhals"
    pypi = "narwhals/narwhals-1.8.1.tar.gz"

    license("MIT")

    version("2.24.0", sha256="b5c0f684ccd9d7475b564111e319a4964abcf2baf79d3cf6b1003d06ac9b828d")
    version("2.23.0", sha256="13e7ff5b4bb4a2f77b907c2e4d8a76e273dfc1323a3c997440a2f9fd26aed408")
    version("2.22.1", sha256="d62920805a0a43b7ff8b54b0c0d3142d796f8a9301836ada37e573d6a33cbcd9")
    version("2.21.2", sha256="5c5b2d0b47aef7c73ea412cfcbcd467f2f2d5be73e3c2ab19d78f4a97718790a")
    version("2.20.0", sha256="c10994975fa7dc5a68c2cffcddbd5908fc8ebb2d463c5bab085309c0ee1f551e")
    version("2.19.0", sha256="14fd7040b5ff211d415a82e4827b9d04c354e213e72a6d0730205ffd72e3b7ff")
    version("2.3.0", sha256="b66bc4ab7b6746354f60c4b3941e3ce60c066588c35360e2dc6c063489000a16")
    version("1.38.0", sha256="0a356a21ad00de0db0e631332a823a6a6755544bd10b8e68a02d75029c71392e")
    version("1.8.1", sha256="97527778e11f39a1e5e2113b8fbb9ead788be41c0337f21852e684e378f583e8")

    with default_args(type=("build", "run")):
        depends_on("python@3.10:", when="@2.21.1:")
        depends_on("python@3.9:", when="@1.43:")
        depends_on("python@3.8:")

    with default_args(type="build"):
        depends_on("py-uv-build@0.11", when="@2.22:")

        # Historical dependencies
        depends_on("py-hatchling", when="@:2.21")
