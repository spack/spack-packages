# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyElecsolver(PythonPackage):
    """Formalizes electric systems as linear problems for temporal and frequency-domain studies."""

    homepage = "https://github.com/williampiat3/ElecSolver"
    pypi = "ElecSolver/elecsolver-2.0.1.tar.gz"

    maintainers = ["williampiat3"]

    version("2.0.1", sha256="126b02e90e01405109ddd52255a43015d5e0e634945c46baa13c6d41d0e4e05e")

    with default_args(type="build"):
        depends_on("py-setuptools")
    # Python dependencies
    with default_args(type=("run")):
        depends_on("python@3.9:")
        depends_on("py-numpy")
        depends_on("py-scipy")
        depends_on("py-networkx")

    # Optional/test deps
    depends_on("py-pytest", type="test")
    depends_on("py-python-mumps", type="test")
