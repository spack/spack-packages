# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyEdfio(PythonPackage):
    """Read and write EDF/EDF+ files."""

    homepage = "https://github.com/the-siesta-group/edfio"
    pypi = "edfio/edfio-0.4.3.tar.gz"
    git = "https://github.com/the-siesta-group/edfio"

    license("Apache-2.0")

    version("0.4.13", sha256="1744a7e7fc354d4e39082edcd4cac72ec1fa13414ca8a07c630d35f78da6c4dd")
    version("0.4.3", sha256="9250e67af190379bb3432356b23c441a99682e97159ea58d4507b0827175b487")

    depends_on("python@3.9:", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-hatchling", when="@0.4.6:")
        depends_on("py-hatch-vcs", when="@0.4.6:")

        # Historical dependencies
        depends_on("py-poetry-core@1:", when="@:0.4.5")
        depends_on("py-poetry-dynamic-versioning@1", when="@:0.4.5")

    with default_args(type=("build", "run")):
        depends_on("py-numpy@1.22.0:")
        depends_on("py-typing-extensions@4:", when="^python@:3.10")
