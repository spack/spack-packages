# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyElecsolver(PythonPackage):
    """Formalizes electric systems as linear problems for temporal and frequency-domain studies."""

    homepage = "https://github.com/williampiat3/ElecSolver"
    pypi = "ElecSolver/elecsolver-2.0.1.tar.gz"

    maintainers("williampiat3")

    version("2.1.0", sha256="17a33dd4d6f8551904baa55c840d561cff00dc046b4bf7e11bad7e69722c4faa")
    version("2.0.1", sha256="126b02e90e01405109ddd52255a43015d5e0e634945c46baa13c6d41d0e4e05e")

    depends_on("py-setuptools@80:", type="build")
    with default_args(type=("build", "run")):
        depends_on("python@3.9:")
        depends_on("py-numpy")
        depends_on("py-scipy")
        depends_on("py-networkx")

    # Optional/test deps
    depends_on("py-pytest", type="test")
    depends_on("py-python-mumps", type="test")

    @run_after("install")
    @on_package_attributes(run_tests=True)
    def install_test(self):
        with working_dir(self.stage.source_path):
            python("-m", "pytest", "tests")
