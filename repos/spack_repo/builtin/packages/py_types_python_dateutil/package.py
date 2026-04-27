# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTypesPythonDateutil(PythonPackage):
    """Typing stubs for python-dateutil."""

    homepage = "https://github.com/python/typeshed"
    pypi = "types_python_dateutil/types_python_dateutil-2.9.0.20251008.tar.gz"

    version(
        "2.9.0.20251008", sha256="c3826289c170c93ebd8360c3485311187df740166dbab9dd3b792e69f2bc1f9c"
    )
    version("2.8.19.14", sha256="1f4f10ac98bb8b16ade9dbee3518d9ace017821d94b057a425b069f834737f4b")
    version("2.8.19", sha256="bfd3eb39c7253aea4ba23b10f69b017d30b013662bb4be4ab48b20bbd763f309")

    depends_on("python@3.9:", type=("build", "run"), when="@2.9.0.20250516:")
    depends_on("py-setuptools@77.0.3:", type="build", when="@2.9.0.20250516:")
    depends_on("py-setuptools", type="build")

    def url_for_version(self, version):
        if self.spec.satisfies("@2.9.0.20241206:"):
            name = "types_python_dateutil"
        else:
            name = "types-python-dateutil"
        return f"https://files.pythonhosted.org/packages/source/{name[0]}/{name}/{name}-{version}.tar.gz"
