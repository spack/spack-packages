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
    version("10.0.0", sha256="806e5e24a06f26bbd42344dd1f13d75e3214c9eb29901553574b9c87217d8722")

    variant("python", default=False, description="Build the pychrono Python module")
    variant("openmp", default=True, description="Enable OpenMP parallelism")
    variant("shared", default=True, description="Build shared libraries")
    variant("simd", default=False, description="Enable SIMD vectorization")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.18:", type="build")

    # Chrono's public headers include Eigen, so consumers need it too
    depends_on("eigen@3.3.0:")

    # pychrono is generated with SWIG at build time
    with when("+python"):
        # Not extends("python"): pychrono installs into share/chrono/python, not site-packages.
        # PYTHONPATH is set below for this package and its dependents.
        depends_on("python@3.8:", type=("build", "run"))
        depends_on("swig@4:", type="build")

    depends_on("llvm-openmp", when="+openmp platform=darwin")

    # ChClassFactory.h uses std::is_polymorphic etc. without including <type_traits>;
    # newer libc++ no longer provides it transitively. Remove once fixed upstream.
    @run_before("cmake")
    def add_missing_type_traits_include(self):
        header = join_path(self.stage.source_path, "src", "chrono", "core", "ChClassFactory.h")
        if not os.path.exists(header):
            return
        filter_file(r"^#include <cstdio>$", "#include <cstdio>\n#include <type_traits>", header)

    def cmake_args(self):
        args = [
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define("BUILD_TESTING", False),
            self.define("BUILD_DEMOS", False),
            # Optional modules that pull dependencies multibody dynamics does not need
            self.define("CH_ENABLE_MODULE_CASCADE", False),
            self.define("CH_ENABLE_MODULE_IRRLICHT", False),
            self.define("CH_ENABLE_MODULE_MATLAB", False),
            self.define("CH_ENABLE_MODULE_POSTPROCESS", False),
            self.define("CH_ENABLE_MODULE_ROS", False),
            self.define("CH_ENABLE_MODULE_VEHICLE", False),
            self.define_from_variant("CH_ENABLE_MODULE_PYTHON", "python"),
            self.define_from_variant("CH_ENABLE_OPENMP", "openmp"),
            self.define_from_variant("CH_USE_SIMD", "simd"),
            # Debug builds append "_d" to library names, but consumers link the unsuffixed name
            self.define("CH_DEBUG_POSTFIX", ""),
        ]

        if self.spec.satisfies("+python"):
            # CMake's FindPython3 may find only the executable; pass library and headers explicitly
            python = self.spec["python"]
            args += [
                self.define("Python3_EXECUTABLE", python.command.path),
                self.define("Python3_INCLUDE_DIR", python.headers.directories[0]),
                self.define("Python3_LIBRARY", python.libs[0]),
            ]
            if self.spec.satisfies("platform=darwin"):
                # the _core bundle does not link libpython; macOS needs -undefined dynamic_lookup
                args.append(self.define("CMAKE_MODULE_LINKER_FLAGS", "-undefined dynamic_lookup"))

        return args

    # pychrono lives in share/chrono/python (CH_INSTALL_PYTHON does not move it), so expose it
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
