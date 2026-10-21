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
    version("6.07.1-390-g3e591453", commit="3e591453c9d95bb837f87b578e10f79f9c5f0952")
    version("7.14.cfcd089", commit="cfcd089f1647d378f20665783bbef70519e78bfa")

    
    depends_on("c", type="build")
    depends_on("fortran", type="build")
    depends_on("cmake@3.19:", type="build")
    depends_on("mpi")
    # NetCDF - Optionally searched for to build NetCDF executables
    # Required when SCRIPNC, TRKNC, or OASIS in switch, but included by default
    depends_on("netcdf-c")
    depends_on("netcdf-fortran")
    depends_on("hdf5+fortran")
    # ESMF - Required when MULTI_ESMF in switch
    depends_on("esmf", when="switch=multi_esmf")

    # WW3 configuration variants
    variant(
        "switch",
        default="Ifremer1",
        values=(
            "Ifremer1",
            "Ifremer2",
            "NCEP_gwm",
            "NCEP_st2",
            "NCEP_st4",
            "NCEP_st4sbs",
            "NRL1",
            "NRL2",
            "NRL3",
            "NRL4",
            "SMCMlt",
            "UKMO",
            "UKMO_gbl",
            "UKMO_reg",
            "UKMO_uk",
            "UoM_nl1",
            "UoM_nl3",
            "UoM_nl3s",
            "multi_esmf",
        ),
        description="WW3 switch configuration to build",
    )


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
