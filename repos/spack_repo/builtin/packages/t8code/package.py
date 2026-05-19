# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class T8code(AutotoolsPackage, CMakePackage):
    """t8code is a C/C++ library to manage parallel adaptive meshes with various element types.
    t8code uses a collection (a forest) of multiple connected adaptive space-trees in parallel
    and scales to at least one million MPI ranks and over one Trillion mesh elements."""

    homepage = "https://github.com/DLR-AMR/t8code"

    url = "https://github.com/DLR-AMR/t8code/releases/download/v4.0.0/T8CODE-4.0.0-Source.tar.gz"

    maintainers("Davknapp", "melven")

    license("GPL-2.0-or-later", checked_by="melven")

    version("4.0.0", sha256="668536f82730a23fc6fd96ff13e64762b6b0890d04e99a7a38d66341332d5770")
    version("2.0.0", sha256="b83f6c204cdb663cec7e0c1059406afc4c06df236b71d7b190fb698bec44c1e0", deprecated=True,
            url = "https://github.com/DLR-AMR/t8code/releases/download/v2.0.0/t8-2.0.0.tar.gz")

    variant("mpi", default=True, description="Enable MPI parallel code")
    variant("vtk", default=False, description="Enable vtk-dependent code")
    variant("petsc", default=False, description="Enable PETSc-dependent code")
    variant("netcdf", default=False, description="Enable NetCDF-dependent code")
    variant("metis", default=False, description="Enable metis-dependent code")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("mpi", when="+mpi")
    depends_on("vtk@9.1:", when="+vtk")
    # t8code@1.4.1 doesn't build with petsc@3.19.1
    depends_on("petsc@3.18", when="@:2.0.0 +petsc")
    depends_on("netcdf-c~mpi", when="+netcdf~mpi")
    depends_on("netcdf-c+mpi", when="+netcdf+mpi")
    depends_on("metis", when="+metis")

    build_system(conditional("cmake", when="@4:"), conditional("autotools", when="@:2"), default="cmake")

    # Per default, t8code uses hardcoded zlib library from vtk package
    # The configure command is overwritten to choose the integrated spack package
    def patch(self):
        if "@:2 +vtk" in self.spec:
            filter_file(r"vtkzlib-\$t8_vtk_version", "z", "configure")

    def configure_args(self):
        args = ["CFLAGS=-O3", "CXXFLAGS=-O3"]
        spec = self.spec

        if "+mpi" in spec:
            args.append("--enable-mpi")
            args.append("CC=mpicc")
            args.append("CXX=mpicxx")
        else:
            args.append("--disable-mpi")

        if "+vtk" in spec:
            args.append("--with-vtk")
            vtk_ver = spec["vtk"].version.up_to(2)
            include_dir = os.path.join(spec["vtk"].headers.directories[0], f"vtk-{vtk_ver}")
            lib_dir = spec["vtk"].prefix.lib

            # vtk paths need to be passed to configure command
            args.append(f"CPPFLAGS=-I{include_dir}")
            if "%gcc@14:" in spec:
                args.append(f"LDFLAGS=-L{lib_dir} -lm")
            else:
                args.append(f"LDFLAGS=-L{lib_dir}")
            # Chosen vtk version number is needed for t8code to find the right version
            args.append(f"--with-vtk_version_number={vtk_ver}")
        elif "%gcc@14:" in spec:
            args.append("LDFLAGS=-lm")

        if "+petsc" in spec:
            args.append(f"--with-petsc={spec['petsc'].prefix}")

        if "+netcdf" in spec:
            args.append("--with-netcdf")

        if "+metis" in spec:
            args.append(f"--with-metis={spec['metis'].prefix}")

        return args

    def cmake_args(self):
        args = [
            self.define_from_variant("T8CODE_ENABLE_MPI", "mpi"),
            self.define_from_variant("T8CODE_ENABLE_VTK", "vtk"),
            self.define_from_variant("T8CODE_ENABLE_NETCDF", "netcdf"),
        ]

        return args
