# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import platform

from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.generic import Package

from spack.package import *

_versions = {
    "11.4.0.6": {
        "Linux-x86_64": dict(
            sha256="6a0597e10e698ab46ea9a607efe06f681ba6e2bf0d8eddd8a72a09c18a8f7253",
            url="https://developer.download.nvidia.com/compute/cufftmp/redist/libcufftmp/linux-x86_64/libcufftmp-linux-x86_64-11.4.0.6_cuda12-archive.tar.xz",
        ),
        "Linux-aarch64": dict(
            sha256="c0f944fd6ef2e13ef5adfd48ef2e02660f5f573a69c515580096a9eaae13be16",
            url="https://developer.download.nvidia.com/compute/cufftmp/redist/libcufftmp/linux-sbsa/libcufftmp-linux-sbsa-11.4.0.6_cuda12-archive.tar.xz",
        ),
    }
}


class Cufftmp(Package, CudaPackage):
    """
    NVIDIA cuFFTMp library.
    """

    homepage = "https://docs.nvidia.com/cuda/cufftmp/"
    url = "https://developer.download.nvidia.com/compute/cufftmp/redist/libcufftmp"

    maintainers("albestro")

    # https://docs.nvidia.com/cuda/cufftmp/license.html
    license("NVIDIA Software License Agreement")

    for ver, packages in _versions.items():
        package = packages.get(f"{platform.system()}-{platform.machine()}")
        if package:
            version(ver, **package)

    conflicts("~cuda", msg="cuFFTMp requires CUDA")

    depends_on("cuda@12:")
    depends_on("nvshmem")

    # cuFFTMp requires a specific version of NVSHMEM
    # https://docs.nvidia.com/cuda/cufftmp/usage/nvshmem_and_cufftmp.html#compatibility
    depends_on("nvshmem@3.1.7:", when="@11.4.0")

    for cuda_arch in CudaPackage.cuda_arch_values:
        with when(f"cuda_arch={cuda_arch}"):
            depends_on(f"nvshmem cuda_arch={cuda_arch}")

    def install(self, spec, prefix):
        install_tree(".", prefix)
