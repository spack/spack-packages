# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import platform

from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.generic import Package

from spack.package import *

_versions = {
    "0.5.0.898": {
        "Linux-x86_64": dict(
            sha256="e8bc831d743bbbf5f5af8b728ab4da74acdcea37c4ee1022e63f8f537d5488a2",
            url="https://developer.download.nvidia.com/compute/cublasmp/redist/libcublasmp/linux-x86_64/libcublasmp-linux-x86_64-0.5.0.898_cuda12-archive.tar.xz",
        ),
        "Linux-aarch64": dict(
            sha256="6e548a11bd6ba6c4aef77c9d1c16bdc39b7ec268547f856c5dab39085fbb7fd4",
            url="https://developer.download.nvidia.com/compute/cublasmp/redist/libcublasmp/linux-sbsa/libcublasmp-linux-sbsa-0.5.0.898_cuda12-archive.tar.xz",
        ),
    }
}


class Cublasmp(Package, CudaPackage):
    """
    NVIDIA cuBLASMp is a high-performance, multi-process, GPU-accelerated library
    for distributed basic dense linear algebra.
    """

    homepage = "https://docs.nvidia.com/cuda/cublasmp/"
    url = "https://developer.download.nvidia.com/compute/cublasmp/redist/libcublasmp/"

    maintainers("albestro")

    license("UNKNOWN")

    for ver, packages in _versions.items():
        package = packages.get(f"{platform.system()}-{platform.machine()}")
        if package:
            version(ver, **package)

    conflicts("~cuda", msg="cuBLASMp requires CUDA")

    depends_on("cuda@12:")
    depends_on("nvshmem@3.1:")
    depends_on("nccl@2.18.5:")

    for cuda_arch in CudaPackage.cuda_arch_values:
        with when(f"cuda_arch={cuda_arch}"):
            depends_on(f"nvshmem cuda_arch={cuda_arch}")
            depends_on(f"nccl cuda_arch={cuda_arch}")

    def install(self, spec, prefix):
        install_tree(".", prefix)
