# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems import cmake, meson
from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.meson import MesonPackage

from spack.package import *


class Mstore(MesonPackage, CMakePackage):
    """
    Molecular structure store for testing
    """

    homepage = "https://github.com/grimme-lab/mstore"
    url = "https://github.com/grimme-lab/mstore/releases/download/v0.3.0/mstore-0.3.0.tar.xz"
    git = "https://github.com/grimme-lab/mstore.git"

    maintainers("awvwgk")

    license("LGPL-3.0-or-later")

    build_system("cmake", "meson", default="meson")

    version("main", branch="main")
    version("0.3.0", sha256="8cbae54a47339de0f47457d7d0931fb5ac23a6cfc8b54872b925528cf5138523")
    version("0.2.0", sha256="932ec27cb327f7bfcdc316ae7d39a13cff03b95946bda79b52fd2fa43c4fd4d4")

    variant("openmp", default=True, description="Use OpenMP parallelisation")

    depends_on("c", type="build")
    depends_on("fortran", type="build")

    depends_on("meson@0.57.1:", type="build")  # mesonbuild/meson#8377
    depends_on("pkgconfig", type="build")

    for build_system in ["cmake", "meson"]:
        depends_on(f"mctc-lib build_system={build_system}", when=f"build_system={build_system}")


class MesonBuilder(meson.MesonBuilder):
    def meson_args(self):
        return ["-Dopenmp={0}".format(str("+openmp" in self.spec).lower())]


class CMakeBuilder(cmake.CMakeBuilder):
    def cmake_args(self):
        return [self.define_from_variant("WITH_OpenMP", "openmp")]
