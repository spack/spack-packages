# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyValidatePyproject(PythonPackage):
    """Validation library and CLI tool for checking pyproject.toml files
    using JSON Schema definitions."""

    homepage = "https://github.com/abravalheri/validate-pyproject"
    pypi = "validate-pyproject/validate_pyproject-0.25.tar.gz"

    license("MPL-2.0", checked_by="abhishek1297")

    version("0.25", sha256="e68c12d1cb0d8ddc269ffc42875a81727ddb7865000aa6d2f77d833b55c53f0b")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools@61.2:", type="build")
    depends_on("py-setuptools-scm+toml@7.1:", type="build")
    depends_on("py-wheel", type="build")

    # runtime deps
    depends_on("py-fastjsonschema@2.16.2:3", type=("build", "run"))
    depends_on("py-packaging@24.2:", type=("build", "run"))
    depends_on("py-tomli@1.2.1:", when="^python@3.11", type=("build", "run"))
    depends_on("py-trove-classifiers@2021.10.20:", type=("build", "run"))
