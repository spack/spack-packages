# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Nep(CMakePackage):
    """NEP (NetCDF Extension Pack) provides high-performance LZ4 and BZIP2
    compression filters for HDF5/NetCDF-4 files and transparent read access
    to scientific data formats (GeoTIFF, GRIB2, FITS, NASA CDF, PDS4)
    through the standard NetCDF API via User Defined Format handlers."""

    homepage = "https://github.com/Intelligent-Data-Design-Inc/NEP"
    url = "https://github.com/Intelligent-Data-Design-Inc/NEP/archive/v1.0.0.tar.gz"
    git = "https://github.com/Intelligent-Data-Design-Inc/NEP.git"

    maintainers("edhartnett")

    license("Apache-2.0")

    version("main", branch="main")

    version(
        "2.3.0",
        sha256="ce6eb7640a44e4b068af4beef3a1b7c5a4772666fbea73db34d81d71b4144dde",
        url="https://github.com/Intelligent-Data-Design-Inc/NEP/archive/v2.3.0.tar.gz",
    )

    version(
        "2.5.0",
        sha256="fbc160eb8333b2b34c49119c07947f5fa2f526c3ba747d482c8578be8b8c97ef",
        url="https://github.com/Intelligent-Data-Design-Inc/NEP/archive/v2.5.0.tar.gz",
    )

    version(
        "2.4.0",
        sha256="d4144894ed5f7f544bd68252fdd905b5e8f8b27f8829049a9a344f226278c84b",
        url="https://github.com/Intelligent-Data-Design-Inc/NEP/archive/v2.4.0.tar.gz",
    )

    variant("docs", default=True, description="Build documentation with Doxygen")
    variant("lz4", default=True, description="Enable LZ4 compression support")
    variant("bzip2", default=True, description="Enable BZIP2 compression support")
    variant("fortran", default=True, description="Build Fortran wrappers")
    variant("fits", default=False, description="Enable FITS reader support via CFITSIO")
    variant("geotiff", default=False, description="Enable GeoTIFF reader support via libgeotiff")
    variant("grib2", default=False, description="Enable GRIB2 reader support via NCEPLIBS-g2c")
    variant("cdf", default=False, description="Enable NASA CDF reader support")
    variant("pds4", default=False, description="Enable PDS4 reader support via libxml2")
    variant(
        "parallel",
        default=False,
        description="Enable parallel I/O tests (requires MPI-enabled HDF5 and netcdf-c)",
    )
    variant("examples", default=False, description="Build example programs")
    variant("benchmarks", default=False, description="Build performance benchmark programs")

    depends_on("c", type="build")
    depends_on("fortran", when="+fortran", type="build")

    depends_on("netcdf-c@4.10.1:", type=("build", "link"))
    depends_on("netcdf-c +mpi", when="+parallel", type=("build", "link"))
    depends_on("hdf5@1.12:+hl~mpi", when="~parallel", type=("build", "link"))
    depends_on("hdf5@1.12:+hl+mpi", when="+parallel", type=("build", "link"))
    depends_on("lz4", when="+lz4", type=("build", "link"))
    depends_on("bzip2", when="+bzip2", type=("build", "link"))
    depends_on("netcdf-fortran", when="+fortran", type=("build", "link"))
    depends_on("cfitsio", when="+fits", type=("build", "link"))
    depends_on("libgeotiff", when="+geotiff", type=("build", "link"))
    depends_on("g2c", when="+grib2", type=("build", "link"))
    # cdf: NASA CDF library; not a Spack builtin. Register spack/cdf/package.py
    # from the NEP repo in a local Spack repository before using +cdf.
    depends_on("libxml2", when="+pds4", type=("build", "link"))
    depends_on("mpi", when="+parallel", type=("build", "link", "run"))
    depends_on("libtiff", when="+geotiff", type=("build", "link"))
    depends_on("doxygen", when="+docs", type="build")

    def cmake_args(self):
        args = [
            self.define_from_variant("NEP_BUILD_DOCUMENTATION", "docs"),
            self.define_from_variant("NEP_BUILD_LZ4", "lz4"),
            self.define_from_variant("NEP_BUILD_BZIP2", "bzip2"),
            self.define_from_variant("NEP_ENABLE_FORTRAN", "fortran"),
            self.define_from_variant("NEP_ENABLE_FITS", "fits"),
            self.define_from_variant("NEP_ENABLE_GEOTIFF", "geotiff"),
            self.define_from_variant("NEP_ENABLE_GRIB2", "grib2"),
            self.define_from_variant("NEP_ENABLE_CDF", "cdf"),
            self.define_from_variant("NEP_ENABLE_PDS4", "pds4"),
            self.define_from_variant("NEP_ENABLE_PARALLEL_TESTS", "parallel"),
            self.define_from_variant("NEP_BUILD_EXAMPLES", "examples"),
            self.define_from_variant("NEP_ENABLE_BENCHMARKS", "benchmarks"),
        ]
        return args

    def check(self):
        """Run tests to verify build."""
        with working_dir(self.build_directory):
            make("test")

    @run_after("install")
    def check_install(self):
        """Verify that plugin libraries are installed."""
        plugin_dir = join_path(self.prefix.lib, "plugin")
        if "+lz4" in self.spec:
            assert os.path.exists(join_path(plugin_dir, "libh5lz4.so"))
        if "+geotiff" in self.spec:
            assert os.path.exists(join_path(self.prefix.lib, "libncgeotiff.so"))
        if "+grib2" in self.spec:
            assert os.path.exists(join_path(self.prefix.lib, "libncgrib2.so"))
        if "+cdf" in self.spec:
            assert os.path.exists(join_path(self.prefix.lib, "libnccdf.so"))
        if "+pds4" in self.spec:
            assert os.path.exists(join_path(self.prefix.lib, "libncpds4.so"))
        if "+fits" in self.spec:
            assert os.path.exists(join_path(self.prefix.lib, "libncfits.so"))
