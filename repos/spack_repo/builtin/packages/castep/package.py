# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


import os

from spack_repo.builtin.build_systems import cmake, makefile
from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Castep(CMakePackage, MakefilePackage):
    """
    CASTEP is a leading code for calculating the
    properties of materials from first principles.
    Using density functional theory, it can simulate
    a wide range of properties of materials
    proprieties including energetics, structure at
    the atomic level, vibrational properties,
    electronic response properties etc.
    """

    homepage = "http://castep.org"
    url = f"file://{os.getcwd()}/CASTEP-25.12.tar.gz"
    manual_download = True

    version("25.12", sha256="e21177bfe4cb3f3d098b666c90771e3da2826503b002b8e325e3ca1e230cfc7d")
    version("21.11", sha256="d909936a51dd3dff7a0847c2597175b05c8d0018d5afe416737499408914728f")
    version(
        "19.1.1.rc2", sha256="1fce21dc604774e11b5194d5f30df8a0510afddc16daf3f8b9bbb3f62748f86a"
    )

    build_system(
        conditional("cmake", when="@25:"), conditional("makefile", when="@:21"), default="cmake"
    )

    # GCC 9+ for f2008 features
    requires("%gcc@9:", when="@25.12:")
    requires("%gcc@4.9.1:", when="@21.11:")

    variant("mpi", default=True, description="Enable MPI build")
    variant(
        "portable",
        default=True,
        description="Build a generic executable which ought to run on most CPUs",
    )

    with when("build_system=makefile"):
        depends_on("gmake@3.82:", when="@21:21", type="build")

    with when("build_system=cmake"):
        depends_on("cmake@3.18:", type="build")
        depends_on("pkgconfig", type="build")
        variant("grimmed3", default=True, description="Use Grimme D3 functionals")
        variant("grimmed4", default=True, description="Use Grimme D4 functionals")
        variant("dlmg", default=True, description="Use DLMG Functionality functionals")
        variant("openmp", default=True, description="Use OpenMP threading")
        variant("tools", default=True, description="Build the executable auxilliary programs")
        variant(
            "utilities", default=True, description="Build the third-party scripts and utilities"
        )

    depends_on("c", type="build")
    depends_on("fortran", type="build")

    depends_on("gcc@9:", when="@25:", type="build")
    depends_on("gcc@4.9:", when="@21.11:", type="build")
    extends("python@:3.11", type=("build", "run"))
    depends_on("py-pip", type="build")
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("perl", type=("build", "run"))
    depends_on("rsync", type="build")
    depends_on("blas")
    depends_on("lapack")
    depends_on("fftw-api")
    depends_on("mpi", type=("build", "link", "run"), when="+mpi")

    parallel = True


class CMakeBuilder(cmake.CMakeBuilder):

    @property
    def build_targets(self):
        spec = self.spec
        targetlist = ["castep"]
        if spec.satisfies("+tools"):
            targetlist.append("tools")
        if spec.satisfies("+utilities"):
            targetlist.append("utilities")
        return targetlist

    def cmake_args(self):
        args = [
            self.define_from_variant("WITH_MPI", "mpi"),
            self.define_from_variant("WITH_GRIMMED3", "grimmed3"),
            self.define_from_variant("WITH_GRIMMED4", "grimmed4"),
            self.define_from_variant("WITH_DLMG", "dlmg"),
            self.define_from_variant("WITH_OpenMP", "openmp"),
            self.define_from_variant("PORTABLE", "portable"),
        ]
        return args


class MakefileBuilder(makefile.MakefileBuilder):

    def edit(self, pkg, spec, prefix):
        if spec.satisfies("%gcc"):
            if self.spec.satisfies("@21:21"):
                if spec.satisfies("%gcc@10:"):
                    platfile = FileFilter("obj/platforms/linux_x86_64_gfortran10.mk")
                else:
                    platfile = FileFilter("obj/platforms/linux_x86_64_gfortran.mk")
            elif self.spec.satisfies("@19:19"):
                if spec.satisfies("%gcc@9:"):
                    platfile = FileFilter("obj/platforms/linux_x86_64_gfortran9.0.mk")
                else:
                    platfile = FileFilter("obj/platforms/linux_x86_64_gfortran.mk")
                dlmakefile.filter(
                    r"MPIFLAGS = -DMPI", "MPIFLAGS = -fallow-argument-mismatch -DMPI"
                )
                platfile.filter(r"^\s*FFLAGS_E\s*=.*", "FFLAGS_E = -fallow-argument-mismatch ")

            platfile.filter(r"^LD_FLAGS\s=.*$", "LD_FLAGS = $(OPT) -fopenmp")
        elif spec.satisfies("%intel"):
            if self.spec.satisfies("@20:"):
                platfile = FileFilter("obj/platforms/linux_x86_64_ifort.mk")
            else:
                platfile = FileFilter("obj/platforms/linux_x86_64_ifort19.mk")
            platfile.filter(r"^\s*OPT_CPU\s*=.*", "OPT_CPU = ")

    @property
    def build_targets(self):
        spec = self.spec
        targetlist = [f"PWD={self.stage.source_path}"]

        if spec.satisfies("+mpi"):
            targetlist.append("COMMS_ARCH=mpi")

        if spec.satisfies("+portable"):
            targetlist.append("TARGETCPU=portable")

        targetlist.append(f"FFTLIBDIR={spec['fftw-api'].prefix.lib}")
        targetlist.append(f"MATHLIBDIR={spec['blas'].prefix.lib}")

        if spec.satisfies("^mkl"):
            targetlist.append("FFT=mkl")
            if self.spec.satisfies("@20:"):
                targetlist.append("MATHLIBS=mkl")
            else:
                targetlist.append("MATHLIBS=mkl10")
        else:
            targetlist.append("FFT=fftw3")
            targetlist.append("MATHLIBS=openblas")

        if spec.satisfies("target=x86_64:"):
            if spec.satisfies("platform=linux"):
                if spec.satisfies("%gcc"):
                    if self.spec.satisfies("@21:21") and spec.satisfies("%gcc@10:"):
                        targetlist.append("ARCH=linux_x86_64_gfortran10")
                    elif self.spec.satisfies("@19:19") and spec.satisfies("%gcc@9:"):
                        targetlist.append("ARCH=linux_x86_64_gfortran9.0")
                    else:
                        targetlist.append("ARCH=linux_x86_64_gfortran")
                if spec.satisfies("%intel"):
                    if self.spec.satisfies("@20:"):
                        targetlist.append("ARCH=linux_x86_64_ifort")
                    else:
                        targetlist.append("ARCH=linux_x86_64_ifort19")

        return targetlist

    def install(self, pkg, spec, prefix):
        mkdirp(prefix.bin)
        make("install", "install-tools", *self.build_targets, "INSTALL_DIR={0}".format(prefix.bin))
