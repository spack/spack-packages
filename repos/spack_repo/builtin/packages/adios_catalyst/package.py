from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class AdiosCatalyst(CMakePackage):
    """AdiosCatalyst is a new Catalyst implementation for Adios2.

    The aim of this specific implementation is to be able to make in-transit simulation
    with the SST engine of ADIOS2."""

    homepage = "https://gitlab.kitware.com/paraview/adioscatalyst"
    url = "https://gitlab.kitware.com/paraview/adioscatalyst"
    git = "https://gitlab.kitware.com/paraview/adioscatalyst.git"

    maintainers("albestro")

    license("Apache-2.0", checked_by="albestro")

    version("main", branch="main")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("cmake@3.20:", type="build")

    depends_on("libcatalyst")
    depends_on("adios2")
    depends_on("mpi")
