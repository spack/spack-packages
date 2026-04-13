# Copyright 2013-2026 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
import glob
import math
import os
import re

from spack_repo.builtin.build_systems import cmake, makefile

from spack.package import *


class Castep(cmake.CMakePackage, makefile.MakefilePackage):
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

    maintainers("pjpbyrne")

    # Versions
    version("26.11", sha256="cd38ec9e87fd92b91fe7910179acad6486ee57935832846959151ec406fb5fb6")
    version("25.12", sha256="e21177bfe4cb3f3d098b666c90771e3da2826503b002b8e325e3ca1e230cfc7d")
    version("25.11", sha256="af6851a973ef83bbd725f6f33ff7616dd9d589bd75cf74cd106b13c3369167f6")
    version("24.1", sha256="97d77a4f3ce3f5c5b87e812f15a2c2cb23918acd7034c91a872b6d66ea0f7dbb")
    version("23.1", sha256="7fba0450d3fd71586c8498ce51975bbdde923759ab298a656409280c29bf45b5")
    version("22.11", sha256="aca3fc2207c677561293585a4edaf233676a759c5beb8389cf938411226ef1f5")
    version("21.11", sha256="d909936a51dd3dff7a0847c2597175b05c8d0018d5afe416737499408914728f")
    version(
        "19.1.1.rc2", sha256="1fce21dc604774e11b5194d5f30df8a0510afddc16daf3f8b9bbb3f62748f86a"
    )

    build_system(
        conditional("cmake", when="@23:"), conditional("makefile", when="@:22"), default="cmake"
    )

    parallel = True

    with when("build_system=makefile"):
        depends_on("gmake@3.82:", when="@21:21", type="build")
        depends_on("gmake@4.2:", when="@22:", type="build")
        requires("%gcc@9:", when="@25.12:")
        requires("%gcc@4.9.1:", when="@21.11:")

    with when("build_system=cmake"):
        cmake.generator("ninja", "make", default="make")
        depends_on("pkgconfig", type="build")
        depends_on("cmake@3.25:", type="build", when="generator=make")
        depends_on("gmake@4.2:", type="build", when="generator=make")
        depends_on("ninja", type="build", when="generator=ninja")
        depends_on("cmake@3.27.9:", type="build", when="generator=ninja")

    # Variants
    variant("mpi", description="Build with MPI parallelism", default=True)
    variant(
        "portable",
        default=True,
        description="Build a generic executable which ought to run on most CPUs",
    )

    with when("build_system=cmake"):
        variant(
            "build_type",
            default="fast",
            description="CASTEP build type",
            values=("debug", "intermediate", "fast"),
        )
        variant("libxc", description="Build with libXC support", default=False)
        variant("openmp", description="Use OpenMP threading", default=True)
        variant("grimmed3", default=True, description="Use Grimme D3 functionals")
        variant("grimmed4", default=True, description="Use Grimme D4 functionals")
        variant("dlmg", default=True, description="Use DLMG Functionality functionals")
        variant("openmp", default=True, description="Use OpenMP threading")
        variant("tools", default=True, description="Build the executable auxilliary programs")
        variant(
            "utilities", default=True, description="Build the third-party scripts and utilities"
        )

    # Depedencies
    depends_on("c", type="build")
    depends_on("fortran", type="build")
    depends_on("awk@3:", type="build")
    extends("python", type=("build", "run"))
    extends("python@:3.11", type=("build", "run"), when="@:22")
    depends_on("py-pip", type="build")
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-setuptools", type=("build", "run"), when="@:24")
    depends_on("perl", type=("build", "run"))
    depends_on("blas")
    depends_on("lapack")
    depends_on("fftw-api@3")

    # MPI must have fortran bindings
    with when("+mpi"):
        depends_on("mpi", type=("build", "link", "run"))
        depends_on("mpich+fortran", when="%mpi=mpich")
        depends_on("openmpi+fortran", when="%mpi=openmpi")

    # GCC 9+ for f2008 features
    requires("%gcc@9:", when="@25.12: %gcc")
    requires("%gcc@4.9.1:", when="@21.11: %gcc")

    # To use FFT mkl option only allowed when also using mkl as lapack/blas
    requires(
        "%lapack=intel-oneapi-mkl",
        when="%fftw-api=intel-oneapi-mkl",
        msg="MKL must be used as the BLAS/LAPACK library to use it for FFTs",
    )

    # Block older compiler versions that are not supported (and explicitly do not work)
    conflicts("%oneapi", when="@:23", msg="Intel LLVM requires CASTEP 24 or newer")
    conflicts("%llvm", when="@:25", msg="LLVM(Flang) requires CASTEP 26 or newer")

    # Fortran dependencies must be compiled with the same compiler
    sub_packages = {
        "mpi": ["openmpi", "mpich"],
        "blas": ["openblas", "flexiblas"],
        "lapack": ["openblas", "flexiblas"],
        "fftw-api": ["fftw"],
    }

    for compiler in ["gcc", "llvm", "intel", "oneapi"]:
        for virtual_package, package_providers in sub_packages.items():
            for actual_package in package_providers:
                depends_on(
                    f"{actual_package}%fortran={compiler}",
                    when=f"%fortran={compiler} %{virtual_package}={actual_package}",
                )

    # Special rules for mkl
    requires("%fortran=intel", "%fortran=oneapi", "%fortran=gcc", when="%lapack=intel-oneapi-mkl")
    requires(
        "%fortran=intel", "%fortran=oneapi", "%fortran=gcc", when="%fftw-api=intel-oneapi-mkl"
    )
    requires("%fortran=intel", "%fortran=oneapi", "%fortran=gcc", when="%mpi=intel-oneapi-mpi")

    # Patches to fix the python script installation
    patch("Fix-castepconv-strings-with-invalid-escape-character.patch")
    patch("Fixed-arguments-not-being-passed-to-python-scripts.patch", when="@=26.11")
    patch("Fix_python_install_25.patch", when="@25")
    patch("Fix_python_install_24.patch", when="@24")
    patch("Fix_python_install_23.patch", when="@23")

    sanity_check_is_file = [join_path("bin", "castep.mpi")]

    @property
    def castep_exe(self):
        """Get the main executable filename"""
        if self.spec.satisfies("+mpi"):
            return "castep.mpi"
        else:
            return "castep.serial"

    @property
    def sanity_check_is_file(self):
        """List of files to check on a completed install"""
        # Main castep executable
        bin_files = [self.castep_exe]

        # Fortran tool check
        if self.spec.satisfies("+tools"):
            bin_files.append("phonon_kpoints")

        if self.spec.satisfies("+utilities"):
            # Python script check
            bin_files.append("cif2cell")

            # Perl script check
            bin_files.append("dos.pl")

        return [join_path("bin", f) for f in bin_files]

    #################################################
    # Tests that are run at build/installation time #
    #################################################

    def check(self) -> None:
        """Run the check-quick target."""
        with working_dir(self.build_directory):
            if self.generator == "Unix Makefiles":
                self._if_make_target_execute("check-quick")
            elif self.generator == "Ninja":
                self._if_ninja_target_execute("check-quick")

    @run_after("install")
    @on_package_attributes(run_tests=True)
    def test_castep_executable(self):
        """Test that the executable launches and returns a version number"""
        spec_version = re.compile(r"CASTEP version: " + str(self.spec.version))
        castep = Executable(join_path(self.prefix.bin, self.castep_exe))
        output = castep("-v", output=str)
        check_outputs(spec_version, output)

    @run_after("install")
    def prepare_postinstal_tests(self):
        """Store a simple test of basic castep functionality"""
        cache_extra_test_sources(self, join_path("Test", "Electronic", "Si2-den"))

    ############################################
    # Tests that can be run at some later time #
    ############################################

    def test_castep_si2(self):
        """Run the Si2 test case and verify the total energy"""
        test_dir = join_path(
            self.test_suite.current_test_cache_dir, "Test", "Electronic", "Si2-den"
        )
        energy_re = re.compile(r"Final energy =\s+(\S+)\s+eV")
        seedname = "Si2-den-NCP"

        def get_energy_from_file(filename: str) -> float:
            with open(filename) as f:
                for line in f:
                    if m := re.search(energy_re, line):
                        return float(m.group(1))
            raise KeyError(f"Total energy not found in {filename}")

        with working_dir(test_dir):
            # Get reference data
            bench_file = glob.glob("benchmark*param")[0]
            benchmark_energy = get_energy_from_file(bench_file)

            # Get castep data
            castep = which(self.castep_exe, required=True)
            castep(seedname)
            castep_energy = get_energy_from_file(f"{seedname}.castep")

            assert math.isclose(castep_energy, benchmark_energy, rel_tol=1e-6)

    def test_elastics_wrapper(self):
        """Check that the python script elastics.py installed correctly"""
        if self.spec.satisfies("+utilities"):
            elastics = Executable(join_path(self.prefix.bin, "elastics.py"))
            elastics("-h")
        else:
            raise SkipTest("Test only available with utilities installed.")

    def test_castepconv_wrapper(self):
        """
        Check that the python script wrapper installed correctly
        and passes arguments for castepconv.py
        """
        if self.spec.satisfies("+utilities"):
            castepconv = Executable(join_path(self.prefix.bin, "castepconv.py"))
            castepconv("-h")
        else:
            raise SkipTest("Test only available with utilities installed.")


