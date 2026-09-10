# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Fortuno(CMakePackage):
    """Flexible & extensible object oriented Fortran unit testing framework for
    serial, MPI-parallel and coarray-parallel projects"""

    homepage = "https://fortuno.readthedocs.io/en/latest/"
    url = "https://github.com/fortuno-repos/fortuno/archive/refs/tags/v0.1.0.tar.gz"
    git = "https://github.com/fortuno-repos/fortuno.git"

    maintainers("SeanBryan51")

    license("BSD-2-Clause-Patent", checked_by="SeanBryan51")

    version("0.1.0", sha256="9639be1159e03d5e31032af6aa9d4f8483d1f3df0b84a3b43a564273a68ff5e1")

    variant("serial", default=True, description="Build serial interface")
    variant("mpi", default=False, description="Build MPI interface")
    variant("coarray", default=False, description="Build coarray interface")
    variant("shared", default=True, description="Build as shared library")

    depends_on("fortran", type="build")
    depends_on("cmake@3.22:", type="build")
    depends_on("mpi", when="+mpi")
    depends_on("opencoarrays", when="+coarray%gcc")

    def cmake_args(self):
        args = []
        args.append(self.define_from_variant("FORTUNO_WITH_SERIAL", "serial"))
        args.append(self.define_from_variant("FORTUNO_WITH_MPI", "mpi"))
        args.append(self.define_from_variant("FORTUNO_WITH_COARRAY", "coarray"))
        args.append(self.define_from_variant("FORTUNO_BUILD_SHARED_LIBS", "shared"))
        args.append(self.define("FORTUNO_WITH_TESTS", self.run_tests))
        args.append(self.define("FORTUNO_INSTALL", True))
        args.append(self.define("FORTUNO_WITH_EXAMPLES", False))
        if self.spec.satisfies("^opencoarrays"):
            args.append(self.define("CMAKE_Fortran_COMPILER", "caf"))
            args.append(self.define("FORTUNO_FFLAGS_COARRAY", ""))
            args.append(self.define("FORTUNO_LDFLAGS_COARRAY", ""))
        return args
