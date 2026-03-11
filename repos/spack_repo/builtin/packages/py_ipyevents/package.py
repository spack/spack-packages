# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyIpyevents(PythonPackage):
    """A custom widget for returning mouse and keyboard events to Python."""

    homepage = "https://github.com/mwcraig/ipyevents"
    pypi = "ipyevents/ipyevents-2.0.1.tar.gz"

    license("BSD-3-Clause")

    version("2.0.4", sha256="bd8c66a9ff26f481494cda1ec1d979722ca9eba19f8ef52538c7cc2db2a1a139")
    version("2.0.2", sha256="26e878b0c5854bc8b6bd6a2bd2c89b314ebe86fda642f4d2434051545bab258f")

    depends_on("python@3.9:", type=("build", "run"), when="@2.0.4:")

    with default_args(type="build"):
        depends_on("py-hatchling")
        depends_on("py-jupyterlab@4", when="@2.0.3:")
        depends_on("py-jupyterlab@3", when="@:2.0.2")
        depends_on("py-hatch-jupyter-builder@0.8.3:")

    depends_on("py-ipywidgets@7.6:", type=("build", "run"))
