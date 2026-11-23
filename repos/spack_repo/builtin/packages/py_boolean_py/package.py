# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyBooleanPy(PythonPackage):
    """boolean.py is a small library implementing a boolean algebra. It defines two base elements,
    TRUE and FALSE, and a Symbol class that can take on one of these two values. Calculations are
    done in terms of AND, OR and NOT - other compositions like XOR and NAND are not implemented
    but can be emulated with AND or and NOT. Expressions are constructed from parsed strings or in
    Python."""

    homepage = "https://github.com/bastikr/boolean.py"
    pypi = "boolean_py/boolean_py-5.0.tar.gz"

    maintainers("ebagrenrut")

    license("BSD-2-Clause")

    version("5.0", sha256="60cbc4bad079753721d32649545505362c754e121570ada4658b852a3a318d95")

    depends_on("py-setuptools", type="build")
    depends_on("python@3.6:", type=("build", "run"))
