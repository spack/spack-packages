# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTypepy(PythonPackage):
    """typepy is a Python library for variable type checker/validator/converter at a run time."""

    homepage = "https://github.com/thombashi/typepy"
    pypi = "typepy/typepy-1.3.4.tar.gz"

    license("MIT")

    version("1.3.4", sha256="89c1f66de6c6133209c43a94d23431d320ba03ef5db18f241091ea594035d9de")

    variant(
        "datetime", default=False, description="Install dependencies needed for datetime support"
    )

    with default_args(type="build"):
        depends_on("py-setuptools@64:")
        depends_on("py-setuptools-scm@8:")

    with default_args(type=("build", "run")):
        depends_on("py-mbstrdecoder@1")

        with when("+datetime"):
            depends_on("py-python-dateutil@2.8:2")
            depends_on("py-pytz@2018.9:")
            depends_on("py-packaging")
