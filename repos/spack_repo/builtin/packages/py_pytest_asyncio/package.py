# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPytestAsyncio(PythonPackage):
    """pytest-asyncio is an Apache2 licensed library, written in Python,
    for testing asyncio code with pytest."""

    homepage = "https://github.com/pytest-dev/pytest-asyncio"
    pypi = "pytest-asyncio/pytest_asyncio-1.4.1.tar.gz"

    license("Apache-2.0")

    version("1.4.1", sha256="e8266eb094e5ee9ffdb2068c9836f33e209ea77a970eb846933d416b5602669b")
    version("0.23.5", sha256="3a048872a9c4ba14c3e90cc1aa20cbc2def7d01c7c8db3777ec281ba9c057675")
    version("0.18.3", sha256="7659bdb0a9eb9c6e3ef992eef11a2b3e69697800ad02fb06374a210d85b29f91")
    version("0.9.0", sha256="fbd92c067c16111174a1286bfb253660f1e564e5146b39eeed1133315cf2c2cf")

    with default_args(type="build"):
        depends_on("py-setuptools@77:", when="@0.26:")
        depends_on("py-setuptools@51.0:", when="@0.18.3:")
        depends_on("py-setuptools")
        depends_on("py-wheel@0.36:", when="@0.18.3:0.25")
        depends_on("py-setuptools-scm@6.2:+toml", when="@0.18.3:")

    with default_args(type=("build", "run")):
        depends_on("python@3.10:", when="@1.3:")
        depends_on("python@3.7:", when="@0.18.3:")
        depends_on("python@3.5:")
        depends_on("py-pytest@8.4:", when="@1.4:")
        depends_on("py-pytest@7:8", when="@0.23")
        depends_on("py-pytest@6.1.0:7", when="@0.18.3")
        depends_on("py-pytest@3.0.6:4.0", when="@0.9.0")
        depends_on("py-backports-asyncio-runner@1.1:1", when="@1.1: ^python@:3.10")
        depends_on("py-typing-extensions@4.12:", when="@1.2: ^python@:3.12")

    def url_for_version(self, version):
        if version >= Version("0.24"):
            name = "pytest_asyncio"
        else:
            name = "pytest-asyncio"
        return f"https://files.pythonhosted.org/packages/source/p/{name}/{name}-{version}.tar.gz"
