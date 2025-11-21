# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.generic import Package
from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *

class Mpi(Package):
    """Virtual package for the Message Passing Interface."""

    homepage = "https://www.mpi-forum.org/"
    virtual = True

    def set_dependent_cmake_args(self, pkg: PackageBase, args: List[str]) -> None:
        if not getattr(pkg, "find_mpi_hints", True):
            return

        args.extend([
            "-DMPIEXEC:FILEPATH=%s/bin/mpiexec" % spec["mpi"].prefix,
            "-DMPIEXEC_EXECUTABLE:FILEPATH=%s/bin/mpiexec" % spec["mpi"].prefix,
            "-DMPI_HOME:PATH=%s", spec["mpi"].prefix),
        ]

        # MSMPI does not provide compiler wrappers
        # and pointing these variables at the MSVC compilers
        # breaks CMake's mpi detection for MSMPI.
        if "msmpi" in self.spec:
            return

        if "c" in pkg.spec:
            args.append(pkg.define("MPI_C_COMPILER", pkg.spec["mpi"].mpicc))
        if "cxx" in pkg.spec:
            args.append(pkg.define("MPI_CXX_COMPILER", pkg.spec["mpi"].mpicxx))
        if "fortran" in pkg.spec:
            # By default use the generic fortran wrapper not F77
            if getattr(pkg, "find_mpi_fortan77", False):
                args.append(pkg.define("MPI_Fortran_COMPILER", pkg.spec["mpi"].mpif77))
            else:
                args.append(pkg.define("MPI_Fortran_COMPILER", pkg.spec["mpi"].mpifc))

    def test_mpi_hello(self):
        """build and run mpi hello world"""
        for lang in ("c", "f"):
            filename = self.test_suite.current_test_data_dir.join("mpi_hello." + lang)

            compiler_var = "MPICC" if lang == "c" else "MPIF90"
            compiler = which(os.environ[compiler_var])
            mpirun = which(self.prefix.bin.mpirun)

            exe_name = "mpi_hello_%s" % lang

            with test_part(self, f"test_mpi_hello_{lang}", purpose=f"build and run {filename}"):
                compiler("-o", exe_name, filename)
                out = mpirun("-np", "1", exe_name, output=str.split, error=str.split)
                expected = [r"Hello world! From rank \s*0 of \s*1"]
                check_outputs(expected, out)
