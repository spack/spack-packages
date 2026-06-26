# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Macaulay2(AutotoolsPackage):
    """
    Macaulay2 is a software system devoted to supporting research in
    algebraic geometry and commutative algebra. It provides a specialized
    programming language designed for computations with polynomial rings,
    ideals, modules, and other algebraic structures, with a particular
    emphasis on Gröbner basis techniques.
    """

    homepage = "https://macaulay2.com/"
    url = "https://macaulay2.com/Downloads/SourceCode/Macaulay2-1.25.11.tar.gz"

    maintainers("d-torrance")

    license("GPL-2.0-or-later", checked_by="d-torrance")

    version("1.26.06", sha256="9ba54041626f6364036f84b4168704d74136d1bec2dbe08d9d0fb3fef2a0c854")
    version("1.26.05", sha256="a76213b4a23542abe5742a4d2b782e26ee5f3f9b1f6a2fc3a992615cc3aa3431")
    version("1.25.11", sha256="ecee06ea456f87d8182bdaf59f9e2f4a330d861516ab7d00faf9f37699ddeb58")

    # compilers
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")

    # libraries
    depends_on("bdw-gc threads=posix +cxx")
    depends_on("blas")
    depends_on("boost+regex")
    depends_on("cddlib")
    depends_on("eigen")
    depends_on("singular-factory")
    depends_on("fflas-ffpack")
    depends_on("flint")
    depends_on("fplll")
    depends_on("frobby")
    depends_on("gdbm")
    depends_on("givaro")
    depends_on("glpk")
    depends_on("gmp")
    depends_on("googletest")
    depends_on("jansson", when="@1.26.05:")
    depends_on("lapack")
    depends_on("mathic")
    depends_on("mathicgb")
    depends_on("memtailor")
    depends_on("mpfi")
    depends_on("mpfr")
    depends_on("mpsolve")
    depends_on("ncurses")
    depends_on("normaliz")
    depends_on("ntl")
    depends_on("python", type=("build", "link", "run"))
    depends_on("tbb")

    # build-only programs
    depends_on("bison", type="build")
    depends_on("diffutils", type="build")
    depends_on("flex", type="build")
    depends_on("pkgconfig", type="build")

    # programs
    depends_on("4ti2", type=("build", "run"))
    depends_on("cohomcalg", type=("build", "run"))
    depends_on("csdp", type=("build", "run"))
    depends_on("gfan", type=("build", "run"))
    depends_on("lrslib", type=("build", "run"))
    depends_on("msolve", type=("build", "run"))
    depends_on("nauty", type=("build", "run"))
    depends_on("topcom", type=("build", "run"))

    # drop minimum version of gfan (0.8 can't be built w/ older compilers)
    patch("allow-older-gfan.patch", when="@1.26.06")

    configure_directory = "M2"

    def configure_args(self) -> List[str]:
        return [
            "--with-system-libs",
            "--with-fplll",
            "--enable-documentation=download",
            f"--with-boost-libdir={self.spec['boost'].prefix.lib}",
            f"CPPFLAGS=-I{self.spec['cddlib'].prefix.include}/cddlib",
        ]
