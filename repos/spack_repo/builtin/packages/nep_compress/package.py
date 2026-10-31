# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class NepCompress(CMakePackage):
    """nep-compress provides additional compression filters for NetCDF-4/HDF5:
    an LZ4 HDF5 filter plugin with C and Fortran APIs, and Fortran wrappers for
    NetCDF-C's BZIP2 filter."""

    homepage = "https://captainkirk99.github.io/nep-compress/"
    url = "https://github.com/captainkirk99/nep-compress/archive/refs/tags/v1.2.0.tar.gz"
    git = "https://github.com/captainkirk99/nep-compress.git"

    maintainers("edhartnett")

    license("MIT", checked_by="edhartnett")

    version("main", branch="main")
    version("1.2.0", sha256="de1d83d9fee6d3dddce1798d9811626b576d75a6d75367dc268e88fbe7631349")

    variant("lz4", default=True, description="Build the LZ4 API and HDF5 filter plugin")
    variant(
        "bzip2",
        default=True,
        description="Build the Fortran BZIP2 API and tests (uses NetCDF-C's BZIP2 plugin)",
    )
    variant("fortran", default=True, description="Build the Fortran wrappers")

    conflicts("~lz4~bzip2", msg="Enable at least one compression filter")

    depends_on("c", type="build")
    depends_on("fortran", type="build", when="+fortran")
    depends_on("cmake@3.18:", type=("build", "test"))
    depends_on("pkgconfig", type=("build", "test"))

    depends_on("netcdf-c@4.10.0:")
    depends_on("netcdf-c+shared", when="+bzip2")
    depends_on("hdf5@1.14:+hl")
    depends_on("lz4", when="+lz4")
    depends_on("netcdf-fortran", when="+fortran")

    def cmake_args(self):
        spec = self.spec
        plugins = spec["netcdf-c"].prefix.plugins
        args = [
            self.define("CMAKE_INSTALL_LIBDIR", "lib"),
            self.define("BUILD_TESTING", self.run_tests),
            self.define("NEPCOMPRESS_BUILD_DOCS", False),
            self.define_from_variant("NEPCOMPRESS_BUILD_LZ4", "lz4"),
            self.define_from_variant("NEPCOMPRESS_BUILD_BZIP2", "bzip2"),
            self.define_from_variant("NEPCOMPRESS_ENABLE_FORTRAN", "fortran"),
        ]
        if spec.satisfies("+bzip2"):
            args.append(self.define("NEPCOMPRESS_BZIP2_PLUGIN_DIR", plugins))
        if self.run_tests and spec.satisfies("^netcdf-c+shared+zstd"):
            args.append(self.define("NEPCOMPRESS_ZSTD_PLUGIN_DIR", plugins))
        return args

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        if self.spec.satisfies("+lz4"):
            env.append_path("HDF5_PLUGIN_PATH", self.prefix.lib.plugin)

    @run_after("install")
    def cache_test_sources(self):
        cache_extra_test_sources(self, [join_path("test", "consumer")])

    def test_consumer(self):
        """build and run a CMake consumer of the installed package"""
        src = join_path(self.test_suite.current_test_cache_dir, "test", "consumer")
        cmake = which(self.spec["cmake"].prefix.bin.cmake)
        prefixes = [self.prefix, self.spec["netcdf-c"].prefix]
        if self.spec.satisfies("+fortran"):
            prefixes.append(self.spec["netcdf-fortran"].prefix)
        cmake(
            "-S",
            src,
            "-B",
            "build",
            "-DCMAKE_PREFIX_PATH={0}".format(";".join(str(p) for p in prefixes)),
        )
        cmake("--build", "build")
        which(join_path("build", "consumer_c"))()
        if self.spec.satisfies("+fortran"):
            which(join_path("build", "consumer_fortran"))()
