# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.generic import Package
from spack_repo.builtin.packages.openfoam.package import add_extra_files

from spack.package import *


class Solids4foam(Package):
    """solids4foam is a solid mechanics and fluid-solid interaction toolbox for
    OpenFOAM. It provides solid solvers (linear-elastic through finite-strain
    hyperelastic and plastic) and a set of fluidSolidInterface coupling schemes,
    which can be driven either standalone or as a preCICE participant."""

    homepage = "https://solids4foam.github.io"
    git = "https://github.com/solids4foam/solids4foam.git"

    license("GPL-3.0-or-later")

    maintainers("failed33")

    version("2.4", tag="v2.4", commit="1341312f951caf4d8fcc69499c6ce1a588826156")

    variant("eigen", default=True, description="Build with Eigen")
    variant(
        "petsc",
        default=True,
        description="Enable PETSc SNES solvers and monolithic coupling",
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("gmake", type="build")
    depends_on("openfoam@2312:+source")
    depends_on("openfoam~int64 precision=dp", when="+petsc")
    # ThirdParty/Allwmake can download Eigen unless given EIGEN_DIR.
    depends_on("eigen", when="+eigen")

    # The assembly passes OpenFOAM label and scalar arrays directly to PETSc.
    depends_on("petsc@3.15:+double+mpi+mumps+hypre~complex~int64", when="+petsc")

    patch("neo-hookean-rest-stress.patch", when="@=2.4")
    # https://github.com/solids4foam/solids4foam/pull/380
    patch("flux-corrected-velocity-restart-history.patch", when="@=2.4")

    build_script = "./spack-derived-Allwmake"
    build_userdir = "spack-userdir"

    phases = ["configure", "build", "install"]

    def patch(self):
        add_extra_files(self, ("change-userdir.sh", "spack-derived-Allwmake"), ())

    def configure(self, spec, prefix):
        config = join_path(self.stage.source_path, "spack-config.sh")
        lines = []
        if spec.satisfies("+petsc"):
            # PETSc installs include and lib directly under its prefix.
            lines += [
                'export PETSC_DIR="%s"\n' % spec["petsc"].prefix,
                'export PETSC_ARCH=""\n',
            ]
        if spec.satisfies("~eigen"):
            lines.append("export S4F_NO_USE_EIGEN=1\n")
        else:
            lines.append('export EIGEN_DIR="%s"\n' % spec["eigen"].prefix.include.eigen3)
        lines.append(". ./change-userdir.sh $PWD/%s\n" % self.build_userdir)
        with open(config, "w") as out:
            out.writelines(lines)

    def build(self, spec, prefix):
        if self.parallel:
            os.environ["WM_NCOMPPROCS"] = str(make_jobs)
        Executable(self.build_script)()

    def install(self, spec, prefix):
        for f in ["README.md", "LICENSE"]:
            if os.path.isfile(f):
                install(f, join_path(self.prefix, f))
        for d in ["lib", "bin"]:
            src = join_path(self.build_userdir, d)
            if os.path.isdir(src):
                install_tree(src, join_path(self.prefix, d))

    @run_after("install")
    def verify_petsc(self):
        """Check that Make/options enabled the requested PETSc solvers."""
        if self.spec.satisfies("~petsc"):
            return
        lib = join_path(self.prefix, "lib", "libsolids4FoamModels.so")
        if not os.path.isfile(lib):
            raise InstallError("libsolids4FoamModels.so was not installed")
        nm = which("nm")
        if nm is None:
            return
        symbols = nm(
            "-D", "--defined-only", lib, output=str, error=os.devnull, fail_on_error=False
        )
        if "foamPetscSnesHelper" not in symbols:
            raise InstallError(
                "+petsc build produced no foamPetscSnesHelper symbols; "
                "PETSC_DIR did not reach src/solids4FoamModels/Make/options"
            )

    def setup_run_environment(self, env):
        env.prepend_path("LD_LIBRARY_PATH", join_path(self.prefix, "lib"))
        env.prepend_path("PATH", join_path(self.prefix, "bin"))
