# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *
from spack.util.executable import Executable


class PyScotchpy(PythonPackage):
    """This project provides a Python3 interface for the Scotch graph partitioning library."""

    homepage = "https://pypi.org/project/scotchpy64"
    git = "https://codeberg.org/fpellegr/scotchpy.git"
    url = "https://codeberg.org/fpellegr/scotchpy/archive/v1.0.1.tar.gz"

    maintainers("jcortial_safran")

    license("BSD-2-Clause", checked_by="jcortial_safran")

    version("1.0.1", sha256="18de746b3fc78e1fd13cd22e5da09bef0775d0ed7c797ca1a245cd0af537a9c1")

    variant("mpi", default=False, description="Enable parallel version (ptscotch)")

    variant(
        "intsize",
        default="64",
        values=("32", "64"),
        multi=False,
        sticky=True,
        description="The integer size",
    )

    depends_on("py-scikit-build-core", type="build")
    depends_on("c", type="build")

    depends_on("scotch@7.0.9: +shared", type=("build", "run"))
    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))

    with when("+mpi"):
        depends_on("py-mpi4py", type=("build", "run"))
        depends_on("scotch +mpi", type=("build", "run"))

    depends_on("scotch ~int64", when="intsize=32", type=("build", "run"))
    depends_on("scotch +int64", when="intsize=64", type=("build", "run"))

    @run_before("install")
    def run_before_install_is_invoked(self) -> None:
        env = EnvironmentModifications()
        for size in (32, 64):
            if self.spec.satisfies(f"intsize={size}"):
                env.set("INTSIZE", f"{size}")
        if self.spec.satisfies("+mpi"):
            env.set("PTSCOTCH", "ON")
        configure = Executable(join_path(self.stage.source_path, "configure"))
        configure(env=env)

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.set("SCOTCHPY_SCOTCH", self.spec["scotch"].prefix.lib)
