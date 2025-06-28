# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class Iotaa(PythonPackage):
    """A simple workflow engine with semantics inspired by Luigi
    and tasks expressed as decorated Python functions"""

    homepage = "https://github.com/maddenp/iotaa"
    url = "https://github.com/maddenp/iotaa/archive/refs/tags/v1.2.3-0.tar.gz"

    maintainers("maddenp")

    license("Apache-2.0", checked_by="WeirAE")

    version("1.3.0", sha256="2e3a31cfae0000f2440917ecc9cb7c769bd1024952a299d0db263761b388693f")
    version("1.2.3", sha256="010842cc3f20f203f1154b29befe7d58db7ed45ca7c8d972c08487de5d7dc43e")
    version("1.1.6", sha256="b375edafec7dc00f854f7122e0817924ce53f05e0a62e01422ea44aff25c5f8d")
    version("0.8.3", sha256="d92bf7a1a41f46987effb7aeeacc12b1fc7dbe8bbaedda8ec71dcf188e5d05bb")

    depends_on("python@3.9:")
    depends_on("py-setuptools@42:", type="build")

    build_directory = "src"

    def url_for_version(self, version):
        return f"https://github.com/maddenp/iotaa/archive/refs/tags/v{version}-0.tar.gz"
