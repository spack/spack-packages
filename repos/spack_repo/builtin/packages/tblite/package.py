# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems import cmake, meson
from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.meson import MesonPackage

from spack.package import *


class Tblite(CMakePackage, MesonPackage):
    """Light-weight tight-binding framework"""

    homepage = "https://tblite.readthedocs.io"
    url = "https://github.com/tblite/tblite/releases/download/v0.3.0/tblite-0.3.0.tar.xz"
    git = "https://github.com/tblite/tblite.git"

    maintainers("awvwgk")

    license("LGPL-3.0-or-later")

    version("main", branch="main")
    version("0.6.0", sha256="372281aedb89234168d00eb691addb303197a9462a9c55d145c835f2cf5e8b42")
    version("0.5.0", sha256="e8a70b72ed0a0db0621c7958c63667a9cd008c97c868a4a417ff1bc262052ea8")
    version("0.4.0", sha256="5c2249b568bfd3b987d3b28f2cbfddd5c37f675b646e17c1e750428380af464b")
    version("0.3.0", sha256="46d77c120501ac55ed6a64dea8778d6593b26fb0653c591f8e8c985e35884f0a")

    build_system("cmake", "meson", default="meson")

    variant("shared", default=True, description="Build shared libraries")
    variant("openmp", default=True, description="Use OpenMP parallelisation")
    variant("python", default=False, description="Build Python extension module")
    variant("trexio", default=False, description="Enable TREXIO support", when="@0.7.0:")
    variant("hdf5", default=False, description="Enable HDF5 support", when="@0.7.0:")
    # variant("ddx", default=False, description="Enable DDX support", when="@0.7.0:")

    depends_on("c", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    depends_on("blas")
    depends_on("lapack")
    depends_on("trexio", when="+trexio")
    depends_on("hdf5", when="+hdf5")
    # depends_on("ddx", when="+ddx")

    for build_system in ["cmake", "meson"]:
        depends_on(
            f"mctc-lib@0.3: build_system={build_system}", when=f"build_system={build_system}"
        )
        depends_on(
            f"simple-dftd3@0.3: build_system={build_system}", when=f"build_system={build_system}"
        )
        depends_on(f"dftd4@3: build_system={build_system}", when=f"build_system={build_system}")
        depends_on(f"toml-f build_system={build_system}", when=f"build_system={build_system}")

    depends_on("dftd4@:3.7", when="@:0.5")
    depends_on("meson@0.57.2:", type="build", when="build_system=meson")  # mesonbuild/meson#8377
    depends_on("pkgconfig", type="build")
    depends_on("py-cffi", when="+python")
    depends_on("py-numpy", when="+python")
    depends_on("py-setuptools", type="build", when="+python")
    depends_on("python@3.6:", when="+python")

    extends("python", when="+python")


class MesonBuilder(meson.MesonBuilder):
    def meson_args(self):
        lapack = self.spec["lapack"].libs.names[0]
        if lapack == "lapack":
            lapack = "netlib"
        elif lapack.startswith("mkl"):
            lapack = "mkl"
        elif lapack != "openblas":
            lapack = "auto"

        args = [
            "-Ddefault_library={0}".format("shared" if "+shared" in self.spec else "static"),
            "-Dlapack={0}".format(lapack),
            "-Dopenmp={0}".format(str("+openmp" in self.spec).lower()),
            "-Dpython={0}".format(str("+python" in self.spec).lower()),
        ]
        if self.spec.satisfies("@0.7.0:"):
            args += [
                "-Dtrexio={0}".format("enabled" if "+trexio" in self.spec else "disabled"),
                "-Dhdf5={0}".format("enabled" if "+hdf5" in self.spec else "disabled"),
                "-Dddx=false",
            ]
        return args


class CMakeBuilder(cmake.CMakeBuilder):
    def cmake_args(self):
        args = [
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define_from_variant("WITH_OpenMP", "openmp"),
        ]
        if self.spec.satisfies("@0.7.0:"):
            args += [
                self.define_from_variant("TBLITE_WITH_TREXIO", "trexio"),
                self.define_from_variant("TBLITE_WITH_HDF5", "hdf5"),
                self.define("TBLITE_WITH_DDX", False),
            ]
        return args
