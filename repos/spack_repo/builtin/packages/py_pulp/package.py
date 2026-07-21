# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPulp(PythonPackage):
    """PuLP is an LP modeler written in Python. PuLP can generate MPS or LP
    files and call GLPK, COIN-OR CLP/CBC, CPLEX, GUROBI, MOSEK, XPRESS, CHOCO,
    MIPCL, SCIP to solve linear problems."""

    homepage = "https://github.com/coin-or/pulp"
    pypi = "PuLP/PuLP-2.6.0.tar.gz"

    maintainers("marcusboden")

    license("MIT")

    version(
        "3.3.1",
        sha256="f979a2e08c32279234a802ede4e5e26d493300e8ccf94f9223236d228c3941f5",
        url="https://github.com/coin-or/pulp/archive/refs/tags/3.3.1.tar.gz",
    )
    version("2.6.0", sha256="4b4f7e1e954453e1b233720be23aea2f10ff068a835ac10c090a93d8e2eb2e8d")

    depends_on("python@3.9:", type=("build", "run"), when="@3.3.1:")
    depends_on("python@2.7:2.8,3.4:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
