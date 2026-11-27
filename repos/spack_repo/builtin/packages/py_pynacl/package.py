# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPynacl(PythonPackage):
    """Python binding to the Networking and Cryptography (NaCl) library."""

    homepage = "https://github.com/pyca/pynacl/"
    pypi = "PyNaCl/PyNaCl-1.4.0.tar.gz"

    version("1.6.2", sha256="018494d6d696ae03c7e656e5e74cdfd8ea1326962cc401bcf018f1ed8436811c")
    version(
        "1.5.0",
        sha256="8ac7448f09ab85811607bdd21ec2464495ac8b7c66d146bf545b0f08fb9220ba",
        deprecated=True,
    )
    version(
        "1.4.0",
        sha256="54e9a2c849c742006516ad56a88f5c74bf2ce92c9f67435187c3c5953b346505",
        deprecated=True,
    )

    depends_on("c", type="build")
    depends_on("gmake", type="build")

    depends_on("python@2.7:2.8,3.4:", type=("build", "run"))
    depends_on("python@3.6:", type=("build", "run"), when="@1.5.0:")
    depends_on("python@3.8:", type=("build", "run"), when="@1.6:")
    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools@40.8:", type="build", when="@1.5.0:")
    depends_on("py-setuptools@61:73,74.0.1:", type="build", when="@1.6:")
    depends_on("py-six", type=("build", "run"), when="@1.4.0")
    depends_on("py-cffi@1.4.1:", type=("build", "run"))
    depends_on("py-cffi@2:", type=("build", "run"), when="@1.6.1: ^python@3.9:")

    def url_for_version(self, version):
        name = "pynacl" if version >= Version("1.6") else "PyNaCl"
        return f"https://files.pythonhosted.org/packages/source/P/PyNaCl/{name}-{version}.tar.gz"
