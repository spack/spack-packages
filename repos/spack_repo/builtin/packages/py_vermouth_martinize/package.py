# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyVermouthMartinize(PythonPackage):
    """
    Vermouth (and Martinize2) - build coarse-grained
    Martini topologies from atomistic structures.
    """

    homepage = "https://github.com/marrink-lab/vermouth-martinize"
    pypi = "vermouth/vermouth-0.14.0.tar.gz"

    license("Apache-2.0")
    maintainers("adamwitmer")

    version("0.15.0", sha256="30da3ecadf6cda6068677d1a2de8ea62990d98fedd200ae71a05e89442cd0b24")
    version("0.14.0", sha256="9f1c6221ea8b6b6da2a4eff32fe7374b76adced3f2fd85da5cbb1cfcfbf10696")

    # Runtime dependencies
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-networkx@2:", type=("build", "run"))
    depends_on("py-setuptools@30.3:", type="build")
    depends_on("py-pbr", type=("build", "run"))
