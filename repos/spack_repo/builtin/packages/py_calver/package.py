# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyCalver(PythonPackage):
    """The calver package is a setuptools extension for automatically
    defining your Python package version as a calendar version."""

    homepage = "https://github.com/di/calver"
    pypi = "calver/calver-2022.6.26.tar.gz"

    license("Apache-2.0")

    version(
        "2025.10.20", sha256="c98b376c2424642224d456b2f70c51402343e008c63d204634665e1a2a2835f5"
    )
    version("2025.4.17", sha256="460702737d620f5c3d4175450485180a1b7f7a422c5db0e6af3e655c7395ec7e")
    version("2022.6.26", sha256="e05493a3b17517ef1748fbe610da11f10485faa7c416b9d33fd4a52d74894f8b")

    depends_on("python@3.9:", type=("build", "run"), when="@2025.4.1:")

    depends_on("py-setuptools@77.0.1:", type="build", when="@2025.4.2:")
    depends_on("py-setuptools", type="build")
