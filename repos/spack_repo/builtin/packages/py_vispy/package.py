# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyVispy(PythonPackage):
    """VisPy is a high-performance interactive 2D/3D data visualization
    library. VisPy leverages the computational power of modern Graphics
    Processing Units (GPUs) through the OpenGL library to display very large
    datasets."""

    homepage = "https://www.vispy.org"
    pypi = "vispy/vispy-0.15.2.tar.gz"

    maintainers("Markus92")

    license("BSD-3-Clause", checked_by="Markus92")

    version("0.16.1", sha256="b93c32c85d08c06ae8f5e3177f9cfd6c495e1745f2120b777830adee5d9c3648")
    version("0.15.2", sha256="d52d10c0697f48990555cea2a2bad3f9f5a772391856fda364ea4bbc69fd075c")
    version("0.12.2", sha256="141c2ddccc1158555bc89f09010c4b1d754487e816357333f31e795a7146a024")

    depends_on("py-setuptools@69.4.0:", when="@0.15:", type="build")
    depends_on("py-setuptools@30.3.0:", type="build")
    depends_on("py-setuptools-scm@8.1: +toml", when="@0.15:", type="build")
    depends_on("py-setuptools-scm", type="build")

    depends_on("py-numpy@2:", when="@0.14.3:", type=("build", "run"))
    depends_on(
        "py-numpy@1", when="@:0.14.2", type=("build", "run")
    )  # https://github.com/numpy/numpy/issues/26191
    depends_on("py-cython@3:", when="@0.15:", type=("build", "run"))
    depends_on("py-cython@0.29.2:", type=("build", "run"))
    depends_on("py-freetype-py", type=("build", "run"))
    depends_on("py-hsluv", type=("build", "run"))
    depends_on("py-kiwisolver", type=("build", "run"))
    depends_on("py-packaging", type=("build", "run"))
