# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.makefile import MakefilePackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Laghos(MakefilePackage, CudaPackage, ROCmPackage):
    """Laghos (LAGrangian High-Order Solver) is a CEED miniapp that solves the
    time-dependent Euler equations of compressible gas dynamics in a moving
    Lagrangian frame using unstructured high-order finite element spatial
    discretization and explicit high-order time-stepping.
    """

    tags = ["proxy-app", "ecp-proxy-app", "e4s"]

    homepage = "https://computing.llnl.gov/projects/co-design/laghos"
    url = "https://github.com/CEED/Laghos/archive/v1.0.tar.gz"
    git = "https://github.com/CEED/Laghos.git"

    maintainers("v-dobrev", "tzanio", "vladotomov")

    license("BSD-2-Clause")

    version("develop", branch="master")
    version("3.2", sha256="2f2d4a916a057cd5c8f2483f8930b4de363ab8fd21cbc08150abd1386ecae3de")
    version("3.1", sha256="49b65edcbf9732c7f6c228958620e18980c43ad8381315a8ba9957ecb7534cd5")
    version("3.0", sha256="4db56286e15b42ecdc8d540c4888a7dec698b019df9c7ccb8319b7ea1f92d8b4")
    version("2.0", sha256="dd3632d5558889beec2cd3c49eb60f633f99e6d886ac868731610dd006c44c14")
    version("1.1", sha256="53b9bfe2af263c63eb4544ca1731dd26f40b73a0d2775a9883db51821bf23b7f")
    version("1.0", sha256="af50a126355a41c758fcda335a43fdb0a3cd97e608ba51c485afda3dd84a5b34")

    variant("metis", default=True, description="Enable/disable METIS support")
    variant("ofast", default=False, description="Enable gcc optimization flags")
    variant("caliper", default=False, description="Enable/disable Caliper support")
    variant("gpu-aware-mpi", default=False, description="Enable GPU aware MPI")
    variant("raja", default=True, description="Use RAJA backend for MFEM")

    depends_on("cxx", type="build")  # generated

    depends_on("mpi")

    depends_on("umpire@2026.07.2:", when="@develop")
    depends_on("raja@2026.07.1: ~examples~exercises cxxstd=20", when="@develop")

    depends_on("umpire@2026.07.2", when="@3.2")
    depends_on("raja@2026.07.1 ~examples~exercises cxxstd=20", when="@3.2")

    depends_on("mfem+mpi+metis", when="+metis")
    depends_on("mfem+mpi~metis", when="~metis")
    depends_on("mfem+raja", when="+raja")

    depends_on("mfem@develop", when="@develop")
    depends_on("mfem@4.10", when="@3.2")
    depends_on("mfem@4.2.0:", when="@3.1")
    depends_on("mfem@4.1.0:4.1", when="@3.0")
    # Recommended mfem version for laghos v2.0 is: ^mfem@3.4.1-laghos-v2.0
    depends_on("mfem@3.4.1-laghos-v2.0", when="@2.0")
    # Recommended mfem version for laghos v1.x is: ^mfem@3.3.1-laghos-v1.0
    depends_on("mfem@3.3.1-laghos-v1.0", when="@1.0,1.1")
    depends_on("mfem+caliper", when="+caliper")
    depends_on("mfem cxxstd=20", when="@develop")
    depends_on("mfem cxxstd=20", when="@3.2")

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

    # Replace MPI_Session
    patch(
        "https://github.com/CEED/Laghos/commit/c800883ab2741c8c3b99486e7d8ddd8e53a7cb95.patch?full_index=1",
        sha256="e783a71c3cb36886eb539c0f7ac622883ed5caf7ccae597d545d48eaf051d15d",
        when="@3.1 ^mfem@4.4:",
    )

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
            targets.append("LAGHOS_USE_CALIPER=ON")
            targets.append("CALIPER_DIR=%s" % spec["caliper"].prefix)
            targets.append("ADIAK_DIR=%s" % spec["adiak"].prefix)
        # Only the legacy releases need CXX overridden.
        if spec.satisfies("@1.0,1.1,2.0"):
            targets.append("CXX=%s" % spec["mpi"].mpicxx)
        if self.spec.satisfies("+ofast %gcc"):
            targets.append("CXXFLAGS = -Ofast -finline-functions")
        return targets

    # See lib/spack/spack/build_systems/makefile.py
    def check(self):
        with working_dir(self.build_directory):
            make("test", *self.build_targets)

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install("laghos", prefix.bin)
        install_tree("data", prefix.data)
