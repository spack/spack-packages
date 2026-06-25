# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyFiefClient(PythonPackage):
    """Fief Client for Python."""

    homepage = "https://github.com/fief-dev/fief-python"
    pypi = "fief_client/fief_client-0.20.0.tar.gz"

    version("0.20.0", sha256="dbfb906d03c4a5402ceac5c843aa4708535fb6f5d5c1c4e263ec06fbbbc434d7")

    variant("cli", default=False, description="Install the CLI")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-hatchling", type="build")

    depends_on("py-httpx@0.21.3:0.27", type=("build", "run"))
    depends_on("py-jwcrypto@1.4:1", type=("build", "run"))

    with when("+cli"):
        depends_on("py-yaspin", type=("build", "run"))
