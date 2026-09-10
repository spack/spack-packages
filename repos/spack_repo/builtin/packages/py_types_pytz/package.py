# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTypesPytz(PythonPackage):
    """This is a PEP 561 type stub package for the pytz package. It can be used
    by type-checking tools like mypy, pyright, pytype, PyCharm, etc. to check
    code that uses pytz."""

    homepage = "https://github.com/python/typeshed"
    pypi = "types_pytz/types_pytz-2025.2.0.20250809.tar.gz"

    version(
        "2025.2.0.20250809",
        sha256="222e32e6a29bb28871f8834e8785e3801f2dc4441c715cd2082b271eecbe21e5",
    )
    version(
        "2023.3.0.0", sha256="ecdc70d543aaf3616a7e48631543a884f74205f284cefd6649ddf44c6a820aac"
    )

    depends_on("python@3.9:", type=("build", "run"), when="@2025.1.0.20250204:")

    depends_on("py-setuptools@77.0.3:", type="build", when="@025.2.0.20250516:")
    depends_on("py-setuptools", type="build")

    def url_for_version(self, version):
        if self.spec.satisfies("@2024.2.0.20241221:"):
            name = "types_pytz"
        else:
            name = "types-pytz"
        return f"https://files.pythonhosted.org/packages/source/{name[0]}/{name}/{name}-{version}.tar.gz"
