# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack.package import *


class CodeSaturne(AutotoolsPackage):
    """code_saturne is the free, open-source software developed primarily 
       by EDF for computational fluid dynamics (CFD) applications."""

    homepage = "https://www.code-saturne.org"
    url = "https://github.com/code-saturne/code_saturne/archive/refs/tags/v9.1.0.tar.gz"

    maintainers("green-br")

    license("GPL-2.0-or-later", checked_by="green-br")

    version("9.1.0", sha256="1ebdc2e7fbfda3477919d28aba1b979eaeb2895e7c315da14ee2f36856d4f175")

    # Enable or disable options.
    variant("shared", default=False, description="Build shared libraries")
    variant("gui", default=False, description="Enable the Graphical User Interface.")
    variant("long-gnum", default=True, description="Use long global numbers")
    variant("debug", default=False, description="Enable debug")

    # With or without options.
    variant("cgns", default=True, description="Enable CGNS")
    variant("hdf5", default=True, description="Enable HDF5")
    variant("med", default=True, description="Enable MED")
    variant("scotch", default=True, description="Enable SCOTCH")
    variant("mpi", default=True, description="Enable MPI")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")

    depends_on("mpi", when="+mpi")
    depends_on("hdf5@1.12~mpi", when="+hdf5")
    depends_on("med@5.0~mpi", when="+med")
    depends_on("cgns@4.4~mpi+hdf5", when="+cgns+hdf5")
    depends_on("cgns@4.4~mpi~hdf5", when="+cgns~hdf5")
    depends_on("scotch@7.0~mpi", when="+scotch")
    
    conflicts("~hdf5 +med", msg="Cannot build without HDF5 and with MED support.")

    depends_on("python")

    def autoreconf(self, spec, prefix):
        autoreconf("--install", "--verbose", "--force")

    def configure_args(self):
        args = []
        args.extend(self.enable_or_disable("shared"))
        args.extend(self.enable_or_disable("gui"))
        args.extend(self.enable_or_disable("long-gnum"))
        args.extend(self.enable_or_disable("debug"))
        args.extend(self.with_or_without("cgns", activation_value="prefix"))
        args.extend(self.with_or_without("hdf5", activation_value="prefix"))
        args.extend(self.with_or_without("med", activation_value="prefix"))
        args.extend(self.with_or_without("scotch", activation_value="prefix"))
        args.extend(self.with_or_without("mpi", activation_value="prefix"))

        return args
