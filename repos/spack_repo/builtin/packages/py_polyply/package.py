# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPolyply(PythonPackage):
    """Polyply is a Python suite for facilitating the setup of molecular dynamics
    simulations of complex polymers, carbohydrates, and other materials."""

    homepage = "https://github.com/marrink-lab/polyply_1.0"
    git = "https://github.com/marrink-lab/polyply_1.0.git"
    pypi = "polyply/polyply-1.8.0.tar.gz"

    version("gen_ff_clean", branch="gen_ff_clean")
    version("1.8.0", sha256="98b4c36c05f3436368c8d86425182200862ac16520f29eaa06568099497dafd8")

    license("Apache-2.0")
    maintainers("adamwitmer")

    # Build dependencies
    depends_on("py-setuptools@46.4.0:", type="build")
    depends_on("python@3.11:", type=("build", "run"))
    depends_on("py-pbr", type=("build", "run"))
    depends_on("py-wheel", type="build")

    # Runtime dependencies
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-decorator@4.4.2", type=("build", "run"))
    depends_on("py-networkx@2.0:", type=("build", "run"))
    depends_on("py-vermouth-martinize@0.9.6:", type=("build", "run"))
    depends_on("py-scipy@1.6.0:", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))

    # Optional: Performance variant
    variant("numba", default=False, description="Enable optional numba acceleration")
    depends_on("py-numba@0.51.2:", type=("build", "run"), when="+numba")
