# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Fvtkhdf(CMakePackage):
    """Modern Fortran library for writing VTKHDF format files."""

    maintainers("nncarlson")

    homepage = "https://github.com/nncarlson/fvtkhdf"
    url = "https://github.com/nncarlson/fvtkhdf/releases/download/v0.5.0/fvtkhdf-0.5.0.tar.gz"
    git = "https://github.com/nncarlson/fvtkhdf.git"

    license("BSD-2-Clause")

    version("0.5.0", sha256="01e2f26a495570418f5d53dc5577eedb74969c7837fe53f6e749522d5f4b58e3")

    patch("remove-unneeded-hdf5-hl.patch", when="@0.5.0")

    variant("shared", default=True, description="Build shared libraries")

    depends_on("c", type="build")
    depends_on("fortran", type="build")
    depends_on("cmake@3.28:", type="build")
    depends_on("mpi")
    depends_on("hdf5@1.14:1.14+mpi")
    depends_on("python@3:", type="build")
    depends_on("py-fypp", type="build")

    def cmake_args(self):
        return [
            self.define("ENABLE_MPI", True),
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define("BUILD_HTML", False),
            self.define("BUILD_EXAMPLES", False),
            self.define("BUILD_TESTING", False),
        ]
