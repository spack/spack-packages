# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.rocm import ROCmLibrary

from spack.package import *


class RocprofTraceDecoder(ROCmLibrary, CMakePackage):
    """ROCm trace decoder library for rocprofiler-sdk"""

    homepage = "https://github.com/ROCm/rocm-systems"
    git = "https://github.com/ROCm/rocm-systems.git"

    rocm_url_map = [
        (None, "https://github.com/ROCm/rocm-systems/archive/refs/tags/therock-{1}.{2}.tar.gz"),
    ]
    tags = ["rocm"]

    maintainers("afzpatel", "srekolam", "renjithravindrankannath")

    license("MIT")

    version(
        "10.0.0",
        sha256="f30517ed6d9e18cde104eb487f173e62fed0175083a9498ca383f8136a9f4eec",
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("cmake@3.16:", type="build")
    # rocprof-trace-decoder dependency for newer versions
    for ver in ["10.0.0"]:
        depends_on(f"rocm-cmake@{ver}", when=f"@{ver}")

    @property
    def root_cmakelists_dir(self):
        return "projects/rocprof-trace-decoder"

    def cmake_args(self):
        args = []
        return args
