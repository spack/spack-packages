# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPytestCov(PythonPackage):
    """Pytest plugin for measuring coverage."""

    homepage = "https://github.com/pytest-dev/pytest-cov"
    pypi = "pytest_cov/pytest_cov-7.0.0.tar.gz"

    license("MIT")

    version("7.0.0", sha256="33c97eda2e049a0c5298e91f519302a1334c26ac65c1a483d6206fd458361af1")
    version("4.0.0", sha256="996b79efde6433cdbd0088872dbc5fb3ed7fe1578b68cdbba634f14bb8dd0470")
    version("3.0.0", sha256="e7f0f5b1617d2210a2cabc266dfe2f4c75a8d32fb89eafb7ad9d06f6d076d470")
    version("2.8.1", sha256="cc6742d8bac45070217169f5f72ceee1e0e55b0221f54bcf24845972d3a47f2b")
    version("2.3.1", sha256="fa0a212283cdf52e2eecc24dd6459bb7687cc29adb60cb84258fab73be8dda0f")

    depends_on("python@3.9:", type=("build", "run"), when="@6:")
    depends_on("py-hatchling", type="build", when="@7:")
    depends_on("py-hatch-fancy-pypi-readme", type="build", when="@7:")

    depends_on("py-coverage+toml@7.10.6:", type=("build", "run"), when="@7:")
    depends_on("py-coverage+toml@5.2.1:", type=("build", "run"), when="@3:")
    depends_on("py-coverage@4.4:", type=("build", "run"), when="@:2.10")
    depends_on("py-pytest@7:", type=("build", "run"), when="@7:")
    depends_on("py-pytest@4.6:", type=("build", "run"), when="@3:")
    depends_on("py-pytest@3.6:", type=("build", "run"))
    depends_on("py-pluggy@1.2:", type=("build", "run"), when="@6.2.1:")

    # Historical dependencies
    depends_on("py-setuptools", type="build", when="@:4.1")

    def url_for_version(self, version):
        if self.spec.satisfies("@6.1:"):
            name = "pytest_cov"
        else:
            name = "pytest-cov"
        return f"https://files.pythonhosted.org/packages/source/p/{name}/{name}-{version}.tar.gz"
