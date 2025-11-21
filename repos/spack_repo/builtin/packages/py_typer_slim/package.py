# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTyperSlim(PythonPackage):
    """Typer, build great CLIs. Easy to code. Based on Python type hints."""

    homepage = "https://github.com/fastapi/typer"
    pypi = "typer_slim/typer_slim-0.20.0.tar.gz"

    license("MIT")

    version("0.20.0", sha256="9fc6607b3c6c20f5c33ea9590cbeb17848667c51feee27d9e314a579ab07d1a3")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-pdm-backend", type="build")
    depends_on("py-click@8", type=("build", "run"))
    depends_on("py-typing-extensions@3.7.4.3:", type=("build", "run"))
