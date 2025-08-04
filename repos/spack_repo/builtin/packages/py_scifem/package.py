# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install scifem
#
# You can edit this file again by typing:
#
#     spack edit scifem
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from marshal import version

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyScifem(PythonPackage):
    """A collection of tools for scientific computing with a focus on finite element methods.
    The tools are written in Python and are intended to be used in conjunction with the py-fenics-dolfinx.
    """

    homepage = "https://scientificcomputing.github.io/scifem/"
    url = "https://github.com/scientificcomputing/scifem/archive/refs/tags/v0.6.0.tar.gz"
    git = "https://github.com/scientificcomputing/scifem.git"

    maintainers("finsberg", "jorgensd")

    license("MIT", checked_by="jorgensd")

    version("main", branch="main")
    version("0.6.0", sha256="548c9af8997537bc6830c898a9ffe7007dda16b5e40f3240c97e646cfd0a30b3")
    version("0.5.0", sha256="1e5978ab97889c2d6bad80e375c9db1b050bfb68c197eada17928e6908f15372")
    version("0.4.0", sha256="c4494008c974c3303de7d28d40e038478c4fc1c7c24b7117305bd552a2a1c5a4")

    variant("adios2", default=False, description="ADIOS2 support")
    variant("petsc", default=False, description="PETSc support")
    variant("biomed", default=False, description="Biomedical imaging support")
    variant("hdf5", default=False, description="HDF5 support")

    depends_on("cxx", type="build")
    depends_on("py-nanobind@2:", type="build")
    depends_on("py-scikit-build-core+pyproject", type="build")
    depends_on("py-setuptools@42:", type="build")
    depends_on("cmake@3.21:", type="build")

    depends_on("python@3.10:", type=("build", "run"))

    depends_on("py-fenics-dolfinx@0.9:", when="@0.4:", type="run")
    depends_on("py-fenics-dolfinx@main", when="@main", type="run")

    with when("+adios2"):
        depends_on("adios2+python", type="run")

    with when("+petsc"):
        depends_on("py-petsc4py", type="run")
        depends_on("fenics-dolfinx+petsc", type="run")

    with when("+biomed"):
        depends_on("py-nibabel", type="run")

    with when("+hdf5"):
        depends_on("py-h5py+mpi", when="+hdf5", type="run")

    depends_on("py-numpy@1.20:", type=("run"))

    depends_on("py-packaging", type=("run"))

    def test_python(self):
        """Test PyDolfinxMPC python"""
        with test_part(self, "test_import", purpose="import scifem in python"):
            python = Executable(self.spec["python"].prefix.bin.python)
            python(*(["-c", "import scifem"]))
        with (
            when("+petsc"),
            test_part(
                self, "test_solver_import", purpose="Check that PETSc is configured correctly"
            ),
        ):
            python = Executable(self.spec["python"].prefix.bin.python)
            python(*(["-c", "from scifem.solvers import *"]))

        with (
            when("+biomed"),
            test_part(
                self, "test_biomed_import", purpose="Check that biomed is configured correctly"
            ),
        ):
            python = Executable(self.spec["python"].prefix.bin.python)
            python(*(["-c", "from scifem.biomedical import *"]))
