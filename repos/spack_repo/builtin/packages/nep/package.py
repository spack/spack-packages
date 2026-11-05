# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Nep(CMakePackage):
    """NEP (NetCDF Expansion Pack) provides format readers and the
    NEXTCDF-4 backend through the NetCDF User Defined Format API.
    Compression filters are provided separately by nep-compress."""

    homepage = "https://github.com/Intelligent-Data-Design-Inc/NEP"
    url = "https://github.com/Intelligent-Data-Design-Inc/NEP/archive/refs/tags/v4.2.0.tar.gz"
    git = "https://github.com/Intelligent-Data-Design-Inc/NEP.git"

    maintainers("edhartnett")

    license("Apache-2.0")

    version("main", branch="main")
    version("4.2.0", sha256="18656ce4f7095f3e52234645224144d2558ff001a7444fcc9b6ed7b7e718eccd")

    variant("docs", default=True, description="Build documentation with Doxygen")
    variant("fortran", default=True, description="Build Fortran format reader tests")
    variant("fits", default=False, description="Enable FITS reader support via CFITSIO")
    variant("geotiff", default=False, description="Enable GeoTIFF reader support via libgeotiff")
    variant("grib2", default=False, description="Enable GRIB2 reader support via NCEPLIBS-g2c")
    variant("pds4", default=False, description="Enable PDS4 reader support via libxml2")
    # cdf: the NASA CDF reader needs the cdf package, which is not yet in
    # spack-packages (https://github.com/spack/spack-packages/pull/2797).
    # Enable once it merges:
    # variant("cdf", default=False, description="Enable NASA CDF reader support")
    # depends_on("cdf", when="+cdf")
    # dicom: omitted because NEP's DICOM reader requires GDCM's lossless
    # JPEG libraries, which Spack does not package.
    variant(
        "pdb",
        default=True,
        description="Enable legacy PDB reader support (no external library required)",
    )
    variant(
        "mmcif",
        default=False,
        description="Enable PDBx/mmCIF reader support (no external library required)",
    )
    variant("nextcdf4", default=False, description="Enable the NEXTCDF-4 UDF backend")
    variant(
        "parallel",
        default=False,
        description="Enable parallel I/O tests (requires MPI-enabled HDF5 and netcdf-c)",
    )
    variant("examples", default=False, description="Build example programs")
    variant("benchmarks", default=False, description="Build performance benchmark programs")

    depends_on("c", type="build")
    depends_on("fortran", when="+fortran", type="build")
    depends_on("pkgconfig", type="build")

    depends_on("netcdf-c@4.10.1:", type=("build", "link"))
    depends_on("netcdf-c +mpi", when="+parallel", type=("build", "link"))
    depends_on("hdf5@1.14:+hl~mpi", when="~parallel", type=("build", "link"))
    depends_on("hdf5@1.14:+hl+mpi", when="+parallel", type=("build", "link"))
    # NEXTCDF-4 uses the HDF5 2.1 small floating-point and complex types.
    depends_on("hdf5@2.1.1:", when="+nextcdf4", type=("build", "link"))
    depends_on("netcdf-fortran", when="+fortran", type=("build", "link"))
    depends_on("cfitsio", when="+fits", type=("build", "link"))
    depends_on("libgeotiff", when="+geotiff", type=("build", "link"))
    depends_on("g2c", when="+grib2", type=("build", "link"))
    depends_on("libxml2", when="+pds4", type=("build", "link"))
    depends_on("mpi", when="+parallel", type=("build", "link", "run"))
    depends_on("libtiff", when="+geotiff", type=("build", "link"))
    depends_on("doxygen", when="+docs", type="build")

    conflicts(
        "+geotiff",
        when="@4.2.0",
        msg="NEP 4.2.0 requires libgeotiff headers under include/geotiff/, "
        "which Spack does not provide",
    )

    def cmake_args(self):
        args = [
            self.define("CMAKE_INSTALL_LIBDIR", "lib"),
            # HDF5 2.x CMake config files only accept requests for major
            # version 2, and NEP asks for 1.14, so use the spec's HDF5
            # compiler wrapper instead of any HDF5 config file CMake finds.
            self.define("HDF5_NO_FIND_PACKAGE_CONFIG_FILE", True),
            self.define("HDF5_C_COMPILER_EXECUTABLE", self._hdf5_wrapper()),
            self.define_from_variant("NEP_BUILD_DOCUMENTATION", "docs"),
            self.define_from_variant("NEP_ENABLE_FORTRAN", "fortran"),
            self.define_from_variant("NEP_ENABLE_FITS", "fits"),
            self.define_from_variant("NEP_ENABLE_GEOTIFF", "geotiff"),
            self.define_from_variant("NEP_ENABLE_GRIB2", "grib2"),
            self.define_from_variant("NEP_ENABLE_PDS4", "pds4"),
            self.define_from_variant("NEP_ENABLE_PDB", "pdb"),
            self.define_from_variant("NEP_ENABLE_MMCIF", "mmcif"),
            self.define_from_variant("NEP_ENABLE_NEXTCDF4", "nextcdf4"),
            self.define("NEP_ENABLE_DICOM", False),
            self.define("NEP_ENABLE_CDF", False),
            self.define_from_variant("NEP_ENABLE_PARALLEL_TESTS", "parallel"),
            self.define_from_variant("NEP_BUILD_EXAMPLES", "examples"),
            self.define_from_variant("NEP_ENABLE_BENCHMARKS", "benchmarks"),
        ]
        return args

    def _hdf5_wrapper(self):
        name = "h5pcc" if self.spec.satisfies("^hdf5+mpi") else "h5cc"
        return join_path(self.spec["hdf5"].prefix.bin, name)

    @run_after("install")
    def check_install(self):
        """Verify that enabled format libraries are installed."""
        assert os.path.exists(join_path(self.prefix.lib, "libnep.so"))
        reader_libs = {
            "geotiff": "libncgeotiff.so",
            "grib2": "libncgrib2.so",
            "pds4": "libncpds4.so",
            "fits": "libncfits.so",
            "pdb": "libncpdb.so",
            "mmcif": "libncmmcif.so",
            "nextcdf4": "libncnextcdf4.so",
        }
        any_reader = False
        for variant_name, lib_name in reader_libs.items():
            if self.spec.satisfies(f"+{variant_name}"):
                any_reader = True
                assert os.path.exists(join_path(self.prefix.lib, lib_name))
        if any_reader:
            assert os.path.exists(join_path(self.prefix.share, ".ncrc"))
