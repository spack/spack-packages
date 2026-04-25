# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyAcres(PythonPackage):
    """Access resources on your terms."""

    homepage = "https://github.com/nipreps/acres"
    pypi = "acres/acres-0.5.0.tar.gz"

    license("Apache-2.0")

    version("0.5.0", sha256="128b6447bf5df3b6210264feccbfa018b4ac5bd337358319aec6563f99db8f3a")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-pdm-backend", type="build")

    depends_on("py-importlib-resources@5.7:", when="^python@:3.9", type=("build", "run"))
