# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyAffine(PythonPackage):
    """Matrices describing affine transformation of the plane."""

    homepage = "https://github.com/rasterio/affine"
    pypi = "affine/affine-3.0.0.tar.gz"

    license("BSD-3-Clause")
    maintainers("adamjstewart")

    version("3.0.1", sha256="e1b3c38c5d4d3ef5024a182a6d1bf1e0c51ab221825781c741aeb4d0c079a7e2")
    version("3.0.0", sha256="573514d5c37e98401a0ec34139c2b725d9f9ae4d074662f4b62a47d6a2ba9f06")
    version("2.4.0", sha256="a24d818d6a836c131976d22f8c27b8d3ca32d0af64c1d8d29deb7bafa4da1eea")
    version("2.3.1", sha256="d676de66157ad6af99ffd94e0f54e89dfc35b0fb7252ead2ed0ad2dca431bdd0")
    version("2.2.2", sha256="ff0d0f40a90faa651f7bc7fece15bdbb7a0e0658b1e7ba6a03422c21efa7da90")
    version("2.1.0", sha256="5f97938c63195551d89237e241c435cdeb296b81bcfaa46140afc12cac7bc447")

    with default_args(type="build"):
        depends_on("py-flit-core@3.2:3", when="@2.4:")
        depends_on("py-setuptools", when="@:2.3")

    with default_args(type=("build", "run")):
        depends_on("py-attrs@21.3:", when="@3:")
