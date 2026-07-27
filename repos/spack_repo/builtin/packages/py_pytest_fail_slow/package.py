# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPytestFailSlow(PythonPackage):
    """Fail tests that take too long to run."""

    homepage = "https://github.com/jwodder/pytest-fail-slow"
    pypi = "pytest_fail_slow/pytest_fail_slow-0.6.0.tar.gz"

    license("MIT")

    version("0.6.0", sha256="b367a5bdfadb0a4d35d4ef1c220737aa46bc8d6035256171004c67f7f2f5235c")
    version("0.3.0", sha256="bc022f3f4f170b7e3e7d4dff45bd9e7855e4935ae396bb40b4521ce1ef8ea41c")

    depends_on("python@3.8:", type=("build", "run"), when="@0.5:")
    depends_on("python@3.6:3", type=("build", "run"), when="@0.3")
    depends_on("py-hatchling", type="build", when="@0.5:")

    depends_on("py-pytest@7:", type=("build", "run"), when="@0.5:")
    depends_on("py-pytest@6:", type=("build", "run"))
    depends_on("py-pluggy@1.1:", type=("build", "run"), when="@0.5:")

    # Historical dependencies
    depends_on("py-setuptools@46.4:", type="build", when="@:0.4")

    def url_for_version(self, version):
        if version >= Version("0.5.0"):
            name = "pytest_fail_slow"
        else:
            name = "pytest-fail-slow"
        return f"https://files.pythonhosted.org/packages/source/p/{name}/{name}-{version}.tar.gz"
