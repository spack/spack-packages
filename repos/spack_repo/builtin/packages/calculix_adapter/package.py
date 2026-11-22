# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import glob
import os

from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class CalculixAdapter(MakefilePackage, CudaPackage):
    """The preCICE adapter for the CalculiX finite-element solver. It builds the
    ccx_preCICE executable, which couples CalculiX to other solvers (e.g. an
    OpenFOAM fluid solver) through the preCICE coupling library for
    fluid-structure interaction."""

    homepage = "https://precice.org/adapter-calculix-overview.html"
    url = "https://github.com/precice/calculix-adapter/archive/refs/tags/v2.20.1.tar.gz"

    license("GPL-3.0-or-later")

    maintainers("failed33")

    version(
        "2.20.2",
        sha256="033f6e61e707283df708d3eda3c5930146bb7f8acd3a0469ab707e77cba30199",
    )
    version(
        "2.20.1",
        sha256="3372e0d66321c2173899e1db4841c6c4f3c16ffb99067c36dba04e8a34e35d39",
    )

    variant("pardiso", default=False, description="Use Intel oneMKL PARDISO")
    variant("pastix", default=False, description="Use the ILP64 GPU PaStiX4CalculiX solver")

    conflicts("+pastix", when="+pardiso")
    conflicts("~cuda", when="+pastix", msg="PaStiX4CalculiX requires CUDA")
    conflicts("cuda_arch=none", when="+pastix", msg="Select a CUDA architecture")
    conflicts("+cuda", when="~pastix", msg="CUDA is only used by PaStiX4CalculiX")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")
    depends_on("pkgconfig", type="build")

    # preCICE replaces parts of the CCX 2.20 source tree.
    resource(
        name="calculix",
        url="https://www.dhondt.de/ccx_2.20.src.tar.bz2",
        sha256="63bf6ea09e7edcae93e0145b1bb0579ea7ae82e046f6075a27c8145b72761bcf",
        placement="calculix",
    )
    depends_on("spooles", when="~pardiso ~pastix")
    depends_on("yaml-cpp", when="@:2.20.1")
    depends_on("arpack-ng~mpi")
    depends_on("blas")
    depends_on("lapack")
    depends_on("mpi")
    depends_on("precice@3:")

    requires("^[virtuals=blas,lapack] intel-oneapi-mkl~ilp64 threads=openmp", when="+pardiso")
    requires("^openblas~ilp64", when="~pastix ^[virtuals=blas,lapack] openblas")

    depends_on("pastix4calculix+cuda", when="+pastix")
    requires("^[virtuals=blas,lapack] openblas+ilp64 threads=openmp", when="+pastix")
    requires("%fortran=gcc", when="+pastix", msg="The ILP64 build uses GNU Fortran flags")
    for arch in CudaPackage.cuda_arch_values:
        depends_on(f"pastix4calculix+cuda cuda_arch={arch}", when=f"+pastix cuda_arch={arch}")

    patch("calculix-pastix-gpu.patch", working_dir="calculix", when="+pastix")
    patch("calculix-pastix-rebuild-csc.patch", working_dir="calculix", when="+pastix")
    patch("calculix-adapter-i8.patch", when="@=2.20.1,=2.20.2 +pastix")
    patch("calculix-adapter-i8-mesh-2.20.1.patch", when="@=2.20.1 +pastix")
    patch("calculix-adapter-i8-mesh-2.20.2.patch", when="@=2.20.2 +pastix")
    patch("calculix-adapter-numelements-init.patch", when="@=2.20.1")

    @property
    def ccx_source(self):
        return join_path(self.stage.source_path, "calculix", "ccx_2.20", "src")

    @property
    def build_targets(self):
        spec = self.spec
        cflags = [
            "-Wall -O3 -fopenmp $(INCLUDES) -DARCH=Linux -DARPACK -DMATRIXSTORAGE",
            "-Wno-error=int-conversion -Wno-error=implicit-function-declaration",
            "-Wno-error=implicit-int -Wno-error=incompatible-pointer-types",
        ]
        fflags = []
        if spec.satisfies("%gcc@10:"):
            fflags.append("-fallow-argument-mismatch")

        includes = ""
        solver_libs = ""
        library_specs = [
            spec["precice"],
            spec["arpack-ng"],
            spec["lapack"],
            spec["blas"],
        ]
        arpack_libs = [lib.libs.ld_flags for lib in library_specs[1:]]
        ccx = self.ccx_source
        if spec.satisfies("+pardiso"):
            cflags.append("-DPARDISO")
            mkl = spec["intel-oneapi-mkl"]
            includes = mkl.headers.include_flags
            arpack_libs = [
                spec["arpack-ng"].libs.ld_flags,
                mkl.libs.ld_flags,
            ]
        elif spec.satisfies("+pastix"):
            cflags.append("-DPASTIX -DLONGLONG -DPASTIX_FP32 -DPASTIX_GPU")
            fflags.append("-fdefault-integer-8")
            pastix = spec["pastix4calculix"]
            cuda = spec["cuda"]
            includes = f"-I{pastix.prefix.include} -I{cuda.prefix.include}"
            solver_libs = "$(shell pkg-config --libs pastix)"
            library_specs.extend([pastix, spec["parsec-pastix"]])
        else:
            cflags.append("-DSPOOLES -DUSE_MT")
            spooles = spec["spooles"].prefix
            includes = "-I" + spooles.include
            solver_libs = join_path(spooles.lib, "libspooles.a")

        targets = []
        if spec.satisfies("@:2.20.1"):
            yaml = spec["yaml-cpp"]
            library_specs.append(yaml)
            targets.extend(
                [
                    "YAML_INCLUDE=-I" + yaml.prefix.include,
                    "YAML_LIBS=" + yaml.libs.ld_flags,
                ]
            )

        # MPI Fortran wrappers do not necessarily inject dependency rpaths.
        rpaths = dict.fromkeys(d for dep in library_specs for d in dep.libs.directories)
        arpack_libs.extend(f"-Wl,-rpath,{d}" for d in rpaths if d)
        return targets + [
            "CC=" + spec["mpi"].mpicc,
            "CXX=" + spec["mpi"].mpicxx,
            "FC=" + spec["mpi"].mpifc,
            "CCX=" + ccx,
            "CFLAGS=" + " ".join(cflags),
            "SPOOLES_INCLUDE=" + includes,
            "SPOOLES_LIBS=" + solver_libs,
            "ARPACK_LIBS=" + " ".join(arpack_libs),
            "ADDITIONAL_FFLAGS=" + " ".join(fflags),
            "bin/ccx_preCICE",
        ]

    def edit(self, spec, prefix):
        # The upstream Makefile lists bin as a peer prerequisite of the objects.
        mkdirp("bin")
        if spec.satisfies("@:2.20.1"):
            filter_file("g++ -std=c++11", "$(CXX) -std=c++11", "Makefile", string=True)

        if spec.satisfies("+pastix"):
            # CCX's private header and the PaStiX public header share a basename.
            ccx = self.ccx_source
            sources = glob.glob(join_path(ccx, "*.c"))
            sources.extend(["dyna_precice.c", "nonlingeo_precice.c"])
            filter_file('#include "pastix.h"', '#include "pastix_ccx.h"', *sources, string=True)
            os.rename(join_path(ccx, "pastix.h"), join_path(ccx, "pastix_ccx.h"))

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install(join_path("bin", "ccx_preCICE"), prefix.bin)
