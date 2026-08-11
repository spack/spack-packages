# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyProteus(PythonPackage):
    """Proteus: Computational Methods and Simulation Toolkit. Python tools
    for rapidly developing computer models and numerical methods, built
    around PETSc for parallel linear/nonlinear solves."""

    homepage = "http://proteustoolkit.org"
    # Tracks cekees/proteus's torino_narwhal branch rather than erdc/proteus
    # releases: upstream unconditionally requires a Chrono install.
    # torino_narwhal makes Chrono and SCOREC independently optional.
    git = "https://github.com/cekees/proteus.git"

    maintainers("cekees")

    license("MIT")

    version("torino_narwhal", branch="torino_narwhal")

    # Chrono (pychrono) has no upstream Spack package and stays disabled.
    # SCOREC/PUMI does (`pumi`); this variant wires it in instead of
    # always skipping it.
    variant("scorec", default=False, description="Enable SCOREC/PUMI mesh adaptation support")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools@61:", type="build")
    depends_on("py-cython@3:", type="build")
    # pybind11 3.x + xtensor@0.27.1 fails to compile: ambiguous operator*=
    # overload in xtensor's xsemantic.hpp.
    depends_on("py-pybind11@2.11:2", type="build")

    depends_on("py-numpy@1.25:", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-mpi4py", type=("build", "run"))
    depends_on("py-petsc4py", type=("build", "run"))
    depends_on("py-h5py+mpi", type=("build", "run"))

    depends_on("mpi")
    depends_on("petsc+mpi")
    depends_on("hdf5+mpi+hl")
    # config/default.py hard-codes '-lopenblas' on Linux.
    depends_on("openblas")
    depends_on("superlu")
    depends_on("triangle")
    # proteus.fenton.Fenton links ncurses unconditionally.
    depends_on("ncurses")

    # zoltan and parmetis are linked directly, not just via pumi, so each
    # needs its own *_DIR in setup_build_environment.
    # +shared: pumi's static libs aren't built with -fPIC and can't link
    # into the shared MeshAdaptPUMI.MeshAdapt extension.
    depends_on("pumi+zoltan+shared", when="+scorec")
    # ~fortran: unused here, and zoltan's Fortran interface leaves
    # unresolved libgfortran symbols in libzoltan.so on this toolchain.
    depends_on("zoltan+parmetis~fortran", when="+scorec")
    depends_on("parmetis", when="+scorec")

    # Header-only deps: get_xtensor_include() looks under sys.prefix/include
    # rather than a *_DIR var, so these are added to CPATH instead.
    depends_on("eigen@3.4")
    # 0.27.1 + py-pybind11@3.x fails to compile (see pybind11 pin above).
    depends_on("xtensor@0.26.0")
    # 0.28.0 is exploratory, added locally to xtensor_python; builtin
    # spack-packages only had 0.23.1, which forces pybind11@2.2.
    depends_on("xtensor-python@0.28.0:")
    depends_on("xtl")

    def setup_build_environment(self, env):
        env.set("PROTEUS_SKIP_CHRONO", "1")
        if self.spec.satisfies("~scorec"):
            env.set("PROTEUS_SKIP_PUMI", "1")

        # config/default.py's get_flags() reads a <PACKAGE>_DIR per dependency.
        env.set("PETSC_DIR", self.spec["petsc"].prefix)
        env.set("MPI_DIR", self.spec["mpi"].prefix)
        env.set("HDF5_DIR", self.spec["hdf5"].prefix)
        env.set("BLAS_DIR", self.spec["openblas"].prefix)
        env.set("LAPACK_DIR", self.spec["openblas"].prefix)
        env.set("SUPERLU_DIR", self.spec["superlu"].prefix)
        env.set("TRIANGLE_DIR", self.spec["triangle"].prefix)
        env.set("NCURSES_DIR", self.spec["ncurses"].prefix)

        if self.spec.satisfies("+scorec"):
            env.set("SCOREC_DIR", self.spec["pumi"].prefix)
            env.set("ZOLTAN_DIR", self.spec["zoltan"].prefix)
            env.set("PARMETIS_DIR", self.spec["parmetis"].prefix)

        for dep in ("eigen", "xtensor", "xtensor-python", "xtl"):
            env.prepend_path("CPATH", self.spec[dep].prefix.include)
