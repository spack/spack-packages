# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTypesRequests(PythonPackage):
    """Typing stubs for requests."""

    homepage = "https://github.com/python/typeshed"
    pypi = "types_requests/types_requests-2.32.0.20250301.tar.gz"

    version(
        "2.32.4.20250913",
        sha256="abd6d4f9ce3a9383f269775a9835a4c24e5cd6b9f647d64f88aa4613c33def5d",
    )
    version("2.31.0.2", sha256="6aa3f7faf0ea52d728bb18c0a0d1522d9bfd8c72d26ff6f61bfc3d06a411cf40")
    version("2.28.10", sha256="97d8f40aa1ffe1e58c3726c77d63c182daea9a72d9f1fa2cafdea756b2a19f2c")

    depends_on("python@3.9:", type="build", when="@2.32.0.20250301:")

    depends_on("py-setuptools@77.0.3:", type="build", when="@2.32.0.20250515:")
    depends_on("py-setuptools", type="build")

    depends_on("py-urllib3@2:", type=("build", "run"), when="@2.31.0.7:")

    # Historical dependencies
    depends_on("py-types-urllib3", type=("build", "run"), when="@:2.31.0.6")
    depends_on("py-types-urllib3@:1.26", type=("build", "run"), when="@:2.29")

    def url_for_version(self, version):
        if self.spec.satisfies("@2.32.0.20250301:"):
            name = "types_requests"
        else:
            name = "types-requests"
        return f"https://files.pythonhosted.org/packages/source/{name[0]}/{name}/{name}-{version}.tar.gz"
