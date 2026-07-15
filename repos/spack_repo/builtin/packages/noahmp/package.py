from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Noahmp(CMakePackage):
    """Noah-MP is a state-of-the-art community land surface model used in
    weather and climate models including WRF, MPAS, WRF-Hydro/NWM, NOAA/UFS,
    NASA/LIS, and ERF.

    Noah-MP ships source plus per-host driver/interface code rather than a
    standalone library; only the ERF driver provides an installable CMake
    build, so this package builds the Noah-MP library through its ERF coupling
    interface. Other hosts (WRF, LIS, HRLDAS) compile Noah-MP into their own
    build and do not consume this package."""

    homepage = "https://github.com/NCAR/noahmp"
    git = "https://github.com/NCAR/noahmp.git"
    url = "https://github.com/NCAR/noahmp/archive/refs/tags/v5.2.1.tar.gz"

    maintainers("larenspear")

    # Noah-MP ships under a custom UCAR license (see LICENSE.txt); there is no
    # matching SPDX identifier, so no license() directive is set.

    version("5.2.1", sha256="4c9d4c6ebb2ccf707317933d704fe6f6d764f56a72aff1a7b35164e4ec80b4ed")
    version("5.2.0", sha256="3930250a4459859fbeb5583939fa680d84567764b4272fdb65dcb2f8836439fb")
    version("5.1.1", sha256="d3a2a2429b3edb32366e2810e7bc401cc925e6112708407023eef970deaa6bd6")
    version("5.1.0", sha256="45e1dd87eeffb56125a397fe82106185d989104ea9c1172d907b318c4aca7493")

    # Noah-MP has no top-level build system: it is meant to be compiled inside a
    # host model. The drivers/erf tree is the only one that provides a
    # standalone, installable CMake project (added with install/export rules in
    # v5.1.0), so it is used as the build root here. The resulting library
    # bundles the shared physics (src/, utility/) with the ERF coupling layer.
    # Earlier releases (5.0.0 and the 3.x series) lack drivers/erf entirely and
    # cannot be built this way.
    root_cmakelists_dir = "drivers/erf"

    variant("shared", default=True, description="Build a shared library")

    with default_args(type="build"):
        depends_on("cmake@3.17:")
        depends_on("c")
        depends_on("cxx")
        depends_on("fortran")

    with default_args(type=("build", "link")):
        depends_on("mpi")
        depends_on("netcdf-c")
        depends_on("netcdf-fortran")

    def cmake_args(self):
        netcdf_fortran = self.spec["netcdf-fortran"]
        return [
            # The project's CMakeLists prepends NETCDF_DIR to CMAKE_PREFIX_PATH;
            # point it at netcdf-c so the base C interface (netcdf.h / libnetcdf)
            # is found.
            self.define("NETCDF_DIR", self.spec["netcdf-c"].prefix),
            # The bundled cmake-modules/FindNetCDF.cmake assumes the C and
            # Fortran NetCDF libraries share one prefix: it searches for the F90
            # interface (netcdf.mod / libnetcdff) only under the C library's
            # directory with NO_DEFAULT_PATH. Spack keeps netcdf-c and
            # netcdf-fortran in separate prefixes, so pre-seed the F90 result
            # variables to bypass that search. The compiler still gets the right
            # -I/-l flags from Spack's compiler wrapper.
            self.define("NETCDF_INCLUDES_F90", netcdf_fortran.prefix.include),
            self.define("NETCDF_LIBRARIES_F90", netcdf_fortran.libs[0]),
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
        ]

    @run_after("install")
    def make_consumable(self):
        """Make the install usable by downstream packages.

        Upstream CMake installs only the library and the exported targets file;
        ``INCLUDES DESTINATION include`` copies nothing, leaving ``include``
        empty. Downstream consumers need the compiler-generated Fortran ``.mod``
        files (to ``use`` Noah-MP modules) and the C/C++ I/O headers (used by
        C++ hosts such as ERF), and a CMake config file so ``find_package`` can
        resolve the ``NoahMP::noahmp`` target.
        """
        mkdirp(self.prefix.include)

        # Fortran module interfaces, emitted into the build tree by the compiler.
        for mod in find(self.build_directory, "*.mod", recursive=True):
            install(mod, self.prefix.include)

        # C/C++ headers for the Noah-MP I/O layer.
        driver = join_path(self.stage.source_path, self.root_cmakelists_dir)
        for hdr in find(driver, ["*.H", "*.h", "*.hpp"], recursive=False):
            install(hdr, self.prefix.include)

        # Runtime parameter table and SNICAR optics data tables.
        mkdirp(self.prefix.share.noahmp)
        for data in find(driver, ["*.TBL", "*.nc"], recursive=False):
            install(data, self.prefix.share.noahmp)

        # Upstream installs NoahMPTargets.cmake but no package config file, so
        # find_package(NoahMP) in CONFIG mode would fail. Provide a minimal one.
        cmake_dir = join_path(self.prefix.lib, "cmake", "noahmp")
        mkdirp(cmake_dir)
        with open(join_path(cmake_dir, "NoahMPConfig.cmake"), "w") as f:
            f.write(
                "include(CMakeFindDependencyMacro)\n"
                "find_dependency(MPI COMPONENTS Fortran)\n"
                'include("${CMAKE_CURRENT_LIST_DIR}/NoahMPTargets.cmake")\n'
            )
