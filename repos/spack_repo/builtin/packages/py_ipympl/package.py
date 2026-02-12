# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyIpympl(PythonPackage):
    """Matplotlib Jupyter Extension."""

    homepage = "https://github.com/matplotlib/ipympl"
    pypi = "ipympl/ipympl-0.8.8.tar.gz"
    maintainers("haralmha")

    license("BSD-3-Clause")

    version("0.9.4", sha256="cfb53c5b4fcbcee6d18f095eecfc6c6c474303d5b744e72cc66e7a2804708907")

    with default_args(type="build"):
        depends_on("py-hatchling")
        depends_on("py-jupyterlab@4")
        depends_on("py-hatch-nodejs-version@0.3.2:")

    with default_args(type=("build", "run")):
        depends_on("py-ipython@:8")
        depends_on("py-ipython-genutils")
        depends_on("py-ipywidgets@7.6:8")
        depends_on("py-matplotlib@3.4:3")
        depends_on("py-numpy")
        depends_on("pil")
        depends_on("py-traitlets@:5")

        # Necessary for jupyter extension env vars
        depends_on("py-jupyter-core")
