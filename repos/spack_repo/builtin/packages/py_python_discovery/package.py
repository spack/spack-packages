# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPythonDiscovery(PythonPackage):
    """Python interpreter discovery."""

    homepage = "https://github.com/tox-dev/python-discovery"
    pypi = "python_discovery/python_discovery-1.2.1.tar.gz"

    license("MIT")

    version("1.4.0", sha256="eb8bc7daad3c226c147e45bb4e970a1feb1bf4048ee178e6db59e197b8010ce3")
    version("1.2.2", sha256="876e9c57139eb757cb5878cbdd9ae5379e5d96266c99ef731119e04fffe533bb")
    version("1.2.1", sha256="180c4d114bff1c32462537eac5d6a332b768242b76b69c0259c7d14b1b680c9e")

    depends_on("python@3.8:", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-hatch-vcs@0.5:")
        depends_on("py-hatchling@1.28:")

    with default_args(type=("build", "run")):
        depends_on("py-filelock@3.15.4:")
        depends_on("py-platformdirs@4.3.6:4")
