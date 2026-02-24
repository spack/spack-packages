# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


import glob
import os

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.packages.boost.package import Boost

from spack.package import *


class Vtk(CMakePackage):
    """The Visualization Toolkit (VTK) is an open-source, freely
    available software system for 3D computer graphics, image
    processing and visualization."""

    homepage = "https://www.vtk.org"
    url = "https://www.vtk.org/files/release/9.0/VTK-9.0.0.tar.gz"
    list_url = "https://www.vtk.org/download/"

    maintainers("chuckatkins", "danlipsa", "johnwparent", "vicentebolea")

    license("BSD-3-Clause")

    version(
        "9.5.1",
        sha256="14443661c7b095d05b4e376fb3f40613f173e34fc9d4658234e9ec1d624a618f",
        preferred=True,
    )
    version("9.5.0", sha256="04ae86246b9557c6b61afbc534a6df099244fbc8f3937f82e6bc0570953af87d")
    version("9.4.1", sha256="c253b0c8d002aaf98871c6d0cb76afc4936c301b72358a08d5f3f72ef8bc4529")
    version("9.3.1", sha256="8354ec084ea0d2dc3d23dbe4243823c4bfc270382d0ce8d658939fd50061cab8")
    version("9.2.6", sha256="06fc8d49c4e56f498c40fcb38a563ed8d4ec31358d0101e8988f0bb4d539dd12")
    version("9.2.2", sha256="1c5b0a2be71fac96ff4831af69e350f7a0ea3168981f790c000709dcf9121075")
    version("9.1.0", sha256="8fed42f4f8f1eb8083107b68eaa9ad71da07110161a3116ad807f43e5ca5ce96")
    version("9.0.3", sha256="bc3eb9625b2b8dbfecb6052a2ab091fc91405de4333b0ec68f3323815154ed8a")
    version("9.0.1", sha256="1b39a5e191c282861e7af4101eaa8585969a2de05f5646c9199a161213a622c7")
    version("9.0.0", sha256="15def4e6f84d72f82386617fe595ec124dda3cbd13ea19a0dcd91583197d8715")

    with default_args(deprecated=True):
        # v8.2.1a is a compatability version of VTK to allow VisIt to build in CI and contains
        # patches that were not tested by VTK CI or for a VTK release
        # - Python 3.8 compatability
        # - VisIt 3.3.3 compatability
        version(
            "8.2.1a",
            url="https://www.vtk.org/files/release/8.2/VTK-8.2.0.tar.gz",
            sha256="34c3dc775261be5e45a8049155f7228b6bd668106c72a3c435d95730d17d57bb",
        )
        version("8.2.0", sha256="34c3dc775261be5e45a8049155f7228b6bd668106c72a3c435d95730d17d57bb")
        version("8.1.2", sha256="0995fb36857dd76ccfb8bb07350c214d9f9099e80b1e66b4a8909311f24ff0db")
        version("8.1.1", sha256="71a09b4340f0a9c58559fe946dc745ab68a866cf20636a41d97b6046cb736324")
        version("8.1.0", sha256="6e269f07b64fb13774f5925161fb4e1f379f4e6a0131c8408c555f6b58ef3cb7")
        version("8.0.1", sha256="49107352923dea6de05a7b4c3906aaf98ef39c91ad81c383136e768dcf304069")
        version("7.1.0", sha256="5f3ea001204d4f714be972a810a62c0f2277fbb9d8d2f8df39562988ca37497a")
        version("7.0.0", sha256="78a990a15ead79cdc752e86b83cfab7dbf5b7ef51ba409db02570dbdd9ec32c3")
        version("6.3.0", sha256="92a493354c5fa66bea73b5fc014154af5d9f3f6cee8d20a826f4cd5d4b0e8a5e")
        version("6.1.0", sha256="bd7df10a479606d529a8b71f466c44a2bdd11fd534c62ce0aa44fad91883fa34")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("pkgconfig", type="build", when="platform=linux")

    # VTK7 defaults to OpenGL2 rendering backend
    variant("opengl2", default=True, description="Enable OpenGL2 backend", when="@:9.4")
    variant("python", default=False, description="Enable Python support", when="@9.0.2:")
    variant("qt", default=False, description="Build with support for Qt")
    variant("mpi", default=True, description="Enable MPI support")
    variant("examples", default=False, description="Enable building & installing the VTK examples")
    variant("versioned_install", default=True, description="Include version in library filenames")
    variant("shared", default=True, description="Builds a shared version of the library")
    variant("kits", default=False, description="Use module kits")

    variant(
        "io",
        values=any_combination_of(
            "adios2", "cgns", "exodusii", "ffmpeg", "fides", "ioss", "netcdf", "xdmf"
        ).with_default("cgns,exodusii,ioss,netcdf"),
        description="Enable IO modules",
    )
    requires("io=adios2", when="io=fides")

    variant(
        "raytracing",
        values=any_combination_of("ospray").with_default("none"),
        description="Enable raytracing support",
    )
    variant("advanced_debug", default=False, description="Enable the VTK_DEBUG_LEAKS flag")

    patch("gcc.patch", when="@6.1.0")

    # Fix missing standard includes that lead to build errors on newer compilers
    # Patch for <limits>
    # https://gitlab.kitware.com/vtk/vtk/-/commit/e066c3f4fbbfe7470c6207db0fc3f3952db633c
    patch("vtk_9_include_missing_limits.patch", when="@9:9.0")
    # Patch for <cstdint>
    # See https://gitlab.kitware.com/vtk/vtk/-/issues/18782

    patch("vtk_9_1_2_improve_cstdint_includes.patch", when="@9.1:9.2")

    # Patch for paraview 5.10: +hdf5 ^hdf5@1.13.2:
    # https://gitlab.kitware.com/vtk/vtk/-/merge_requests/9690
    # patch seems to effectively been added to vtk@9.2.3 (e81a2fe)
    patch("xdmf2-hdf51.13.2.patch", when="@9:9.2.2 io=xdmf")

    # We cannot build with both osmesa and qt in spack
    conflicts("^osmesa", when="+qt")

    conflicts("%gcc@13", when="@9.2")

    # VTK 8 vendors a heavily outdated version of CMake's GenerateExportHeader module, which
    # has a bogus version check for GCC/Intel version to early exit. This drops the early exit.
    patch("vtk-bogus-compiler-check.patch", when="@7.1:8")

    # Based on PyPI wheel availability
    with when("+python"), default_args(type=("build", "link", "run")):
        extends("python@:3.13")
        extends("python@:3.12", when="@:9.3")
        extends("python@:3.11", when="@:9.2")
        extends("python@:3.10", when="@:9.2.2")
        extends("python@:3.9", when="@:9.1")

    # We need mpi4py if buidling python wrappers and using MPI
    depends_on("py-mpi4py", when="+python+mpi", type="run")

    # python3.7 compatibility patch backported from upstream
    # https://gitlab.kitware.com/vtk/vtk/commit/706f1b397df09a27ab8981ab9464547028d0c322
    patch("python3.7-const-char.patch", when="@7.0.0:8.1.1 ^python@3.7:")

    # Broken downstream FindMPI
    patch("vtkm-findmpi-downstream.patch", when="@9.0.0")

    for plat in ["linux", "darwin", "freebsd"]:
        # use internal FindHDF5
        patch("internal_findHDF5.patch", when=f"@:8 platform={plat}")

    # Fix IOADIOS2 module to work with kits
    # https://gitlab.kitware.com/vtk/vtk/-/merge_requests/8653
    patch("vtk-adios2-module-no-kit.patch", when="@9:9.0.3")

    # Python 3.8 compatibility for VTK 8.2
    # https://gitlab.kitware.com/vtk/vtk/-/merge_requests/6269
    # https://gitlab.kitware.com/vtk/vtk/-/merge_requests/6275
    patch("vtk82_python38.patch", when="@8.2.1a")

    # Fix link error in exodusII
    patch("vtk-8.2-exodusII-gcc11.patch", when="@8.2.1a")

    # The use of the OpenGL2 backend requires at least OpenGL Core Profile
    # version 3.2 or higher.
    depends_on("gl@3.2:", when="+opengl2")
    depends_on("gl@1.2:", when="~opengl2")

    depends_on("xz")
    patch("vtk_find_liblzma.patch", when="@8.2")
    patch("vtk_movie_link_ogg.patch", when="@8.2")
    patch("vtk_use_sqlite_name_vtk_expects.patch", when="@8.2")
    patch("vtk_proj_include_no_strict.patch", when="@9: platform=windows")
    # allow proj to be detected via a CMake produced export config file
    # failing that, falls back on standard library detection
    # required for VTK to build against modern proj/more robustly
    patch("vtk_findproj_config.patch", when="@9:")
    # adds a fake target alias'ing the hdf5 target to prevent
    # checks for that target from falling on VTK's empty stub target
    # Required to consume netcdf and hdf5 both built
    # with CMake from VTK
    # a patch with the same name is also applied to paraview
    # the two patches are the same but for the path to the files they patch
    patch("vtk_alias_hdf5.patch", when="@9:")
    # VTK 9.5 adds linkage to inonit when using an external IOSS
    # backport that to 9.4
    # https://gitlab.kitware.com/vtk/vtk/-/merge_requests/12279
    patch("vtk_9.4_external_ioss_linkage.patch", when="@9.4")
    # Linking against an external gl2ps causes linker errors due to a lack of
    # glgetdoublev on macos. Vtk provides an alias for this, us it
    # Upstream issue: https://gitlab.kitware.com/vtk/vtk/-/issues/19561
    patch("vtk-alias-gldoublev.patch", when="platform=darwin @9.4:")

    # VTK 9.0 on Windows uses dll instead of lib for hdf5-hl target, which fails linking. Can't
    # be fixed by bumping CMake lower bound, because VTK vendors FindHDF5.cmake. Various other
    # patches to FindHDF5.cmake are missing, so add conflict instead of a series of patches.
    conflicts("@9.0 platform=windows")
    depends_on("libxt", when="^[virtuals=gl] glx platform=linux")

    # VTK will need Qt5OpenGL, and qt needs '-opengl' for that
    depends_on("qt+opengl", when="+qt")

    depends_on("boost", when="io=xdmf")
    depends_on("boost+mpi", when="io=xdmf +mpi")

    # TODO: replace this with an explicit list of components of Boost,
    # for instance depends_on('boost +filesystem')
    # See https://github.com/spack/spack/pull/22303 for reference
    depends_on(Boost.with_default_variants, when="io=xdmf")
    depends_on("ffmpeg", when="io=ffmpeg")
    depends_on("mpi", when="+mpi")

    depends_on("adios2+mpi", when="io=adios2 +mpi")
    depends_on("adios2~mpi", when="io=adios2 ~mpi")
    depends_on("expat")
    # See <https://gitlab.kitware.com/vtk/vtk/-/issues/18033> for why vtk doesn't
    # work yet with freetype 2.10.3 (including possible patches)
    depends_on("freetype @:2.10.2", when="@:9.0.1")
    depends_on("freetype")
    depends_on("glew")
    depends_on("hdf5+hl")
    depends_on("hdf5~mpi", when="~mpi")
    depends_on("hdf5+mpi", when="+mpi")
    depends_on("hdf5@1.8:", when="@8:9.0")
    depends_on("hdf5@1.10:", when="@9.1:")
    depends_on("jpeg")
    depends_on("jsoncpp")
    depends_on("libxml2")
    depends_on("lz4")
    depends_on("netcdf-c@:4.9.2", when="io=exodusii")
    depends_on("netcdf-c@:4.9.2~mpi", when="io=netcdf ~mpi")
    depends_on("netcdf-c@:4.9.2+mpi", when="io=netcdf +mpi")
    depends_on("netcdf-cxx4", when="io=netcdf @:8.1.2")
    depends_on("libpng")
    depends_on("libtiff")
    depends_on("zlib-api")
    depends_on("eigen@:3", when="@8.2.0:")
    depends_on("double-conversion", when="@8.2.0:")
    depends_on("sqlite", when="@8.2.0:")
    depends_on("pugixml", when="@8.3.0:")
    depends_on("libogg")
    depends_on("libtheora")
    depends_on("utf8cpp", when="@9:")
    depends_on("gl2ps", when="@8.1:")
    depends_on("gl2ps@1.4.1:", when="@9:")
    # "8.2.1a" uses an internal proj so this special cases 8.2.1a
    depends_on("proj@4:7", when="@:8.2.0, 9:9.1")
    depends_on("proj@8:", when="@9.2:")
    depends_on("cgns@4.1.1:+mpi", when="@9.1: io=cgns +mpi")
    depends_on("cgns@4.1.1:~mpi", when="@9.1: io=cgns ~mpi")
    depends_on("ospray@2.1:2", when="raytracing=ospray")
    depends_on("openimagedenoise", when="raytracing=ospray")
    depends_on("ospray +mpi", when="raytracing=ospray +mpi")

    # VTK introduced Seacas IOSS dependency on 9.1
    with when("@9.1: io=ioss"):
        depends_on("seacas+mpi", when="+mpi")
        depends_on("seacas~mpi", when="~mpi")
        depends_on("seacas@2021-05-12:2022-10-14", when="@9.1")
        # vtk@9.2: need Ioss::Utils::get_debug_stream() which only 2022-10-14 provides,
        # and to be safe against other issues, make them build with this version only:
        depends_on("seacas@2022-10-14", when="@9.2:9.3")
        depends_on("seacas@2024-06-27", when="@9.4:")

    depends_on("nlohmann-json", when="@9.2:")

    # For finding Fujitsu-MPI wrapper commands
    patch("find_fujitsu_mpi.patch", when="@:8.2.0%fj")
    # Freetype@2.10.3 no longer exports FT_CALLBACK_DEF, this
    # patch replaces FT_CALLBACK_DEF with simple extern "C"
    # See https://gitlab.kitware.com/vtk/vtk/-/issues/18033
    patch("vtk_freetype_2.10.3_replace_FT_CALLBACK_DEF.patch", when="@:9.0.1 ^freetype@2.10.3:")

    patch("vtk_module_skip_argless_target_calls.patch", when="@9.1")

    # SEACAS >= 2024-06-27 needs c++17 which is already required in VTK master.
    patch("vtk_minimum_version_cpp_17.patch", when="@9.4")

    # Needed to build VTK with external SEACAS.
    patch("vtk_ioss_transform_2d_elem_block_to_3d.patch", when="@9.4")

    # https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=280893
    #  incorrect member accesses fixed in 9.4
    # https://gitlab.kitware.com/vtk/vtk/-/commit/98af50ca33
    patch("vtk_patch_octree_m_children.patch", when="@9.2:9.3")

    # clang 19+ no long providers std::char_traits<> for char8_t
    # impacts any clang derivative compiler. But can be patched
    # regardless of compiler
    # https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=280893
    patch("vtk_clang19_size_t.patch", when="@9.2:9.4.2")

    def patch(self):
        if self.spec.satisfies("@9.2: io=ioss"):
            # provide definition for Ioss::Init::Initializer::Initializer(),
            # required on macOS, as "-undefined error" is the default,
            # but not on Linux, as undefined symbols are tolerated
            filter_file("TARGETS Ioss", "TARGETS Ioss Ionit", "ThirdParty/ioss/CMakeLists.txt")

        if self.spec.satisfies("@9.4: io=ioss"):
            # Needed to build VTK with external SEACAS >= 2022-10-14
            filter_file(
                "^.*USE_VARIABLES SEACASIoss_INCLUDE_DIRS.*$", "", "ThirdParty/ioss/CMakeLists.txt"
            )

    def url_for_version(self, version):
        return f"http://www.vtk.org/files/release/{version.up_to(2)}/VTK-{version}.tar.gz"

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        # VTK has some trouble finding freetype unless it is set in
        # the environment
        env.set("FREETYPE_DIR", self.spec["freetype"].prefix)

        # Force API compatibility with HDF5
        if self.spec.satisfies("@9.1:"):
            env.append_flags("CFLAGS", "-DH5_USE_110_API")
            env.append_flags("CXXFLAGS", "-DH5_USE_110_API")
        elif self.spec.satisfies("@8:"):
            env.append_flags("CFLAGS", "-DH5_USE_18_API")
            env.append_flags("CXXFLAGS", "-DH5_USE_18_API")

    def cmake_args(self):
        spec = self.spec

        cmake_args = [
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define_from_variant("VTK_ENABLE_KITS", "kits"),
            # prevents installation into lib64 which might not be in the path
            # (solves #26314)
            "-DCMAKE_INSTALL_LIBDIR:PATH=lib",
            # Allow downstream codes (e.g. VisIt) to override VTK's classes
            "-DVTK_ALL_NEW_OBJECT_FACTORY:BOOL=ON",
        ]

        def module_variant(feature, on="YES", off="NO"):
            """Ternary for spec variant to YES/NO string"""
            if spec.satisfies(feature):
                return on
            return off

        adios2_enabled = module_variant("io=adios2")
        cmake_args.append(self.define("VTK_MODULE_ENABLE_VTK_IOADIOS2", adios2_enabled))

        cgns_enabled = module_variant("io=cgns")
        cmake_args.append(self.define("VTK_MODULE_ENABLE_VTK_cgns", cgns_enabled))
        cmake_args.append(self.define("VTK_MODULE_ENABLE_VTK_IOCGNSReader", cgns_enabled))

        exodusii_enabled = module_variant("io=exodusii")
        cmake_args.append(self.define("VTK_MODULE_ENABLE_VTK_exodusII", exodusii_enabled))
        cmake_args.append(self.define("VTK_MODULE_ENABLE_VTK_IOExodus", exodusii_enabled))

        fides_enabled = module_variant("io=fides")
        cmake_args.append(self.define("VTK_MODULE_ENABLE_VTK_fides", fides_enabled))
        cmake_args.append(self.define("VTK_MODULE_ENABLE_VTK_IOFides", fides_enabled))

        ioss_enabled = module_variant("io=ioss")
        cmake_args.append(self.define("VTK_MODULE_ENABLE_VTK_ioss", ioss_enabled))
        cmake_args.append(self.define("VTK_MODULE_ENABLE_VTK_IOIOSS", ioss_enabled))

        netcdf_enabled = module_variant("io=netcdf")
        cmake_args.append(self.define("VTK_MODULE_ENABLE_VTK_IONetCDF", netcdf_enabled))

        # Needed by netcdf and exodusii io modules
        cmake_args.append(
            self.define("VTK_MODULE_ENABLE_VTK_netcdf", "YES" if "netcdf-c" in spec else "NO")
        )

        if spec.satisfies("+mpi"):
            cmake_args.append(
                self.define("VTK_MODULE_ENABLE_VTK_IOParallelNetCDF", netcdf_enabled)
            )

        if spec.satisfies("raytracing=ospray"):
            cmake_args.append(self.define("VTK_MODULE_ENABLE_VTK_RenderingRayTracing", "YES"))
            cmake_args.append("-DVTK_ENABLE_OSPRAY:BOOL=ON")
            cmake_args.append("-DVTKOSPRAY_ENABLE_DENOISER:BOOL=ON")

        # Version 8.2.1a using internal libproj/pugixml for compatability
        if spec.satisfies("@8.2.1a"):
            cmake_args.append("-DVTK_USE_SYSTEM_LIBPROJ:BOOL=OFF")
            cmake_args.append("-DVTK_USE_SYSTEM_PUGIXML:BOOL=OFF")

        # Disable wrappers for other languages.
        cmake_args.append("-DVTK_WRAP_JAVA=OFF")
        if spec.satisfies("@:8.1"):
            cmake_args.append("-DVTK_WRAP_TCL=OFF")

        # In general, we disable use of VTK "ThirdParty" libs, preferring
        # spack-built versions whenever possible but there are exceptions.
        if spec.satisfies("@:8"):
            cmake_args.extend(
                ["-DVTK_USE_SYSTEM_LIBRARIES:BOOL=ON", "-DVTK_USE_SYSTEM_LIBHARU=OFF"]
            )
            if spec.satisfies("@:8.0"):
                cmake_args.append("-DVTK_USE_SYSTEM_GL2PS=OFF")
        else:
            cmake_args.extend(
                [
                    "-DVTK_USE_EXTERNAL:BOOL=ON",
                    "-DVTK_MODULE_USE_EXTERNAL_VTK_fast_float:BOOL=OFF",
                    "-DVTK_MODULE_USE_EXTERNAL_VTK_libharu:BOOL=OFF",
                    "-DVTK_MODULE_USE_EXTERNAL_VTK_pegtl:BOOL=OFF",
                    "-DVTK_MODULE_USE_EXTERNAL_VTK_token:BOOL=OFF",
                    f"-DHDF5_ROOT={spec['hdf5'].prefix}",
                ]
            )
            if spec.satisfies("@9.1:"):
                cmake_args.extend(
                    [
                        "-DVTK_MODULE_USE_EXTERNAL_VTK_exprtk:BOOL=OFF",
                        # uses an unreleased version of fmt
                        "-DVTK_MODULE_USE_EXTERNAL_VTK_fmt:BOOL=OFF",
                    ]
                )
            if spec.satisfies("@9.2:"):
                cmake_args.append("-DVTK_MODULE_USE_EXTERNAL_VTK_verdict:BOOL=OFF")
            if spec.satisfies("@9.5:"):
                cmake_args.append("-DVTK_MODULE_USE_EXTERNAL_VTK_vtkviskores:BOOL=OFF")

        # Some variable names have changed
        if spec.satisfies("@8.2.0"):
            cmake_args.append("-DVTK_USE_SYSTEM_PUGIXML:BOOL=OFF")
        elif spec.satisfies("@:8.1"):
            cmake_args.extend(
                [
                    "-DVTK_USE_SYSTEM_LIBPROJ4:BOOL=OFF",
                    f"-DNETCDF_CXX_ROOT={spec['netcdf-cxx'].prefix}",
                ]
            )

        if "+mpi" in spec:
            if spec.satisfies("@:8.2.0"):
                cmake_args.extend(["-DVTK_Group_MPI:BOOL=ON", "-DVTK_USE_SYSTEM_DIY2:BOOL=OFF"])
            else:
                cmake_args.extend(["-DVTK_USE_MPI=ON"])
        else:
            cmake_args.append("-DVTK_USE_MPI=OFF")

        if spec.satisfies("io=ffmpeg"):
            if spec.satisfies("@:8"):
                cmake_args.append("-DModule_vtkIOFFMPEG:BOOL=ON")
            else:
                cmake_args.append("-DVTK_MODULE_ENABLE_VTK_IOFFMPEG:STRING=YES")

        # Enable/Disable wrappers for Python.
        if "+python" in spec:
            cmake_args.append("-DVTK_WRAP_PYTHON=ON")
            if "+mpi" in spec and spec.satisfies("@:8"):
                cmake_args.append("-DVTK_USE_SYSTEM_MPI4PY:BOOL=ON")
            if spec.satisfies("@9.0.0: ^python@3:"):
                cmake_args.append("-DVTK_PYTHON_VERSION=3")
        else:
            cmake_args.append("-DVTK_WRAP_PYTHON=OFF")

        if "darwin" in spec.architecture:
            cmake_args.extend(["-DCMAKE_MACOSX_RPATH=ON"])

        if "+qt" in spec:
            qt_ver = spec["qt"].version.up_to(1)
            qt_bin = spec["qt"].prefix.bin
            qmake_exe = os.path.join(qt_bin, "qmake")

            # https://github.com/martijnkoopman/Qt-VTK-viewer/blob/master/doc/Build-VTK.md
            # The content of the above link changes over time with versions.
            # Older commits have information on VTK-8.
            if spec.satisfies("@:8"):
                cmake_args.extend(
                    [
                        f"-DVTK_QT_VERSION:STRING={qt_ver}",
                        f"-DQT_QMAKE_EXECUTABLE:PATH={qmake_exe}",
                        "-DVTK_Group_Qt:BOOL=ON",
                    ]
                )
            else:
                cmake_args.extend(
                    [
                        "-DVTK_GROUP_ENABLE_Qt:STRING=YES",
                        "-DVTK_MODULE_ENABLE_VTK_GUISupportQt:STRING=YES",
                    ]
                )

            # NOTE: The following definitions are required in order to allow
            # VTK to build with qt~webkit versions (see the documentation for
            # more info: http://www.vtk.org/Wiki/VTK/Tutorials/QtSetup).
            if "~webkit" in spec["qt"]:
                if spec.satisfies("@:8"):
                    cmake_args.extend(
                        [
                            "-DVTK_Group_Qt:BOOL=OFF",
                            "-DModule_vtkGUISupportQt:BOOL=ON",
                            "-DModule_vtkGUISupportQtOpenGL:BOOL=ON",
                        ]
                    )
                else:
                    cmake_args.extend(
                        [
                            "-DVTK_GROUP_ENABLE_Qt:STRING=NO",
                            "-DVTK_MODULE_ENABLE_VTK_GUISupportQt:STRING=YES",
                        ]
                    )

        if spec.satisfies("io=xdmf"):
            if spec.satisfies("^cmake@3.12:"):
                # This policy exists only for CMake >= 3.12
                cmake_args.extend(["-DCMAKE_POLICY_DEFAULT_CMP0074=NEW"])

            if spec.satisfies("@:8"):
                cmake_args.extend(
                    [
                        # Enable XDMF Support here
                        "-DModule_vtkIOXdmf2:BOOL=ON",
                        "-DModule_vtkIOXdmf3:BOOL=ON",
                        f"-DBOOST_ROOT={spec['boost'].prefix}",
                        f"-DBOOST_LIBRARY_DIR={spec['boost'].prefix.lib}",
                        f"-DBOOST_INCLUDE_DIR={spec['boost'].prefix.include}",
                        "-DBOOST_NO_SYSTEM_PATHS:BOOL=ON",
                        # This is needed because VTK has multiple FindBoost
                        # and they stick to system boost if there's a system boost
                        # installed with CMake
                        "-DBoost_NO_BOOST_CMAKE:BOOL=ON",
                        # The xdmf project does not export any CMake file...
                        "-DVTK_USE_SYSTEM_XDMF3:BOOL=OFF",
                        "-DVTK_USE_SYSTEM_XDMF2:BOOL=OFF",
                    ]
                )
            else:
                cmake_args.extend(
                    [
                        "-DVTK_MODULE_ENABLE_VTK_xdmf2:STRING=YES",
                        "-DVTK_MODULE_ENABLE_VTK_xdmf3:STRING=YES",
                        "-DVTK_MODULE_ENABLE_VTK_IOXdmf2:STRING=YES",
                        "-DVTK_MODULE_ENABLE_VTK_IOXdmf3:STRING=YES",
                    ]
                )

            if "+mpi" in spec:
                if spec.satisfies("@:8"):
                    cmake_args.append("-DModule_vtkIOParallelXdmf3:BOOL=ON")
                else:
                    cmake_args.append("-DVTK_MODULE_ENABLE_VTK_IOParallelXdmf3:STRING=YES")

        if spec.satisfies("@:9.4"):
            opengl_ver = "OpenGL2" if "+opengl2" in spec else "OpenGL"
            cmake_args.append(self.define("VTK_RENDERING_BACKEND", opengl_ver))

        if spec.satisfies("^[virtuals=gl] osmesa"):
            cmake_args.extend(
                [
                    "-DVTK_USE_X:BOOL=OFF",
                    "-DVTK_USE_COCOA:BOOL=OFF",
                    "-DVTK_OPENGL_HAS_OSMESA:BOOL=ON",
                ]
            )

        else:
            cmake_args.append("-DVTK_OPENGL_HAS_OSMESA:BOOL=OFF")
            if spec.satisfies("@:7.9.9"):
                # This option is gone in VTK 8.1.2
                cmake_args.append("-DOpenGL_GL_PREFERENCE:STRING=LEGACY")

            if "platform=darwin" in spec:
                cmake_args.extend(["-DVTK_USE_X:BOOL=OFF", "-DVTK_USE_COCOA:BOOL=ON"])

            elif "platform=linux" in spec:
                cmake_args.extend(["-DVTK_USE_X:BOOL=ON", "-DVTK_USE_COCOA:BOOL=OFF"])

        compile_flags = []

        if spec.satisfies("@:6.1.0"):
            compile_flags.append("-DGLX_GLXEXT_LEGACY")

            # VTK 6.1.0 (and possibly earlier) does not use
            # NETCDF_CXX_ROOT to detect NetCDF C++ bindings, so
            # NETCDF_CXX_INCLUDE_DIR and NETCDF_CXX_LIBRARY must be
            # used instead to detect these bindings
            if spec.satisfies("io=netcdf"):
                netcdf_cxx_lib = spec["netcdf-cxx"].libs.joined()
                cmake_args.extend(
                    [
                        f"NETCDF_CXX_INCLUDE_DIR={spec['netcdf-cxx'].prefix.include}",
                        f"NETCDF_CXX_LIBRARY={netcdf_cxx_lib}",
                    ]
                )

            # Garbage collection is unsupported in Xcode starting with
            # version 5.1; if the Apple clang version of the compiler
            # is 5.1.0 or later, unset the required Objective-C flags
            # to remove the garbage collection flags.  Versions of VTK
            # after 6.1.0 set VTK_REQUIRED_OBJCXX_FLAGS to the empty
            # string. This fix was recommended on the VTK mailing list
            # in March 2014 (see
            # https://public.kitware.com/pipermail/vtkusers/2014-March/083368.html)
            if self.spec.satisfies("%apple-clang@5.1.0:"):
                cmake_args.extend(["-DVTK_REQUIRED_OBJCXX_FLAGS="])

            # A bug in tao pegtl causes build failures with intel compilers
            if "%intel" in spec and spec.version >= Version("8.2"):
                cmake_args.append("-DVTK_MODULE_ENABLE_VTK_IOMotionFX:BOOL=OFF")

        cmake_args.append(self.define_from_variant("VTK_VERSIONED_INSTALL", "versioned_install"))

        # -no-ipo prevents an internal compiler error from multi-file
        # optimization (https://github.com/spack/spack/issues/20471)
        if "%intel" in spec:
            compile_flags.append("-no-ipo")

        if compile_flags:
            compile_flags = " ".join(compile_flags)
            cmake_args.extend(
                [f"-DCMAKE_C_FLAGS={compile_flags}", f"-DCMAKE_CXX_FLAGS={compile_flags}"]
            )
        if spec.satisfies("@:8"):
            vtk_example_arg = "BUILD_EXAMPLES"
        else:
            vtk_example_arg = "VTK_BUILD_EXAMPLES"
        cmake_args.append(self.define_from_variant(f"{vtk_example_arg}", "examples"))

        cmake_args.append(self.define_from_variant("VTK_DEBUG_LEAKS", "advanced_debug"))

        return cmake_args

    @when("+examples")
    def install(self, spec, prefix):
        super().install(spec, prefix)
        with working_dir(self.build_directory):
            examples = glob.glob("bin\\*.exe")
            for example in examples:
                install(example, prefix.bin)
