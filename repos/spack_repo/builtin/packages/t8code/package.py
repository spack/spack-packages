# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems import autotools, cmake

from spack.package import *


class T8code(autotools.AutotoolsPackage, cmake.CMakePackage):
    """t8code is a C/C++ library to manage parallel adaptive meshes with various element types.
    t8code uses a collection (a forest) of multiple connected adaptive space-trees in parallel
    and scales to at least one million MPI ranks and over one Trillion mesh elements."""

    homepage = "https://github.com/DLR-AMR/t8code"

    def url_for_version(self, version):
        if version < Version("3.0.0"):
            url = "https://github.com/DLR-AMR/t8code/releases/download/v{0}/t8-{0}.tar.gz"
        else:
            url = (
                "https://github.com/DLR-AMR/t8code/releases/download/v{1}/T8CODE-{0}-Source.tar.gz"
            )
        return url.format(version.up_to(3), version)

    maintainers("Davknapp", "melven")

    license("GPL-2.0-or-later", checked_by="melven")

    version(
        "4.0.0-26.06", sha256="407281956091ca5b1baaa7d6a00ad27bdb766a5f69423d33a864979f31a350ef"
    )
    version("4.0.0", sha256="668536f82730a23fc6fd96ff13e64762b6b0890d04e99a7a38d66341332d5770")
    version("3.0.1", sha256="71732ac0f898feed1af8a81c2deac2e5031e37e94384d3e5b10d1b5861be24d0")
    version(
        "2.0.0",
        sha256="b83f6c204cdb663cec7e0c1059406afc4c06df236b71d7b190fb698bec44c1e0",
        deprecated=True,
    )
    version(
        "1.6.1",
        sha256="dc96effa7c1ad1d50437fefdd0963f6ef7c943eb10a372a4e8546a5f2970a412",
        deprecated=True,
    )
    version(
        "1.6.0",
        sha256="94fb8dd9d9401130867ff18e8f71249cbb0fc34995fd04412a983eb2c93db3d5",
        deprecated=True,
    )
    version(
        "1.5.0",
        sha256="22ce6492c0f808c6859a42921352d857639fddd48ecdc9935e419db95c466f28",
        deprecated=True,
    )
    version(
        "1.4.1",
        sha256="b0ec0c9b4a182f8ac7e930ba80cd20e6dc5baefc328630e4a9dac8c688749e9a",
        deprecated=True,
    )

    variant("mpi", default=True, description="Enable MPI parallel code")
    variant("vtk", default=False, description="Enable vtk-dependent code")
    variant(
        "petsc",
        when="build_system=autotools",
        default=False,
        description="Enable PETSc-dependent code",
    )
    variant("netcdf", default=False, description="Enable NetCDF-dependent code")
    variant(
        "metis",
        when="build_system=autotools",
        default=False,
        description="Enable metis-dependent code",
    )

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("mpi", when="+mpi")
    depends_on("vtk@9.1:", when="+vtk")
    # t8code@1.4.1 doesn't build with petsc@3.19.1
    depends_on("petsc@3.18", when="@:2.0.0 +petsc")
    depends_on("netcdf-c~mpi", when="+netcdf~mpi")
    depends_on("netcdf-c+mpi", when="+netcdf+mpi")
    depends_on("metis", when="+metis")

    # theoretically, version 3.0.* still support autotools, but it does not work out-of-the box
    # (missing configure script and .ac files)
    build_system(
        conditional("cmake", when="@3:"), conditional("autotools", when="@:2"), default="cmake"
    )

    # Per default, t8code uses hardcoded zlib library from vtk package
    # The configure command is overwritten to choose the integrated spack package
    def patch(self):
        if "@:2 +vtk" in self.spec:
            filter_file(r"vtkzlib-\$t8_vtk_version", "z", "configure")


class AutotoolsBuilder(autotools.AutotoolsBuilder):
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


class CMakeBuilder(cmake.CMakeBuilder):
    def cmake_args(self):
        args = [
            self.define_from_variant("T8CODE_ENABLE_MPI", "mpi"),
            self.define_from_variant("T8CODE_ENABLE_VTK", "vtk"),
            self.define_from_variant("T8CODE_ENABLE_NETCDF", "netcdf"),
        ]

        return args
