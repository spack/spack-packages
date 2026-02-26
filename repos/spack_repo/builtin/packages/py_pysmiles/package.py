# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPysmiles(PythonPackage):
    """A lightweight Python-only library for reading and writing SMILES strings."""

    homepage = "https://github.com/pckroon/pysmiles"
    pypi = "pysmiles/pysmiles-2.0.0.tar.gz"

    license("Apache-2.0")
    maintainers("adamwitmer")

    version("2.0.0", sha256="9bd1da9bf172fc79f71d647d21bbba34178702c664ae0778e59b4d4d149cbe4d")

    depends_on("py-networkx", type=("build", "run"))
    depends_on("py-setuptools@30.3.0:", type="build")
    depends_on("py-pbr", type=("build", "run"))
