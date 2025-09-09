# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyDolfinxMpc(PythonPackage):
    """Python interface of DOLFINx-MPC, an extension of DOLFINx for multipoint constraints."""

    homepage = "https://www.jsdokken.com/dolfinx_mpc"
    url = "https://github.com/jorgensd/dolfinx_mpc/archive/v0.9.3.tar.gz"
    git = "https://github.com/jorgensd/dolfinx_mpc.git"

    maintainers("jorgensd")

    license("MIT", checked_by="jorgensd")

    version("main", branch="main")
    version("0.9.3", sha256="efa312cc498e428aab44acccc9bb0c74c200eda005742de7778c8e68fa84e8df")
    version("0.8.1", sha256="e0254b4a1c9c1456583c1415821946b11b0b2e48dbfee6558da2bbedfe78b461")

    variant("numba", default=False, description="numba support")

    depends_on("cxx", type="build")

    depends_on("cmake@3.21:", when="@0.9:", type="build")
    depends_on("cmake@3.19:", when="@:0.8", type="build")
    depends_on("py-packaging")

    depends_on("python@3.10:", when="@main:", type=("build", "run"))
    depends_on("python@3.8:", when="@0.8:", type=("build", "run"))

    depends_on("py-cffi@:1.16", type=("build", "run"))
    depends_on("py-numpy@1.21:", type=("build", "run"))
    depends_on("py-mpi4py", type=("build", "run"))

    depends_on("dolfinx-mpc@main", when="@main", type=("build"))
    depends_on("dolfinx-mpc@0.9.3", when="@0.9.3", type=("build"))
    depends_on("dolfinx-mpc@0.8.1", when="@0.8.1", type=("build"))

    depends_on("py-fenics-dolfinx@main+petsc4py", when="@main")
    depends_on("py-fenics-dolfinx@0.9:+petsc4py", when="@0.9")
    depends_on("py-fenics-dolfinx@0.8+petsc4py", when="@0.8")

    depends_on("py-nanobind@2:", when="@0.9:", type="build")
    depends_on("py-nanobind@1.8:1.9", when="@0.8", type="build")
    depends_on("py-scikit-build-core@0.10: +pyproject", when="@0.10:", type="build")
    depends_on("py-scikit-build-core@0.5: +pyproject", when="@0.8:0.9", type="build")

    depends_on("py-petsc4py", type=("build", "run"))
    depends_on("py-numba", when="+numba", type="run")

    build_directory = "python"
