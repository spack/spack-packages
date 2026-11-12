# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyCgsmiles(PythonPackage):
    """Coarse-Grained SMILES (CGsmiles)"""

    homepage = "https://github.com/gruenewald-lab/CGsmiles#"
    pypi = "cgsmiles/cgsmiles-1.0.2.tar.gz"
    git = "https://github.com/gruenewald-lab/CGsmiles.git"

    license("Apache-2.0")
    maintainers("adamwitmer")

    version("1.0.2", sha256="d74a21b5c54139d980ff457946b99a56364294cad46bf6147c0d166a67dfafca")

    depends_on("py-networkx@2.0:", type=("build", "run"))
    depends_on("py-setuptools@46.4.0:", type="build")
    depends_on("py-pbr", type="build")
    depends_on("py-pysmiles", type=("build", "run"))
    depends_on("py-numpy")
