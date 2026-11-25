# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.rocm import ROCmLibrary

from spack.package import *


class Hipthreads(ROCmLibrary, CMakePackage):
    """hipthreads is a library that provides thread-level parallelism
    primitives for HIP applications on AMD GPUs."""

    homepage = "https://github.com/ROCm/hipthreads"
    git = "https://github.com/ROCm/rocm-libraries.git"

    tags = ["rocm"]
    maintainers("srekolam", "renjithravindrankannath", "afzpatel")
    license("Apache-2.0")

    rocm_url_map = [
        (None, "https://github.com/ROCm/rocm-libraries/archive/refs/tags/therock-{1}.{2}.tar.gz"),
    ]

    version("10.1.0", sha256="70e9a7e2118e44328fc2fb2d20f7d414cca6a8f7cbcefc0af245db1982129bf5")
    version("10.0.0", sha256="eb7f255d6627d3cfb312a7bcf41d701517ecaeac88382b56f2bde8d4947ea592")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("cmake@3.31:", type="build")

    for ver in ["10.0.0", "10.1.0"]:
        depends_on(f"hip@{ver}", when=f"@{ver}")
        depends_on(f"rocm-cmake@{ver}:", type="build", when=f"@{ver}")
        depends_on(f"libhipcxx@{ver}:", when=f"@{ver}")

    @property
    def root_cmakelists_dir(self):
        return "projects/hipthreads"

    def cmake_args(self):
        args = [
            self.define("BUILD_TESTING", "OFF"),
        ]
        return args
