# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyAuth0Python(PythonPackage):
    """Auth0 Python SDK - Management and Authentication APIs"""

    homepage = "https://github.com/auth0/auth0-python"
    pypi = "auth0-python/auth0-python-6.2.0.tar.gz"

    supplier = "Person: Auth0"

    maintainers("LydDeb")

    license("MIT", checked_by="LydDeb")

    version("6.2.0", sha256="92ee2f23be1bf633b129cbc408f314b1ca35a6c742192cba225c13bf3c59eeac")
    version("3.24.1", sha256="62c2e177b9517879bd8632da9eb7668aedd5775fddea87b0e0e1e9a89b9dd096")

    with default_args(type="build"):
        depends_on("py-poetry-core", when="@6")
        depends_on("py-setuptools", when="@3")

    with default_args(type=("build", "run")):
        with default_args(when="@6"):
            depends_on("python@3.10:")
            depends_on("py-httpx@0.21.2:")
            depends_on("py-pydantic@1.9.2:")
            depends_on("py-pydantic-core@2.18.2:")
            depends_on("py-typing-extensions@4.0.0:")
            # Authentication API dependencies)
            depends_on("py-aiohttp@3.11.18:")
            depends_on("py-cryptography@44.0.0:")
            depends_on("py-pyjwt@2.8.0:")
            depends_on("py-requests@2.32.3:")
            depends_on("py-urllib3@2.3.0:")

        with default_args(when="@3"):
            depends_on("py-pyjwt@1.7.1: +crypto")
            depends_on("py-requests@2.14.0:")

    def url_for_version(self, version):
        url = "https://files.pythonhosted.org/packages/source/a/auth0-python/{0}-{1}.tar.gz"
        if version >= Version("4.4.1"):
            name = "auth0_python"
        else:
            name = "auth0-python"
        return url.format(name, version)
