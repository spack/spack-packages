# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Nvbench(CMakePackage):
    """NVBench is a C++17 library designed to simplify CUDA kernel benchmarking.
    It solves challenges inherent to CUDA kernel benchmarking."""

    homepage = "https://github.com/NVIDIA/nvbench"
    url = "https://github.com/NVIDIA/nvbench"
    git = "https://github.com/NVIDIA/nvbench"

    supplier = "NVIDIA"

    maintainers("gusser93")

    license("Apache-2.0 WITH LLVM-exception", checked_by="gusser93")

    version("main", branch="main")
    depends_on("cmake@4:", type="build")
