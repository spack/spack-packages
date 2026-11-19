# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyLicenseExpression(PythonPackage):
    """A comprehensive utility library to parse, compare, simplify and normalize license
    expressions (such as SPDX license expressions) using boolean logic."""

    homepage = "https://github.com/aboutcode-org/license-expression"
    pypi = "license_expression/license_expression-30.4.4.tar.gz"

    maintainers("ebagrenrut")

    license("Apache-2.0")

    version("30.4.4", sha256="73448f0aacd8d0808895bdc4b2c8e01a8d67646e4188f887375398c761f340fd")

    depends_on("py-setuptools@50:", type="build")

    depends_on("python@3.10:", type=("build", "run"))
