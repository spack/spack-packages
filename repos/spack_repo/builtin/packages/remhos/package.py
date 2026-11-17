# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.makefile import MakefilePackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Remhos(MakefilePackage, CudaPackage, ROCmPackage):
    """Remhos (REMap High-Order Solver) is a CEED miniapp that performs monotonic
    and conservative high-order discontinuous field interpolation (remap)
    using DG advection-based spatial discretization and explicit high-order
    time-stepping.
    """

    tags = ["proxy-app"]

    homepage = "https://github.com/CEED/Remhos"
    url = "https://github.com/CEED/Remhos/archive/refs/tags/v2.0.tar.gz"
    git = "https://github.com/CEED/Remhos.git"

    maintainers("v-dobrev", "tzanio", "vladotomov")

    license("BSD-2-Clause")

    version("develop", branch="master")
    version("2.0", sha256="68209a529f7559b6add9e02dadd2bb05012a9080a1eb4d2c1b39a4732d7a1ba5")
    version("1.0", sha256="e60464a867fe5b1fd694fbb37bb51773723427f071c0ae26852a2804c08bbb32")

    variant("metis", default=True, description="Enable/disable METIS support")
    variant("caliper", default=False, description="Enable/disable Caliper support")
    variant("gpu-aware-mpi", default=False, description="Enable GPU aware MPI")
    variant("raja", default=True, description="Use RAJA backend for MFEM")

    depends_on("cxx", type="build")  # generated

    depends_on("mpi")

    depends_on("umpire@2026.07.2:", when="@develop")
    depends_on("raja@2026.07.1: ~examples~exercises cxxstd=20", when="@develop")

    depends_on("umpire@2026.07.2", when="@2.0")
    depends_on("raja@2026.07.1 ~examples~exercises cxxstd=20", when="@2.0")

    depends_on("mfem+mpi+metis", when="+metis")
    depends_on("mfem+mpi~metis", when="~metis")
    depends_on("mfem+raja", when="+raja")

    depends_on("mfem@develop", when="@develop")
    depends_on("mfem@4.10", when="@2.0")
    depends_on("mfem@4.1.0:", when="@1.0")
    depends_on("mfem+caliper", when="+caliper")
    depends_on("mfem cxxstd=20", when="@develop")
    depends_on("mfem cxxstd=20", when="@2.0")

    depends_on("caliper", when="+caliper")
    depends_on("adiak~shared", when="+caliper")

    depends_on("mfem~zlib")

    depends_on("hypre+mpi")
    depends_on("hypre+mixedint~fortran")
    depends_on("hypre+caliper", when="+caliper")

    depends_on("hypre~cuda", when="~cuda")
    depends_on("mfem~cuda", when="~cuda")

    with when("+cuda"):
        depends_on("hypre+cuda+umpire")
        depends_on("mfem+cuda+umpire")
        for sm_ in CudaPackage.cuda_arch_values:
            depends_on("hypre cuda_arch={0}".format(sm_), when="cuda_arch={0}".format(sm_))
            depends_on("mfem cuda_arch={0}".format(sm_), when="cuda_arch={0}".format(sm_))
            depends_on("umpire cuda_arch={0}".format(sm_), when="cuda_arch={0}".format(sm_))

    depends_on("hypre~rocm", when="~rocm")
    depends_on("mfem~rocm", when="~rocm")

    with when("+rocm"):
        depends_on("hypre+rocm+umpire")
        depends_on("mfem+rocm+umpire")
        for arch in ROCmPackage.amdgpu_targets:
            depends_on(
                "hypre amdgpu_target={0}".format(arch), when="amdgpu_target={0}".format(arch)
            )
            depends_on(
                "mfem amdgpu_target={0}".format(arch), when="amdgpu_target={0}".format(arch)
            )
            depends_on(
                "umpire amdgpu_target={0}".format(arch), when="amdgpu_target={0}".format(arch)
            )

    depends_on("hypre+gpu-aware-mpi", when="+gpu-aware-mpi")

    def setup_run_environment(self, env):
        if "+gpu-aware-mpi" in self.spec:
            env.set("MFEM_GPU_AWARE_MPI", "1")

    @property
    def build_targets(self):
        targets = []
        spec = self.spec

        targets.append("MFEM_DIR=%s" % spec["mfem"].prefix)
        targets.append("CONFIG_MK=%s" % spec["mfem"].package.config_mk)
        targets.append("TEST_MK=%s" % spec["mfem"].package.test_mk)
        if "+caliper" in self.spec:
            targets.append("CALIPER_DIR=%s" % spec["caliper"].prefix)
            targets.append("ADIAK_DIR=%s" % spec["adiak"].prefix)
        return targets

    # See lib/spack/spack/build_systems/makefile.py
    def check(self):
        with working_dir(self.build_directory):
            make("test", *self.build_targets)

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install("remhos", prefix.bin)
        install_tree("data", prefix.data)
