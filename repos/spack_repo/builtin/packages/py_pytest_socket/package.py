# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPytestSocket(PythonPackage):
    """Pytest Plugin to disable socket calls during tests."""

    homepage = "https://github.com/miketheman/pytest-socket"
    pypi = "pytest_socket/pytest_socket-0.7.0.tar.gz"

    license("MIT")

    version("0.7.0", sha256="71ab048cbbcb085c15a4423b73b619a8b35d6a307f46f78ea46be51b1b7e11b3")

    depends_on("py-poetry-core@1:", type="build")
    depends_on("python@3.8:3", type=("build", "run"))
    depends_on("py-pytest@6.2.5:", type=("build", "run"))
