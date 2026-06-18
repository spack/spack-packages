# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyAsgiLifespan(PythonPackage):
    """Programmatic startup/shutdown of ASGI apps."""

    homepage = "https://github.com/florimondmanca/asgi-lifespan"
    pypi = "asgi-lifespan/asgi-lifespan-2.1.0.tar.gz"

    license("MIT")

    version("2.1.0", sha256="5e2effaf0bfe39829cf2d64e7ecc47c7d86d676a6599f7afba378c31f5e3a308")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools-scm", type="build")

    depends_on("py-sniffio", type=("build", "run"))
