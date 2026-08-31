# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyRestrictedpython(PythonPackage):
    """A restricted execution environment for Python to run untrusted code."""

    homepage = "https://github.com/zopefoundation/RestrictedPython"
    pypi = "RestrictedPython/restrictedpython-8.5.tar.gz"

    license("ZPL-2.1", checked_by="aprozo")

    version("8.5", sha256="4ed1269dbe3caa88db650d1af325198a952aeb1451eca05df0cfa65db4466215")

    depends_on("python@3.10:3.15", type=("build", "run"))
    depends_on("py-setuptools@78.1.1:81", type="build")
    depends_on("py-wheel", type="build")
