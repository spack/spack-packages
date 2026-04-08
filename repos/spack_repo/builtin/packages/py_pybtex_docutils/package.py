# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPybtexDocutils(PythonPackage):
    """A docutils backend for pybtex."""

    pypi = "pybtex-docutils/pybtex-docutils-0.2.1.tar.gz"

    license("MIT")

    version("1.0.3", sha256="3a7ebdf92b593e00e8c1c538aa9a20bca5d92d84231124715acc964d51d93c6b")
    version("1.0.2", sha256="43aa353b6d498fd5ac30f0073a98e332d061d34fe619d3d50d1761f8fd4aa016")
    version("1.0.1", sha256="d53aa0c31dc94d61fd30ea3f06c749e6f510f9ff0e78cb2765a9300f173d8626")
    version("1.0.0", sha256="cead6554b4af99c287dd29f38b1fa152c9542f56a51cb6cbc3997c95b2725b2e")
    version("0.2.2", sha256="ea90935da188a0f4de2fe6b32930e185c33a0e306154322ccc12e519ebb5fa7d")
    version("0.2.1", sha256="e4b075641c1d68a3e98a6d73ad3d029293fcf9e0773512315ef9c8482f251337")

    depends_on("py-setuptools", type="build")
    with default_args(type=("build", "run")):
        depends_on("python@3.6:", when="@1.0.0:")
        depends_on("python@2.7:2.8,3.4:", when="@:0.2")

        depends_on("py-docutils@0.14:", when="@1.0.3:")
        depends_on("py-docutils@0.8:", when="@1")

        depends_on("py-pybtex@0.16:")

        depends_on("py-six", when="@:0.2")
