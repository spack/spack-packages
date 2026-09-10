# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyDash(PythonPackage):
    """Dash is the most downloaded, trusted Python framework
    for building ML & data science web apps."""

    homepage = "https://dash.plotly.com/"
    pypi = "dash/dash-2.17.1.tar.gz"
    git = "https://github.com/plotly/dash.git"

    license("MIT")

    version("3.4.0", sha256="3944beb32000ee8b22cd7fbb33545a0a43e25916c63aa41ba59ee5611997815e")
    version("2.17.1", sha256="ee2d9c319de5dcc1314085710b72cd5fa63ff994d913bf72979b7130daeea28e")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-typing-extensions")
    depends_on("py-typing-extensions@4.1.1:", when="@3:")
    depends_on("py-flask")
    depends_on("py-plotly@5", when="@:2")
    depends_on("py-plotly@5:", when="@3:")
    depends_on("py-werkzeug@:3.1")
    depends_on("py-requests")
    depends_on("py-retrying")
    depends_on("py-importlib-metadata")
