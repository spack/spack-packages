# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Clapack(MakefilePackage):
    """CLAPACK is a f2c'ed version of LAPACK 3.2.1.

       The CLAPACK library was built using a Fortran to C conversion utility
    called f2c.  The entire Fortran 77 LAPACK library is run through f2c to
    obtain C code, and then modified to improve readability.  CLAPACK's goal
    is to provide LAPACK for someone who does not have access to a Fortran
    compiler."""

    homepage = "https://www.netlib.org/clapack/"
    url = "https://www.netlib.org/clapack/clapack.tgz"

    license("BSD-3-Clause")

    version("3.2.1", sha256="6dc4c382164beec8aaed8fd2acc36ad24232c406eda6db462bd4c41d5e455fac")

    depends_on("c", type="build")  # generated

    build_targets = ["f2clib", "blaslib", "lib"]

    def edit(self, spec, prefix):
        copy("make.inc.example", "make.inc")

    def install(self, spec, prefix):
        install_tree(".", prefix)
