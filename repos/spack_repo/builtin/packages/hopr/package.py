# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


import glob

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Hopr(CMakePackage):
    """
    HOPR is an open-source tool for the generation of three-dimensional unstructured high-order meshes.
    """

    homepage = "https://hopr.readthedocs.io"
    git = "https://github.com/hopr-framework/hopr.git"

    license("GPL-3.0-only")

    version("master", get_full_repo=True)

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    depends_on("mpi")
    depends_on("hdf5@1.12.0+fortran")
    depends_on("lapack")
    depends_on("blas")
    # CGNS at 3.4.1 has CMake issues due to h5dump
    # See: https://github.com/CGNS/CGNS/pull/215
    depends_on("cgns@4.0:+fortran~scoping")
    depends_on("cmake@3.17:", type="build")

    def cmake_args(self):
        args = []
        args.extend(
            [
                self.define("CGNS_DIR", self.spec["cgns"].prefix),
                self.define("LIBS_BUILD_CGNS", "OFF"),
                self.define("LIBS_USE_CGNS", "ON"),
                self.define("HDF5_DIR", self.spec["hdf5"].prefix),
                self.define("LIBS_BUILD_HDF5", "OFF"),
                self.define("LAPACK_LIBRARIES", self.spec["lapack"].libs.joined(";")),
                self.define("BLAS_LIBRARIES", self.spec["blas"].libs.joined(";")),
            ]
        )
        return args
