# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import platform

from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.generic import Package

from spack.package import *

_versions = {
    "0.7.0.833": {
        "Linux-x86_64": dict(
            sha256="5383f35eefd45cc0a5cbd173a4a353941f02b912eb2f8d3a85c30345054df5e9",
            url="https://developer.download.nvidia.com/compute/cusolvermp/redist/libcusolvermp/linux-x86_64/libcusolvermp-linux-x86_64-0.7.0.833_cuda12-archive.tar.xz",
        ),
        "Linux-aarch64": dict(
            sha256="a0012c5be7ac742a26cf8894bed3c703edea84eddf0d5dca42d35582622ffb9b",
            url="https://developer.download.nvidia.com/compute/cusolvermp/redist/libcusolvermp/linux-sbsa/libcusolvermp-linux-sbsa-0.7.0.833_cuda12-archive.tar.xz",
        ),
    }
}


class Cusolvermp(Package, CudaPackage):
    """
    NVIDIA cuSOLVERMp is a high-performance, distributed-memory, GPU-accelerated library
    that provides tools for the solution of dense linear systems and eigenvalue problems.
    """

    homepage = "https://docs.nvidia.com/cuda/cusolvermp/"
    url = "https://developer.download.nvidia.com/compute/cusolvermp/redist/libcusolvermp"

    maintainers("albestro")

    # https://docs.nvidia.com/cuda/cusolvermp/license.html
    license("NVIDIA Software License Agreement")

    for ver, packages in _versions.items():
        package = packages.get(f"{platform.system()}-{platform.machine()}")
        if package:
            version(ver, **package)

    conflicts("~cuda", msg="cuSOLVERMp requires CUDA")

    depends_on("cuda@12:")
    depends_on("nccl@2.18.5:")

    for cuda_arch in CudaPackage.cuda_arch_values:
        depends_on(f"nccl cuda_arch={cuda_arch}", when=f"cuda_arch={cuda_arch}")

    def install(self, spec, prefix):
        install_tree(".", prefix)
