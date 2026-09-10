# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPytestMemray(PythonPackage):
    """pytest-memray is a pytest plugin for easy integration of memray."""

    homepage = "https://github.com/bloomberg/pytest-memray"
    pypi = "pytest_memray/pytest_memray-1.8.0.tar.gz"

    license("Apache-2.0")

    version("1.8.0", sha256="c0c706ef81941a7aa7064f2b3b8b5cdc0cea72b5277c6a6a09b113ca9ab30bdb")

    with default_args(type="build"):
        depends_on("py-hatchling@1.12.2:")
        depends_on("py-hatch-vcs@0.3:")

    with default_args(type=("build", "run")):
        depends_on("py-pytest@7.2:")
        depends_on("py-memray@1.12:")
