# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import re

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.rocm import ROCmLibrary

from spack.package import *


def submodules(package):
    submodules = [
        "projects/rocprofiler-systems/external/timemory",
        "projects/rocprofiler-systems/external/perfetto",
        "projects/rocprofiler-systems/external/elfio",
        "projects/rocprofiler-systems/external/dyninst",
        "projects/rocprofiler-systems/external/papi",
        "projects/rocprofiler-systems/external/pybind11",
        "projects/rocprofiler-systems/external/onetbb",
    ]
    if package is not None and package.spec.satisfies("@:7.2"):
        submodules.append("projects/rocprofiler-systems/external/PTL")
    if package is not None and package.spec.satisfies("@:7.13"):
        submodules.append("projects/rocprofiler-systems/examples/openmp/external/ompvv")
    return submodules


class RocprofilerSystems(ROCmLibrary, CMakePackage):
    """Application Profiling, Tracing, and Analysis"""

    homepage = "https://github.com/ROCm/rocprofiler-systems"
    git = "https://github.com/ROCm/rocm-systems.git"

    rocm_url_map = [
        ("7.1.1", "https://github.com/ROCm/rocprofiler-systems/archive/refs/tags/rocm-{0}.tar.gz"),
        ("7.2.3", "https://github.com/ROCm/rocm-systems/archive/rocm-{0}.tar.gz"),
        (None, "https://github.com/ROCm/rocm-systems/archive/refs/tags/therock-{1}.{2}.tar.gz"),
    ]
    executables = ["rocprof-sys-sample"]
    tags = ["rocm"]

    maintainers("dgaliffiAMD", "afzpatel", "srekolam", "renjithravindrankannath")

    license("MIT")

    version(
        "10.0.0",
        tag="therock-10.0",
        commit="6b0e43f341195e203754e08f850e437ff2fc09f9",
        submodules=submodules,
    )
    version(
        "7.14.0",
        tag="therock-7.14",
        commit="2b22ab0195cc1461cd9abf3b969e9dd7c10af350",
        submodules=submodules,
    )
    version(
        "7.13.0",
        git="https://github.com/ROCm/rocm-systems.git",
        tag="therock-7.13",
        submodules=submodules,
    )
    version(
        "7.2.3",
        tag="rocm-7.2.3",
        commit="c2d94761153e1033a91744842dfc66eddd631fde",
        submodules=submodules,
    )
    version(
        "7.2.1",
        git="https://github.com/ROCm/rocm-systems.git",
        tag="rocm-7.2.1",
        commit="e1a6bc5663304b9c586b3254b8920f2981057804",
        submodules=submodules,
    )
    version(
        "7.2.0",
        git="https://github.com/ROCm/rocm-systems.git",
        tag="rocm-7.2.0",
        commit="fc0010cf6a5a972d42b276df946510f30343d493",
        submodules=submodules,
    )
    version(
        "7.1.1",
        git="https://github.com/ROCm/rocprofiler-systems",
        branch="release/rocm-rel-7.1.1",
        submodules=True,
    )
    version(
        "7.1.0",
        git="https://github.com/ROCm/rocprofiler-systems",
        tag="rocm-7.1.0",
        commit="427f656162559f21fc3d6cb0e3688f3d31ae374c",
        submodules=True,
    )
    version(
        "7.0.2",
        git="https://github.com/ROCm/rocprofiler-systems",
        tag="rocm-7.0.2",
        commit="8bad624afb06ea2b567e985484d1b5d604865743",
        submodules=True,
    )
    version(
        "7.0.0",
        git="https://github.com/ROCm/rocprofiler-systems",
        tag="rocm-7.0.0",
        commit="1030d99db9934a07f1d276f6aadd0eb810b5f5f9",
        submodules=True,
    )
    version(
        "6.4.3",
        git="https://github.com/ROCm/rocprofiler-systems",
        tag="rocm-6.4.3",
        commit="ba0bfe8cf344294347cbb854084ab5b5df1b1a43",
        submodules=True,
    )
    version(
        "6.4.2",
        git="https://github.com/ROCm/rocprofiler-systems",
        tag="rocm-6.4.2",
        commit="ba0bfe8cf344294347cbb854084ab5b5df1b1a43",
        submodules=True,
    )
    version(
        "6.4.1",
        git="https://github.com/ROCm/rocprofiler-systems",
        tag="rocm-6.4.1",
        commit="2e945e4a08781e13a822f568814e2c434fd8858f",
        submodules=True,
    )
    version(
        "6.4.0",
        git="https://github.com/ROCm/rocprofiler-systems",
        tag="rocm-6.4.0",
        commit="c4cec593b6021f2b84294838f2ffe388ed8e911a",
        submodules=True,
    )
    version(
        "6.3.3",
        git="https://github.com/ROCm/rocprofiler-systems",
        tag="rocm-6.3.3",
        commit="f03ef1dd9a4e984e3e72056352532e6149e742fc",
        submodules=True,
    )
    version(
        "6.3.2",
        git="https://github.com/ROCm/rocprofiler-systems",
        tag="rocm-6.3.2",
        commit="2fd5fbbef941ff219a1ecef702f8cfaae6e8e5ba",
        submodules=True,
    )
    version(
        "6.3.1",
        git="https://github.com/ROCm/rocprofiler-systems",
        tag="rocm-6.3.1",
        commit="04a84dd0b0df3dfd61f7765696e0e474ec29f10b",
        submodules=True,
    )

    version(
        "6.3.0",
        git="https://github.com/ROCm/rocprofiler-systems",
        tag="rocm-6.3.0",
        commit="71a5e271b5e07efd2948fb6e7b451db5e8e40cb8",
        submodules=True,
    )

    variant(
        "rocm",
        default=True,
        description="Enable ROCm API, kernel tracing, and GPU HW counters support",
    )
    variant("strip", default=False, description="Faster binary instrumentation, worse debugging")
    variant(
        "python", default=False, description="Enable support for Python function profiling and API"
    )
    variant("papi", default=True, description="Enable HW counters support via PAPI")
    variant("ompt", default=True, description="Enable OpenMP Tools support")
    variant(
        "tau",
        default=False,
        description="Enable support for using TAU markers in omnitrace instrumentation",
    )
    variant(
        "caliper",
        default=False,
        description="Enable support for using Caliper markers in omnitrace instrumentation",
    )
    variant(
        "perfetto_tools",
        default=False,
        description="Install perfetto tools (e.g. traced, perfetto)",
    )
    variant(
        "mpi",
        default=False,
        description=(
            "Enable intercepting MPI functions and aggregating output during finalization "
            "(requires target application to use same MPI installation)"
        ),
    )
    variant(
        "mpi_headers",
        default=True,
        description=(
            "Enable intercepting MPI functions but w/o support for aggregating output "
            "(target application can use any MPI installation)"
        ),
    )
    variant(
        "internal-dyninst",
        default=False,
        when="@:7.2",
        description="build internal dyninst",
    )
    variant(
        "internal-dyninst",
        default=True,
        when="@7.13:",
        description="build internal dyninst",
    )
    variant("internal-tbb", default=False, description="build internal tbb")

    conflicts("%rocmcc", when="+internal-tbb")
    conflicts("%clang", when="+internal-tbb")
    extends("python", when="+python")

    resource(
        name="dyninst",
        url="https://github.com/ROCm/dyninst/archive/81cd27fc9ae4984df307bc41d5cb8c1ce9bf761e.tar.gz",
        sha256="f546d524be665628b6aae2bfb297155f2029933d31b0a427cf449e236c1f51e9",
        placement="projects/rocprofiler-systems/external/dyninst",
        when="@10.0: +internal-dyninst",
    )
    resource(
        name="onetbb",
        url="https://github.com/uxlfoundation/oneTBB/archive/f1862f38f83568d96e814e469ab61f88336cc595.tar.gz",
        sha256="9e90b619ced869b45e8ead5fbb00c421d00589ac76ddd217a9e3a72bf5cea6b2",
        placement="projects/rocprofiler-systems/external/onetbb",
        when="@10.0: +internal-tbb",
    )
    resource(
        name="perfetto",
        url="https://github.com/google/perfetto/archive/35b3d9845c2f4017865c4dc93fafcf6d202f1651.tar.gz",
        sha256="a9c557da7717d4c36689365f2b016d191b3921187da1a6e49a1ce2f23e7fd774",
        placement="projects/rocprofiler-systems/external/perfetto",
        when="@10.0:",
    )
    resource(
        name="timemory",
        url="https://github.com/ROCm/timemory/archive/54ae9d214a63132da22c7cab21c5fb4b7b5049f8.tar.gz",
        sha256="24bf512416e8ad1646cfe43333a1ddcf3a7ba2c40432ad7dd361ca80ff228307",
        placement="projects/rocprofiler-systems/external/timemory",
        when="@10.0:",
    )
    resource(
        name="binutils",
        url="https://ftpmirror.gnu.org/gnu/binutils/binutils-2.46.0.tar.bz2",
        sha256="0f3152632a2a9ce066f20963e9bb40af7cf85b9b6c409ed892fd0676e84ecd12",
        expand=False,
        placement="binutils-2.46.0.tar.bz2",
        when="@10.0",
    )

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    # hard dependencies
    depends_on("cmake@3.16:", type="build")
    depends_on("dyninst@:12", when="@6 ~internal-dyninst")
    depends_on("dyninst@13", when="@7 ~internal-dyninst")
    depends_on(
        "boost@:1.88"
        "+atomic+chrono+date_time+filesystem+system+thread+timer+container+random+exception",
        when="@:7.1.0 +internal-dyninst",
    )
    depends_on(
        "boost@:1.88"
        "+atomic+chrono+date_time+filesystem+system+thread+timer+container+random+exception",
        when="@7.1.1:",
    )
    depends_on("libiberty+pic", when="+internal-dyninst")
    depends_on("intel-tbb@2019:2020.3", when="@:7.13 ~internal-tbb")
    depends_on("intel-tbb@2019:2021.3", when="@7.14: ~internal-tbb")
    depends_on("sqlite", when="@7.1:")
    depends_on("tcl", type="build", when="@7.1:")
    depends_on("elfutils")
    depends_on("m4")
    depends_on("texinfo")
    depends_on("libunwind", type=("build", "run"))
    depends_on("papi+shared", when="+papi")
    depends_on("mpi", when="+mpi")
    depends_on("tau", when="+tau")
    depends_on("caliper", when="+caliper")
    depends_on("python@3:", when="+python", type=("build", "run"))
    depends_on("libunwind", when="+rocm")
    depends_on("autoconf", when="+rocm")
    depends_on("automake", when="+rocm")
    depends_on("libtool", when="+rocm")
    depends_on("sqlite", when="@7.1:")
    depends_on("spdlog", when="@10:")
    depends_on("nlohmann-json", when="@10:")
    depends_on("libiberty", when="@10:")
    # timemory Packages.cmake air-gap: BUILD_*=OFF uses find_package(...)
    depends_on("yaml-cpp@:0.8.0", when="@10.0")
    depends_on("gotcha", when="@10.0")

    with when("+rocm"):
        for ver in ["6.3.0", "6.3.1", "6.3.2", "6.3.3"]:
            depends_on(f"roctracer-dev@{ver}", when=f"@{ver}")
            depends_on(f"rocprofiler-dev@{ver}", when=f"@{ver}")

        for ver in ["6.3.0", "6.3.1", "6.3.2", "6.3.3", "6.4.0", "6.4.1", "6.4.2", "6.4.3"]:
            depends_on(f"rocm-smi-lib@{ver}", when=f"@{ver}")

        for ver in [
            "6.3.0",
            "6.3.1",
            "6.3.2",
            "6.3.3",
            "6.4.0",
            "6.4.1",
            "6.4.2",
            "6.4.3",
            "7.0.0",
            "7.0.2",
            "7.1.0",
            "7.1.1",
            "7.2.0",
            "7.2.1",
            "7.2.3",
            "7.13.0",
            "7.14.0",
            "10.0.0",
        ]:
            depends_on(f"hip@{ver}", when=f"@{ver}")

        for ver in [
            "6.4.0",
            "6.4.1",
            "6.4.2",
            "6.4.3",
            "7.0.0",
            "7.0.2",
            "7.1.0",
            "7.1.1",
            "7.2.0",
            "7.2.1",
            "7.2.3",
            "7.13.0",
            "7.14.0",
            "10.0.0",
        ]:
            depends_on(f"rocprofiler-sdk@{ver}", when=f"@{ver}")

        for ver in [
            "7.0.0",
            "7.0.2",
            "7.1.0",
            "7.1.1",
            "7.2.0",
            "7.2.1",
            "7.2.3",
            "7.13.0",
            "7.14.0",
            "10.0.0",
        ]:
            depends_on(f"amdsmi@{ver}", when=f"@{ver}")

        depends_on("profiler-hub@10.0.0", when="@10.0.0")

    # Fix GCC 13 build failure caused by a missing include of <array> in dyninst
    patch(
        "https://github.com/ROCm/dyninst/commit/09e781d414c83b4ad587083d449a3e976546937d.patch?full_index=1",
        sha256="e64c6b75393e7fbd711c0bd0233628c176a352cd10b4057f00eec283426eaf0a",
        when="@:6.4.0 +internal-dyninst",
        working_dir="external/dyninst",
    )
    patch(
        "https://github.com/ROCm/timemory/commit/b5e41aa9e4b83ab0868211d81924ac4f639bd998.patch?full_index=1",
        sha256="2696f59dd9b6e74bf44bfcc56a0536c3f1f3845c29fac18f0224dee72bd9225f",
        when="@:7.1 %rocmcc",
        working_dir="external/timemory",
    )
    # Allow -DTIMEMORY_BUILD_GOTCHA=OFF with external gotcha (air-gapped builds)
    patch("0001-allow-external-gotcha-10.0.patch", when="@10.0")
    patch(
        "0002-binutils-single-url-10.0.patch",
        when="@10.0",
        working_dir="projects/rocprofiler-systems/external/timemory",
    )

    @property
    def root_cmakelists_dir(self):
        if self.spec.satisfies("@:7.1"):
            return "."
        else:
            return "projects/rocprofiler-systems"

    def cmake_args(self):
        spec = self.spec

        args = [
            self.define("SPACK_BUILD", True),
            self.define("ROCPROFSYS_BUILD_PAPI", False),
            self.define("ROCPROFSYS_BUILD_PYTHON", True),
            self.define("ROCPROFSYS_BUILD_LIBUNWIND", False),
            self.define("ROCPROFSYS_BUILD_STATIC_LIBGCC", False),
            self.define("ROCPROFSYS_BUILD_STATIC_LIBSTDCXX", False),
            self.define_from_variant("ROCPROFSYS_BUILD_DYNINST", "internal-dyninst"),
            self.define_from_variant("ROCPROFSYS_BUILD_LTO", "ipo"),
            self.define_from_variant("ROCPROFSYS_USE_MPI", "mpi"),
            self.define_from_variant("ROCPROFSYS_USE_OMPT", "ompt"),
            self.define_from_variant("ROCPROFSYS_USE_PAPI", "papi"),
            self.define_from_variant("ROCPROFSYS_USE_RCCL", "rocm"),
            self.define_from_variant("ROCPROFSYS_USE_PYTHON", "python"),
            self.define_from_variant("ROCPROFSYS_USE_MPI_HEADERS", "mpi_headers"),
            self.define_from_variant("ROCPROFSYS_STRIP_LIBRARIES", "strip"),
            self.define_from_variant("ROCPROFSYS_INSTALL_PERFETTO_TOOLS", "perfetto_tools"),
            self.define("ElfUtils_ROOT_DIR", spec["elfutils"].prefix),
            # timemory arguments
            self.define("TIMEMORY_BUILD_CALIPER", False),
            self.define_from_variant("TIMEMORY_USE_TAU", "tau"),
            self.define_from_variant("TIMEMORY_USE_CALIPER", "caliper"),
        ]
        if spec.satisfies("@:6.3"):
            args.append(self.define_from_variant("ROCPROFSYS_USE_ROCM_SMI", "rocm"))
            args.append(self.define_from_variant("ROCPROFSYS_USE_HIP", "rocm"))
            args.append(self.define_from_variant("ROCPROFSYS_USE_ROCTRACER", "rocm"))
            args.append(self.define_from_variant("ROCPROFSYS_USE_ROCPROFILER", "rocm"))
        else:
            args.append(self.define_from_variant("ROCPROFSYS_USE_ROCM", "rocm"))

        if "+tau" in spec:
            tau_root = spec["tau"].prefix
            args.append(self.define("TAU_ROOT_DIR", tau_root))

        if "+mpi" in spec:
            args.append(self.define("MPI_C_COMPILER", spec["mpi"].mpicc))
            args.append(self.define("MPI_CXX_COMPILER", spec["mpi"].mpicxx))

        if spec.satisfies("@6.3:"):
            args.append(self.define("dl_LIBRARY", "dl"))
            args.append(
                self.define("libunwind_INCLUDE_DIR", self.spec["libunwind"].prefix.include)
            )
        if spec.satisfies("@7.0:"):
            args.append(self.define_from_variant("ROCPROFSYS_BUILD_TBB", "internal-tbb"))
        if spec.satisfies("+internal-dyninst"):
            args.append(self.define_from_variant("DYNINST_BUILD_TBB", "internal-tbb"))
        if spec.satisfies("@7.2:"):
            args.append(self.define("libunwind_ROOT", self.spec["libunwind"].prefix))
        if spec.satisfies("@10.0"):
            args.append(self.define("ROCPROFSYS_BUILD_SQLITE3", False))
            args.append(self.define("ROCPROFSYS_BUILD_SPDLOG", False))
            args.append(self.define("ROCPROFSYS_BUILD_NLOHMANN_JSON", False))
            args.append(self.define("ROCPROFSYS_BUILD_LIBIBERTY", False))
            args.append(self.define("ROCPROFSYS_BUILD_ELFUTILS", False))
            args.append(
                self.define(
                    "TIMEMORY_BINUTILS_DOWNLOAD_URL",
                    join_path(
                        self.stage.source_path,
                        "binutils-2.46.0.tar.bz2",
                        "binutils-2.46.0.tar.bz2",
                    ),
                )
            )
            args.append(self.define("TIMEMORY_BUILD_YAML", False))
            args.append(self.define("TIMEMORY_BUILD_GOOGLE_TEST", False))
            args.append(self.define("TIMEMORY_BUILD_OMPT", False))
            args.append(self.define("TIMEMORY_BUILD_DYNINST", False))
            args.append(self.define("TIMEMORY_BUILD_GOTCHA", False))
        return args

    def flag_handler(self, name, flags):
        if self.spec.satisfies("@6.3:7.1") or self.spec.satisfies("@7.14:"):
            if name == "ldflags":
                flags.append("-lintl")
        return (flags, None, None)

    @classmethod
    def determine_version(cls, exe):
        output = Executable(exe)("--version", output=str, error=str)
        match = re.search(r"rocm: v(\d+)\.(\d+)", output)
        if match:
            ver = "{0}.{1}".format(int(match.group(1)), int(match.group(2)))
        else:
            ver = None
        return ver

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        if "+tau" in self.spec:
            import glob

            # below is how TAU_MAKEFILE is set in packages/tau/package.py
            pattern = join_path(self.spec["tau"].prefix.lib, "Makefile.*")
            files = glob.glob(pattern)
            if files:
                env.set("TAU_MAKEFILE", files[0])
