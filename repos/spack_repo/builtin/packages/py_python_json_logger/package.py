# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPythonJsonLogger(PythonPackage):
    """ "A python library adding a json log formatter."""

    homepage = "https://github.com/madzak/python-json-logger"
    pypi = "python_json_logger/python_json_logger-3.3.0.tar.gz"

    license("BSD-2-Clause")

    version("4.0.0", sha256="f58e68eb46e1faed27e0f574a55a0455eecd7b8a5b88b85a784519ba3cff047f")
    version("3.3.0", sha256="12b7e74b17775e7d565129296105bbe3910842d9d0eb083fc83a6a617aa8df84")
    version("2.0.7", sha256="23e7ec02d34237c5aa1e29a070193a4ea87583bb4e7f8fd06d3de8264c4b2e1c")
    version("2.0.2", sha256="202a4f29901a4b8002a6d1b958407eeb2dd1d83c18b18b816f5b64476dde9096")
    version("0.1.11", sha256="b7a31162f2a01965a5efb94453ce69230ed208468b0bbc7fdfc56e6d8df2e281")

    depends_on("python@3.8:", type="build", when="@3.1:")
    depends_on("python@3.7:", type="build", when="@3:")

    depends_on("py-setuptools", type="build")
    depends_on("py-typing-extensions", type="build", when="@3.1: ^python@:3.9")

    def url_for_version(self, version):
        if self.spec.satisfies("@3.1:"):
            name = "python_json_logger"
        else:
            name = "python-json-logger"
        return f"https://files.pythonhosted.org/packages/source/p/{name}/{name}-{version}.tar.gz"
