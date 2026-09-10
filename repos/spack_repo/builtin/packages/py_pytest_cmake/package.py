# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPytestCmake(PythonPackage):
    """Provide CMake module for Pytest"""

    pypi = "pytest_cmake/pytest_cmake-1.3.0.tar.gz"

    license("MIT")

    maintainers("pearzt")

    version("1.3.0", sha256="6291881b85f8810068552ac9ccc5c9d74ecd3d0c59b395253905e82c930682b9")

    depends_on("py-pytest")
    depends_on("py-hatchling@1.4:")
    depends_on("cmake@3.20:4.2")
    depends_on("python@3.7:4")
