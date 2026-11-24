# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPybigwig(PythonPackage):
    """A package for accessing bigWig files using libBigWig."""

    pypi = "pybigwig/pybigwig-0.3.25.tar.gz"

    license("MIT")

    version("0.3.26", sha256="8b01c6542ed9e65d0758ff18a43d6fd7b1c517e1f6aa6132368fe17ee32c1533")
    version("0.3.25", sha256="8c717b0222e6677956fd659c8a21650983679ffb3314427d7f68d2910fad202a")
    version("0.3.22", sha256="5d4426f754bd7b7f6dc21d6c3f93b58a96a65b6eb2e578ae03b31a71272d2243")
    version("0.3.12", sha256="e01991790ece496bf6d3f00778dcfb136dd9ca0fd28acc1b3fb43051ad9b8403")
    version("0.3.4", sha256="8c97a19218023190041c0e426f1544f7a4944a7bb4568faca1d85f1975af9ee2")

    variant("numpy", default=True, description="Enable support for numpy integers and vectors")

    patch("python3_curl.patch", when="@:0.3.12 ^python@3:")

    depends_on("c", type="build")  # generated

    depends_on("curl", type=("build", "link", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools-scm", type="build", when="@0.3.20:")
    depends_on("python@3.9:", type=("build", "run"), when="@0.3.23:")

    depends_on("py-numpy", type=("build", "run"), when="+numpy")

    def url_for_version(self, version):
        # sdists are named pybigwig-<version> (normalized) from 0.3.23
        name = "pybigwig" if version >= Version("0.3.23") else "pyBigWig"
        return f"https://files.pythonhosted.org/packages/source/p/{name}/{name}-{version}.tar.gz"
