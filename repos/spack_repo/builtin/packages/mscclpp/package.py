# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Mscclpp(CMakePackage, ROCmPackage, CudaPackage):
    """MSCCL++: A GPU-driven communication stack for scalable AI applications"""

    homepage = "https://microsoft.github.io/mscclpp/index.html"
    url = "https://github.com/microsoft/mscclpp/archive/refs/tags/v0.7.0.tar.gz"

    license("MIT")

    version("0.7.0", sha256="d9d5166dc300b63a2c70d4a25b7c72e811661360abb8195d08a62b38fed06840")
    version("0.6.0", sha256="d88578261ece5a0aebd4e42cee2b0711d72c3e20287c3fafccda6ccb3f4fbfc3")

    variant("rocm", default=True, description="Enable ROCm support")
    variant("cuda", default=False, description="Enable CUDA support")

    conflicts("+cuda +rocm", msg="CUDA and ROCm support are mutually exclusive")
    conflicts("~cuda ~rocm", msg="CUDA or ROCm support is required")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("cmake@3.20:", type="build")
    depends_on("python@3:", type=("build", "run"))
    depends_on("hip@6.2.0:", when="+rocm")
    depends_on("nlohmann-json", type="link")
    depends_on("numactl@2:")
    depends_on("mpi")

    patch("mscclpp-numa-include-dir-001.patch")

    def cmake_args(self):
        args = [
            self.define("PYTHON_BIN_PATH", python.path),
            self.define_from_variant("MSCCLPP_USE_CUDA", "cuda"),
            self.define_from_variant("MSCCLPP_USE_ROCM", "rocm"),
        ]
        if self.spec.satisfies("+rocm"):
            args.append(f"-DCMAKE_CXX_COMPILER={self.spec['hip'].prefix.bin.hipcc}")
            rocm_arch = self.spec.variants["amdgpu_target"].value
            if "none" not in rocm_arch:
                args.append(f"-DCMAKE_CXX_FLAGS={self.hip_flags(rocm_arch)}")
        return args
