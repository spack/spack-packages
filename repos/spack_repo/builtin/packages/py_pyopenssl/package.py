# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPyopenssl(PythonPackage):
    """High-level wrapper around a subset of the OpenSSL library.

    Note: The Python Cryptographic Authority strongly suggests the use of
    pyca/cryptography where possible. If you are using pyOpenSSL for anything
    other than making a TLS connection you should move to cryptography and
    drop your pyOpenSSL dependency."""

    homepage = "https://pyopenssl.org/"
    pypi = "pyopenssl/pyopenssl-26.0.0.tar.gz"

    license("Apache-2.0")

    version("26.0.0", sha256="f293934e52936f2e3413b89c6ce36df66a0b34ae1ea3a053b8c5020ff2f513fc")
    version("23.2.0", sha256="276f931f55a452e7dea69c7173e984eb2a4407ce413c918aa34b55f82f9b8bac")
    version("22.1.0", sha256="7a83b7b272dd595222d672f5ce29aa030f1fb837630ef229f62e72e395ce8968")
    version("19.0.0", sha256="aeca66338f6de19d1aa46ed634c3b9ae519a64b458f8468aec688e7e3c20f200")
    version("18.0.0", sha256="6488f1423b00f73b7ad5167885312bb0ce410d3312eb212393795b53c8caa580")

    depends_on("py-setuptools", type="build")

    with default_args(type=("build", "run")):
        depends_on("py-cryptography@46", when="@26:")
        depends_on("py-cryptography@38:41", when="@23.2")
        depends_on("py-cryptography@38", when="@22")
        depends_on("py-cryptography@2.3:", when="@19")
        depends_on("py-cryptography@2.2.1:", when="@18")

        depends_on("py-typing-extensions@4.9:", when="@25: ^python@3.8:3.12")

        # Historical dependencies
        depends_on("py-six@1.5.2:", when="@:19")

    conflicts("^py-cryptography@40:40.0.1", when="@23.2:")

    def url_for_version(self, version):
        if self.spec.satisfies("@24.2:"):
            name = "pyopenssl"
        else:
            name = "pyOpenSSL"
        return f"https://files.pythonhosted.org/packages/source/{name[0]}/{name}/{name}-{version}.tar.gz"
