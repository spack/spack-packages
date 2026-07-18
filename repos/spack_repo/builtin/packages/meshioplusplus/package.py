# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Meshioplusplus(CMakePackage):
    """meshio++: a C++20 mesh I/O core with an installable C API
    (``libmeshioplusplus``, a pure-C99 header with pkg-config and
    ``find_package`` support) and an optional modern OO Fortran 2008 interface
    for HPC codes. Reads and writes ~40 unstructured mesh formats.

    This package builds the standalone C / C++ / Fortran library. For the
    Python bindings (the pybind11 ``_core`` extension) use ``py-meshioplusplus``.
    """

    homepage = "https://github.com/loumalouomega/meshioplusplus"
    url = "https://github.com/loumalouomega/meshioplusplus/archive/refs/tags/v6.6.1.tar.gz"
    git = "https://github.com/loumalouomega/meshioplusplus.git"

    maintainers("loumalouomega")

    license("MIT", checked_by="loumalouomega")

    version("main", branch="main")
    version("6.6.1", sha256="327c1b146fefa3eb19404e2b422b5cf789fe81b8f402fea9694124d50b13e88b")
    version("6.6.0", sha256="a585a7b932a9a893b17710f68ed64a04b492d12abfe74c5744812fb44599cbae")
    version("6.5.0", sha256="f0ebdb7a547097ae338b2295eaa2cb08fe728a7d32c408f4109511ded3196779")
    version("6.4.0", sha256="d969bb081ac5bb9b43ce0fa32d3c6a5a8fc53a9f4ad086b03d7ebb40368a01fb")
    version("6.3.0", sha256="ead9fd2264ba809903c91347b7cbd1e526ac78373b2935590c967cad20aacf59")
    # The installable C API and Fortran interface were introduced in 6.2.0.
    # Earlier C++ releases only ship the Python extension, so with Python off a
    # CMake build of them installs nothing -- see py-meshioplusplus for those.
    version("6.2.0", sha256="275c1a938845a416040b1517fb8f9c1c008e86ad888b432d0852eba0fac83126")

    variant(
        "fortran",
        default=False,
        description="Build the OO Fortran 2008 interface (implies the C API)",
    )
    variant(
        "hdf5", default=True, description="C++ HDF5-backed formats (CGNS, HMF, H5M, MED, XDMF-HDF)"
    )
    variant("netcdf", default=True, description="C++ netCDF-backed format (Exodus)")
    variant("zlib", default=True, description="C++ VTU zlib compression path")
    variant(
        "parallel",
        default="auto",
        values=("auto", "seq", "stl", "openmp", "tbb"),
        multi=False,
        description="Parallel backend for meshioplusplus::parallel_for",
    )
    variant(
        "mesh_backend",
        default="native",
        values=("meshio", "native", "kratos"),
        multi=False,
        description="In-memory mesh backend for the standalone C++ build",
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build", when="+fortran")
    depends_on("cmake@3.15:", type="build")

    depends_on("hdf5", when="+hdf5")
    # A parallel HDF5 needs mpi.h even for serial use of the C API.
    depends_on("mpi", when="+hdf5 ^hdf5+mpi")
    depends_on("netcdf-c", when="+netcdf")
    depends_on("zlib-api", when="+zlib")
    # The TBB and (on libstdc++) the STL parallel backends need TBB.
    depends_on("tbb", when="parallel=tbb")
    depends_on("tbb", when="parallel=stl")

    # meshio++ requires a C++20 toolchain.
    conflicts("%gcc@:9", msg="meshio++ needs GCC >= 10 for C++20")

    def cmake_args(self):
        spec = self.spec
        args = [
            # Python is packaged separately as py-meshioplusplus; here the C API
            # is the installable artifact, so keep it on unconditionally.
            self.define("MESHIOPLUSPLUS_BUILD_PYTHON", False),
            self.define("MESHIOPLUSPLUS_BUILD_C_API", True),
            self.define_from_variant("MESHIOPLUSPLUS_BUILD_FORTRAN", "fortran"),
            self.define_from_variant("MESHIOPLUSPLUS_WITH_HDF5", "hdf5"),
            self.define_from_variant("MESHIOPLUSPLUS_WITH_NETCDF", "netcdf"),
            self.define_from_variant("MESHIOPLUSPLUS_WITH_ZLIB", "zlib"),
            # Eigen is a vendored git submodule (a MED-transpose optimization
            # only); the release tarball omits it, so use the plain-loop fallback.
            self.define("MESHIOPLUSPLUS_WITH_EIGEN", False),
            self.define(
                "MESHIOPLUSPLUS_PARALLEL_BACKEND",
                spec.variants["parallel"].value.upper(),
            ),
            self.define(
                "MESHIOPLUSPLUS_MESH_BACKEND",
                spec.variants["mesh_backend"].value.upper(),
            ),
        ]
        return args
