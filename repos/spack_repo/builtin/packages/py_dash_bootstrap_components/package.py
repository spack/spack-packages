# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyDashBootstrapComponents(PythonPackage):
    """Bootstrap themed components for use in Plotly Dash"""

    homepage = "https://dash-bootstrap-components.opensource.faculty.ai/"
    pypi = "dash_bootstrap_components/dash_bootstrap_components-1.6.0.tar.gz"
    git = "https://github.com/facultyai/dash-bootstrap-components/"

    license("Apache-2.0")

    version("2.0.4", sha256="c3206c0923774bbc6a6ddaa7822b8d9aa5326b0d3c1e7cd795cc975025fe2484")
    version("1.6.0", sha256="960a1ec9397574792f49a8241024fa3cecde0f5930c971a3fc81f016cbeb1095")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("python@3.9:", when="@2.0.4:", type=("build", "run"))
    depends_on("py-setuptools", when="@:1.6.0", type="build")
    depends_on("py-hatchling", when="@2.0.4:", type="build")
    depends_on("py-dash@3.0.4:", when="@2.0.4:", type=("build", "run"))
