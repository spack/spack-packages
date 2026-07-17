# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyRestrictedpython(PythonPackage):
    """A restricted execution environment for Python to run untrusted code."""

    homepage = "https://github.com/zopefoundation/RestrictedPython"
    pypi = "RestrictedPython/restrictedpython-8.1.tar.gz"

    maintainers("aprozo")

    license("ZPL-2.1", checked_by="aprozo")

    version("8.1", sha256="4a69304aceacf6bee74bdf153c728221d4e3109b39acbfe00b3494927080d898")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools@78.1.1:80", type="build")
    depends_on("py-wheel", type="build")
