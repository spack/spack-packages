# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import re
import socket
import sys

from spack_repo.builtin.build_systems.cached_cmake import (
    CachedCMakePackage,
    cmake_cache_option,
    cmake_cache_path,
    cmake_cache_string,
)
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Caliper(CachedCMakePackage, CudaPackage, ROCmPackage):
    """Caliper is a program instrumentation and performance measurement
    framework. It is designed as a performance analysis toolbox in a
    library, allowing one to bake performance analysis capabilities
    directly into applications and activate them at runtime.
    """

    homepage = "https://github.com/LLNL/Caliper"
    git = "https://github.com/LLNL/Caliper.git"
    url = "https://github.com/LLNL/Caliper/archive/v2.14.0.tar.gz"
    tags = ["e4s", "radiuss"]

    maintainers("daboehme", "adrienbernede")

    test_requires_compiler = True

    license("BSD-3-Clause")

    version("master", branch="master")
    version("2.14.0", sha256="b42c35dfbe485960dd326033893dae37ac00d9807c5c3e6b5b1f396bc4af273f")
    version("2.13.1", sha256="7cef0173e0e0673abb7943a2641b660adfbc3d6bc4b33941ab4f431f92a4d016")
    version("2.13.0", sha256="28c6e8fd940bdee9e80d1e8ae1ce0f76d6a690cbb6242d4eec115d6c0204e331")
    version("2.12.1", sha256="2b5a8f98382c94dc75cc3f4517c758eaf9a3f9cea0a8dbdc7b38506060d6955c")
    version("2.11.0", sha256="b86b733cbb73495d5f3fe06e6a9885ec77365c8aa9195e7654581180adc2217c")
    version("2.10.0", sha256="14c4fb5edd5e67808d581523b4f8f05ace8549698c0e90d84b53171a77f58565")
    version("2.9.1", sha256="4771d630de505eff9227e0ec498d0da33ae6f9c34df23cb201b56181b8759e9e")
    version("2.9.0", sha256="507ea74be64a2dfd111b292c24c4f55f459257528ba51a5242313fa50978371f")

    is_linux = sys.platform.startswith("linux")
    variant("shared", default=True, description="Build shared libraries")
    variant("adiak", default=True, description="Enable Adiak support")
    variant("mpi", default=True, description="Enable MPI support")
    # libunwind has some issues on Mac
    variant(
        "libunwind", default=sys.platform != "darwin", description="Enable stack unwind support"
    )
    variant("libdw", default=is_linux, description="Enable DWARF symbol lookup")
    # pthread_self() signature is incompatible with PAPI_thread_init() on Mac
    variant("papi", default=sys.platform != "darwin", description="Enable PAPI service")
    variant("libpfm", default=False, description="Enable libpfm (perf_events) service")
    # Gotcha is Linux-only
    variant("gotcha", default=is_linux, description="Enable GOTCHA support")
    variant("sampler", default=is_linux, description="Enable sampling support on Linux")
    variant("fortran", default=False, description="Enable Fortran support")
    variant("variorum", default=False, description="Enable Variorum support")
    variant("vtune", default=False, description="Enable Intel Vtune support")
    variant("kokkos", default=True, description="Enable Kokkos profiling support")
    variant("tests", default=False, description="Enable tests")
    variant("tools", default=True, description="Enable tools")
    variant("python", default=False, description="Build Python bindings")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", when="+fortran", type="build")

    depends_on("rocprofiler-sdk", when="@2.14: +rocm")

    depends_on("adiak@0.1:0", when="@:2.10 +adiak")
    depends_on("adiak@0.4:0", when="@2.11: +adiak")

    depends_on("papi@5.3:", when="+papi")

    depends_on("libpfm4@4.8:4", when="+libpfm")

    depends_on("mpi", when="+mpi")
    depends_on("unwind@1.2:1", when="+libunwind")
    depends_on("elfutils", when="+libdw")
    depends_on("variorum", when="+variorum")
    depends_on("intel-oneapi-vtune", when="+vtune")

    depends_on("cmake", type="build")
    depends_on("python", type="build")

    depends_on("python@3", when="+python", type=("build", "link", "run"))
    depends_on("py-pybind11", when="+python", type=("build", "link", "run"))

    conflicts("+rocm+cuda")
    # Legacy nvtx is only supported until cuda@12.8, newer cuda only provides nvtx3.
    depends_on("cuda@:12.8", when="@:2.13.1 +cuda")
    # rocprofiler-sdk is only supported since rocm@6.2.4.
    depends_on("llvm-amdgpu@6.2.4:", when="@2.14: +rocm")

    patch("libunwind.patch", when="@:2.13")
    patch(
        "https://github.com/LLNL/Caliper/commit/648f8ab496a4a2c3f38e0cfa572340e429d8c76e.patch?full_index=1",
        sha256="d947b5df6b68a24f516bb3b4ec04c28d4b8246ac0cbe664cf113dd2b6ca92073",
        when="@2.12:2.13",
    )
    patch("for_aarch64.patch", when="@:2.11 target=aarch64:")
    patch(
        "sampler-service-missing-libunwind-include-dir.patch",
        when="@2.9.0:2.9.1 +libunwind +sampler",
    )

    def _get_sys_type(self, spec):
        sys_type = spec.architecture
        if "SYS_TYPE" in env:
            sys_type = env["SYS_TYPE"]
        return sys_type

    @property
    def cache_name(self):
        hostname = socket.gethostname()
        if "SYS_TYPE" in env:
            hostname = hostname.rstrip("1234567890")
        return "{0}-{1}-{2}@{3}-{4}.cmake".format(
            hostname,
            self._get_sys_type(self.spec),
            self.spec.compiler.name,
            self.spec.compiler.version,
            self.spec.dag_hash(8),
        )

    def initconfig_compiler_entries(self):
        spec = self.spec
        entries = super().initconfig_compiler_entries()

        if spec.satisfies("+rocm"):
            entries.insert(0, cmake_cache_path("CMAKE_CXX_COMPILER", spec["hip"].hipcc))

        entries.append(cmake_cache_option("WITH_FORTRAN", spec.satisfies("+fortran")))

        entries.append(cmake_cache_option("BUILD_SHARED_LIBS", spec.satisfies("+shared")))
        entries.append(cmake_cache_option("BUILD_TESTING", spec.satisfies("+tests")))
        entries.append(cmake_cache_option("WITH_TOOLS", spec.satisfies("+tools")))
        entries.append(cmake_cache_option("BUILD_DOCS", False))
        entries.append(cmake_cache_path("PYTHON_EXECUTABLE", spec["python"].command.path))

        return entries

    def initconfig_hardware_entries(self):
        spec = self.spec
        entries = super().initconfig_hardware_entries()

        if spec.satisfies("+cuda"):
            entries.append(cmake_cache_option("WITH_CUPTI", True))
            entries.append(cmake_cache_option("WITH_NVTX", True))
            entries.append(cmake_cache_path("CUDA_TOOLKIT_ROOT_DIR", spec["cuda"].prefix))
            entries.append(cmake_cache_path("CUPTI_PREFIX", spec["cuda"].prefix))

            # CUDA configuration from cuda_for_radiuss_projects
            cuda_flags = []
            if not spec.satisfies("cuda_arch=none"):
                cuda_archs = ";".join(spec.variants["cuda_arch"].value)
                entries.append(cmake_cache_string("CMAKE_CUDA_ARCHITECTURES", cuda_archs))

            # gcc-toolchain support
            gcc_toolchain_regex = re.compile(".*gcc-toolchain.*")
            using_toolchain = list(
                filter(gcc_toolchain_regex.match, spec.compiler_flags["cxxflags"])
            )
            if using_toolchain:
                cuda_flags.append("-Xcompiler {}".format(using_toolchain[0]))

            if cuda_flags:
                entries.append(cmake_cache_string("CMAKE_CUDA_FLAGS", " ".join(cuda_flags)))
        else:
            entries.append(cmake_cache_option("WITH_CUPTI", False))
            entries.append(cmake_cache_option("WITH_NVTX", False))

        if spec.satisfies("+rocm"):
            # HIP configuration from hip_for_radiuss_projects
            rocm_root = spec["llvm-amdgpu"].prefix
            gcc_toolchain_regex = re.compile(".*gcc-toolchain.*")
            using_toolchain = list(
                filter(gcc_toolchain_regex.match, spec.compiler_flags["cxxflags"])
            )
            hip_link_flags = ""

            if using_toolchain:
                gcc_prefix = using_toolchain[0]
                entries.append(
                    cmake_cache_string("HIP_CLANG_FLAGS", "--gcc-toolchain={0}".format(gcc_prefix))
                )
                entries.append(
                    cmake_cache_string(
                        "CMAKE_EXE_LINKER_FLAGS",
                        hip_link_flags + " -Wl,-rpath={0}/lib64".format(gcc_prefix),
                    )
                )
            else:
                entries.append(
                    cmake_cache_string(
                        "CMAKE_EXE_LINKER_FLAGS", "-Wl,-rpath={0}/llvm/lib/".format(rocm_root)
                    )
                )

            if spec.satisfies("@2.14:"):
                entries.append(cmake_cache_option("WITH_ROCPROFILER", True))
                entries.append(cmake_cache_option("WITH_ROCTRACER", False))
                entries.append(cmake_cache_option("WITH_ROCTX", False))
            else:
                entries.append(cmake_cache_option("WITH_ROCPROFILER", False))
                entries.append(cmake_cache_option("WITH_ROCTRACER", True))
                entries.append(cmake_cache_option("WITH_ROCTX", True))
        else:
            entries.append(cmake_cache_option("WITH_ROCPROFILER", False))
            entries.append(cmake_cache_option("WITH_ROCTRACER", False))
            entries.append(cmake_cache_option("WITH_ROCTX", False))

        return entries

    def initconfig_mpi_entries(self):
        spec = self.spec
        entries = super().initconfig_mpi_entries()

        entries.append(cmake_cache_option("WITH_MPI", spec.satisfies("+mpi")))

        return entries

    def initconfig_package_entries(self):
        spec = self.spec
        entries = []

        # TPL locations
        entries.append("#------------------{0}".format("-" * 60))
        entries.append("# TPLs")
        entries.append("#------------------{0}\n".format("-" * 60))

        if spec.satisfies("+adiak"):
            entries.append(cmake_cache_path("adiak_DIR", spec["adiak"].prefix))
        if spec.satisfies("+papi"):
            entries.append(cmake_cache_path("PAPI_PREFIX", spec["papi"].prefix))
        if spec.satisfies("+libdw"):
            entries.append(cmake_cache_path("LIBDW_PREFIX", spec["elfutils"].prefix))
        if spec.satisfies("+libpfm"):
            entries.append(cmake_cache_path("LIBPFM_INSTALL", spec["libpfm4"].prefix))
        if spec.satisfies("+sosflow"):
            entries.append(cmake_cache_path("SOS_PREFIX", spec["sosflow"].prefix))
        if spec.satisfies("+variorum"):
            entries.append(cmake_cache_path("VARIORUM_PREFIX", spec["variorum"].prefix))
        if spec.satisfies("+vtune"):
            itt_dir = join_path(spec["intel-oneapi-vtune"].prefix, "vtune", "latest")
            entries.append(cmake_cache_path("ITT_PREFIX", itt_dir))
        if spec.satisfies("+libunwind"):
            entries.append(cmake_cache_path("LIBUNWIND_PREFIX", spec["unwind"].prefix))

        # Build options
        entries.append("#------------------{0}".format("-" * 60))
        entries.append("# Build Options")
        entries.append("#------------------{0}\n".format("-" * 60))

        entries.append(cmake_cache_option("WITH_ADIAK", spec.satisfies("+adiak")))
        entries.append(cmake_cache_option("WITH_GOTCHA", spec.satisfies("+gotcha")))
        entries.append(cmake_cache_option("WITH_SAMPLER", spec.satisfies("+sampler")))
        entries.append(cmake_cache_option("WITH_PAPI", spec.satisfies("+papi")))
        entries.append(cmake_cache_option("WITH_LIBDW", spec.satisfies("+libdw")))
        entries.append(cmake_cache_option("WITH_LIBPFM", spec.satisfies("+libpfm")))
        entries.append(cmake_cache_option("WITH_SOSFLOW", spec.satisfies("+sosflow")))
        entries.append(cmake_cache_option("WITH_KOKKOS", spec.satisfies("+kokkos")))
        entries.append(cmake_cache_option("WITH_VARIORUM", spec.satisfies("+variorum")))
        entries.append(cmake_cache_option("WITH_VTUNE", spec.satisfies("+vtune")))
        entries.append(cmake_cache_option("WITH_PYTHON_BINDINGS", spec.satisfies("+python")))
        entries.append(cmake_cache_option("WITH_LIBUNWIND", spec.satisfies("+libunwind")))

        return entries

    def cmake_args(self):
        return []

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        if self.spec.satisfies("+python"):
            env.prepend_path("PYTHONPATH", self.spec.prefix.join(python_platlib))
            env.prepend_path("PYTHONPATH", self.spec.prefix.join(python_purelib))

    @run_after("install")
    def cache_test_sources(self):
        """Copy the example source files after the package is installed to an
        install test subdirectory for use during `spack test run`."""
        cache_extra_test_sources(self, [join_path("examples", "apps")])

    def test_cxx_example(self):
        """build and run cxx-example"""

        exe = "cxx-example"
        source_file = "{0}.cpp".format(exe)

        source_path = find_required_file(
            self.test_suite.current_test_cache_dir, source_file, expected=1, recursive=True
        )

        lib_dir = self.prefix.lib if os.path.exists(self.prefix.lib) else self.prefix.lib64

        cxx = which(os.environ["CXX"])
        test_dir = os.path.dirname(source_path)
        with working_dir(test_dir):
            cxx(
                "-L{0}".format(lib_dir),
                "-I{0}".format(self.prefix.include),
                source_path,
                "-o",
                exe,
                "-std=c++11",
                "-lcaliper",
                "-lstdc++",
            )

            cxx_example = which(exe)
            cxx_example()
