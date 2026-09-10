# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyFlask(PythonPackage):
    """A simple framework for building complex web applications."""

    homepage = "https://palletsprojects.com/p/flask/"
    pypi = "flask/flask-3.0.3.tar.gz"
    git = "https://github.com/pallets/flask.git"

    license("BSD-3-Clause")

    version("3.1.2", sha256="bf656c15c80190ed628ad08cdfd3aaa35beb087855e2f494910aa3774cc4fd87")
    version("3.0.3", sha256="ceb27b0af3823ea2737928a4d99d125a06175b8512c445cbd9a9ce200ef76842")
    version("2.3.2", sha256="8c2f9abd47a9e8df7f0c3f091ce9497d011dc3b31effcf4c85a6e2b50f4114ef")

    depends_on("python@3.9:", type=("build", "run"), when="@3.1:")
    depends_on("py-flit-core@:3", type=("build", "run"), when="@3:")

    depends_on("py-blinker@1.9:", when="@3.1:", type=("build", "run"))
    depends_on("py-blinker@1.6.2:", when="@2.3:", type=("build", "run"))
    depends_on("py-click@8.1.3:", when="@3:", type=("build", "run"))
    depends_on("py-click@8:", when="@2.1:", type=("build", "run"))
    depends_on("py-importlib-metadata@3.6:", when="@2.1: ^python@:3.9", type=("build", "run"))
    depends_on("py-itsdangerous@2.2:", when="@3.1:", type=("build", "run"))
    depends_on("py-itsdangerous@2.1.2:", when="@3:", type=("build", "run"))
    depends_on("py-itsdangerous@2:", when="@2:", type=("build", "run"))
    depends_on("py-jinja2@3.1.2:", when="@3:", type=("build", "run"))
    depends_on("py-jinja2@3:", when="@2:", type=("build", "run"))
    depends_on("py-markupsafe@2.1.1:", when="@3.1.1:", type=("build", "run"))
    depends_on("py-werkzeug@3.1:", when="@3.1:", type=("build", "run"))
    depends_on("py-werkzeug@3:", when="@3:", type=("build", "run"))
    depends_on("py-werkzeug@2.3.3:", when="@2.3.2:", type=("build", "run"))

    # Historical dependencies
    depends_on("py-setuptools", type=("build", "run"), when="@:2")
