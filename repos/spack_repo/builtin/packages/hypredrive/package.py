# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Hypredrive(CMakePackage):
    """Hypredrive is a flexible engine for solving linear systems with hypre.
    It provides a command-line driver (hypredrive-cli) and a C API library
    (libHYPREDRV) accepting YAML input."""

    homepage = "https://hypredrive.readthedocs.io"
    url = "https://github.com/hypre-space/hypredrive/archive/v0.2.0.tar.gz"
    git = "https://github.com/hypre-space/hypredrive.git"

    maintainers("victorapm")

    license("MIT", checked_by="victorapm")

    version("master", branch="master")
    version("0.2.0", sha256="2fe6c5b2779de41fbd294cb4647c7bbd210ec95934639117e56a790e56c32e41")
    version("0.1.0", sha256="39db73b75e37457035c64b4c8831abe716bf2f596c4ca79a32293d9bd51ca8d6")

    variant("shared", default=False, description="Build shared libraries")
    variant("pic", default=False, description="Build position independent code")
    variant("examples", default=False, description="Build and install example programs")
    variant("hwloc", default=False, description="Enable hwloc support for system topology")
    variant("caliper", default=False, description="Enable Caliper performance profiling")
    variant("compression", default=False, description="Enable lossless compression backends")

    depends_on("c", type="build")
    depends_on("cxx", type="build", when="+caliper")

    depends_on("cmake@3.23:", type="build")
    depends_on("mpi")
    depends_on("hypre@2.20.0: +mpi")
    depends_on("hwloc", when="+hwloc")
    depends_on("caliper", when="+caliper")
    depends_on("zlib-api", when="+compression")
    depends_on("zstd", when="+compression")
    depends_on("lz4", when="+compression")

    conflicts("+shared ~pic")

    def cmake_args(self):
        spec = self.spec
        from_variant = self.define_from_variant

        args = [
            from_variant("BUILD_SHARED_LIBS", "shared"),
            from_variant("HYPREDRV_ENABLE_EXAMPLES", "examples"),
            from_variant("HYPREDRV_ENABLE_HWLOC", "hwloc"),
            from_variant("HYPREDRV_ENABLE_CALIPER", "caliper"),
            from_variant("HYPREDRV_ENABLE_COMPRESSION", "compression"),
            from_variant("CMAKE_POSITION_INDEPENDENT_CODE", "pic"),
            self.define("HYPRE_ROOT", spec["hypre"].prefix),
            self.define("HYPREDRV_ENABLE_TESTING", self.run_tests),
            self.define("HYPREDRV_ENABLE_COVERAGE", False),
            self.define("HYPREDRV_ENABLE_ANALYSIS", False),
            self.define("HYPREDRV_ENABLE_DOCS", False),
        ]

        return args

    @property
    def headers(self):
        """Export the main HYPREDRV header.
        Sample usage: spec['hypredrive'].headers.cpp_flags
        """
        hdrs = find_headers("HYPREDRV", self.prefix.include, recursive=False)
        return hdrs or None

    @property
    def libs(self):
        """Export the HYPREDRV library.
        Sample usage: spec['hypredrive'].libs.ld_flags
        """
        is_shared = self.spec.satisfies("+shared")
        libs = find_libraries("libHYPREDRV", root=self.prefix, shared=is_shared, recursive=True)
        return libs or None

    @property
    def sanity_check_is_file(self):
        sanity_files = [join_path("bin", "hypredrive-cli")]

        if self.spec.satisfies("+shared"):
            if self.spec.satisfies("platform=darwin"):
                lib_name = "libHYPREDRV.dylib"
            else:
                lib_name = "libHYPREDRV.so"
        else:
            lib_name = "libHYPREDRV.a"

        for lib_dir, rel_name in ((self.prefix.lib64, "lib64"), (self.prefix.lib, "lib")):
            if os.path.isfile(join_path(lib_dir, lib_name)):
                sanity_files.append(join_path(rel_name, lib_name))
                break
        else:
            expected_lib_dir = "lib64" if os.path.isdir(self.prefix.lib64) else "lib"
            sanity_files.append(join_path(expected_lib_dir, lib_name))

        return sanity_files

    @when("+examples")
    def test_laplacian_example(self):
        """run the laplacian example (requires +examples)"""

        laplacian = which(self.prefix.bin.laplacian)
        if laplacian is None:
            raise SkipTest("laplacian example binary not found")

        mpirun = which("mpirun", "mpiexec", required=True)
        mpirun("-np", "1", laplacian, "-n", "6", "6", "6", "-s", "7", "-ns", "1", "-v", "1")
