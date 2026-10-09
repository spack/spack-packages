# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
from shutil import copyfile

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Nek5000(Package):
    """A fast and scalable high-order solver for computational fluid
    dynamics"""

    homepage = "https://nek5000.mcs.anl.gov/"
    url = "https://github.com/Nek5000/Nek5000/archive/v17.0.tar.gz"
    git = "https://github.com/Nek5000/Nek5000.git"

    tags = [
        "cfd",
        "flow",
        "hpc",
        "solver",
        "navier-stokes",
        "spectral-elements",
        "fluid",
        "ecp",
        "ecp-apps",
        "e4s",
    ]

    version("develop", branch="master")
    version("17.0", sha256="4d8d4793ce3c926c54e09a5a5968fa959fe0ba46bd2e6b8043e099528ee35a60")
    version("19.0", sha256="db129877a10ff568d49edc77cf65f9e732eecb1fce10edbd91ffc5ac10c41ad6")

    # MPI, Profiling and Visit variants
    variant("mpi", default=True, description="Build with MPI.")
    variant("profiling", default=True, description="Build with profiling data.")
    variant("visit", default=False, description="Build with Visit.")

    # TODO: add a variant 'blas' or 'external-blas' to enable the usage of
    #       Spack installed/configured blas.

    # Dependencies
    depends_on("c", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    depends_on("mpi", when="+mpi")

    depends_on("visit", when="+visit")

    patch("add_fjfortran.patch", when="%fj")

    @run_after("install")
    def check_install(self):
        with working_dir("short_tests/eddy"):
            f_size = join_path(os.getcwd(), "SIZE")
            f_size_legacy = join_path(os.getcwd(), "SIZE.legacy")
            if not os.access(f_size, os.F_OK):
                if os.access(f_size_legacy, os.F_OK):
                    copyfile(f_size_legacy, f_size)
                else:
                    raise RuntimeError("Can not find {0}".format(f_size))

            os.system(join_path(self.prefix.bin, "makenek") + " eddy_uv")
            if not os.path.isfile(join_path(os.getcwd(), "nek5000")):
                msg = "Cannot build example: short_tests/eddy."
                raise RuntimeError(msg)

    def install(self, spec, prefix):
        bin_dir = "bin"

        # The installed 'makenek' runs outside a Spack build environment, where wrappers fail.
        fc = spec["fortran"].package.fortran
        cc = spec["c"].package.cc

        # the flag lists stored on the spec must not be modified in place
        fflags = list(spec.compiler_flags["fflags"])
        cflags = list(spec.compiler_flags["cflags"])

        if spec.satisfies("%fortran=xl"):
            # Use '-qextname' to add underscores.
            # Use '-WF,-qnotrigraph' to fix an error about a string: '... ??'
            fflags += ["-qextname", "-WF,-qnotrigraph"]

        if spec.satisfies("%fortran=gcc"):
            # Use '-std=legacy' to suppress an error that was a warning in older gfortran.
            fflags += ["-std=legacy"]

        fflags = " ".join(fflags)
        cflags = " ".join(cflags)

        with working_dir(bin_dir):
            if spec.satisfies("+mpi"):
                fc = spec["mpi"].mpif77
                cc = spec["mpi"].mpicc
            else:
                filter_file(r"^#MPI=0", "MPI=0", "makenek")

            # The nekmpi wrapper uses srun when OpenMPI is not built with mpiexec
            if spec.satisfies("^openmpi~legacylaunchers"):
                filter_file(r"mpiexec -np", "srun -n", "nekmpi")

            if not spec.satisfies("+profiling"):
                filter_file(r"^#PROFILING=0", "PROFILING=0", "makenek")

            if spec.satisfies("+visit"):
                filter_file(r"^#VISIT=1", "VISIT=1", "makenek")
                filter_file(
                    r"^#VISIT_INSTALL=.*",
                    'VISIT_INSTALL="' + spec["visit"].prefix.bin + '"',
                    "makenek",
                )

            # Update the makenek to use correct compilers and
            # Nek5000 source.
            filter_file(r"^#FC\s*=.*", 'FC="{0}"'.format(fc), "makenek")
            filter_file(r"^#CC\s*=.*", 'CC="{0}"'.format(cc), "makenek")
            if self.spec.version == Version("17.0"):
                filter_file(
                    r"^#SOURCE_ROOT\s*=\"\$H.*",
                    'SOURCE_ROOT="' + prefix.bin.Nek5000 + '"',
                    "makenek",
                )
            else:
                filter_file(
                    r"^#NEK_SOURCE_ROOT\s*=\"\$H.*",
                    'NEK_SOURCE_ROOT="' + prefix.bin.Nek5000 + '"',
                    "makenek",
                )

            if fflags:
                filter_file(r"^#FFLAGS=.*", 'FFLAGS+=" {0}"'.format(fflags), "makenek")
            if cflags:
                filter_file(r"^#CFLAGS=.*", 'CFLAGS+=" {0}"'.format(cflags), "makenek")

        with working_dir("core"):
            if spec.satisfies("%fortran=xl"):
                # 'xl' adds underscores with '-qextname', so patch the underscore check.
                filter_file(r"^\$FCcomp -c ", "$FCcomp -qextname -c ", "makenek.inc")
                filter_file(
                    r"\$\(FC\) -c \$\(L0\)", "$(FC) -c -qextname $(L0)", "makefile.template"
                )

        # Install Nek5000/bin in prefix/bin
        install_tree(bin_dir, prefix.bin)

        # Copy Nek5000 source to prefix/bin
        install_tree(self.stage.source_path, prefix.bin.Nek5000)
