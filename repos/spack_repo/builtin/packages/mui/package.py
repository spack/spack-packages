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
#     spack install mui
#
# You can edit this file again by typing:
#
#     spack edit mui
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------


from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Mui(CMakePackage):
    """Multiscale Universal Interface: A Concurrent Framework for Coupling Heterogeneous Solvers """

    homepage = "https://mxui.github.io/"
    git      = "https://github.com/MxUI/MUI.git"


    maintainers("Wendi-L", "SLongshaw")

    license("Apache-2.0", checked_by="blairSmcc03")

    version("2.0", branch="master")

    # Core dependency: needs an MPI implementation 
    depends_on("cmake@3.27:")
    depends_on("mpi")

   

    def cmake_args(self):
        """Map Spack variants to the project's CMake options."""
        args = []

        # Optionally you can be explicit about MPI, but usually not needed:
        # spec = self.spec
        # args.append(self.define("MPI_CXX_COMPILER", spec["mpi"].mpicxx))

        return args