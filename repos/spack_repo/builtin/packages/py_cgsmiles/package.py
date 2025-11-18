# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyCgsmiles(PythonPackage):
    """Coarse-Grained SMILES (CGsmiles)"""

    homepage = "https://github.com/gruenewald-lab/CGsmiles#"
    pypi = "cgsmiles/cgsmiles-1.0.0.tar.gz"
    git = "https://github.com/gruenewald-lab/CGsmiles.git"

    license("Apache-2.0")
    maintainers("adamwitmer")

    version("1.0.0", sha256="83fdb6dadfc4efa065fb8ef66af5d461ec50a629680ba6faf117877f37174aa9")
    version("cg_smiles_polyply", commit="f53efae4e7dee69e63c51a69cb220e4a5f30b68f")

    depends_on("py-networkx@2.0:", type=("build", "run"))
    depends_on("py-setuptools@46.4.0:", type="build")
    depends_on("py-pbr", type="build")
    depends_on("py-pysmiles", type=("build", "run"))
    depends_on("py-numpy")
