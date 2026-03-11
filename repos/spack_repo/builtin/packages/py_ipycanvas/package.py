# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyIpycanvas(PythonPackage):
    """Interactive Canvas in Jupyter."""

    homepage = "https://github.com/martinRenou/ipycanvas"
    pypi = "ipycanvas/ipycanvas-0.9.0.tar.gz"

    license("BSD-3-Clause")

    version("0.14.3", sha256="c6a53a22eebf4d611b168b8f4434145883f27a7575509bd99a4bfc48c5385a39")
    version("0.14.1", sha256="921f1482258b5929b599317b5c129931d80e16be35fa38300a32e7aa4cfe9f89")
    version("0.10.2", sha256="a02c494834cb3c60509801172e7429beae837b3cb6c61d3becf8b586c5a66004")
    version("0.9.0", sha256="f29e56b93fe765ceace0676c3e75d44e02a3ff6c806f3b7e5b869279f470cc43")

    with default_args(type="build"):
        depends_on("py-hatchling", when="@0.14:")
        depends_on("py-jupyterlab@3:4", when="@0.14:")
        depends_on("py-jupyterlab@3", when="@:0.10")

        # Historical dependencies
        depends_on("py-setuptools@40.8:", when="@:0.10")
        depends_on("py-jupyter-packaging@0.7", when="@:0.10")

    with default_args(type=("build", "run")):
        depends_on("py-ipywidgets@7.6:8")
        depends_on("py-numpy")
        depends_on("pil@6:")
