# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class AoclDlp(CMakePackage):
    """AOCL-DLP is a library designed to provide optimized deep learning primitives for AMD
    processors. It implements Low Precision GEMM (LPGEMM) and batch GEMM for deep learning
    applications, supporting multiple data types as well as pre-operations and post-operations.
    The library is tailored to leverage the full potential of AMD hardware, ensuring efficient
    computation, scalability, and accelerated deep learning workloads."""

    _name = "aocl-dlp"
    homepage = "https://www.amd.com/en/developer/aocl/dlp.html"
    git = "https://github.com/amd/aocl-dlp"
    url = "https://github.com/amd/aocl-dlp/archive/refs/tags/5.2.tar.gz"

    maintainers("amd-toolchain-support")

    version("5.3", sha256="103607ba75a84f623d8ad1a2164ea100a0ce925f75c9dfdb65933cf3982ecb29")
    version("5.2", sha256="1eec26eeaf427cb2377ec21415ddce6e1bc62d4eab8ec51630a9c02711019c1c")

    # Feature toggles mapping directly to AOCL-DLP CMake options
    variant("benchmarks", default=True, description="Build benchmarks")
    variant("tests", default=True, description="Enable tests")
    variant("ctest", default=False, description="Enable ctest")
    variant("examples", default=True, description="Build examples")
    variant("shared", default=True, description="Build shared libraries")

    # Threading model selection (maps to DLP_THREADING_MODEL)
    variant(
        "threads",
        default="none",
        values=("none", "openmp", "pthread"),
        description="Select threading backend for AOCL-DLP",
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.26:", type="build")
    depends_on("numactl", when="+benchmarks")

    def cmake_args(self):
        spec = self.spec
        args = []

        # Map multi-valued 'threads' variant to CMake var DLP_THREADING_MODEL
        tmodel = spec.variants["threads"].value  # 'none' | 'openmp' | 'pthread'
        args.append(self.define("DLP_THREADING_MODEL", tmodel))

        # Straight boolean mappings
        args.append(self.define_from_variant("BUILD_BENCHMARKS", "benchmarks"))
        args.append(self.define_from_variant("BUILD_TESTING", "tests"))
        args.append(
            self.define("DLP_CTEST_DISABLED", "OFF" if spec.variants["ctest"].value else "ON")
        )
        args.append(self.define_from_variant("BUILD_EXAMPLES", "examples"))
        args.append(self.define_from_variant("BUILD_SHARED_LIBS", "shared"))

        return args
