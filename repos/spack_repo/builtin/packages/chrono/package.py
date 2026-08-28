# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Chrono(CMakePackage):
    """Project Chrono is an open-source multi-physics simulation engine for
    rigid and flexible multibody dynamics, collision detection, granular
    material, fluid-solid interaction and vehicle dynamics.

    The ``+python`` variant additionally builds ``pychrono``, the SWIG-generated
    Python module, which Chrono builds from the same tree rather than shipping
    as a separate project.
    """

    homepage = "https://projectchrono.org/"
    url = "https://github.com/projectchrono/chrono/archive/refs/tags/10.0.0.tar.gz"
    git = "https://github.com/projectchrono/chrono.git"

    maintainers("cekees")

    license("BSD-3-Clause")

    version("main", branch="main")
    version(
        "10.0.0",
        sha256="806e5e24a06f26bbd42344dd1f13d75e3214c9eb29901553574b9c87217d8722",
    )

    variant("python", default=False, description="Build the pychrono Python module")
    variant("openmp", default=True, description="Enable OpenMP parallelism")
    variant("shared", default=True, description="Build shared libraries")
    variant("simd", default=False, description="Enable SIMD vectorization")

    # Chrono compiles C as well as C++ (e.g. chrono_thirdparty/libstl/stlfile.c),
    # so both must be declared -- omitting "c" fails at cmake time with
    # "[spack cc]: Error: SPACK_CC_* variables not set".
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.18:", type="build")

    # Chrono's core headers include Eigen directly, so it is a link-time
    # dependency of every consumer, not just a build-time one.
    depends_on("eigen@3.3.0:")

    # The Python module is generated with SWIG at build time
    # (src/chrono_swig/chrono_python/CMakeLists.txt does find_package(SWIG)).
    with when("+python"):
        # NOT extends("python"): Chrono installs pychrono into
        # share/chrono/python, never into site-packages -- verified on an actual
        # install, whose prefix contains only include/ lib/ share/
        # importer_blender/. extends() would promise spack a layout that does not
        # exist. PYTHONPATH is set for this package and its dependents below,
        # which is the same thing PETSc's own proteus build does
        # (PYTHONPATH="$PREFIX/share/chrono/python").
        depends_on("python@3.8:", type=("build", "run"))
        depends_on("swig@4:", type="build")

    depends_on("llvm-openmp", when="+openmp platform=darwin")

    # ------------------------------------------------------------------
    # ChClassFactory.h uses std::enable_if, std::is_polymorphic and
    # std::is_abstract but includes only <cstdio> <string> <functional>
    # <typeindex> <unordered_map> <memory>, relying on one of those to pull in
    # <type_traits> transitively. libstdc++ and Apple's libc++ still do;
    # newer libc++ (e.g. conda-forge's) does not, and Chrono_core then fails
    # with 14 errors of the form
    #
    #   ChClassFactory.h:48:53: error: no member named 'is_polymorphic' in
    #                                  namespace 'std'
    #
    # Belongs upstream in projectchrono/chrono; done here as a filter_file
    # rather than a patch so it stays a no-op once upstream adds the include.
    # ------------------------------------------------------------------
    @run_before("cmake")
    def add_missing_type_traits_include(self):
        header = join_path(self.stage.source_path, "src", "chrono", "core", "ChClassFactory.h")
        if not os.path.exists(header):
            return
        with open(header) as f:
            if "#include <type_traits>" in f.read():
                return
        filter_file(
            r"^#include <cstdio>$",
            "#include <cstdio>\n#include <type_traits>",
            header,
        )

    def cmake_args(self):
        args = [
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define("BUILD_TESTING", False),
            self.define("BUILD_DEMOS", False),
            # Optional modules, each pulling dependencies Chrono does not need
            # for multibody dynamics. Option names carry the CH_ prefix as of
            # 10.0.0 (confirmed against the tag's own CMakeLists.txt).
            self.define("CH_ENABLE_MODULE_CASCADE", False),
            self.define("CH_ENABLE_MODULE_IRRLICHT", False),
            self.define("CH_ENABLE_MODULE_MATLAB", False),
            self.define("CH_ENABLE_MODULE_POSTPROCESS", False),
            self.define("CH_ENABLE_MODULE_ROS", False),
            self.define("CH_ENABLE_MODULE_VEHICLE", False),
            self.define_from_variant("CH_ENABLE_MODULE_PYTHON", "python"),
            self.define_from_variant("CH_ENABLE_OPENMP", "openmp"),
            self.define_from_variant("CH_USE_SIMD", "simd"),
            # Chrono appends CH_DEBUG_POSTFIX ("_d") to every library name in a
            # Debug build, but consumers link the unsuffixed name. Force it
            # empty so a Debug build keeps -g without renaming the libraries.
            self.define("CH_DEBUG_POSTFIX", ""),
        ]

        if self.spec.satisfies("+python"):
            # Chrono's find_package(Python3 ... COMPONENTS Development) has been
            # observed to populate only Python3_EXECUTABLE, after which the SWIG
            # module links without libpython and fails on every CPython symbol.
            # Point CMake at the library and headers directly.
            python = self.spec["python"]
            args += [
                self.define("Python3_EXECUTABLE", python.command.path),
                self.define("Python3_INCLUDE_DIR", python.headers.directories[0]),
                self.define("Python3_LIBRARY", python.libs[0]),
            ]
            if self.spec.satisfies("platform=darwin"):
                # chrono_python's _core module target neither links -lpython nor
                # passes -undefined dynamic_lookup. Unresolved symbols in a
                # shared object are fine on Linux and resolve at dlopen time,
                # but are a hard link error for a macOS bundle.
                args.append(
                    self.define("CMAKE_MODULE_LINKER_FLAGS", "-undefined dynamic_lookup")
                )

        return args

    # pychrono lives in share/chrono/python, so nothing finds it by default.
    # Setting CH_INSTALL_PYTHON does not move it (tried against 10.0.0: the
    # module still installed to share/chrono/python), so expose it explicitly --
    # for this package's own run environment and for anything depending on it.
    @property
    def _pychrono_dir(self):
        return join_path(self.prefix, "share", "chrono", "python")

    def setup_run_environment(self, env):
        if self.spec.satisfies("+python"):
            env.prepend_path("PYTHONPATH", self._pychrono_dir)

    def setup_dependent_build_environment(self, env, dependent_spec):
        if self.spec.satisfies("+python"):
            env.prepend_path("PYTHONPATH", self._pychrono_dir)

    def setup_dependent_run_environment(self, env, dependent_spec):
        if self.spec.satisfies("+python"):
            env.prepend_path("PYTHONPATH", self._pychrono_dir)
