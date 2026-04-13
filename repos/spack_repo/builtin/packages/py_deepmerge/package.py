# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyDeepmerge(PythonPackage):
    """A tool to handle merging of nested data structures in Python."""

    homepage = "https://deepmerge.readthedocs.io/en/latest/"
    pypi = "deepmerge/deepmerge-2.0.tar.gz"

    license("MIT", checked_by="abhishek1297")

    version("2.0", sha256="5c3d86081fbebd04dd5de03626a0607b809a98fb6ccba5770b62466fe940ff20")

    depends_on("py-setuptools@69:", type="build")
    depends_on("py-setuptools-scm@8:", type="build")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-typing-extensions", when="^python@:3.9", type=("build", "run"))
