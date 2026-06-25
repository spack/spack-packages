# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import itertools
import os
import re
import sys
from subprocess import Popen

from spack_repo.builtin.build_systems.cmake import CMakePackage, generator
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *

IS_WINDOWS = sys.platform == "win32"


# This is (more or less) the mapping hard-coded in VTK-m logic
# see https://gitlab.kitware.com/vtk/vtk-m/-/blob/v2.1.0/CMake/VTKmDeviceAdapters.cmake?ref_type=tags#L221-247
supported_cuda_archs = {
    "20": "fermi",
    "21": "fermi",
    "30": "kepler",
    "32": "kepler",
    "35": "kepler",
    "37": "kepler",
    "50": "maxwel",
    "52": "maxwel",
    "53": "maxwel",
    "60": "pascal",
    "61": "pascal",
    "62": "pascal",
    "70": "volta",
    "72": "volta",
    "75": "turing",
    "80": "ampere",
    "86": "ampere",
}


# This is a list of paraview variants that require the viskores library.
viskores_dependency_variants = ["+cuda", "+fides", "+rocm"]


class Paraview(CMakePackage, CudaPackage, ROCmPackage):
    """ParaView is an open-source, multi-platform data analysis and
    visualization application. This package includes the Catalyst
    in-situ library for versions 5.7 and greater, otherwise use the
    catalyst package.

    """

    homepage = "https://www.paraview.org"
    url = "https://www.paraview.org/files/v5.7/ParaView-v5.7.0.tar.xz"
    list_url = "https://www.paraview.org/files"
    list_depth = 1
    git = "https://gitlab.kitware.com/paraview/paraview.git"

    maintainers("danlipsa", "vicentebolea", "kwryankrattiger")
    tags = ["e4s"]

    license("Apache-2.0")

    version("master", branch="master", submodules=True)
    version("6.1.1", sha256="43671df11e1629cf9079815bfdfa9f22063a90cd1baed694072f80622f5ad92f")
    version("6.1.0", sha256="4e9d882874b2a161f3338a6644a5d8bc63748f0d7846f4690701b86a8a821dfc")
    version("6.0.1", sha256="5e56ac7af5e925b3cfd3fab82470933cbabc7e8fda87e14af64f995d6064eb06")
    version("5.13.3", sha256="3bd31bb56e07aa2af2a379895745bbc430c565518a363d935f2efc35b076df09")
    version("5.12.1", sha256="927f880c13deb6dde4172f4727d2b66f5576e15237b35778344f5dd1ddec863e")
    version("5.11.2", sha256="5c5d2f922f30d91feefc43b4a729015dbb1459f54c938896c123d2ac289c7a1e")

    with default_args(deprecated=True):
        version("6.0.0", sha256="0ee07ae6377e5e97766aebf858eb9758668a52df041f319e7c975037a63bf189")
        version(
            "5.13.2", sha256="4e116250f8e1a9c480f97c5696c9cd72b4d4998b039ca46da8b224f27445f13e"
        )
        version(
            "5.13.1", sha256="a16503ce37b999c2967d84234596e7bf67ac98221851a288bb1399c7e1dc2004"
        )
        version(
            "5.13.0", sha256="886f530bebd6b24c6a7f8a5f4b1afa72c53d4737ccaa4b5fd5946b4e5a758c91"
        )
        version(
            "5.12.0", sha256="d289afe7b48533e2ca4a39a3b48d3874bfe67cf7f37fdd2131271c57e64de20d"
        )
        version(
            "5.11.1", sha256="5cc2209f7fa37cd3155d199ff6c3590620c12ca4da732ef7698dec37fa8dbb34"
        )
        version(
            "5.11.0", sha256="9a0b8fe8b1a2cdfd0ace9a87fa87e0ec21ee0f6f0bcb1fdde050f4f585a25165"
        )

    variant(
        "development_files",
        default=True,
        description="Install include files for Catalyst or plugins support",
    )
    variant("python", default=False, description="Enable Python support")
    variant("fortran", default=False, description="Enable Fortran support")
    variant("mpi", default=True, description="Enable MPI support")
    variant("qt", default=False, description="Enable Qt (gui) support")
    variant("opengl2", default=True, description="Enable OpenGL2 backend", when="@5")
    variant("osmesa_fallback", default=False, description="Enable OpenGL2 backend", when="@6:")
    variant("x", default=True, description="Enable X11 support")
    variant("examples", default=False, description="Build examples")
    variant("hdf5", default=False, description="Use external HDF5")
    variant("shared", default=True, description="Builds a shared version of the library")
    variant("kits", default=True, description="Use module kits")
    variant("pagosa", default=False, description="Build the pagosa adaptor")
    variant("eyedomelighting", default=False, description="Enable Eye Dome Lighting feature")
    variant("nvindex", default=False, description="Enable the pvNVIDIAIndeX plugin")
    variant("tbb", default=False, description="Enable multi-threaded parallelism with TBB")
    variant("adios2", default=False, description="Enable ADIOS2 support")
    variant("fides", default=False, description="Enable Fides support")
    variant("visitbridge", default=False, description="Enable VisItBridge support")
    variant("raytracing", default=False, description="Enable Raytracing support")
    variant("cdi", default=False, description="Enable CDI support")
    variant(
        "openpmd",
        default=False,
        description="Enable openPMD support (w/ ADIOS2/HDF5)",
        when="@5.9: +python",
    )
    variant("catalyst", default=False, description="Enable Catalyst 1")
    variant(
        "libcatalyst",
        default=False,
        description="Enable Catalyst 2 (libcatalyst) implementation",
    )

    variant(
        "advanced_debug",
        default=False,
        description="Enable all other debug flags beside build_type, such as VTK_DEBUG_LEAK",
    )
    variant(
        "build_edition",
        default="canonical",
        multi=False,
        values=("canonical", "catalyst_rendering", "catalyst", "rendering", "core"),
        description="Build editions include only certain modules. "
        "Editions are listed in decreasing order of size.",
    )
    variant(
        "use_vtkm",
        default="default",
        when="@5",
        multi=False,
        values=("default", "on", "off"),
        description="Build VTK-m with ParaView."
        ' "default" lets the build_edition make the decision.'
        ' "on" or "off" will always override the build_edition.',
    )

    conflicts("~hdf5", when="+visitbridge")
    conflicts("+fides", when="~adios2", msg="Fides needs ADIOS2")
    conflicts("+fides", when="@5 use_vtkm=off", msg="Fides needs VTK-m")
    conflicts("+fides", when="@5 use_vtkm=default", msg="Fides needs VTK-m")
    conflicts("+openpmd", when="~adios2 ~hdf5", msg="openPMD needs ADIOS2 and/or HDF5")
    conflicts("~shared", when="+cuda")
    conflicts("+cuda", when="use_vtkm=off")
    conflicts("+rocm", when="+cuda")
    conflicts("+rocm", when="use_vtkm=off")
    # Legacy rendering dropped in 5.5
    # See commit: https://gitlab.kitware.com/paraview/paraview/-/commit/798d328c
    conflicts("~opengl2", when="@5")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    depends_on("cmake@3.3:", type="build")
    depends_on("cmake@3.21:", type="build", when="+rocm")

    extends("python", when="+python")

    depends_on("python@3:", when="+python", type=("build", "run"))

    depends_on("py-numpy", when="+python", type=("build", "run"))
    depends_on("py-mpi4py", when="+python+mpi", type=("build", "run"))

    depends_on("py-matplotlib", when="+python", type="run")
    depends_on("py-pandas@0.21:", when="+python", type="run")

    # openPMD is implemented as a Python module and provides ADIOS2 and HDF5 backends
    depends_on("openpmd-api@0.14.5: +python", when="+python +openpmd", type=("build", "run"))
    depends_on("openpmd-api +adios2", when="+openpmd +adios2", type=("build", "run"))
    depends_on("openpmd-api +hdf5", when="+openpmd +hdf5", type=("build", "run"))

    depends_on("tbb", when="+tbb")

    depends_on("mpi", when="+mpi")
    conflicts("mpi", when="~mpi")

    # Handle X11 dependencies
    # X is only used on Unix like platforms
    conflicts("glx", when="~x")
    # When on linux, X is required for Qt
    for plat in ["linux", "freebsd"]:
        with when(f"platform={plat}"):
            requires("+x", when="+qt", msg="Qt support requires GLX on Linux/FreeBSD")

    with when("+x"):
        depends_on("libxt", when="@:5.12")
        depends_on("libx11")
        depends_on("libxcursor")
        # When Qt and X are enabled, GLX is required in the runtime
        requires("^[virtuals=gl] glx", when="@5")
        depends_on("glx", when="@6:", type=("run"))

    # ParaView@5 support Qt5 and requires a GL provider to be known at
    # build/link time.
    with when("@5"):
        with when("+qt"):
            # https://discourse.paraview.org/t/paraview-5-9-and-minimum-recommended-qt-version/5333
            depends_on("qt@5.12:5", when="@5")
            depends_on("qt+sql")
            depends_on("qt+opengl", when="@5 +opengl2")
            depends_on("qt~opengl", when="@5 ~opengl2")
            # Headless rendering not supported with Qt
            conflicts("osmesa")
            conflicts("egl")

        depends_on("gl@3.2:", when="+opengl2")
        depends_on("gl@1.2:", when="~opengl2")
        depends_on("glew")

        # CUDA ARCH

        # VTK-m and transitively ParaView does not support Tesla Arch
        for _arch in ("10", "11", "12", "13"):
            conflicts(f"cuda_arch={_arch}", when="+cuda", msg="ParaView requires cuda_arch >= 20")

        # Starting from cmake@3.18, CUDA architecture managament can be delegated to CMake.
        # Hence, it is possible to rely on it instead of relying on custom logic updates from
        # VTK-m for newer architectures (wrt mapping).
        pattern = re.compile(r"\d+")
        for _arch in CudaPackage.cuda_arch_values:
            _number = re.match(pattern, _arch).group()
            if int(_number) > 86:
                conflicts("cmake@:3.17", when=f"cuda_arch={_arch}")

        # We only support one single Architecture
        for _arch, _other_arch in itertools.permutations(CudaPackage.cuda_arch_values, 2):
            conflicts(
                "cuda_arch={0}".format(_arch),
                when="cuda_arch={0}".format(_other_arch),
                msg="Paraview only accepts one architecture value",
            )

        # Dependencies for vendored VTK-m
        depends_on("hip@5.2:", when="+rocm")
        # CUDA thrust is already include in the CUDA pkg
        depends_on("rocthrust", when="@5.13: +rocm ^cmake@3.24:")
        for target in ROCmPackage.amdgpu_targets:
            depends_on(
                "kokkos@:3.7 +rocm amdgpu_target={0}".format(target),
                when="+rocm amdgpu_target={0}".format(target),
            )

    with when("@6:"):
        # ParaView 6 and later will not support Spack builds with Qt5.
        with when("+qt"):
            depends_on("qt-base@6.9.0 +accessibility+gui+opengl+sql+network")
            depends_on("qt-tools+assistant")
            depends_on("qt-5compat")
            depends_on("qt-svg")
            depends_on("libxslt")

        depends_on("scnlib")

        # ParaView@6: and later will depend on OSMesa as a fallback for
        # OpenGL.
        # The search order for GL is:
        # * the system rendering default (WGL/AGL/GLX)
        # * EGL
        # * OSMesa (guarenteed to exist and work on all systems)
        depends_on("osmesa", type=("link", "run"), when="+osmesa_fallback")

        # Depend on Viskores when it is needed
        for vk_variant in viskores_dependency_variants:
            depends_on("viskores +vtktypes +64bitids +doubleprecision", when=f"{vk_variant}")
            depends_on("viskores +fpic", when=f"+shared {vk_variant}")

        with when("+fides"):
            depends_on("fides@1.3:")
            depends_on("fides +mpi", when="+mpi")

        with when("+cuda"):
            # Kokkos vs Viskores Native CUDA is intentionally left configurable
            depends_on("viskores +cuda")
            for _arch in CudaPackage.cuda_arch_values:
                depends_on(f"viskores cuda_arch={_arch}", when=f"cuda_arch={_arch}")

        with when("+rocm"):
            depends_on("viskores +rocm")
            for target in ROCmPackage.amdgpu_targets:
                depends_on(f"viskores amdgpu_target={target}", when=f"amdgpu_target={target}")

    depends_on("ospray@2.1:2", when="+raytracing")
    depends_on("openimagedenoise", when="+raytracing")
    depends_on("ospray +mpi", when="+raytracing +mpi")

    depends_on("cdi", when="+cdi")

    depends_on("bzip2")
    depends_on("double-conversion")
    depends_on("expat")
    depends_on("eigen@3")
    depends_on("freetype")
    depends_on("hdf5+hl+mpi", when="+hdf5+mpi")
    depends_on("hdf5+hl~mpi", when="+hdf5~mpi")
    depends_on("hdf5@1.10:", when="+hdf5")
    depends_on("adios2+mpi", when="+adios2+mpi")
    depends_on("adios2~mpi", when="+adios2~mpi")
    depends_on("silo", when="+visitbridge")
    depends_on("silo+mpi", when="+visitbridge+mpi")
    depends_on("silo~mpi", when="+visitbridge~mpi")
    depends_on("boost", when="+visitbridge")
    depends_on("jpeg")
    depends_on("jsoncpp")
    depends_on("libogg")
    depends_on("libpng")
    depends_on("libtheora")
    depends_on("libtiff")
    depends_on("netcdf-c")
    depends_on("netcdf-c+parallel-netcdf", when="+mpi platform=darwin")
    depends_on("netcdf-c+parallel-netcdf", when="+mpi platform=freebsd")
    depends_on("netcdf-c+parallel-netcdf", when="+mpi platform=linux")
    depends_on("netcdf-c@:4.9.2", when="@5")
    depends_on("pegtl@2.8.3")
    depends_on("protobuf@3.4:")
    # protobuf requires newer abseil-cpp, which in turn requires C++14,
    # but paraview uses C++11 by default. Use until ParaView updates
    # its C++ standard level.
    depends_on("protobuf@3.4:21", when="%gcc")
    depends_on("protobuf@3.4:21", when="%clang")
    depends_on("protobuf@3.4:21", when="@5.11:")
    depends_on("protobuf@3.4:21", when="@master")
    depends_on("libxml2")
    depends_on("lz4")
    depends_on("xz")
    depends_on("zlib-api")
    depends_on("libcatalyst@2:", when="+libcatalyst")

    # Older builds of pugi export their symbols differently,
    # and pre-5.9 is unable to handle that.
    depends_on("pugixml")
    # 5.13 uses 'remove_children': https://github.com/spack/spack/issues/47098
    depends_on("pugixml@1.11:", when="@5.13:")

    # ParaView depends on cli11 due to changes in MR
    # https://gitlab.kitware.com/paraview/paraview/-/merge_requests/4951
    depends_on("cli11@1.9.1")

    # ParaView depends on nlohmann-json due to changes in MR
    # https://gitlab.kitware.com/vtk/vtk/-/merge_requests/8550
    depends_on("nlohmann-json", when="@5.11:")

    # ParaView depends on proj@8.1.0 due to changes in MR
    # v8.1.0 is required for VTK::GeoVis
    # https://gitlab.kitware.com/vtk/vtk/-/merge_requests/8474
    depends_on("proj@8.1.0", when="@5.11:")

    # Patches to vendored VTK-m are needed for forward compat with CUDA 12 (mr 2972 and 3259)
    depends_on("cuda@:11", when="@5:5.12 +cuda")

    # Fix IOADIOS2 module to work with kits
    # https://gitlab.kitware.com/vtk/vtk/-/merge_requests/8653
    patch("vtk-adios2-module-no-kit.patch", when="@5:5.11")

    # Patch for paraview 5.8: ^hdf5@1.13.2:
    # Even with ~hdf5, hdf5 is part of the dependency tree due to netcdf-c
    # https://gitlab.kitware.com/vtk/vtk/-/merge_requests/9690
    patch("vtk-xdmf2-hdf51.13.2.patch", when="@5.11.0")
    # a patch with the same name is also applied to vtk
    # the two patches are the same but for the path to the files they patch
    patch("vtk_alias_hdf5.patch")

    # Fix VTK to work with external freetype using CONFIG mode for find_package
    patch("FindFreetype.cmake.patch")

    # Fix VTK to remove deprecated ADIOS2 functions
    # https://gitlab.kitware.com/vtk/vtk/-/merge_requests/10113
    patch("adios2-remove-deprecated-functions.patch", when="@5.11 ^adios2@2.9:")

    patch("kits_with_catalyst_5_12.patch", when="@5.12.0")

    # https://github.com/Kitware/VTK-m/commit/c805a6039ea500cb96158cfc11271987c9f67aa4
    patch("vtkm-remove-unused-method-from-mir-tables.patch", when="@5.13.2 %oneapi@2025:")

    # https://github.com/Kitware/VTK-m/commit/48e385af319543800398656645327243a29babfb
    patch("vtkm-fix-problems-in-class-member-names.patch", when="@5.13.2 %oneapi@2025:")

    # Vtk's findpegtl's include search is wrong: https://gitlab.kitware.com/vtk/vtk/-/issues/17876
    patch("pegtl_tao_find.patch", when="platform=windows")

    # https://gitlab.kitware.com/paraview/paraview/-/merge_requests/7593
    patch("paraview-cdireader-lazy.patch", when="@:6.0 +cdi")

    # Fix for linking external Fides library
    # https://gitlab.kitware.com/vtk/vtk/-/merge_requests/13130
    patch("vtk-external-fides-pv61.patch", working_dir="VTK", when="@6.0:6.1")

    # Fixes for linking external Viskores library
    # https://gitlab.kitware.com/vtk/vtk/-/merge_requests/13094
    # https://gitlab.kitware.com/vtk/vtk/-/merge_requests/13127
    patch("vtk-fine-grained-viskores-targets-pv61.patch", working_dir="VTK", when="@6.0:6.1")
    patch("vtk-consolidate-viskores-wrapping-pv60.patch", working_dir="VTK", when="@6.0")
    patch("vtk-consolidate-viskores-wrapping-pv61.patch", working_dir="VTK", when="@6.1")

    generator("ninja", "make", default="ninja")
    # https://gitlab.kitware.com/paraview/paraview/-/issues/21223
    conflicts("generator=ninja", when="%xl")
    conflicts("generator=ninja", when="%xl_r")

    # Versions 5.13.0-5.13.2 do not compile with Intel classic compilers
    conflicts("%intel", when="@5.13:5.13.2")

    def url_for_version(self, version):
        _urlfmt = "http://www.paraview.org/files/v{0}/ParaView-v{1}{2}.tar.{3}"
        # Handle ParaView version-based custom URLs
        return _urlfmt.format(version.up_to(2), version, "", "xz")

    @property
    def paraview_subdir(self):
        """The paraview subdirectory name as paraview-major.minor"""
        if self.spec.version == Version("master"):
            return "paraview-5.11"
        else:
            return "paraview-{0}".format(self.spec.version.up_to(2))

    def setup_dependent_build_environment(
        self, env: EnvironmentModifications, dependent_spec: Spec
    ) -> None:
        if os.path.isdir(self.prefix.lib64):
            lib_dir = self.prefix.lib64
        else:
            lib_dir = self.prefix.lib
        env.set("ParaView_DIR", self.prefix)

        env.set("PARAVIEW_VTK_DIR", join_path(lib_dir, "cmake", self.paraview_subdir, "vtk"))

    def flag_handler(self, name, flags):
        if name == "ldflags" and self.spec.satisfies("%intel"):
            flags.append("-shared-intel")
            return (None, flags, None)
        # -no-ipo prevents internal compiler error from multi-file
        # optimization (https://github.com/spack/spack/issues/18192)
        if (name == "cflags" or name == "cxxflags") and self.spec.satisfies("%intel"):
            flags.append("-no-ipo")
            return (None, None, flags)

        if name in ("cflags", "cxxflags"):
            # Constrain the HDF5 API
            if self.spec["hdf5"].satisfies("@1.12:"):
                flags.append("-DH5_USE_110_API")

            if self.spec.satisfies("%oneapi@2025:"):
                flags.append("-Wno-error=missing-template-arg-list-after-template-kw")
                flags.append("-Wno-missing-template-arg-list-after-template-kw")

        return flags, None, None

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        # paraview 5.5 and later
        # - cmake under lib/cmake/paraview-5.5
        # - libs  under lib
        # - python bits under lib/python2.8/site-packages
        if os.path.isdir(self.prefix.lib64):
            lib_dir = self.prefix.lib64
        else:
            lib_dir = self.prefix.lib

        env.set("ParaView_DIR", self.prefix)

        env.set("PARAVIEW_VTK_DIR", join_path(lib_dir, "cmake", self.paraview_subdir, "vtk"))

        env.prepend_path("LIBRARY_PATH", lib_dir)
        env.prepend_path("LD_LIBRARY_PATH", lib_dir)

        if "+python" in self.spec:
            python_version = self.spec["python"].version.up_to(2)
            pv_pydir = join_path(lib_dir, "python{0}".format(python_version), "site-packages")
            if "+shared" in self.spec:
                env.prepend_path("PYTHONPATH", pv_pydir)
                # The Trilinos Catalyst adapter requires
                # the vtkmodules directory in PYTHONPATH
                env.prepend_path("PYTHONPATH", join_path(pv_pydir, "vtkmodules"))
            else:
                env.prepend_path("PYTHONPATH", join_path(pv_pydir, "_paraview.zip"))
                env.prepend_path("PYTHONPATH", join_path(pv_pydir, "_vtk.zip"))

    def cmake_args(self):
        """Populate cmake arguments for ParaView."""
        spec = self.spec

        build_edition = spec.variants["build_edition"].value.upper()

        cmake_args = [
            "-DBUILD_TESTING:BOOL=OFF",
            "-DOpenGL_GL_PREFERENCE:STRING=LEGACY",
            "-DVTK_MODULE_USE_EXTERNAL_ParaView_vtkcatalyst:BOOL=OFF",
            "-DVTK_MODULE_USE_EXTERNAL_VTK_ioss:BOOL=OFF",
            "-DVTK_MODULE_USE_EXTERNAL_VTK_exprtk:BOOL=OFF",
            "-DVTK_MODULE_USE_EXTERNAL_VTK_fmt:BOOL=OFF",
            "-DVTK_MODULE_USE_EXTERNAL_ParaView_cgns:BOOL=OFF",
            "-DVTK_MODULE_USE_EXTERNAL_VTK_gl2ps:BOOL=OFF",
            "-DVTK_MODULE_USE_EXTERNAL_VTK_libharu:BOOL=OFF",
            "-DVTK_MODULE_USE_EXTERNAL_VTK_utf8:BOOL=OFF",
            "-DPARAVIEW_BUILD_WITH_EXTERNAL=ON",
            f"-DPARAVIEW_BUILD_EDITION:STRING={build_edition}",
            self.define_from_variant("PARAVIEW_INSTALL_DEVELOPMENT_FILES", "development_files"),
            self.define_from_variant("VTK_USE_X", "x"),
            self.define_from_variant("PARAVIEW_ENABLE_VISITBRIDGE", "visitbridge"),
            self.define_from_variant("VISIT_BUILD_READER_Silo", "visitbridge"),
            self.define_from_variant("PARAVIEW_BUILD_WITH_KITS", "kits"),
            self.define_from_variant("PARAVIEW_BUILD_PAGOSA_ADAPTOR", "pagosa"),
            self.define_from_variant("PARAVIEW_BUILD_PLUGIN_EyeDomeLighting", "eyedomelighting"),
            self.define_from_variant("PARAVIEW_PLUGIN_ENABLE_pvNVIDIAIndeX", "nvindex"),
            self.define_from_variant("PARAVIEW_USE_QT", "qt"),
            self.define_from_variant("PARAVIEW_ENABLE_EXAMPLES", "examples"),
            self.define_from_variant("PARAVIEW_ENABLE_ADIOS2", "adios2"),
            self.define_from_variant("PARAVIEW_ENABLE_FIDES", "fides"),
            self.define_from_variant("PARAVIEW_USE_FORTRAN", "fortran"),
            self.define_from_variant("PARAVIEW_USE_CUDA", "cuda"),
            self.define_from_variant("PARAVIEW_USE_MPI", "mpi"),
            self.define_from_variant("PARAVIEW_BUILD_SHARED_LIBS", "shared"),
            self.define_from_variant("PARAVIEW_ENABLE_RAYTRACING", "raytracing"),
            # Currently only support OSPRay ray tracing
            self.define_from_variant("VTK_ENABLE_OSPRAY", "raytracing"),
            self.define_from_variant("VTKOSPRAY_ENABLE_DENOISER", "raytracing"),
            # CDI
            self.define_from_variant("PARAVIEW_PLUGIN_ENABLE_CDIReader", "cdi"),
            self.define_from_variant("PARAVIEW_PLUGIN_AUTOLOAD_CDIReader", "cdi"),
        ]

        # Configure OSMesa
        if spec.satisfies("@5"):
            if spec.satisfies("^[virtuals=gl] osmesa"):
                cmake_args.append("-DVTK_OPENGL_HAS_OSMESA:BOOL=ON")
            else:
                cmake_args.append("-DVTK_OPENGL_HAS_OSMESA:BOOL=OFF")
        else:
            cmake_args.append(self.define_from_variant("VTK_OPENGL_HAS_OSMESA", "osmesa_fallback"))

        # Configure EGL
        if spec.satisfies("^[virtuals=gl] egl"):
            cmake_args.append("-DVTK_OPENGL_HAS_EGL:BOOL=ON")

        # Disable patched externals
        if spec.satisfies("@5.12:"):
            cmake_args.append("-DVTK_MODULE_USE_EXTERNAL_VTK_fast_float:BOOL=OFF")
            cmake_args.append("-DVTK_MODULE_USE_EXTERNAL_VTK_token:BOOL=OFF")

        if spec.satisfies("@5.11:"):
            cmake_args.append("-DVTK_MODULE_USE_EXTERNAL_VTK_verdict:BOOL=OFF")

        if spec.satisfies("%cce"):
            cmake_args.append("-DVTK_PYTHON_OPTIONAL_LINK:BOOL=OFF")

        # The assumed qt version changed to QT5 (as of paraview 5.2.1),
        # so explicitly specify which QT major version is actually being used
        if spec.satisfies("+qt"):
            if spec.satisfies("^qt"):
                cmake_args.extend(["-DPARAVIEW_QT_VERSION=%s" % spec["qt"].version[0]])
            else:
                cmake_args.extend(["-DPARAVIEW_QT_VERSION=%s" % spec["qt-base"].version[0]])
                cmake_args.extend(["-DVTK_QT_VERSION=%s" % spec["qt-base"].version[0]])

            if IS_WINDOWS:
                # Windows does not currently support Qt Quick
                cmake_args.append("-DVTK_MODULE_ENABLE_VTK_GUISupportQtQuick:STRING=NO")

        # CMake flags for python have changed with newer ParaView versions
        # Make sure Spack uses the right cmake flags
        if "+python" in spec:
            cmake_args.extend(
                [
                    "-DPARAVIEW_USE_PYTHON:BOOL=ON",
                    "-DPARAVIEW_PYTHON_VERSION:STRING=3",
                ]
            )
        else:
            cmake_args.append("-DPARAVIEW_ENABLE_PYTHON:BOOL=OFF")

        if "+mpi" in spec:
            mpi_args = ["-DMPIEXEC:FILEPATH=%s/bin/mpiexec" % spec["mpi"].prefix]
            if not sys.platform == "win32":
                mpi_args.extend(
                    [
                        "-DMPI_CXX_COMPILER:PATH=%s" % spec["mpi"].mpicxx,
                        "-DMPI_C_COMPILER:PATH=%s" % spec["mpi"].mpicc,
                        "-DMPI_Fortran_COMPILER:PATH=%s" % spec["mpi"].mpifc,
                    ]
                )
            cmake_args.extend(mpi_args)

        # VTK-m used in ParaView in 5.x
        if spec.satisfies("@5") and spec.variants["use_vtkm"].value != "default":
            cmake_args.append(
                "-DPARAVIEW_USE_VTKM:BOOL=%s" % spec.variants["use_vtkm"].value.upper()
            )

        # Viskores added to ParaView in 6.0.0 and up
        if spec.satisfies("@6:"):
            use_viskores = False
            for variant in viskores_dependency_variants:
                use_viskores |= spec.satisfies(variant)
            if use_viskores:
                cmake_args.append("-DPARAVIEW_USE_VISKORES:BOOL=ON")
                cmake_args.append("-DVTK_MODULE_USE_EXTERNAL_VTK_vtkviskores:BOOL=ON")
            else:
                cmake_args.append("-DPARAVIEW_USE_VISKORES:BOOL=OFF")

        # VTK-m expects cuda_arch to be the arch name vs. the arch version.
        if spec.satisfies("@5 +cuda"):
            if spec["cmake"].satisfies("@3.18:"):
                cmake_args.append(
                    self.define(
                        "CMAKE_CUDA_ARCHITECTURES", ";".join(spec.variants["cuda_arch"].value)
                    )
                )
            else:
                # ParaView/VTK-m only accepts one arch, default to first element
                requested_arch = spec.variants["cuda_arch"].value[0]

                if requested_arch == "none":
                    cuda_arch_value = "native"
                else:
                    try:
                        cuda_arch_value = supported_cuda_archs[requested_arch]
                    except KeyError:
                        raise InstallError("Incompatible cuda_arch=" + requested_arch)

                cmake_args.append(self.define("VTKm_CUDA_Architecture", cuda_arch_value))

        if "darwin" in spec.architecture:
            cmake_args.extend(
                ["-DVTK_USE_X:BOOL=OFF", "-DPARAVIEW_DO_UNIX_STYLE_INSTALLS:BOOL=ON"]
            )

        if "+tbb" in spec:
            cmake_args.append("-DVTK_SMP_IMPLEMENTATION_TYPE=TBB")

        # A bug that has been found in vtk causes an error for
        # intel builds for version 5.6.  This should be revisited
        # with later versions of Paraview to see if the issues still
        # arises.
        if "%intel" in spec and spec.version >= Version("5.6"):
            cmake_args.append("-DPARAVIEW_ENABLE_MOTIONFX:BOOL=OFF")

        # Encourage Paraview to use the correct Python libs
        if spec.satisfies("+python"):
            pylibdirs = spec["python"].libs.directories
            cmake_args.append("-DCMAKE_INSTALL_RPATH={0}".format(":".join(self.rpath + pylibdirs)))

        if "+advanced_debug" in spec:
            cmake_args.append("-DVTK_DEBUG_LEAKS:BOOL=ON")

        # Configure ROCM/Kokkos
        if spec.satisfies("@5.11:5"):
            cmake_args.append(self.define_from_variant("PARAVIEW_USE_HIP", "rocm"))
        elif spec.satisfies("@6:"):
            cmake_args.append(self.define_from_variant("PARAVIEW_USE_KOKKOS", "rocm"))

        if "+rocm" in spec:
            if spec.satisfies("@6:"):
                cmake_args.append("-DPARAVIEW_KOKKOS_BACKEND:STRING=HIP")

            archs = spec.variants["amdgpu_target"].value

            if archs != "none":
                arch_str = ",".join(archs)
                cmake_args.append("-DCMAKE_HIP_ARCHITECTURES=%s" % arch_str)
            cmake_args.append("-DKokkos_CXX_COMPILER=%s" % spec["hip"].hipcc)

        if "+catalyst" in spec:
            cmake_args.append("-DVTK_MODULE_ENABLE_ParaView_Catalyst=YES")
            if "+python" in spec:
                cmake_args.append("-DVTK_MODULE_ENABLE_ParaView_PythonCatalyst=YES")

        if "+libcatalyst" in spec:
            cmake_args.append("-DVTK_MODULE_ENABLE_ParaView_InSitu=YES")
            cmake_args.append("-DPARAVIEW_ENABLE_CATALYST=YES")

        return cmake_args

    def test_smoke_test(self):
        """Simple smoke test for ParaView"""
        pvserver = Executable(self.prefix.bin.pvserver)
        pvserver("--help")

    def test_pvpython(self):
        """Test pvpython"""
        if "~python" in self.spec:
            raise SkipTest("Package must be installed with +python")

        pvpython = Executable(self.prefix.bin.pvpython)
        pvpython("-c", "import paraview")

    def test_mpi_ensemble(self):
        """Test MPI ParaView Client/Server ensemble"""
        spec = self.spec

        if "~mpi" in spec or "~python" in spec:
            raise SkipTest("Package must be installed with +mpi and +python")

        mpirun = spec["mpi"].prefix.bin.mpirun
        pvserver = self.prefix.bin.pvserver
        pvpython = Executable(self.prefix.bin.pvpython)

        with working_dir("smoke_test_build", create=True):
            with Popen(
                [mpirun, "-np", "3", pvserver, "--mpi", "--force-offscreen-rendering"]
            ) as servers:
                pvpython(
                    "--force-offscreen-rendering",
                    "-c",
                    "from paraview.simple import *;"
                    "Connect('127.0.0.1');"
                    "sphere = Sphere(ThetaResolution=16, PhiResolution=32);"
                    "sphere_remote = servermanager.Fetch(sphere);"
                    "Show(sphere);"
                    "Render()",
                )
                servers.terminate()

    @run_after("install")
    @on_package_attributes(run_tests=True)
    def build_test(self):
        self.test_smoke_test()
        self.test_pvpython()
        self.test_mpi_ensemble()
