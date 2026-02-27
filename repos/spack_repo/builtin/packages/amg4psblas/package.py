# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

# flake8: noqa: F401,F403
from spack.package import *


class Amg4psblas(AutotoolsPackage):
    """AMG4PSBLAS: Algebraic MultiGrid preconditioners for PSBLAS.
    Part of the Parallel Sparse Computation Toolkit (PSCToolkit), AMG4PSBLAS provides
    advanced preconditioners including Algebraic Multigrid (AMG) and Domain Decomposition
    methods for use with the PSBLAS sparse linear system solvers.
    """

    homepage = "https://psctoolkit.github.io/"
    git = "https://github.com/sfilippone/amg4psblas.git"
    url = "https://github.com/sfilippone/amg4psblas/archive/refs/tags/v1.2.0.tar.gz"

    # List of GitHub accounts to notify when the package is updated.
    maintainers("pasquadambra", "cirdans-home", "sfilippone")

    # SPDX identifier of the project's license below.
    license("BSD-3-Clause", checked_by="cirdans-home")

    version("develop", branch="development")
    version("1.2.0", sha256="971cac9917a84dad97eccef76feb89b5ea66afa0b80d13f45a62dd5685c01878")
    version("1.2.0-rc3", sha256="589e23829ea569b984db964b0c40fdf2ae7165290c9118da45b0418514b5cf3a")

    # Variants for third-party libraries
    variant("mumps", default=False, description="Activates mumps interface")
    variant("umfpack", default=False, description="Activates UMFPACK interface")
    variant("superlu", default=False, description="Activates SuperLU interface")
    variant("superlu_dist", default=False, description="Activates SuperLU_dist interface")
    # Variants for psblas
    variant("mpi", default=True, description="Activates MPI support")
    variant(
        "cuda",
        default=False,
        description="Activate CUDA support, requires a CUDA-capable psblas with right"
        "cudacc flags",
    )
    variant("openmp", default=False, description="Activate OpenMP support")
    # Additional configure options
    variant("ccopt", default="none", description="Additional CCOPT flags")
    variant("cxxopt", default="none", description="Additional CXXOPT flags")
    variant("fcopt", default="none", description="Additional FCOPT flags")
    variant("extra_opt", default="none", description="Additional EXTRA_OPT flags")
    variant("libs", default="none", description="Additional link flags")
    variant("clibs", default="none", description="Additional CLIBS flags")
    variant("flibs", default="none", description="Additional FLIBS flags")

    # Dependencies:
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")
    # psblas
    depends_on("psblas@develop", when="@develop")
    depends_on("psblas@3.9.0", when="@1.2.0")
    depends_on("psblas@3.9.0-rc3", when="@1.2.0-rc3")
    depends_on("psblas+mpi", when="+mpi")
    depends_on("psblas~mpi", when="~mpi")
    depends_on("psblas+cuda", when="+cuda")
    depends_on("psblas~cuda", when="~cuda")
    depends_on("psblas+openmp", when="+openmp")
    depends_on("psblas~openmp", when="~openmp")
    # third-party libraries
    depends_on("mumps+openmp", when="+openmp+mumps")
    depends_on("mumps~openmp", when="~openmp+mumps")
    depends_on("superlu", when="+superlu")
    depends_on("psblas+metis", when="+superlu")
    depends_on("superlu-dist+openmp", when="+openmp+superlu_dist")
    depends_on("superlu-dist~openmp", when="~openmp+superlu_dist")
    depends_on("suite-sparse", when="+umfpack")
    # Conflicts
    conflicts("~mpi", when="+mumps", msg="MUMPS requires MPI support")
    conflicts("~mpi", when="+superlu_dist", msg="SuperLU_dist requires MPI support")

    def configure_args(self):
        args = [f"--prefix={self.prefix}"]
        args.append(f"--with-psblas={self.spec['psblas'].prefix}")
        # Check external libraries
        if "+mumps" in self.spec:
            args.append(f"--with-mumpsdir={self.spec['mumps'].prefix}")
            args.append(f"--with-mumpsincdir={self.spec['mumps'].prefix.include}")
            args.append(f"--with-mumpslibdir={self.spec['mumps'].libs.directories[0]}")
        if "+umfpack" in self.spec:
            args.append(f"--with-umfpackdir={self.spec['suite-sparse'].prefix}")
            args.append(f"--with-umfpackincdir={self.spec['suite-sparse'].prefix.include}")
            args.append(f"--with-umfpacklibdir={self.spec['suite-sparse'].libs.directories[0]}")
        if "+superlu" in self.spec:
            args.append(f"--with-superludir={self.spec['superlu'].prefix}")
            args.append(f"--with-superluincdir={self.spec['superlu'].prefix.include}")
            args.append(f"--with-superlulibdir={self.spec['superlu'].libs.directories[0]}")
        if "+superlu_dist" in self.spec:
            args.append(f"--with-superludistdir={self.spec['superlu-dist'].prefix}")
            args.append(f"--with-superludistincdir={self.spec['superlu-dist'].prefix.include}")
            args.append(
                f"--with-superludistlibdir={self.spec['superlu-dist'].libs.directories[0]}"
            )
        # All the other options
        for opt in ["ccopt", "cxxopt", "fcopt", "extra_opt", "libs", "clibs", "flibs"]:
            val = self.spec.variants[opt].value
            if val != "none":
                args.append(f"--with-{opt.replace('_', '-')}={val}")
        return args

    @run_after("install")
    def samples(self, spec, prefix):
        with working_dir(prefix.samples.advanced.fileread):
            make()
        with working_dir(prefix.samples.advanced.pdegen):
            make()
