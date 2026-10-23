# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import conflicts, depends_on, license, maintainers, variant, version


class PyMeshioplusplus(PythonPackage):
    """meshio++: I/O for many mesh formats. A C++20 core (pybind11) with a
    pure-Python fallback for every format, so behavior and file compatibility
    are identical whether or not the native libraries are present."""

    homepage = "https://github.com/loumalouomega/meshioplusplus"
    # 6.0.0 has no PyPI sdist, so build every version from the GitHub archive
    # (scikit-build-core builds fine from the source tree) for a uniform source.
    url = "https://github.com/loumalouomega/meshioplusplus/archive/refs/tags/v17.13.0.tar.gz"
    git = "https://github.com/loumalouomega/meshioplusplus.git"

    maintainers("loumalouomega")

    license("MIT", checked_by="loumalouomega")

    # Upstream's default branch moved from main to master at v7.0.0.
    version("master", branch="master")
    # One version per C++ ABI generation, matching meshioplusplus: upstream's
    # MESHIOPLUSPLUS_ABI_VERSION only moves for a layout change or an inline
    # body edit in an installed C++ header, and this package builds the same
    # headers as the pybind11 _core extension's link target, so a version not
    # listed here is binary-compatible with its neighbours. ABI 8 and 9
    # (v10.11.0, v10.12.0) were never tagged, hence the v10.6.0 -> v10.14.0
    # jump. The C API is not involved here at all -- pyproject.toml's Python
    # floor, numpy/rich requirements and pybind11 build requirement are
    # unchanged across this whole range; only scikit-build-core's floor moved
    # to 0.11 at v17.11.0, which the dependency block below follows.
    # v17.13.0 is the latest release and the first tagged ABI 33; it keeps 33
    # (the new mesh_cad header is a pure addition). The ABI 33 break came in
    # v17.12.0, which was never tagged (FitCadOptions grew from 224 to 288
    # bytes and FitCadResult gained members; the C structs kept their sizes).
    # v17.11.0 is the first tagged ABI 32 (FitCadOptions grew from 56 to 224
    # bytes). v17.10.0 shares ABI 31 with v17.9.0 (the parametric primitives
    # added a new header only, so the layouts are unchanged). v17.9.0 is the
    # first tagged ABI 31 (SegmentOptions grew; the C structs kept their
    # sizes). v17.4.0 through v17.8.0 share ABI 30 with v17.3.0 and so need no
    # separate line.
    version("17.13.0", sha256="4fa094ba3a2a0cf2d5579f5635377efe6f6b5f4437f884dc4e9a1a25d6f43a5a")
    version("17.11.0", sha256="24ec1cf7b31be1602dc56b4deffbba4e3856d80c55f08e2423c6fef3580daf83")
    version("17.10.0", sha256="102ac6dcfc6ea70665ca09f3d3e3df1876073fc7a72e00aae6cf9303d53f4815")
    version("17.9.0", sha256="7d10ca7946a817d5f85e8670ff96834533e3fb553df86464ecb0a178fa7697ff")
    # Reader robustness and benchmark/fuzz infrastructure; ABI 22 unchanged.
    version("17.3.0", sha256="dbbc2766fb9908160ee809f56a0ee17017a96e503029607af4de1fa2d6ec3f84")
    version("17.2.0", sha256="d945dc797680f0f05ddfc3128582af883f105262e6a5a6dde1fd0b0688e221a9")
    version("17.0.0", sha256="ec7ce56639acbb857fed589d5b21a43d2c393265a0dda4d0f2124f7f5f224ca1")
    version("16.42.0", sha256="0251a2a48369b43a9ae6dd1cf6d28ac4fa9e347e766a94549353e2d407ecc40d")
    version("16.40.0", sha256="a63c81e1ab72cecbdc575676d4fa417700e87e6fdf9af32df19f42a82da6d501")
    version("16.39.0", sha256="4399d7061c4485028aa1411f8b86718640dd35cadec2d44ed38354987365a937")
    version("16.32.0", sha256="dd362a45e6d830f9a7c364378081f660e0e7168afad62e29cd55b1ea6989d2c0")
    version("16.30.0", sha256="e1a877140e2d5ade9398821af275fe80201e6c1913e21a0582a4d124abdbb9c7")
    # First tagged ABI 22 release (MDPA/Gmsh side-channel layout changes).
    version("16.29.0", sha256="8dfa3564f5140adad895166ed7cb3e52e4654bf17dd4d88a24fce0c3abcba849")
    # Tagged representatives of ABI 20 and 19; ABI 21 was never tagged.
    version("16.27.0", sha256="7f0804742a172d91261307dc309b3977e2164d669cd3eb28034930efa3997b91")
    version("16.25.0", sha256="a3c494814285f9b0a18d6f5568f8ee1810b66da3aad67ced0a11ef9221ca5288")
    version("16.21.0", sha256="86bb461db6e01500aeaced5e8aee43a23d08c54eafc3e3b23c3fa6305b76907d")
    version("16.16.0", sha256="3b58a8528ba6c10f612c870629ef7e5ede1ab5894235302f569b5270e8bb68bf")
    version("16.14.0", sha256="14fd42e97694be41cf01ed3c4bd3ab2a12d59e71e98f74ef12dd026429542963")
    version("16.1.0", sha256="54287229e2cfbcd3233e41921f0f43e517a157ddad2371b2300956d6902bf0b6")
    version("15.1.0", sha256="d6bd51cacb91b0150ccf2f8c40796533f998bc72a79ff55c5cdac96895303134")
    version("14.0.0", sha256="2124d51a7f201dcae6bbedeeb08571e6e3417d9545d374d035ace94a85e66186")
    version("12.0.0", sha256="aefd1acc879ee4d122169250bfd3ba637c50343478a148e0ef4e7d25da0d8be7")
    version("11.0.0", sha256="eb288606f336eba262ac562fd157d2022dc2b97961a08f19632bf49712dba1f7")
    version("10.17.0", sha256="93e726b896fc076c146b3ef1c79358b91c90e2a1650fe31133ed1d474c37a3d5")
    version("10.14.0", sha256="d5e1ed0621f636c7e229529106b8574b24c1525d21e7cedeaabe74b46ffa09c8")
    version("10.6.0", sha256="44e53e14f7bb45350595b871429f35f3baac1e6c0a37f8287a7829eabda26fc0")
    version("10.0.0", sha256="7da63717e57f4a1cf836d206aa3e0f09d1851595a54ab30bdbef963a66fa6b4a")
    version("9.22.0", sha256="00c0953bb237ee3308bb2903c579e34d595ffa6b4b020d058c26dbcc5bddd64b")
    version("9.10.0", sha256="6006148e1afb57f6d9426209775c2c6b008d8e10bd3d80ff7c676af9a99fd5fa")
    version("9.4.1", sha256="dc57060303b90a18128e259c5266d48d4a80e68d535ac028467b3ac8d518d772")
    version("9.2.0", sha256="f42ef3cb835ee563942661ce93a52f8616f135993ccaef31fb2a196a66bd7295")
    version("9.1.0", sha256="c42c8d18dc53d7a63b2b400a3866843229b9b1afca96f64b389d5b874a6ba05d")
    version("9.0.0", sha256="8d7fdab4763a2174291e40c5da503bbb6d37b36591a54f7c0b1fa869eef54798")
    version("8.7.0", sha256="d8721aa4ed82ef2f7fe49062910826a7012f6823eb22d5290690c298eafe68ec")
    # v8.0.0: the WebAssembly build gained every core format; no change to the
    # Python wheel this package builds.
    version("8.0.0", sha256="ba0434950e9e2ef165ff9d50043ee6bb3e4359e7bc72ba77108553b7aad4b83f")
    version("7.0.0", sha256="797809b8c645d4712de9160ea375b0dc301b593844c475ca5bdbeb6490446c9a")
    version("6.6.1", sha256="327c1b146fefa3eb19404e2b422b5cf789fe81b8f402fea9694124d50b13e88b")
    version("6.6.0", sha256="a585a7b932a9a893b17710f68ed64a04b492d12abfe74c5744812fb44599cbae")
    version("6.5.0", sha256="f0ebdb7a547097ae338b2295eaa2cb08fe728a7d32c408f4109511ded3196779")
    version("6.4.0", sha256="d969bb081ac5bb9b43ce0fa32d3c6a5a8fc53a9f4ad086b03d7ebb40368a01fb")
    version("6.3.0", sha256="ead9fd2264ba809903c91347b7cbd1e526ac78373b2935590c967cad20aacf59")
    version("6.2.0", sha256="275c1a938845a416040b1517fb8f9c1c008e86ad888b432d0852eba0fac83126")
    version("6.1.0", sha256="0061d9b3ff20b65f6bb66dc4787b4c8f5c9f3abc9567b0b9e60fab28a8774afa")
    version("6.0.0", sha256="c5edd1c3f961a6282f08a76205e060ed3cb985401381313beb02788bc537ba94")

    variant("hdf5", default=True, description="C++ HDF5-backed formats and the h5py fallback")
    variant(
        "netcdf",
        default=True,
        description="C++ netCDF-backed format (Exodus) and the netCDF4 fallback",
    )
    variant("zlib", default=True, description="C++ VTU zlib compression path")
    variant(
        "zstd",
        default=False,
        description="C++ VTK XML zstd compression codec and the zstandard fallback",
        when="@7.3:",
    )
    variant(
        "lz4",
        default=False,
        description="C++ VTK XML lz4 compression codec and the lz4 fallback",
        when="@7.3:",
    )
    variant(
        "kahip", default=False, description="KaHIP-backed mesh partitioning quality", when="@7.6:"
    )

    variant(
        "bzip2", default=False, description="C++ native bzip2 path for libMesh", when="@16.12:"
    )
    variant("lzma", default=False, description="C++ VTK XML lzma compression codec", when="@17.3:")
    variant(
        "occt",
        default=False,
        description="OpenCASCADE-backed fit_cad operation and STEP/IGES reading",
        when="@16.41:",
    )
    variant(
        "cgnslib",
        default=False,
        description="Official CGNS library for ADF containers",
        when="@9.22:",
    )
    variant("adios2", default=False, description="Native DOLFINx VTX (.bp) reader", when="@16.13:")
    variant(
        "tecio", default=False, description="TecIO .szplt reader (manual download)", when="@16.13:"
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.15:", type="build")
    # +pyproject: py-scikit-build-core@:0.8 only pulls in py-pyproject-metadata
    # / py-pathspec (needed to parse our PEP 621 pyproject.toml) when this
    # variant is set; without it, the concretizer can pick @0.8~pyproject and
    # the build fails at "Preparing metadata (pyproject.toml)".
    depends_on("py-scikit-build-core@0.8: +pyproject", type="build", when="@:17.10")
    # pyproject.toml's minimum-version moved to 0.11 at v17.11.0, when the
    # PEP 639 licence metadata landed; older backends refuse to build it.
    depends_on("py-scikit-build-core@0.11:", type="build", when="@17.11:")
    depends_on("py-pybind11@2.11:", type="build")

    depends_on("python@3.8:", type=("build", "link", "run"))
    depends_on("py-numpy@1.20:", type=("build", "run"))
    depends_on("py-rich", type="run")

    depends_on("hdf5", when="+hdf5")
    # Some HDF5 formats (e.g. MED) always run the Python implementation.
    depends_on("py-h5py", when="+hdf5", type="run")
    depends_on("netcdf-c", when="+netcdf")
    depends_on("py-netcdf4", when="+netcdf", type="run")
    depends_on("zlib-api", when="+zlib")
    depends_on("zstd", when="+zstd")
    depends_on("py-zstandard", when="+zstd", type="run")
    depends_on("lz4", when="+lz4")
    depends_on("bzip2", when="+bzip2")
    depends_on("xz", when="+lzma")
    depends_on("opencascade@7.6:", when="+occt")
    depends_on("hdf5", when="+cgnslib")
    depends_on("cgns~mpi", when="+cgnslib")
    depends_on("adios2~mpi", when="+adios2")
    depends_on("tecio~mpi", when="+tecio")
    depends_on("py-lz4", when="+lz4", type="run")
    # KaHIP has no PyPI/Spack Python fallback package; +kahip only wires up
    # the native accelerator.
    depends_on("kahip", when="+kahip")

    # meshio++ requires a C++20 toolchain for the native core.
    conflicts("%gcc@:9", msg="meshio++ needs GCC >= 10 for C++20")
    conflicts("+cgnslib", when="~hdf5", msg="The CGNS library backend requires +hdf5")

    def config_settings(self, spec, prefix):
        # scikit-build-core forwards these to the CMake configure. The pybind11
        # extension requires the MESHIO mesh backend, which is the CMake default.
        def onoff(variant):
            return "ON" if spec.satisfies(variant) else "OFF"

        settings = {
            # hdf5's shared library reaches the link line only through
            # find_package(HDF5)'s imported target, so the directory CMake
            # resolved it from never makes it into Spack's seeded install
            # RPATH: the built _core extension has a DT_NEEDED on
            # libhdf5.so.<abi> with no RPATH entry for it. `spack load` does not
            # paper over the gap either -- for this spec it exports
            # CMAKE_PREFIX_PATH, PATH and PKG_CONFIG_PATH but no
            # LD_LIBRARY_PATH -- so `import meshioplusplus` fails with
            # "ImportError: libhdf5.so.310: cannot open shared object file" on
            # an otherwise correct +hdf5 build. use-link-path makes CMake add
            # the directory of every external library it actually linked, which
            # is where hdf5's was coming from. Verified by readelf on the
            # installed extension plus a real import. meshioplusplus itself
            # needs no equivalent: its libmeshioplusplus.so.0 already resolves
            # hdf5 without it.
            "cmake.define.CMAKE_INSTALL_RPATH_USE_LINK_PATH": "ON",
            "cmake.define.MESHIOPLUSPLUS_WITH_HDF5": onoff("+hdf5"),
            "cmake.define.MESHIOPLUSPLUS_WITH_NETCDF": onoff("+netcdf"),
            "cmake.define.MESHIOPLUSPLUS_WITH_ZLIB": onoff("+zlib"),
            "cmake.define.MESHIOPLUSPLUS_WITH_ZSTD": onoff("+zstd"),
            "cmake.define.MESHIOPLUSPLUS_WITH_LZ4": onoff("+lz4"),
            "cmake.define.MESHIOPLUSPLUS_WITH_KAHIP": onoff("+kahip"),
        }
        if spec.satisfies("@9.22:"):
            settings["cmake.define.MESHIOPLUSPLUS_WITH_CGNSLIB"] = onoff("+cgnslib")
        if spec.satisfies("@16.12:"):
            settings["cmake.define.MESHIOPLUSPLUS_WITH_BZIP2"] = onoff("+bzip2")
        if spec.satisfies("@16.13:"):
            settings["cmake.define.MESHIOPLUSPLUS_WITH_ADIOS2"] = onoff("+adios2")
            settings["cmake.define.MESHIOPLUSPLUS_WITH_TECIO"] = onoff("+tecio")
            if spec.satisfies("+tecio"):
                settings["cmake.define.TECIO_ROOT"] = str(spec["tecio"].prefix)
        if spec.satisfies("@16.41:"):
            settings["cmake.define.MESHIOPLUSPLUS_WITH_OCCT"] = onoff("+occt")
        if spec.satisfies("@17.3:"):
            settings["cmake.define.MESHIOPLUSPLUS_WITH_LZMA"] = onoff("+lzma")
        return settings
