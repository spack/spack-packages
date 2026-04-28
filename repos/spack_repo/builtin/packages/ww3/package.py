from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Ww3(CMakePackage):
    """WAVEWATCH III (WW3) is a community wave modeling framework that includes
    the latest scientific advancements in the field of wind-wave modeling and dynamics.

    Example installation:
        spack install ww3@develop switch=Ifremer1 %intel-oneapi-compilers@2025.3.2
    """

    homepage = "https://github.com/NOAA-EMC/WW3"
    url = "https://github.com/NOAA-EMC/WW3/archive/refs/tags/6.07.1.tar.gz"
    git = "https://github.com/NOAA-EMC/WW3.git"

    maintainers("rsoutelino")

    license("LGPL-3.0-only", checked_by="rsoutelino")

    # Development version - use with: spack install ww3@develop
    version("develop", branch="develop")

    # WW3 configuration variants
    variant(
        "switch",
        default="Ifremer1",
        values=(
            "Ifremer1",
            "Ifremer2",
            # "Ifremer2_pdlib",  # NOT SUPPORTED - requires libptscotchparmetis (WW3 CMake issue)
            "NCEP_glwu",  # NOT SUPPORTED - NCEPLIBS CMake target export issues
            "NCEP_gwm",
            "NCEP_rwps",  # NOT SUPPORTED - requires libptscotchparmetis (WW3 CMake issue)
            "NCEP_st2",
            "NCEP_st4",
            "NCEP_st4sbs",
            "NRL1",
            "NRL2",
            "NRL3",
            "NRL4",
            # OASIS switches - NOT SUPPORTED: OASIS3-MCT not available in Spack
            # "OASACM",
            # "OASICM",
            # "OASOCM",
            "SMCMlt",
            "UKMO",
            "UKMO_gbl",
            "UKMO_reg",
            "UKMO_uk",
            # "USACE_1",  # NOT SUPPORTED - requires libptscotchparmetis (WW3 CMake issue)
            # "USACE_2",  # NOT SUPPORTED - requires libptscotchparmetis (WW3 CMake issue)
            "UoM_nl1",
            "UoM_nl3",
            "UoM_nl3s",
            "multi_esmf",
            # "ite_pdlib",  # NOT SUPPORTED - requires libptscotchparmetis (WW3 CMake issue)
            # "ugdev2",  # NOT SUPPORTED - requires libptscotchparmetis (WW3 CMake issue)
        ),
        description="WW3 switch configuration to build",
    )

    depends_on("c", type="build")
    depends_on("fortran", type="build")
    depends_on("cmake@3.19:", type="build")

    # Core dependencies
    depends_on("mpi")

    # NetCDF - Optionally searched for to build NetCDF executables
    # Required when SCRIPNC, TRKNC, or OASIS in switch, but included by default
    depends_on("netcdf-c")
    depends_on("netcdf-fortran")
    depends_on("hdf5+fortran")

    # OASIS3-MCT - Required when OASIS in switch
    # NOTE: OASIS switches (OASACM, OASICM, OASOCM) are not supported because
    # OASIS3-MCT is not available as a Spack package. The 'mct' package only
    # provides the base Model Coupling Toolkit without OASIS coupler components.

    # METIS/ParMETIS/SCOTCH - Required when PDLIB in switch
    # NOTE: PDLIB+SCOTCH switches (ite_pdlib, ugdev2, USACE_1, USACE_2, Ifremer2_pdlib)
    # are not currently supported. WW3's FindSCOTCH.cmake expects libptscotchparmetis
    # which is not built by Spack's SCOTCH package. This should be reported to WW3
    # developers to make libptscotchparmetis optional in their CMake configuration.
    # For now, use PDLIB+METIS switches or non-PDLIB switches instead.
    # depends_on("metis", when="switch=Ifremer2_pdlib")
    # depends_on("parmetis", when="switch=Ifremer2_pdlib")
    # depends_on("metis", when="switch=ite_pdlib")
    # depends_on("parmetis", when="switch=ite_pdlib")
    # depends_on("scotch+mpi", when="switch=ite_pdlib")
    # depends_on("metis", when="switch=ugdev2")
    # depends_on("parmetis", when="switch=ugdev2")
    # depends_on("scotch+mpi", when="switch=ugdev2")

    # NCEPLIBS - Required when NCEP2 in switch
    # NOTE: NCEP switches are not currently supported due to CMake target export
    # issues in Spack's NCEPLIBS packages (g2, g2c, bacio, w3emc). The packages
    # export incorrect target names that don't match what WW3 expects. This should
    # be reported to WW3 developers and/or fixed in Spack's NCEPLIBS packages.
    # depends_on("g2c", when="switch=NCEP_glwu")
    # depends_on("g2", when="switch=NCEP_glwu")
    # depends_on("bacio", when="switch=NCEP_glwu")
    # depends_on("w3emc", when="switch=NCEP_glwu")

    # depends_on("scotch", when="switch=NCEP_rwps")

    # ESMF - Required when MULTI_ESMF in switch
    depends_on("esmf", when="switch=multi_esmf")

    def cmake_args(self):
        """Configure CMake arguments for WW3 build"""
        args = [
            # Enable NetCDF support
            self.define("NETCDF", True),
            # Set switch file based on variant
            self.define("SWITCH", self.spec.variants["switch"].value),
            # Use native endianness (or BIG if needed)
            self.define("ENDIAN", "NATIVE"),
        ]

        # Note: PDLIB+SCOTCH configuration removed as those switches are not supported
        # WW3's FindSCOTCH.cmake requires libptscotchparmetis which is not built by
        # Spack's SCOTCH package. This needs to be fixed in WW3's CMake configuration.

        return args
