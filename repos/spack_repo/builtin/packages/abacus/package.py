# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import re

from spack_repo.builtin.build_systems import makefile
from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Abacus(CMakePackage, MakefilePackage):
    """ABACUS (Atomic-orbital Based Ab-initio Computation at UStc)
    is an open-source computer code package aiming
    for large-scale electronic-structure simulations
    from first principles"""

    homepage = "http://abacus.ustc.edu.cn/"
    url = "https://github.com/abacusmodeling/abacus-develop/archive/refs/tags/v3.9.0.19.tar.gz"
    git = "https://github.com/abacusmodeling/abacus-develop.git"

    maintainers("bitllion")

    license("LGPL-3.0-or-later")

    version("develop", branch="develop")
    version("3.10.1", sha256="06873eba8a4e0bc085177a6580455b28e4b62ea8a18f8afe71a02105756d91a0")
    version("3.9.0.19", sha256="c985af3d8ac6edb5767b7a094ac2fd2e0ea70b46cf353cd5a4b60096b289939d")
    version(
        "2.2.3",
        sha256="88dbf6a3bdd907df3e097637ec8e51fde13e2f5e0b44f3667443195481320edf",
        deprecated=True,
    )
    version(
        "2.2.2",
        sha256="4a7cf2ec6e43dd5c53d5f877a941367074f4714d93c1977a719782957916169e",
        deprecated=True,
    )
    version(
        "2.2.1",
        sha256="14feca1d8d1ce025d3f263b85ebfbebc1a1efff704b6490e95b07603c55c1d63",
        deprecated=True,
    )
    version(
        "2.2.0",
        sha256="09d4a2508d903121d29813a85791eeb3a905acbe1c5664b8a88903f8eda64b8f",
        deprecated=True,
    )

    variant("openmp", default=True, description="Enable OpenMP support")
    variant("lcao", default=True, description="Enable LCAO algorithm")
    variant("elpa", default=True, description="Enable ELPA support")
    variant("libxc", default=True, description="Enable LibXC support")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")
    depends_on("mpi")
    depends_on("cereal")
    depends_on("fftw+openmp", when="+openmp")
    depends_on("fftw~openmp", when="~openmp")
    depends_on("elpa", when="+elpa")
    depends_on("libxc", when="+libxc")
    depends_on("openblas", when="build_system=cmake")
    depends_on("mkl", when="build_system=makefile")
    depends_on("cmake", type="build", when="build_system=cmake")

    build_system(conditional("cmake", when="@3.0.0:"), "makefile", default="cmake")

    def cmake_args(self):
        args = [
            self.define("ENABLE_MPI", True),
            self.define("GIT_SUBMODULE", False),
            self.define_from_variant("USE_OPENMP", "openmp"),
            self.define_from_variant("ENABLE_LCAO", "lcao"),
            self.define_from_variant("USE_ELPA", "elpa"),
            self.define_from_variant("ENABLE_LIBXC", "libxc"),
        ]
        return args


class MakefileBuilder(makefile.MakefileBuilder):
    @property
    def build_directory(self):
        return join_path(self.stage.source_path, "source")

    def edit(self, pkg, spec, prefix):
        if spec.satisfies("+openmp"):
            inc_var = "_openmp-"
            system_var = "ELPA_LIB = -L${ELPA_LIB_DIR} -lelpa_openmp -Wl,-rpath=${ELPA_LIB_DIR}"
        else:
            inc_var = "-"
            system_var = "ELPA_LIB = -L${ELPA_LIB_DIR} -lelpa -Wl,-rpath=${ELPA_LIB_DIR}"

        tempInc = f"""
FORTRAN = ifort
CPLUSPLUS = icpc
CPLUSPLUS_MPI = mpiicpc
LAPACK_DIR = $(MKLROOT)
FFTW_DIR = {spec["fftw"].prefix}
ELPA_DIR = {spec["elpa"].prefix}
ELPA_INCLUDE = -I${{ELPA_DIR}}/include/elpa{inc_var}{spec["elpa"].version}
CEREAL_DIR = {spec["cereal"].prefix}
OBJ_DIR = obj
OBJ_DIR_serial = obj
NP      = 14
"""

        with open(join_path(self.build_directory, "Makefile.vars"), "w") as f:
            f.write(tempInc)

        lineList = []
        Pattern1 = re.compile("^ELPA_INCLUDE_DIR")
        Pattern2 = re.compile("^ELPA_LIB\\s*= ")
        with open(join_path(self.build_directory, "Makefile.system"), "r") as f:
            while True:
                line = f.readline()
                if not line:
                    break
                elif Pattern1.search(line):
                    pass
                elif Pattern2.search(line):
                    pass
                else:
                    lineList.append(line)
        with open(join_path(self.build_directory, "Makefile.system"), "w") as f:
            for i in lineList:
                f.write(i)

        with open(join_path(self.build_directory, "Makefile.system"), "a") as f:
            f.write(system_var)

    def install(self, pkg, spec, prefix):
        install_tree("bin", prefix.bin)
