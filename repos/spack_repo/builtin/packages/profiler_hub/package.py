# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.rocm import ROCmLibrary

from spack.package import *


class ProfilerHub(ROCmLibrary, CMakePackage):
    """C++ library for storing and retrieving ROCm profiling data using
    SQLite (rocpd database format)."""

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

    # profiler-hub clones SQLite during configure; vendor for air-gapped builds.
    # Matches SQLITE3_GIT_TAG in profilers/profiler-hub/cmake/sqlite3.cmake
    resource(
        name="sqlite3",
        url="https://github.com/sqlite/sqlite/archive/refs/tags/version-3.45.3.tar.gz",
        sha256="a9502b2794ccf24685e6c4964df08944eed7d76aa0715870b3b62709b13a3fcb",
        destination="deps",
        placement="sqlite3",
        when="@10.0:",
    )
    # Matches NLOHMANN_JSON_VERSION in profilers/profiler-hub/cmake/nlohmann_json.cmake
    resource(
        name="nlohmann_json",
        url="https://github.com/nlohmann/json/archive/refs/tags/v3.11.3.tar.gz",
        sha256="0d8ef5af7f9794e3263480193c491549b2ba6cc74bb018906202ada498a79406",
        destination="deps",
        placement="nlohmann_json",
        when="@10.0:",
    )

    depends_on("tcl")
    depends_on("fmt")
    depends_on("spdlog")
    depends_on("googletest")
    depends_on("benchmark")

    depends_on("rocprof-trace-decoder@10.0.0", when="@10.0.0")

    @property
    def root_cmakelists_dir(self):
        return "profilers/profiler-hub"

    def patch(self):
        # Use the staged SQLite source instead of cloning at configure time.
        # https://github.com/ROCm/rocm-systems/blob/therock-10.0/profilers/profiler-hub/cmake/sqlite3.cmake
        sqlite_src = join_path(self.stage.source_path, "deps", "sqlite3")
        filter_file(
            'set(SQLITE3_SOURCE_DIR "${PROJECT_BINARY_DIR}/external/sqlite3")',
            f'set(SQLITE3_SOURCE_DIR "{sqlite_src}")',
            "profilers/profiler-hub/cmake/sqlite3.cmake",
            string=True,
        )

    def cmake_args(self):
        args = []
        if self.spec.satisfies("@10.0:"):
            args.append(
                self.define(
                    "FETCHCONTENT_SOURCE_DIR_NLOHMANN_JSON",
                    join_path(self.stage.source_path, "deps", "nlohmann_json"),
                )
            )
        return args
