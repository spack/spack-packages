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

    version("1.6.0", sha256="77ccf8bbb913b615ea9e198551019d6e07c3195e411b610e06a922e72cd0dcbb")
    version("1.5.0", sha256="53015e8b783c31a7690274b9ea0bc146a28f7b191061f7c822c6d0a7d45b4c3c")
    version("1.4.1", sha256="eb38d6a1016d6f8dfbfadf25607352a38ed430ad32179bc85e2a7bd782febb46")
    version("1.3.0", sha256="6291881b85f8810068552ac9ccc5c9d74ecd3d0c59b395253905e82c930682b9")

    depends_on("py-pytest@4:9")
    depends_on("py-hatchling@1.4:")
    depends_on("cmake@3.20:4.2", when="@1.3.0")
    depends_on("cmake@3.20:4.4", when="@1.4.1:")
    depends_on("python@3.7:4")
