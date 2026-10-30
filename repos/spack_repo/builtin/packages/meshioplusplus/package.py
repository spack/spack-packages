# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import (
    any_combination_of,
    conditional,
    conflicts,
    depends_on,
    license,
    maintainers,
    variant,
    version,
)


class Meshioplusplus(CMakePackage):
    """meshio++: a C++20 mesh I/O core with an installable C API
    (``libmeshioplusplus``, a pure-C99 header with pkg-config and
    ``find_package`` support) and an optional modern OO Fortran 2008 interface
    for HPC codes. Reads and writes ~80 unstructured mesh formats.

    The C++ libraries' ``SOVERSION`` tracks ``MESHIOPLUSPLUS_ABI_VERSION``,
    which moves only when an installed C++ header changes in a way that breaks
    an already-compiled consumer; the C and Fortran libraries stay at
    ``SOVERSION 0``, so a C consumer never has to re-pin across the major
    versions below. See the version list for which ones move it.

    This package builds the standalone C / C++ / Fortran library. For the
    Python bindings (the pybind11 ``_core`` extension) use ``py-meshioplusplus``.
    """

    homepage = "https://github.com/loumalouomega/meshioplusplus"
    url = "https://github.com/loumalouomega/meshioplusplus/archive/refs/tags/v17.13.0.tar.gz"
    git = "https://github.com/loumalouomega/meshioplusplus.git"

    maintainers("loumalouomega")

    license("MIT", checked_by="loumalouomega")

    # Upstream's default branch moved from main to master at v7.0.0.
    version("master", branch="master")
    # From v9.0.0 on, the C++ libraries' SOVERSION tracks
    # MESHIOPLUSPLUS_ABI_VERSION -- the counter upstream parses out of
    # src/cpp/include/meshioplusplus/abi_version.hpp. It moves only for a
    # layout change to a type a consumer can name, or an edit to the *body* of
    # an existing inline function (both sides emit a vague-linkage copy, so the
    # linker keeps one arbitrarily); purely additive header changes do not move
    # it. The list below therefore carries one version per ABI generation
    # rather than all ~45 releases: anything absent is ABI-neutral against its
    # neighbours, so a consumer of a listed version needs no separate re-pin.
    #
    # Two gaps cannot be closed. ABI 8 and 9 (v10.11.0, v10.12.0) were never
    # tagged on GitHub, so ABI 7's v10.6.0 is followed by ABI 10's v10.14.0.
    # Other ABI-bump releases are untagged too, so what is listed is the first
    # *tagged* release of each ABI -- which is why ABI 6 opens at v9.22.0
    # rather than the v9.20.0 that introduced mPatchTypes.
    #
    # v17.13.0 is the latest release and the first tagged ABI 33; it keeps 33
    # (the new mesh_cad header is a pure addition). The ABI 33 break came in
    # v17.12.0, which was never tagged: FitCadOptions grew from 224 to 288
    # bytes and FitCadResult gained members (the C structs kept their sizes).
    version("17.13.0", sha256="4fa094ba3a2a0cf2d5579f5635377efe6f6b5f4437f884dc4e9a1a25d6f43a5a")
    # v17.11.0 is the first tagged ABI 32: FitCadOptions grew from 56 to 224
    # bytes and FitCadResult gained members; the C structs kept their sizes.
    version("17.11.0", sha256="24ec1cf7b31be1602dc56b4deffbba4e3856d80c55f08e2423c6fef3580daf83")
    # v17.10.0 shares ABI 31 with v17.9.0: the parametric primitives added one
    # new header (operations/primitives.hpp) and changed no existing
    # declaration, so no consumer re-pin is needed.
    version("17.10.0", sha256="102ac6dcfc6ea70665ca09f3d3e3df1876073fc7a72e00aae6cf9303d53f4815")
    # v17.9.0 is the first tagged ABI 31.
    version("17.9.0", sha256="7d10ca7946a817d5f85e8670ff96834533e3fb553df86464ecb0a178fa7697ff")
    # ABI 30 -> 31: SegmentOptions gained the primitive-growth method and
    # tolerance (96 -> 112 bytes); FitCadOptions gained merge_faces and backend
    # and FitCadResult gained backend. The C structs kept their sizes.
    # v17.3.0 shares ABI 30 with v17.2.0 (and v17.4.0 through v17.8.0, which
    # are ABI-neutral against it and so need no separate line).
    version("17.3.0", sha256="dbbc2766fb9908160ee809f56a0ee17017a96e503029607af4de1fa2d6ec3f84")
    # ABI 29 -> 30: FitCadResult gained the vertex-blend, chamfer, conic-blend and
    # tapered/variable-pitch thread counts (the C API reports them through the new
    # mio_fit_cad_report_ex).
    version("17.2.0", sha256="d945dc797680f0f05ddfc3128582af883f105262e6a5a6dde1fd0b0688e221a9")
    # ABI 29: FitCadResult gained the variable-fillet, blend and rounded-thread
    # counts in the untagged v16.44.0; v17.0.0 is a version-only major bump, so it
    # is the first tagged ABI 29.
    version("17.0.0", sha256="ec7ce56639acbb857fed589d5b21a43d2c393265a0dda4d0f2124f7f5f224ca1")
    # ABI 26 -> 28: FitCadOptions and FitCadResult grew (ABI 27 was never tagged).
    version("16.42.0", sha256="0251a2a48369b43a9ae6dd1cf6d28ac4fa9e347e766a94549353e2d407ecc40d")
    # ABI 25 -> 26: CellType gained the Bezier types after Triangle7, so Custom
    # moves from 77 to 84 (and MIO_CELL_Custom with it in the C API).
    version("16.40.0", sha256="a63c81e1ab72cecbdc575676d4fa417700e87e6fdf9af32df19f42a82da6d501")
    # ABI 24 -> 25: RenderOptions grew (ABI 24 was never tagged).
    version("16.39.0", sha256="4399d7061c4485028aa1411f8b86718640dd35cadec2d44ed38354987365a937")
    # First tagged ABI 23 release (additive terminal-rendering header).
    version("16.32.0", sha256="dd362a45e6d830f9a7c364378081f660e0e7168afad62e29cd55b1ea6989d2c0")
    # Reader robustness and benchmark/fuzz infrastructure; ABI 22 unchanged.
    version("16.30.0", sha256="e1a877140e2d5ade9398821af275fe80201e6c1913e21a0582a4d124abdbb9c7")
    # First tagged ABI 22 release (MDPA/Gmsh side-channel layout changes).
    version("16.29.0", sha256="8dfa3564f5140adad895166ed7cb3e52e4654bf17dd4d88a24fce0c3abcba849")
    # Tagged representatives of ABI 20 and 19; ABI 21 was never tagged.
    version("16.27.0", sha256="7f0804742a172d91261307dc309b3977e2164d669cd3eb28034930efa3997b91")
    version("16.25.0", sha256="a3c494814285f9b0a18d6f5568f8ee1810b66da3aad67ced0a11ef9221ca5288")
    # ABI 18 at v16.21.0 is additive only (write_vtu_appended and the appended
    # WriteEncoding::RawAppended enumerator).
    version("16.21.0", sha256="86bb461db6e01500aeaced5e8aee43a23d08c54eafc3e3b23c3fa6305b76907d")
    # ABI 17 -> 18: the MESHIO backend's CellBlock stores polygon and polyhedron
    # blocks as CSR rather than row vectors, and the surface/edge lookup
    # helpers behind it became sorted tables instead of hash maps. Code
    # reading cells through the uniform CellView API is unaffected.
    version("16.16.0", sha256="3b58a8528ba6c10f612c870629ef7e5ede1ab5894235302f569b5270e8bb68bf")
    # ABI 16 -> 17: three inline bodies in NDArray changed -- the zeroing
    # constructor and MakeOwned() skip the null-pointer memset/memcpy of an
    # empty buffer, and the allocating constructors refuse an overflowing
    # shape. sizeof(NDArray) is unchanged.
    version("16.14.0", sha256="14fd42e97694be41cf01ed3c4bd3ab2a12d59e71e98f74ef12dd026429542963")
    # ABI 15 -> 16: CellType gained Triangle7 *before* Custom, so Custom moves
    # from 76 to 77. An appended enumerator is normally additive, but not when
    # something follows it -- this one is Tier A, and MIO_CELL_Custom moves
    # with it in the C API.
    version("16.1.0", sha256="54287229e2cfbcd3233e41921f0f43e517a157ddad2371b2300956d6902bf0b6")
    # ABI 14 -> 15: ReadOptions gained mGhosts (GhostPolicy), the keep-or-drop
    # switch for a partitioned file's ghost cells. It fits in the tail padding
    # after mPieceSet, so sizeof(ReadOptions) stays 72 and the four aggregates
    # embedding it are unchanged -- but a consumer compiled against v14 headers
    # leaves that byte indeterminate, so it is a break all the same.
    version("15.1.0", sha256="d6bd51cacb91b0150ccf2f8c40796533f998bc72a79ff55c5cdac96895303134")
    # ABI 13 -> 14: ReadOptions gained mPiece/mPieceSet (56 -> 72 bytes), the
    # merge-or-select-pieces switch for partitioned files.
    version("14.0.0", sha256="2124d51a7f201dcae6bbedeeb08571e6e3417d9545d374d035ace94a85e66186")
    # ABI 12 -> 13: OpenFoamInfo gained mRegion, the multi-region case selector
    # (96 -> 128 bytes).
    version("12.0.0", sha256="aefd1acc879ee4d122169250bfd3ba637c50343478a148e0ef4e7d25da0d8be7")
    # ABI 11 -> 12: NDArray::Size()'s inline body reported 0 for a rank-0 array,
    # so Nbytes() was 0 and every clone dropped a 0-d scalar's one element.
    version("11.0.0", sha256="eb288606f336eba262ac562fd157d2022dc2b97961a08f19632bf49712dba1f7")
    # ABI 10 -> 11: MeshMetadata gained mProvenance/mProvenanceRecognised
    # (256 -> 288 bytes) for provenance read-back.
    version("10.17.0", sha256="93e726b896fc076c146b3ef1c79358b91c90e2a1650fe31133ed1d474c37a3d5")
    # ABI 9 -> 10: SmoothMethod gained an explicit : std::uint8_t underlying
    # type (previously the scoped-enum default int) plus Odt. ABI 8 and 9
    # (v10.11.0, v10.12.0) were never tagged, hence the jump from v10.6.0.
    version("10.14.0", sha256="d5e1ed0621f636c7e229529106b8574b24c1525d21e7cedeaabe74b46ffa09c8")
    # ABI 6 -> 7: RefineOptions gained mRecordHierarchy.
    version("10.6.0", sha256="44e53e14f7bb45350595b871429f35f3baac1e6c0a37f8287a7829eabda26fc0")
    # v10.0.0: the major bump closing ABI 6 on the 10.x line. No header change
    # of its own -- OpenFoamInfo gained mPatchTypes back in v9.20.0.
    version("10.0.0", sha256="7da63717e57f4a1cf836d206aa3e0f09d1851595a54ab30bdbef963a66fa6b4a")
    # ABI 5 -> 6: OpenFoamInfo gained mPatchTypes. v9.20.0, which introduced
    # it, was never tagged, so v9.22.0 is the first tagged ABI 6.
    version("9.22.0", sha256="00c0953bb237ee3308bb2903c579e34d595ffa6b4b020d058c26dbcc5bddd64b")
    version("9.10.0", sha256="6006148e1afb57f6d9426209775c2c6b008d8e10bd3d80ff7c676af9a99fd5fa")
    version("9.4.1", sha256="dc57060303b90a18128e259c5266d48d4a80e68d535ac028467b3ac8d518d772")
    # ABI 2 -> 3: KratosMesh, PropertySet and NativeMesh gained data members.
    version("9.2.0", sha256="f42ef3cb835ee563942661ce93a52f8616f135993ccaef31fb2a196a66bd7295")
    # ABI 1 -> 2: GeometricalEntity, ModelPart and MdpaInfo gained data members.
    version("9.1.0", sha256="c42c8d18dc53d7a63b2b400a3866843229b9b1afca96f64b389d5b874a6ba05d")
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
    variant("zstd", default=False, description="C++ VTK XML zstd compression codec", when="@7.3:")
    variant("lz4", default=False, description="C++ VTK XML lz4 compression codec", when="@7.3:")
    variant("lzma", default=False, description="C++ VTK XML lzma compression codec", when="@17.3:")
    variant(
        "bzip2",
        default=False,
        description="C++ native bzip2 path (libMesh .xda.bz2/.xdr.bz2 meshes)",
        when="@16.12:",
    )
    variant(
        "occt",
        default=False,
        description="OpenCASCADE-backed fit_cad operation and STEP/IGES reading",
        when="@16.41:",
    )
    variant(
        "kahip", default=False, description="KaHIP-backed mesh partitioning quality", when="@7.6:"
    )
    variant(
        "cgnslib",
        default=False,
        description="Official CGNS Mid-Level Library for CGNS (ADF containers, NGON_n/NFACE_n)",
        when="@9.22:",
    )
    variant(
        "adios2",
        default=False,
        description="ADIOS2-backed DOLFINx VTX (.bp) reader",
        when="@16.13:",
    )
    variant(
        "cli",
        default=False,
        description="Build the native meshioplusplus CLI binary",
        when="@7.0:",
    )
    variant(
        "tecio",
        default=False,
        description="TecIO-backed .szplt reader (manual library download)",
        when="@16.13:",
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
    # CMake's own FindLibLZMA module (LibLZMA::LibLZMA).
    depends_on("xz", when="+lzma")
    # CMake's own FindBZip2 module (BZip2::BZip2).
    depends_on("bzip2", when="+bzip2")
    depends_on("kahip", when="+kahip")
    # Upstream hard-errors at configure time on
    # MESHIOPLUSPLUS_WITH_CGNSLIB without MESHIOPLUSPLUS_WITH_HDF5 -- the
    # cgnslib backend augments the hand-rolled HDF5 CGNS reader (it buys ADF
    # containers and NGON_n/NFACE_n sections), it does not replace it. The
    # +cgnslib~hdf5 conflict below enforces this before configure.
    # cgns~mpi keeps the closure serial: cgns defaults to
    # +mpi, which would drag hdf5+mpi and an MPI into an otherwise serial
    # build. Its +hdf5 and +shared defaults are what we want, since upstream
    # links CGNS::cgns_shared.
    depends_on("hdf5", when="+cgnslib")
    depends_on("cgns~mpi", when="+cgnslib")
    # ADIOS2 ships its own CMake config; upstream requests no language
    # component (the CXX component and target were renamed in 2.9) and opens
    # files with a serial adios2::ADIOS, so ~mpi is the matching choice.
    depends_on("adios2~mpi", when="+adios2")
    depends_on("tecio~mpi", when="+tecio")
    # Upstream's floor is 7.6; it is found through OCCT's own CMake config and
    # linked dynamically.
    depends_on("opencascade@7.6:", when="+occt")
    # The TBB and (on libstdc++) the STL parallel backends need TBB.
    depends_on("tbb", when="parallel=tbb")
    depends_on("tbb", when="parallel=stl")
    # The shared libmeshioplusplus.so needs a PIC Kokkos; its default static
    # archives aren't position-independent and fail to link into it.
    depends_on("kokkos@3.4: +pic", when="parallel=kokkos")

    # meshio++ requires a C++20 toolchain.
    conflicts("%gcc@:9", msg="meshio++ needs GCC >= 10 for C++20")
    conflicts("+cgnslib", when="~hdf5", msg="The CGNS library backend requires +hdf5")

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
            self.define_from_variant("MESHIOPLUSPLUS_WITH_LZMA", "lzma"),
            self.define_from_variant("MESHIOPLUSPLUS_WITH_BZIP2", "bzip2"),
            self.define_from_variant("MESHIOPLUSPLUS_WITH_OCCT", "occt"),
            self.define_from_variant("MESHIOPLUSPLUS_WITH_KAHIP", "kahip"),
            self.define_from_variant("MESHIOPLUSPLUS_WITH_CGNSLIB", "cgnslib"),
            self.define_from_variant("MESHIOPLUSPLUS_WITH_ADIOS2", "adios2"),
            self.define_from_variant("MESHIOPLUSPLUS_WITH_TECIO", "tecio"),
            self.define_from_variant("MESHIOPLUSPLUS_BUILD_CLI", "cli"),
            # Eigen and Polyscope are vendored git submodules (an MED-transpose
            # optimization and the CLI's optional 3D viewer, respectively); the
            # release tarball omits both, so Eigen falls back to a plain loop
            # and Polyscope (attached only to the CLI target) stays off.
            self.define("MESHIOPLUSPLUS_WITH_EIGEN", False),
            self.define(
                "MESHIOPLUSPLUS_PARALLEL_BACKEND", spec.variants["parallel"].value.upper()
            ),
            self.define(
                "MESHIOPLUSPLUS_MESH_BACKEND", spec.variants["mesh_backend"].value.upper()
            ),
            self.define_from_variant("MESHIOPLUSPLUS_INSTALL_CPP", "cxx_api"),
        ]
        if spec.satisfies("+cxx_api"):
            backends = ";".join(sorted(v.upper() for v in spec.variants["cxx_api_backends"].value))
            args.append(self.define("MESHIOPLUSPLUS_INSTALL_CPP_BACKENDS", backends))
        if spec.satisfies("+tecio"):
            args.append(self.define("TECIO_ROOT", spec["tecio"].prefix))
        return args
