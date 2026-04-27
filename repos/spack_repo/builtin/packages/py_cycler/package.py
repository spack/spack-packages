# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyCycler(PythonPackage):
    """Composable style cycles."""

    homepage = "https://matplotlib.org/cycler/"
    pypi = "cycler/cycler-0.11.0.tar.gz"

    license("BSD-3-Clause")

    version("0.12.1", sha256="88bb128f02ba341da8ef447245a9e138fae777f6a23943da4540077d3601eb1c")
    version("0.11.0", sha256="9c87405839a19696e837b3b818fed3f5f69f16f1eec1a1ad77e043dcea9c772f")
    version("0.10.0", sha256="cd7b2d1018258d7247a71425e9f26463dfb444d411c39569972f4ce586b0c9d8")

    depends_on("python@3.8:", when="@0.12:", type=("build", "run"))
    depends_on("python@3.6:", when="@0.11:", type=("build", "run"))
    # used pyproject.toml only
    depends_on("py-setuptools@61:", type="build", when="@0.12:")
    depends_on("py-setuptools", type="build")

    # Historical dependencies
    depends_on("py-six", when="@:0.10", type=("build", "run"))
