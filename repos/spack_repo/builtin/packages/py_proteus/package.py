# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import glob
import os

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyProteus(PythonPackage):
    """Proteus: Computational Methods and Simulation Toolkit. Python tools
    for rapidly developing computer models and numerical methods"""

    homepage = "http://proteustoolkit.org"
    git = "https://github.com/cekees/proteus.git"

    maintainers("cekees")

    license("MIT")

    version("main", branch="main")

    # Chrono (pychrono) currently has no upstream Spack package and stays disabled.
    variant("pumi", default=False, description="Enable PUMI mesh adaptation support")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")  # remove in future not a direct proteus dep
    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools@61:", type="build")
    depends_on("py-cython@3:", type="build")
    depends_on("py-pybind11@2.11:2", type="build")  # xtensor@0.27.1 *= overload issue
    depends_on("py-numpy@1.25:", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-mpi4py", type=("build", "run"))
    depends_on("py-petsc4py", type=("build", "run"))
    depends_on("py-h5py+mpi", type=("build", "run"))
    depends_on("mpi")
    depends_on("petsc+mpi+hypre+superlu-dist+superlu+tetgen")  # how much to lock in?
    depends_on("hdf5+mpi+hl")
    depends_on("openblas")  # should relax to generic blas in future
    depends_on("metis")  # through several dependencies
    depends_on("superlu")
    depends_on("triangle")  # shells out but has linked in past
    depends_on("tetgen")  # shells out
    depends_on("gmsh")  # shells oput
    depends_on("ncurses")  # Fenton waves as text gui, generally not used
    depends_on("pumi@4.2.1+zoltan+shared", when="+pumi")  # <4.2.1 requires patch
    depends_on("zoltan+parmetis~fortran", when="+pumi")
    depends_on("parmetis", when="+pumi")
    depends_on("eigen@3.4")  # xtensor dep
    depends_on("xtensor@0.26.0")
    depends_on("xtensor-python@0.28.0:")
    depends_on("xtl")

    def _mpi_dir(self):
        # try to find the right mpi.h as it's not always in self.spec["mpi"]
        mpi_prefix = self.spec["mpi"].prefix
        if os.path.isfile(os.path.join(mpi_prefix, "include", "mpi.h")):
            return mpi_prefix
        for candidate in glob.glob(os.path.join(mpi_prefix, "lib", "*", "mpich")):
            if os.path.isfile(os.path.join(candidate, "include", "mpi.h")):
                return candidate
        for candidate in glob.glob(os.path.join(mpi_prefix, "lib", "*", "openmpi")):
            if os.path.isfile(os.path.join(candidate, "include", "mpi.h")):
                return candidate
        return mpi_prefix

    def setup_build_environment(self, env):
        env.set("PROTEUS_SKIP_CHRONO", "1")
        if self.spec.satisfies("~pumi"):
            env.set("PROTEUS_SKIP_PUMI", "1")
        env.set("PETSC_DIR", self.spec["petsc"].prefix)
        env.set("MPI_DIR", self._mpi_dir())
        env.set("HDF5_DIR", self.spec["hdf5"].prefix)
        env.set("BLAS_DIR", self.spec["openblas"].prefix)
        env.set("LAPACK_DIR", self.spec["openblas"].prefix)
        env.set("SUPERLU_DIR", self.spec["superlu"].prefix)
        env.set("TRIANGLE_DIR", self.spec["triangle"].prefix)
        env.set("NCURSES_DIR", self.spec["ncurses"].prefix)
        env.set("METIS_DIR", self.spec["metis"].prefix)

        if self.spec.satisfies("+pumi"):
            env.set("SCOREC_DIR", self.spec["pumi"].prefix)
            env.set("ZOLTAN_DIR", self.spec["zoltan"].prefix)
            env.set("PARMETIS_DIR", self.spec["parmetis"].prefix)

        for dep in ("eigen", "xtensor", "xtensor-python", "xtl"):
            env.prepend_path("CPATH", self.spec[dep].prefix.include)
