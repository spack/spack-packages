# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import platform

from spack.package import *


class Cusparselt(Package):
    """A high-performance CUDA library dedicated to general matrix-matrix operations
    in which at least one operand is a structured sparse matrix with 50% sparsity ratio."""

    homepage = "https://docs.nvidia.com/cuda/cusparselt/"

    skip_version_audit = ["platform=darwin", "platform=windows"]

    maintainers("thomas-bouvier")

    system = platform.system().lower()
    arch = platform.machine()
    if "linux" in system and arch == "x86_64":
        # version(
        #    "0.8.1-cuda130",
        #    sha256="82dd3e5ebc199a27011f58857a80cd825e77bba634ab2286ba3d4e13115db89a",
        #    url="https://developer.download.nvidia.com/compute/cusparselt/redist/libcusparse_lt/linux-x86_64/libcusparse_lt-linux-x86_64-0.8.1.1_cuda13-archive.tar.xz",
        # )
        version(
            "0.8.1-cuda120",
            sha256="b34272e683e9f798435af05dc124657d1444cd0e13802c3d2f3152e31cd898a3",
            url="https://developer.download.nvidia.com/compute/cusparselt/redist/libcusparse_lt/linux-x86_64/libcusparse_lt-linux-x86_64-0.8.1.1_cuda12-archive.tar.xz",
        )
    elif "linux" in system and arch == "aarch64":
        # version(
        #    "0.8.1-cuda130",
        #    sha256="0fcf5808f66c71f755b4a73af2e955292e4334fec6a851eea1ac2e20878602b7",
        #    url="https://developer.download.nvidia.com/compute/cusparselt/redist/libcusparse_lt/linux-aarch64/libcusparse_lt-linux-aarch64-0.8.1.1_cuda13-archive.tar.xz",
        # )
        version(
            "0.8.1-cuda120",
            sha256="5426a897c73a9b98a83c4e132d15abc63dc4a00f7e38266e7b82c42cd58a01e1",
            url="https://developer.download.nvidia.com/compute/cusparselt/redist/libcusparse_lt/linux-aarch64/libcusparse_lt-linux-aarch64-0.8.1.1_cuda12-archive.tar.xz",
        )

    # cuda130_versions = ("@0.8.1-cuda130",)
    cuda120_versions = ("@0.8.1-cuda120",)

    # for v in cuda130_versions:
    #    depends_on("cuda@13", when=v, type=("build", "run"))
    for v in cuda120_versions:
        depends_on("cuda@12", when=v, type=("build", "run"))

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    # Installation instructions
    def install(self, spec, prefix):
        # Create installation directories
        mkdirp(prefix.lib)
        mkdirp(prefix.include)

        # Copy library files
        install_tree("lib", prefix.lib)

        # Copy header files
        install_tree("include", prefix.include)
