# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyCookiecutter(PythonPackage):
    """A command-line utility that creates projects from cookiecutters
    (project templates).  E.g. Python package projects, jQuery plugin
    projects."""

    homepage = "https://cookiecutter.readthedocs.io/en/latest/"
    url = "https://github.com/audreyr/cookiecutter/archive/1.6.0.tar.gz"

    license("BSD-3-Clause")

    version("2.6.0", sha256="da014a94d85c1b1be14be214662982c8c90d860834cbf9ddb2391a37ad7d08be")

    depends_on("py-setuptools", type="build")
    depends_on("py-binaryornot@0.4.4:", type=("build", "run"), when="@1.7.1:")
    depends_on("py-jinja2@2.7:3", type=("build", "run"))
    depends_on("py-click@7.0:", type=("build", "run"), when="@1.7:")
    depends_on("py-click@:8", type=("build", "run"), when="@2.1:")
    depends_on("py-pyyaml@5.3.1:", type=("build", "run"), when="@2:")
    depends_on("py-python-slugify@4:", type=("build", "run"), when="@1.7.1:")
    depends_on("py-requests@2.23.0:", type=("build", "run"), when="@1.7.1:")
    depends_on("py-arrow", type=("build", "run"), when="@2.2:")
    depends_on("py-rich", type=("build", "run"), when="@2.3:")
