# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage, generator
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class DeepmdLib(CudaPackage, ROCmPackage, CMakePackage):
    """DeePMD-kit is a package written in Python/C++, designed to minimize the effort
    required to build deep learning-based models of interatomic potential energy
    and force field and to perform molecular dynamics (MD)"""

    homepage = "https://docs.deepmodeling.com/projects/deepmd/en/stable/index.html#"
    git = "https://github.com/deepmodeling/deepmd-kit.git"
    url = "https://github.com/deepmodeling/deepmd-kit/archive/refs/tags/v2.2.11.tar.gz"

    license("LGPL-3.0-only")

    maintainers("mtaillefumier")
    version("3.1.0", sha256="45f13df9ed011438d139a7f61416b8d7940f63c47fcde53180bfccd60c9d22ee")
    version("3.0.3", sha256="f562ee5c07e77274425cf6d19e28ffcb07017a6f07c56fe82b5c9974dd0fb3b6")
    version("3.0.2", sha256="b828d3a44730ea852505abbdb24ea5b556f2bf8b16de5a9c76018ed1ced7121b")
    version("3.0.1", sha256="e842edbc2714bc948ce708c411e5fed751e67c88d5c493c2978f11c849027dca")
    version("3.0.0", sha256="4df1091ce90dbea87734a20c6d826b8cbe80ac44646cb592c2e8586be319023c")
    version("2.2.11", sha256="d22893a08c2556c5cb29682378105849cf672545c91ee52b10a97da6e9075ac3")

    variant(
        "tensorflow", default=True, description="Enable tensorflow support (original ML backend)"
    )
    variant(
        "pytorch",
        default=False,
        description="Enable pytorch support (starting v3.0.0)",
        when="@3.0:",
    )
    variant("cuda", default=False, description="Enable cuda support")
    variant("rocm", default=False, description="Enable rocm support")
    variant("gromacs", default=False, description="Enable gromacs plugins")
    variant("jax", default=False, description="Enable JaX support", when="@3.0:")
    variant("fp64", default=True, description="Enable double precision ops", when="+tensorflow")
    variant("fp64", default=False, description="Enable double precision ops", when="+pytorch")

    # deepmd library uses cmake as a build system but deepmd itself uses pip.

    depends_on("c")
    depends_on("cxx")

    # Historical dependencies
    depends_on("py-setuptools", type="build")
    depends_on("py-tensorflow@2.16:", when="+tensorflow")
    depends_on("py-tensorflow+mpi", when="+tensorflow")
    depends_on("py-torch", when="+pytorch")

    with when("+jax"):
        depends_on("py-jax@0.4.33:")
        depends_on("py-flax@0.10.0:")
        depends_on("py-orbax_checkpoint")
        depends_on("jax-ai-stack")

    # we can install deepmd with tensorflow, py-torch and jax
    with when("+cuda"):
        depends_on("nccl")
        for target in CudaPackage.cuda_arch_values:
            depends_on(f"nccl cuda_arch={target}", when=f"cuda_arch={target}")
            depends_on(
                f"py-tensorflow+cuda+nccl+mpi cuda_arch={target}",
                when=f"+tensorflow cuda_arch={target}",
            )
            depends_on(f"py-torch+cuda cuda_arch={target}", when=f"+pytorch cuda_arch={target}")

    with when("+rocm"):
        depends_on("rccl")
        depends_on("hipcub+rocm")
        depends_on("hip+rocm")

        for target in ROCmPackage.amdgpu_targets:
            depends_on(
                f"py-tensorflow@2.16:+rocm+mpi amdgpu_target={target}",
                when=f"+tensorflow amdgpu_target={target}",
            )
            depends_on(
                f"py-torch+rocm amdgpu_target={target}", when=f"+pytorch amdgpu_target={target}"
            )

    root_cmakelists_dir = "source"

    patch("cmake-patch.diff", when="%gcc@14")

    def setup_build_environment(self, env):
        if "+cuda" in self.spec:
            env.set("DP_VARIANT", "cuda")
        if "+rocm" in self.spec:
            env.set("DP_VARIANT", "rocm")
        if "+tensorflow" in self.spec:
            # turn on double presicion suppport
            env.set("DP_ENABLE_TENSORFLOW", "1")
            # turn off all tensorflow errors, warnings and info messages
            env.set("TF_CPP_MIN_LOG_LEVEL", "3")
            env.set("TENSORFLOW_ROOT", self.spec["py-tensorflow"].prefix)
        if "+pytorch" in self.spec:
            env.set("DP_ENABLE_PYTORCH", "1")

    def cmake_args(self):
        spec = self.spec
        args = [
            self.define_from_variant("USE_CUDA_TOOLKIT", "cuda"),
            self.define_from_variant("USE_ROCM_TOOLKIT", "rocm"),
            self.define_from_variant("ENABLE_TENSORFLOW", "tensorflow"),
            self.define_from_variant("ENABLE_PYTORCH", "pytorch"),
            self.define_from_variant("USE_TF_PYTHON_LIBS", "tensorflow"),
            self.define_from_variant("ENABLE_JAX", "jax"),
        ]

        if "+rocm" in spec:
            args += [self.define_from_variant("TENSORFLOW_USE_ROCM", "tensorflow")]
        return args
