# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyDocplex(PythonPackage):
    """The IBM Decision Optimization CPLEX Modeling for Python"""

    homepage = "https://www.ibm.com/cloud/decision-optimization-for-watson-studio"
    pypi = "docplex/docplex-2.32.264.tar.gz"

    license("Apache-2.0")

    version("2.32.264", sha256="4e2b29b3559e702bcfe12c6747428c752b0c39a508a81addf05edaab36b76bd8")

    with default_args(type="build"):
        depends_on("py-setuptools@78.1.1:78.1")

    with default_args(type=("build", "run")):
        depends_on("py-six")
