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
    url = "https://github.com/loumalouomega/meshioplusplus/archive/refs/tags/v9.10.0.tar.gz"
    git = "https://github.com/loumalouomega/meshioplusplus.git"

    maintainers("loumalouomega")

    license("MIT", checked_by="loumalouomega")

    # Upstream's default branch moved from main to master at v7.0.0.
    version("master", branch="master")
    version("9.10.0", sha256="6006148e1afb57f6d9426209775c2c6b008d8e10bd3d80ff7c676af9a99fd5fa")
    version("9.4.1", sha256="dc57060303b90a18128e259c5266d48d4a80e68d535ac028467b3ac8d518d772")
    # v9.0.0: the installable C++ core (MESHIOPLUSPLUS_INSTALL_CPP) landed at
    # v8.9.0; this major bump marks it stabilizing as a real consumer surface.
    # Not a breaking change to any existing build path.
    version("9.0.0", sha256="8d7fdab4763a2174291e40c5da503bbb6d37b36591a54f7c0b1fa869eef54798")
    version("8.7.0", sha256="d8721aa4ed82ef2f7fe49062910826a7012f6823eb22d5290690c298eafe68ec")
    # v8.0.0: the WebAssembly build gained every core format; no change to the
    # native/CMake build this package drives.
    version("8.0.0", sha256="ba0434950e9e2ef165ff9d50043ee6bb3e4359e7bc72ba77108553b7aad4b83f")
    # v7.0.0: find_package(meshioplusplus) consumers now need version >=7.0
    # (the packaged CMake config version was bumped).
    version("7.0.0", sha256="797809b8c645d4712de9160ea375b0dc301b593844c475ca5bdbeb6490446c9a")
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
        "zstd",
        default=False,
        description="C++ VTK XML zstd compression codec",
        when="@7.3:",
    )
    variant("lz4", default=False, description="C++ VTK XML lz4 compression codec", when="@7.3:")
    variant(
        "kahip",
        default=False,
        description="KaHIP-backed mesh partitioning quality",
        when="@7.6:",
    )
    variant(
        "cli",
        default=False,
        description="Build the native meshioplusplus CLI binary",
        when="@7.0:",
    )
    variant(
        "parallel",
        default="auto",
        values=("auto", "seq", "stl", "openmp", "tbb", conditional("kokkos", when="@8.5:")),
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
    variant(
        "cxx_api",
        default=False,
        description="Build the installable, find_package()-able C++ core library",
        when="@8.9:",
    )
    variant(
        "cxx_api_backends",
        values=any_combination_of("meshio", "native", "kratos").with_default(
            "meshio,native,kratos"
        ),
        description="Mesh backends to install as separate C++ libraries",
        when="+cxx_api",
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
    depends_on("zstd", when="+zstd")
    depends_on("lz4", when="+lz4")
    depends_on("kahip", when="+kahip")
    # The TBB and (on libstdc++) the STL parallel backends need TBB.
    depends_on("tbb", when="parallel=tbb")
    depends_on("tbb", when="parallel=stl")
    # The shared libmeshioplusplus.so needs a PIC Kokkos; its default static
    # archives aren't position-independent and fail to link into it.
    depends_on("kokkos@3.4: +pic", when="parallel=kokkos")

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
            self.define_from_variant("MESHIOPLUSPLUS_WITH_ZSTD", "zstd"),
            self.define_from_variant("MESHIOPLUSPLUS_WITH_LZ4", "lz4"),
            self.define_from_variant("MESHIOPLUSPLUS_WITH_KAHIP", "kahip"),
            self.define_from_variant("MESHIOPLUSPLUS_BUILD_CLI", "cli"),
            # Eigen and Polyscope are vendored git submodules (an MED-transpose
            # optimization and the CLI's optional 3D viewer, respectively); the
            # release tarball omits both, so Eigen falls back to a plain loop
            # and Polyscope (attached only to the CLI target) stays off.
            self.define("MESHIOPLUSPLUS_WITH_EIGEN", False),
            self.define(
                "MESHIOPLUSPLUS_PARALLEL_BACKEND",
                spec.variants["parallel"].value.upper(),
            ),
            self.define(
                "MESHIOPLUSPLUS_MESH_BACKEND",
                spec.variants["mesh_backend"].value.upper(),
            ),
            self.define_from_variant("MESHIOPLUSPLUS_INSTALL_CPP", "cxx_api"),
        ]
        if spec.satisfies("+cxx_api"):
            backends = ";".join(sorted(v.upper() for v in spec.variants["cxx_api_backends"].value))
            args.append(self.define("MESHIOPLUSPLUS_INSTALL_CPP_BACKENDS", backends))
        return args
