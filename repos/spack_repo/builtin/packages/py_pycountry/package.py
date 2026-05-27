# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPycountry(PythonPackage):
    """ISO country, subdivision, language, currency and script definitions and their translations."""

    homepage = "https://github.com/pycountry/pycountry"
    pypi = "pycountry/pycountry-26.2.16.tar.gz"

    version("26.2.16", sha256="5b6027d453fcd6060112b951dd010f01f168b51b4bf8a1f1fc8c95c8d94a0801")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-poetry-core", type="build")
