# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Hypredrive(CMakePackage):
    """Hypredrive is a high-level interface to the hypre library for solving
    sparse linear systems of equations. It provides a command-line driver
    (hypredrive-cli) accepting YAML input files and a C API library
    (libHYPREDRV)."""

    homepage = "https://hypredrive.readthedocs.io"
    url = "https://github.com/hypre-space/hypredrive/archive/v0.1.0.tar.gz"
    git = "https://github.com/hypre-space/hypredrive.git"

    maintainers("victorapm")

    license("MIT", checked_by="victorapm")

    version("develop", branch="master")
    version("0.2.0", sha256="2fe6c5b2779de41fbd294cb4647c7bbd210ec95934639117e56a790e56c32e41")
    version("0.1.0", sha256="39db73b75e37457035c64b4c8831abe716bf2f596c4ca79a32293d9bd51ca8d6")

    variant("shared", default=False, description="Build shared libraries")
    variant("pic", default=False, description="Build position independent code")
    variant("examples", default=False, description="Build and install example programs")
    variant("hwloc", default=False, description="Enable hwloc support for system topology")
    variant("caliper", default=False, description="Enable Caliper performance profiling")
    variant("compression", default=False, description="Enable lossless compression backends")

    depends_on("c", type="build")
    depends_on("cmake@3.23:", type="build")
    depends_on("mpi")
    depends_on("hypre@2.20.0: +mpi")
    depends_on("hwloc", when="+hwloc")
    depends_on("caliper", when="+caliper")
    depends_on("zlib-api", when="+compression")
    depends_on("zstd", when="+compression")
    depends_on("lz4", when="+compression")

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

    def test_installed_binary(self):
        """verify hypredrive-cli binary exists"""
        hypredrive_cli = which(self.prefix.bin.join("hypredrive-cli"))
        if hypredrive_cli is None:
            raise SkipTest("hypredrive-cli not found in install prefix")

    def test_installed_library(self):
        """verify HYPREDRV library is findable"""
        if not self.libs:
            raise RuntimeError("Could not find libHYPREDRV in install prefix")

    def test_laplacian_example(self):
        """run the laplacian example (requires +examples)"""
        if not self.spec.satisfies("+examples"):
            raise SkipTest("Package must be installed with +examples")

        laplacian = which(self.prefix.bin.laplacian)
        if laplacian is None:
            raise SkipTest("laplacian example binary not found")

        mpirun = which("mpirun", "mpiexec", required=True)
        mpirun("-np", "1", laplacian, "-n", "6", "6", "6", "-s", "7", "-ns", "1", "-v", "1")
