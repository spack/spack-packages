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
    # NOTE: exploratory choice (not the conda-forge convention, which tracks
    # erdc/proteus release tags) -- erdc/proteus@1.8.3's config/default.py
    # unconditionally requires a Chrono install (unguarded open() of
    # chrono-config.cmake), matching conda-forge's proteus-feedstock, which
    # also hard-depends on pychrono. The PROTEUS_SKIP_PUMI_CHRONO env var
    # and the try/except around that open() call (making Chrono/SCOREC
    # genuinely optional, which is the whole point of this first pass) only
    # exist on cekees/proteus's torino_narwhal branch, not yet released
    # upstream. Revisit tracking erdc/proteus tags once that support lands
    # there.
    git = "https://github.com/cekees/proteus.git"

    maintainers("cekees")

    license("MIT")

    version("torino_narwhal", branch="torino_narwhal")

    # This first pass deliberately omits Chrono (rigid-body/FSI coupling)
    # and SCOREC/PUMI (parallel mesh adaptation) support: both are optional
    # at the proteus code level (proteus/Domain.py degrades gracefully
    # without MeshAdaptPUMI.MeshAdapt; setup.py can skip both extensions
    # via PROTEUS_SKIP_PUMI_CHRONO, used unconditionally below), and neither
    # has an upstream Spack package yet -- pychrono in particular would be
    # a separate, nontrivial packaging effort. Revisit as `scorec`/`chrono`
    # variants once those exist upstream.

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools@61:", type="build")
    depends_on("py-cython@3:", type="build")
    # pybind11 3.x is excluded: combined with xtensor@0.27.1 it triggers a
    # genuine ambiguous-overload compile error in xtensor's own xsemantic.hpp
    # (operator*= on xt::pyarray, hit from proteus/mprans/SW2DCV.h) that
    # doesn't reproduce with the pybind11 2.13.x + xtensor 0.26.0 combination
    # already validated (this session, outside Spack) against the same
    # proteus source.
    depends_on("py-pybind11@2.11:2", type="build")

    depends_on("py-numpy@1.25:", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-mpi4py", type=("build", "run"))
    depends_on("py-petsc4py", type=("build", "run"))
    depends_on("py-h5py+mpi", type=("build", "run"))

    depends_on("mpi")
    depends_on("petsc+mpi")
    depends_on("hdf5+mpi+hl")
    # proteus/config/default.py hard-codes '-lopenblas' on Linux -- not a
    # generic blas/lapack virtual dependency.
    depends_on("openblas")
    depends_on("superlu")
    depends_on("triangle")
    # Only proteus.fenton.Fenton links ncurses; unlike Chrono/SCOREC it has
    # no build-time skip switch, so it's a hard dependency here.
    depends_on("ncurses")

    # Header-only C++ dependencies. setup.py's get_xtensor_include() (used
    # by ~30 of proteus's extensions) looks under sys.prefix/include, not
    # any per-package *_DIR env var, so these need to land on the compiler's
    # search path explicitly -- see setup_build_environment below.
    # Constrained to the long-standing 3.4 branch since Eigen jumped
    # straight from there to a new 5.0.x major version -- kept as a
    # conservative pin even though it turned out NOT to be the cause of
    # the operator*= ambiguity below (that's purely an xtensor/pybind11
    # interaction, verified by testing eigen@3.4 alone first).
    depends_on("eigen@3.4")
    # Pinned to 0.26.0 (not just "xtensor-python@0.28.0:'s @0.26.0:" lower
    # bound) -- xtensor@0.27.1 combined with py-pybind11@3.x produces a
    # genuine ambiguous 'operator*=' compile error in xtensor's own
    # xsemantic.hpp when proteus/mprans/SW2DCV.h calls it on an
    # xt::pyarray; 0.26.0 is the exact version already validated (this
    # session, outside Spack) against this proteus source.
    depends_on("xtensor@0.26.0")
    # xtensor-python@0.28.0 is an exploratory addition to the local
    # xtensor_python package (not yet upstreamed) -- Spack's builtin only
    # had 0.23.1, which forces an ancient py-pybind11@2.2 incompatible
    # with any modern py-scipy.
    depends_on("xtensor-python@0.28.0:")
    depends_on("xtl")

    def setup_build_environment(self, env):
        env.set("PROTEUS_SKIP_PUMI_CHRONO", "1")

        # proteus/config/default.py's get_flags() resolves each dependency
        # via <PACKAGE>_DIR (falling back to one shared PROTEUS_PREFIX) --
        # Spack gives every dependency its own prefix, so set them all
        # individually rather than relying on the single-prefix fallback.
        env.set("PETSC_DIR", self.spec["petsc"].prefix)
        env.set("MPI_DIR", self.spec["mpi"].prefix)
        env.set("HDF5_DIR", self.spec["hdf5"].prefix)
        env.set("BLAS_DIR", self.spec["openblas"].prefix)
        env.set("LAPACK_DIR", self.spec["openblas"].prefix)
        env.set("SUPERLU_DIR", self.spec["superlu"].prefix)
        env.set("TRIANGLE_DIR", self.spec["triangle"].prefix)
        env.set("NCURSES_DIR", self.spec["ncurses"].prefix)

        # Headers-only deps setup.py can't be told about via a *_DIR env
        # var -- fall back to the standard compiler search-path variables.
        for dep in ("eigen", "xtensor", "xtensor-python", "xtl"):
            env.prepend_path("CPATH", self.spec[dep].prefix.include)
