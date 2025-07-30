# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyFiefClient(PythonPackage):
    """Fief Client for Python."""

    homepage = "https://docs.fief.dev/integrate/python/"
    pypi = "fief_client/fief_client-0.20.0.tar.gz"

    version("0.20.0", sha256="425f40cc7c45c651daec63da402e033c53d91dcaa3f9bf208873fd8692fc16dc")

    variant("cli", default=False, description="Install the CLI")

    depends_on("py-hatchling", type="build")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-httpx@0.21.3:0.27", type=("build", "run"))
    depends_on("py-jwcrypto@1.4:1", type=("build", "run"))

    with when("+cli"):
        depends_on("py-yaspin", type=("build", "run"))
