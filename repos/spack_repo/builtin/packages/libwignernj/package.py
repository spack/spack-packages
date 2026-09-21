# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Libwignernj(CMakePackage):
    """
    Exact evaluation of Wigner 3j, 6j, and 9j symbols, Clebsch-Gordan coefficients,
    Racah W-coefficients, Fano X-coefficients, and Gaunt coefficients
    """

    homepage = "https://github.com/susilehtola/libwignernj"
    git = "https://github.com/susilehtola/libwignernj.git"
    url = "https://github.com/susilehtola/libwignernj/archive/refs/tags/v0.0.0.tar.gz"

    supplier = "Susi Lehtola"

    maintainers("RMeli")

    license("BSD-3-Clause", checked_by="RMeli")

    version("0.8.0", sha256="7220cea92652040d6456aba92ff151124d9c69ce8695840490c18dd25a0da80c")

    variant("shared", default=True, description="Build shared library")
    variant("fortran", default=True, description="Build Fortran interface")
    variant("mpfr", default=False, description="Build MPFR arbitrary-precision interface")
    variant("quadmath", default=False, description="Build libquadmath/__float128 interface")
    variant("flint", default=False, description="Use FLINT/GMP/MPFR for bigint backend")
    variant("tests", default=False, description="Build test suite")
    variant("examples", default=False, description="Build test suite")
    variant("cxx-tests", default=False, description="Build C++ header tests")

    depends_on("c", type="build")
    depends_on("cxx", type="build", when="+cxx-tests")
    depends_on("fortran", type="build", when="+fortran")

    depends_on("cmake@3.16:", type="build")

    depends_on("mpfr", when="+mpfr")
    depends_on("flint", when="+flint")

    def cmake_args(self):
        args = [
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define_from_variant("WIGNERNJ_BUILD_FORTRAN", "fortran"),
            self.define_from_variant("WIGNERNJ_BUILD_MPFR", "mpfr"),
            self.define_from_variant("WIGNERNJ_BUILD_QUADMATH", "quadmath"),
            self.define_from_variant("WIGNERNJ_BUILD_FLINT", "flint"),
            self.define_from_variant("WIGNERNJ_BUILD_TESTS", "tests"),
            self.define_from_variant("WIGNERNJ_BUILD_EXAMPLES", "examples"),
            self.define_from_variant("WIGNERNJ_BUILD_CXX_TEST", "cxx-tests"),
        ]
        return args
