# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import glob
import os

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyProteus(PythonPackage):
    """Proteus: Computational Methods and Simulation Toolkit. Python tools
    for rapidly developing computer models and numerical methods, built
    around PETSc for parallel linear/nonlinear solves."""

    homepage = "http://proteustoolkit.org"
    # Tracks cekees/proteus's main branch rather than erdc/proteus releases:
    # upstream unconditionally requires a Chrono install, but main (like the
    # torino_narwhal branch this used to track, now merged into main and
    # fully superseded) makes Chrono and SCOREC independently optional.
    #
    # NOTE: this used to warn about github.com/cekees/proteus's fork-network
    # Git LFS bandwidth budget (billed against upstream erdc/proteus, not
    # cekees, and exhaustible independent of anything the cekees fork owner
    # does) -- moot as of main dropping LFS entirely for its test comparison
    # data (commit c75eb6c9, "Stop tracking test comparison data via Git
    # LFS"). If a similar external-quota issue ever recurs for some other
    # reason, point this at a local, already-cloned checkout instead
    # (`git = "file:///path/to/checkout"`) as a temporary local edit --
    # Spack has no per-invocation override for a version's own git URL
    # (confirmed: `git=` is not a valid spec variant here).
    git = "https://github.com/cekees/proteus.git"

    maintainers("cekees")

    license("MIT")

    version("main", branch="main")

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
    # +hypre+superlu-dist+superlu to match the --download-proteus/HPC and pip
    # paths' own PETSc configure flags (--download-hypre --download-superlu
    # --download-superlu_dist). Without hypre/superlu-dist, a noticeable
    # slice of the solver-heavy test suite fails outright (AMG-based tests,
    # parallel-direct-solve tests) rather than just running slower/
    # differently -- confirmed via a real `spack install py-proteus+scorec`
    # build and full pytest run: 35 failed (mostly AMG/solver tests) vs. the
    # 6 known pre-existing failures other install paths show. +superlu
    # (distinct from +superlu-dist -- PETSc's "superlu" and "superlu_dist"
    # MatSolverTypes aren't interchangeable) is needed too: some tests
    # (RDLS3P, periodic) explicitly request pc_factor_mat_solver_package=
    # 'superlu'; this builtin petsc package had no way to enable that at all
    # until this session added the +superlu variant (see petsc's own
    # package.py).
    # +tetgen matches the pip/HPC pathways' PETSc configure (--download-
    # tetgen): PETSc's DMPlex tetgen-file reader (used by the ci/test_
    # meshPartitionFromTetgenFiles.py tests, which partition pre-generated
    # .node/.ele/.face files rather than shelling out to the tetgen CLI)
    # needs PETSc itself built with tetgen support, not just the standalone
    # CLI on PATH.
    depends_on("petsc+mpi+hypre+superlu-dist+superlu+tetgen")
    depends_on("hdf5+mpi+hl")
    # config/default.py hard-codes '-lopenblas' on Linux.
    depends_on("openblas")
    # superlu's own library calls METIS_NodeND for fill-reducing ordering, but
    # metis was previously only pulled in transitively via parmetis, and only
    # when +scorec. Without a direct dependency Spack never adds metis's lib
    # dir to the rpath/link-path Spack automatically wires up for direct
    # depends_on() packages, so the base (~scorec) build's superluWrappers
    # extension fails at import time with "symbol not found in flat
    # namespace '_METIS_NodeND'" (confirmed via a real `spack install
    # py-proteus` build).
    depends_on("metis")
    depends_on("superlu")
    depends_on("triangle")
    # proteus's own mesh-generation helpers (MeshTools.buildReferenceSimplex,
    # among others) shell out to the standalone "tetgen" CLI directly, same
    # as with "triangle" above; the pip/HPC pathways' own PETSc configure
    # line also builds tetgen (--download-tetgen --download-tetgen-build-
    # exec=1) for the same reason. Confirmed via a real
    # `spack install py-proteus+scorec` test run: test_generate_reference_
    # simplex and both TestPoissonTetgen tests failed with the CLI missing
    # from PATH / PETSc's own tetgen-backed DMPlex support disabled.
    depends_on("tetgen")
    # proteus.fenton.Fenton links ncurses unconditionally.
    depends_on("ncurses")

    # zoltan and parmetis are linked directly, not just via pumi, so each
    # needs its own *_DIR in setup_build_environment.
    # +shared: pumi's static libs aren't built with -fPIC and can't link
    # into the shared MeshAdaptPUMI.MeshAdapt extension.
    # @4.1.0: proteus's own MeshAdaptPUMI source (main) requires the newer
    # PCU API (pcu/PCU_C.h) that pumi's older versions predate -- pinned
    # explicitly rather than relying on Spack's default latest-version
    # preference, since pumi still offers 2.2.9 too (see pumi's own
    # package.py for the full explanation).
    depends_on("pumi@4.1.0+zoltan+shared", when="+scorec")
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

    def _mpi_dir(self):
        # config/default.py's get_flags('mpi') looks for $MPI_DIR/include/
        # mpi.h -- true for a normal, self-contained MPI prefix (e.g. a
        # Spack-built mpich/openmpi), but not for Debian/Ubuntu's system
        # mpich package: when Spack's external-package detection picks that
        # up (as it does whenever `spack external find` runs on a machine
        # with mpich already apt-installed), self.spec["mpi"].prefix is the
        # generic /usr, which has no include/mpi.h at all -- Debian's mpich
        # package instead nests everything under a per-implementation,
        # multiarch-qualified directory (/usr/lib/<triplet>/mpich/include/
        # mpi.h) so it can coexist with an openmpi package's own headers at
        # the same prefix. Confirmed directly on this machine: proteus's
        # pip-install pathway hit the identical gap and needed the same
        # kind of explicit redirect. Prefer the plain prefix/include/mpi.h
        # layout when it exists (true for every Spack-built MPI), and only
        # fall back to searching for Debian's nested layout otherwise.
        mpi_prefix = self.spec["mpi"].prefix
        if os.path.isfile(os.path.join(mpi_prefix, "include", "mpi.h")):
            return mpi_prefix
        for candidate in glob.glob(os.path.join(mpi_prefix, "lib", "*", "mpich")):
            if os.path.isfile(os.path.join(candidate, "include", "mpi.h")):
                return candidate
        for candidate in glob.glob(os.path.join(mpi_prefix, "lib", "*", "openmpi")):
            if os.path.isfile(os.path.join(candidate, "include", "mpi.h")):
                return candidate
        # No known layout matched -- fall back to the plain prefix so the
        # resulting error (if any) still points at a real, inspectable path
        # rather than silently returning something clearly wrong.
        return mpi_prefix

    def setup_build_environment(self, env):
        env.set("PROTEUS_SKIP_CHRONO", "1")
        if self.spec.satisfies("~scorec"):
            env.set("PROTEUS_SKIP_PUMI", "1")

        # config/default.py's get_flags() reads a <PACKAGE>_DIR per dependency.
        env.set("PETSC_DIR", self.spec["petsc"].prefix)
        env.set("MPI_DIR", self._mpi_dir())
        env.set("HDF5_DIR", self.spec["hdf5"].prefix)
        env.set("BLAS_DIR", self.spec["openblas"].prefix)
        env.set("LAPACK_DIR", self.spec["openblas"].prefix)
        env.set("SUPERLU_DIR", self.spec["superlu"].prefix)
        env.set("TRIANGLE_DIR", self.spec["triangle"].prefix)
        env.set("NCURSES_DIR", self.spec["ncurses"].prefix)
        # Needed unconditionally now (config/default.py's get_flags('metis')
        # feeds superluWrappers'/csmoothers' link line), not just +scorec.
        env.set("METIS_DIR", self.spec["metis"].prefix)

        if self.spec.satisfies("+scorec"):
            env.set("SCOREC_DIR", self.spec["pumi"].prefix)
            env.set("ZOLTAN_DIR", self.spec["zoltan"].prefix)
            env.set("PARMETIS_DIR", self.spec["parmetis"].prefix)

        for dep in ("eigen", "xtensor", "xtensor-python", "xtl"):
            env.prepend_path("CPATH", self.spec[dep].prefix.include)
