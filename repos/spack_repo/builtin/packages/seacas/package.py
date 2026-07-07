# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import sys

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *

#
# Need to add:
#  KOKKOS support using an external (i.e. spack-supplied) kokkos library.

is_windows = sys.platform == "win32"


class Seacas(CMakePackage):
    """The SEACAS Project contains the Exodus and IOSS I/O libraries
    and a collection of applications which create, query, modify, or
    translate Exodus databases.  Exodus is a finite element mesh and
    results database file format.

    Default is to build the Exodus and IOSS libraries and the
    io_shell, io_info, io_modify, struc_to_unstruc apps.
    """

    homepage = "https://sandialabs.github.io/seacas/"
    git = "https://github.com/sandialabs/seacas.git"
    url = "https://github.com/sandialabs/seacas/archive/v2019-08-20.tar.gz"
    maintainers("gsjaardema")

    license("BSD-3-Clause")

    # ###################### Versions ##########################
    version("master", branch="master")
    version(
        "2025-10-14", sha256="f9351a8f1a555a015020f249b1e5c26a282fbb6e274f9b71eb38720d61267dda"
    )
    version(
        "2025-08-28", sha256="29125a84859c78b6bb0b5909ce7443aa2774235f0fc75dedf467a223603e0ffd"
    )
    version(
        "2025-08-19", sha256="f745ca9a57bfd7f771632fb5f154eb38ed3260e1430d968f2db725f8d8ee8545"
    )
    version(
        "2025-07-07", sha256="c1700d39cef818c87335dd3789403e47dc9efc2f01c8c3fb8e7d54b2db02a54a"
    )
    version(
        "2025-06-27", sha256="c28f40504b2322cd69e7df6efea1e3be289a7f98a6e533c53655513d18add7bb"
    )
    version(
        "2025-06-07", sha256="2974705f2859e30bca48b619fda078bb771c0e94381af9e624749afb9fd72780"
    )
    version(
        "2025-05-22", sha256="50e941ad2bfffa84d84465576cd118a14698b3f0cfcfc613dbb1aa3f2f4ebdda"
    )
    version(
        "2025-05-05", sha256="9e9872cee4223482d74918b0f50cc3ec77791f79330915611a0e1d5691c15184"
    )
    version(
        "2025-04-29", sha256="2a3a1533a1fbff8e8b78814a3a45f6fadfb3f05b5d9d10a4f0452c7bb4d1aa2f"
    )
    version(
        "2025-04-14", sha256="7704fc27e4f0d283fd9272ea769dbeffd971315a982e265c0d7c99fc77186476"
    )
    version(
        "2025-03-13", sha256="406aff5b8908d6a3bf6687d825905990101caa9cf8c1213a508938eed2134d6d"
    )
    version(
        "2025-02-27", sha256="224468d6215b4f4b15511ee7a29f755cdd9e7be18c08dfece9d9991e68185cfc"
    )
    version(
        "2024-08-15", sha256="c85130b0dac5ab9a08dcb53c8ccff478122d72b08bd41d99c0adfddc5eb18a52"
    )
    version(
        "2024-07-10", sha256="b2ba6ca80359fed8ed2a8a210052582c7a3b7b837253bd1e9be941047dcab3ff"
    )
    version(
        "2024-06-27", sha256="a28db6aa3d03ff0a54a091210cf867661427f0b22ac08f89a4cc3bd8e0c704b2"
    )
    version(
        "2024-04-03", sha256="edf1aacbde87212b10737d3037107dba5cf7e2cce167863e2ebb200dc1a3fbb5"
    )
    version(
        "2024-03-11", sha256="b849d958b34e77300aaf331f29c3e6fe417fd82600850a82e674a9b7ba4045ff"
    )
    version(
        "2023-11-27", sha256="fea1c0a6959d46af7478c9c16aac64e76c6dc358da38e2fe8793c15c1cffa8fc"
    )
    version(
        "2023-05-30", sha256="3dd982841854466820a3902163ad1cf1b3fbab65ed7542456d328f2d1a5373c1"
    )
    version(
        "2022-10-14", sha256="cde91e7561d2352045d669a25bdf46a604d85ed1ea7f3f5028004455e4ce9d56"
    )
    version(
        "2022-05-16", sha256="22ff67045d730a2c7d5394c9034e44a2033cc82a461574f93d899e9aa713d4ae"
    )
    version(
        "2022-03-04", sha256="a934a473e1fdfbc8dbb55058358551a02e03a60e5cdbf2b28b8ecd3d9500bfa5"
    )
    version(
        "2022-02-16", sha256="a6accb9924f0f357f63a01485c3eaaf5ceb6a22dfda73fc9bfb17d7e2f565098"
    )
    version(
        "2022-01-27", sha256="beff12583814dcaf75cf8f1a78bb183c1dcc8937bc18d5206672e3a692db05e0"
    )

    # ###################### Variants ##########################
    # Package options
    # The I/O libraries (exodus, IOSS) are always built
    # -- required of both applications and legacy variants.
    variant(
        "applications",
        default=True,
        description='Build all "current" SEACAS applications. This'
        " includes a debatable list of essential applications: "
        "aprepro, conjoin, cpup, ejoin, epu, exo2mat, mat2exo, "
        "exo_format, exodiff, explore, grepos, io_shell, io_info, "
        "io_modify, nemslice, nemspread, zellij",
    )
    variant(
        "legacy",
        default=True,
        description='Build all "legacy" SEACAS applications. This includes'
        ' a debatable list of "legacy" applications: algebra, blot, '
        "exomatlab, exotxt, fastq, gen3d, genshell, gjoin, mapvar, "
        "mapvar-kd, numbers, txtexo, nemesis",
    )

    # Build options
    variant("fortran", default=not is_windows, description="Compile with Fortran support.")
    # Enable this on Windows at your own risk, SEACAS exports no symbols and so cannot be
    # meaningfully linked against as a shared library
    variant("shared", default=True, description="Enables the build of shared libraries.")
    variant("mpi", default=True, description="Enables MPI parallelism.")
    variant("tests", default=True, description="Enable building the SEACAS tests.")
    variant(
        "thread_safe", default=False, description="Enable thread-safe exodus and IOSS libraries."
    )

    # TPLs (alphabet order)
    variant(
        "adios2",
        default=False,
        description="Enable ADIOS2. See https://github.com/ornladios/ADIOS2",
    )
    # enabling cgns fails builds on Windows, see seacas CI default configuration
    # https://github.com/sandialabs/seacas/blob/master/.appveyor.yml#L71
    for plat in ["linux", "darwin", "freebsd"]:
        with when(f"platform={plat}"):
            variant("cgns", default=True, description="Enable CGNS.")

    variant(
        "aws",
        default=False,
        when="@2025-10-14:",
        description="Enable support for S3 compatible storage using AWS SDK's S3 module",
    )
    variant(
        "faodel",
        default=False,
        description="Enable Faodel. See https://github.com/sandialabs/faodel",
    )
    variant(
        "libcatalyst",
        default=False,
        description="Enable libcatalyst tpl (catalyst api 2); Kitware insitu library",
    )
    variant(
        "matio",
        default=True,
        description="Compile with matio (MatLab) support."
        "  Enables exo2mat and mat2exo translators.",
    )
    variant(
        "metis",
        default=False,
        description="Compile with METIS and ParMETIS. "
        "Provides additional parallel decomposition options.",
    )
    variant(
        "pamgen",
        default=False,
        description="Compile with pamgen. "
        "Provides another ioss database option for internal generation of mesh models.",
    )
    variant(
        "x11",
        default=True,
        description="Compile with X11. "
        "Needed if building blot (visualizer) and fastq (2D mesh generation).",
    )
    variant(
        "zlib",
        default=False,
        description="Compile with zlib. "
        "Sometimes needed when building static libraries on some systems.",
    )
    # ###################### Dependencies ##########################
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build", when="+fortran")

    depends_on("cmake@3.22:", when="@2023-10-24:", type="build")
    depends_on("cmake@3.17:", when="@:2023-05-30", type="build")
    depends_on("mpi", when="+mpi")
    depends_on("zlib-api", when="+zlib")
    depends_on("parallel", when="platform=linux", type="run")
    depends_on("parallel", when="platform=darwin", type="run")
    depends_on("parallel", when="platform=freebsd", type="run")
    depends_on("trilinos~exodus+mpi+pamgen", when="+mpi+pamgen")
    depends_on("trilinos~exodus~mpi+pamgen", when="~mpi+pamgen")
    # Always depends on netcdf-c
    depends_on("netcdf-c@4.8.0:+mpi", when="+mpi")
    depends_on("netcdf-c+parallel-netcdf", when="+mpi platform=linux")
    depends_on("netcdf-c+parallel-netcdf", when="+mpi platform=darwin")
    depends_on("netcdf-c+parallel-netcdf", when="+mpi platform=freebsd")
    depends_on("netcdf-c@4.8.0:~mpi", when="~mpi")
    depends_on("netcdf-c@:4.9.2", when="@:2024-08-15")
    depends_on("hdf5+hl~mpi", when="~mpi")
    depends_on("hdf5+hl+mpi", when="+mpi")

    depends_on("fmt@10:", when="@2024-08-15:")
    depends_on("fmt@10.2.1:10", when="@2024-03-11:2024-07-10")
    depends_on("fmt@10.1.0:10", when="@2023-10-24:2023-11-27")
    depends_on("fmt@9.1.0", when="@2022-10-14:2023-05-30")
    depends_on("fmt@8.1.0:9", when="@2022-03-04:2022-05-16")

    # if fmt@9.1.0%gcc is mixed with an %apple-clang seacas build
    # it triggers a bug in apple-clang w.r.t how symbols are mangled
    # https://github.com/spack/spack/issues/44330
    conflicts(
        "^fmt@9%gcc",
        msg="""Cannot mix gcc/apple-clang toolchains
              for this library combination.
              See https://github.com/spack/spack/issues/44330""",
        when="%apple-clang",
    )

    depends_on("catch2@3:", when="@2024-03-11:+tests")

    depends_on("matio", when="+matio")

    depends_on("libcatalyst+mpi~python", when="+libcatalyst+mpi")
    depends_on("libcatalyst~mpi~python", when="+libcatalyst~mpi")

    depends_on("libx11", when="+x11")

    with when("+cgns"):
        depends_on("cgns@4.2.0:+mpi+scoping", when="+mpi")
        depends_on("cgns@4.2.0:~mpi+scoping", when="~mpi")

    with when("+adios2"):
        depends_on("adios2@2.10.1")
        depends_on("adios2~mpi", when="~mpi")
        depends_on("adios2+mpi", when="+mpi")

    with when("+metis"):
        depends_on("metis+int64+real64")
        depends_on("parmetis+int64", when="+mpi")
    with when("+aws"):
        depends_on("aws-sdk-cpp")
        depends_on("cereal")

    # The Faodel TPL is only supported in seacas@2021-04-05:
    depends_on("faodel@1.2108.1:+mpi", when="+faodel +mpi")
    depends_on("faodel@1.2108.1:~mpi", when="+faodel ~mpi")
    conflicts(
        "+faodel",
        when="@:2021-01-20",
        msg="The Faodel TPL is only compatible with @2021-04-05 and later.",
    )
    conflicts("+shared", when="platform=windows")
    conflicts("+x11", when="platform=windows")

    conflicts("@2024-06-27 platform=windows")

    # Remove use of variable in array assignment (triggers c2057 on MSVC)
    # See https://github.com/sandialabs/seacas/issues/438
    patch(
        "https://github.com/sandialabs/seacas/commit/29a9ebeccb5a656b4b334fa6af904689da9ffddc.diff?full_index=1",
        sha256="d088208511fb0a087e2bf70ae70676e59bfefe8d8f5b24bd53b829566f5147d2",
        when="@:2023-10-24",
    )

    # Based on install-tpl.sh script, cereal seems to only be used when faodel enabled
    depends_on("cereal", when="@2021-04-02: +faodel")

    def flag_handler(self, name: str, flags: List[str]):
        if name == "fflags" and self.spec.satisfies("@2022:2022-03 %fortran=gcc@10:"):
            # Required for recent GCC compilers, flag exists since GCC 10
            flags.append("-fallow-argument-mismatch")
        return (flags, None, None)

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        env.prepend_path("PYTHONPATH", self.prefix.lib)

    def cmake_args(self):
        spec = self.spec
        from_variant = self.define_from_variant
        define = self.define

        if self.spec.satisfies("@2022-10-14:"):
            project_name_base = "Seacas"
        else:
            project_name_base = "SEACASProj"

        options = []

        # #################### Base Settings #######################

        options.extend(
            [
                from_variant(project_name_base + "_ENABLE_TESTS", "tests"),
                define(project_name_base + "_ENABLE_Kokkos", False),
                define(project_name_base + "_HIDE_DEPRECATED_CODE", False),
                # Seacas MSVC tests are not tested with Zoltan
                # which causes build errors, skip for now
                define("ENABLE_ExoNull", True),
                define(project_name_base + "_ENABLE_Zoltan", not is_windows),
                from_variant("CMAKE_INSTALL_RPATH_USE_LINK_PATH", "shared"),
                from_variant("BUILD_SHARED_LIBS", "shared"),
                from_variant("SEACASExodus_ENABLE_THREADSAFE", "thread_safe"),
                from_variant("SEACASIoss_ENABLE_THREADSAFE", "thread_safe"),
                # SEACASExodus_ENABLE_THREADSAFE=ON requires TPL_ENABLE_Pthread=ON
                from_variant("TPL_ENABLE_Pthread", "thread_safe"),
                from_variant("TPL_ENABLE_X11", "x11"),
                from_variant(project_name_base + "_ENABLE_Fortran", "fortran"),
                define(project_name_base + "_ENABLE_SEACAS", True),
            ]
        )
        if spec.satisfies("@2025-08-28:"):
            options.append(define(project_name_base + "_ENABLE_CXX17", True))
        else:
            options.append(define(project_name_base + "_ENABLE_CXX11", True))

        if "~shared" in self.spec and not is_windows:
            options.append(self.define(f"{project_name_base}_EXTRA_LINK_FLAGS", "z;dl"))
        options.append(from_variant("TPL_ENABLE_MPI", "mpi"))
        if "+mpi" in spec and not is_windows:
            options.extend(
                [
                    define("CMAKE_C_COMPILER", spec["mpi"].mpicc),
                    define("CMAKE_CXX_COMPILER", spec["mpi"].mpicxx),
                    define("CMAKE_Fortran_COMPILER", spec["mpi"].mpifc),
                    define("MPI_BASE_DIR", spec["mpi"].prefix),
                ]
            )

        # ########## What applications should be built #############
        # Check whether they want everything; if so, do the easy way...
        if "+applications" in spec and "+legacy" in spec:
            options.extend(
                [
                    define(project_name_base + "_ENABLE_ALL_PACKAGES", True),
                    define(project_name_base + "_ENABLE_ALL_OPTIONAL_PACKAGES", True),
                    define(project_name_base + "_ENABLE_SECONDARY_TESTED_CODE", True),
                ]
            )

        else:
            # Don't want everything; handle the subsets:
            options.extend(
                [
                    define(project_name_base + "_ENABLE_ALL_PACKAGES", False),
                    define(project_name_base + "_ENABLE_ALL_OPTIONAL_PACKAGES", False),
                    define(project_name_base + "_ENABLE_SECONDARY_TESTED_CODE", False),
                    define(project_name_base + "_ENABLE_SEACASIoss", True),
                    define(project_name_base + "_ENABLE_SEACASExodus", True),
                    from_variant(project_name_base + "_ENABLE_SEACASExodus_for", "fortran"),
                    from_variant(project_name_base + "_ENABLE_SEACASExoIIv2for32", "fortran"),
                ]
            )

            if "+applications" in spec:
                # C / C++ applications
                for app in (
                    "Aprepro",
                    "Aprepro_lib",
                    "Conjoin",
                    "Cpup",
                    "Ejoin",
                    "Epu",
                    "Exo2mat",
                    "Exo_format",
                    "Exodiff",
                    "Mat2exo",
                    "Nas2exo",
                    "Nemslice",
                    "Nemspread",
                    "Slice",
                    "Zellij",
                ):
                    options.append(define(project_name_base + "_ENABLE_SEACAS" + app, True))
                # Fortran-based applications
                for app in ("Explore", "Grepos"):
                    options.append(
                        from_variant(project_name_base + "_ENABLE_SEACAS" + app, "fortran")
                    )

            if "+legacy" in spec:
                # Legacy applications -- all are fortran-based except Nemesis
                options.append(define(project_name_base + "_ENABLE_SEACASNemesis", True))

                for app in (
                    "Algebra",
                    "Blot",
                    "Ex1ex2v2",
                    "Ex2ex1v2",
                    "Exomatlab",
                    "Exotec2",
                    "Exotxt",
                    "Fastq",
                    "Gen3D",
                    "Genshell",
                    "Gjoin",
                    "Mapvar",
                    "Mapvar-kd",
                    "Numbers",
                    "Txtexo",
                ):
                    options.append(
                        from_variant(project_name_base + "_ENABLE_SEACAS" + app, "fortran")
                    )

        # ##################### Dependencies ##########################
        # Always need NetCDF-C
        options.extend(
            [define("TPL_ENABLE_Netcdf", True), define("NetCDF_ROOT", spec["netcdf-c"].prefix)]
        )

        if spec.satisfies("+metis+mpi"):
            options.extend(
                [
                    define("TPL_ENABLE_METIS", True),
                    define("METIS_LIBRARY_DIRS", spec["metis"].prefix.lib),
                    define("METIS_LIBRARY_NAMES", "metis"),
                    define("TPL_METIS_INCLUDE_DIRS", spec["metis"].prefix.include),
                    define("TPL_ENABLE_ParMETIS", True),
                    define(
                        "ParMETIS_LIBRARY_DIRS",
                        [spec["parmetis"].prefix.lib, spec["metis"].prefix.lib],
                    ),
                    define("ParMETIS_LIBRARY_NAMES", ["parmetis", "metis"]),
                    define(
                        "TPL_ParMETIS_INCLUDE_DIRS",
                        [spec["parmetis"].prefix.include, spec["metis"].prefix.include],
                    ),
                ]
            )
        elif "+metis" in spec:
            options.extend(
                [
                    define("TPL_ENABLE_METIS", True),
                    define("METIS_LIBRARY_DIRS", spec["metis"].prefix.lib),
                    define("METIS_LIBRARY_NAMES", "metis"),
                    define("TPL_METIS_INCLUDE_DIRS", spec["metis"].prefix.include),
                    define("TPL_ENABLE_ParMETIS", False),
                ]
            )
        else:
            options.extend(
                [define("TPL_ENABLE_METIS", False), define("TPL_ENABLE_ParMETIS", False)]
            )

        options.append(from_variant(f"{project_name_base}_ENABLE_Pamgen", "pamgen"))
        options.append(from_variant("TPL_ENABLE_Pamgen", "pamgen"))

        options.append(from_variant("TPL_ENABLE_Matio", "matio"))
        if "+matio" in spec:
            options.append(define("Matio_ROOT", spec["matio"].prefix))

        options.append(from_variant("TPL_ENABLE_CGNS", "cgns"))
        if "+cgns" in spec:
            options.append(define("CGNS_ROOT", spec["cgns"].prefix))

        options.append(from_variant("TPL_ENABLE_AWSSDK", "aws"))
        if "+aws" in spec:
            options.append(define("AWSSDK_ROOT", spec["aws-sdk-cpp"].prefix))
            options.append(define("TPL_ENABLE_Cereal", True))
            options.append(define("Cereal_INCLUDE_DIRS", spec["cereal"].prefix.include))

        options.append(from_variant("TPL_ENABLE_Faodel", "faodel"))
        for pkg in ("Faodel", "BOOST"):
            if pkg.lower() in spec:
                options.append(define(pkg + "_ROOT", spec[pkg.lower()].prefix))

        if "+faodel" in spec:
            # faodel headers are under $faodel_prefix/include/faodel but seacas
            # leaves off the faodel part
            faodel_incdir = spec["faodel"].prefix.include
            faodel_incdir2 = spec["faodel"].prefix.include.faodel
            faodel_incdirs = [faodel_incdir, faodel_incdir2]
            options.append(define("Faodel_INCLUDE_DIRS", ";".join(faodel_incdirs)))
            options.append(define("Faodel_LIBRARY_DIRS", spec["faodel"].prefix.lib))

        options.append(from_variant("TPL_ENABLE_ADIOS2", "adios2"))
        if "+adios2" in spec:
            options.append(define("ADIOS2_ROOT", spec["adios2"].prefix))

        if "+libcatalyst" in spec:
            options.append(define("TPL_ENABLE_Catalyst2", "ON"))

        # ################# RPath Handling ######################
        if sys.platform == "darwin" and macos_version() >= Version("10.12"):
            # use @rpath on Sierra due to limit of dynamic loader
            options.append(define("CMAKE_MACOSX_RPATH", True))
        else:
            options.append(define("CMAKE_INSTALL_NAME_DIR", self.prefix.lib))

        return options

    @run_after("install")
    def symlink_parallel(self):
        if not self.spec.dependencies("parallel"):
            return
        symlink(self.spec["parallel"].prefix.bin.parallel, self.prefix.bin.parallel)
