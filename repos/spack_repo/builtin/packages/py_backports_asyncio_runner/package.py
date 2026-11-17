# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyBackportsAsyncioRunner(PythonPackage):
    """Backport of asyncio.Runner, a context manager that controls event loop life cycle."""

    homepage = "https://github.com/samypr100/backports.asyncio.runner"
    pypi = "backports_asyncio_runner/backports_asyncio_runner-1.2.0.tar.gz"

    license("PSF-2.0")

    version("1.2.0", sha256="a5aa7b2b7d8f8bfcaa2b57313f70792df84e32a2a746f585213373f900b42162")

    depends_on("python@3.8:3.10", type=("build", "run"))
    depends_on("py-hatchling", type="build")
    depends_on("py-hatch-fancy-pypi-readme", type="build")