class CMakeBuilder(cmake.CMakeBuilder):
    @property
    def build_targets(self):
        targetlist = ["castep"]
        if self.spec.satisfies("+tools"):
            targetlist.append("tools")
        if self.spec.satisfies("+utilities"):
            targetlist.append("utilities")
        return targetlist

    def cmake_args(self):

        # Internal names for blas libraries, otherwise castep will prefer mkl if it is present
        castep_math_libs = {
            "openblas": "OpenBLAS",
            "intel-oneapi-mkl": "Intel",
            "atlas": "ATLAS",
            "flexiblas": "FlexiBLAS",
            "libflame": "FLAME",
            "amdlibflame": "FLAME",
            "nvhpc": "NVHPC",
            "cray-libsci": "SciLib",
            "blis": "BLIS",
            "amdblix": "BLIS",
            "essl": "ESSL",
        }

        # Internal name for fft libraries
        castep_fft_libs = {"intel-oneapi-mkl": "mkl", "fftw": "fftw3"}

        mathlib = castep_math_libs.get(self.spec["blas"].name, None)
        fftlib = castep_fft_libs.get(self.spec["fftw-api"].name, None)

        args = [
            "-DBUILD={0}".format(self.spec.variants["build_type"].value),
            self.define_from_variant("WITH_MPI", "mpi"),
            self.define_from_variant("WITH_LIBXC", "libxc"),
            self.define_from_variant("WITH_GRIMMED3", "grimmed3"),
            self.define_from_variant("WITH_GRIMMED4", "grimmed4"),
            self.define_from_variant("WITH_DLMG", "dlmg"),
            self.define_from_variant("WITH_OpenMP", "openmp"),
            self.define_from_variant("PORTABLE", "portable"),
            self.define("WITH_MACE", False),  # Seems to be broken
        ]

        # Specify lapack/blas and fftw precisely if known
        if mathlib:
            args.append(self.define("MATHLIBS", mathlib))

        if fftlib:
            args.append(self.define("FFT", fftlib))

        return args


class MakefileBuilder(makefile.MakefileBuilder):
    def edit(self, pkg, spec, prefix):
        if spec.satisfies("%gcc"):
            if self.spec.satisfies("@21:"):
                if spec.satisfies("%gcc@10:"):
                    platfile = FileFilter("obj/platforms/linux_x86_64_gfortran10.mk")
                else:
                    platfile = FileFilter("obj/platforms/linux_x86_64_gfortran.mk")
            elif self.spec.satisfies("@19:19"):
                if spec.satisfies("%gcc@9:"):
                    platfile = FileFilter("obj/platforms/linux_x86_64_gfortran9.0.mk")
                else:
                    platfile = FileFilter("obj/platforms/linux_x86_64_gfortran.mk")
                platfile.filter(r"MPIFLAGS = -DMPI", "MPIFLAGS = -fallow-argument-mismatch -DMPI")
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
                    if self.spec.satisfies("@21:") and spec.satisfies("%gcc@10:"):
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
