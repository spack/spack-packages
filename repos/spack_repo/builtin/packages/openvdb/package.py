# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import shutil

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Openvdb(CMakePackage):
    """OpenVDB - a sparse volume data format."""

    homepage = "https://github.com/AcademySoftwareFoundation/openvdb"
    url = "https://github.com/AcademySoftwareFoundation/openvdb/archive/refs/tags/v13.0.0.tar.gz"
    git = "https://github.com/AcademySoftwareFoundation/openvdb.git"
    license("MPL-2.0")

    # Github account name for drew@lagrangian.xyz
    maintainers("eloop")

    version("master", branch="master")
    version("13.0.0", sha256="4d6a91df5f347017496fe8d22c3dbb7c4b5d7289499d4eb4d53dd2c75bb454e1")
    version("10.0.0", sha256="6d4f6b5ccd0f9d35a4886d9a51a98c97fa314f75bf9737c5121e91b706e2db70")
    version("9.1.0", sha256="914ee417b4607c75c95b53bc73a0599de4157c7d6a32e849e80f24e40fb64181")
    version("8.2.0", sha256="d2e77a0720db79e9c44830423bdb013c24a1cf50994dd61d570b6e0c3e0be699")
    version("8.0.1", sha256="a6845da7c604d2c72e4141c898930ac8a2375521e535f696c2cd92bebbe43c4f")
    version("7.1.0", sha256="0c3588c1ca6e647610738654ec2c6aaf41a203fd797f609fbeab1c9f7c3dc116")

    # these variants were for 8.0.1 and probably could be updated...
    variant("shared", default=True, description="Build as a shared library.")
    variant("python", default=False, description="Build the pyopenvdb python extension.")
    variant("vdb_print", default=False, description="Build the vdb_print tool.")
    variant("vdb_lod", default=False, description="Build the vdb_lod tool.")
    variant("vdb_render", default=False, description="Build the vdb_render tool.")
    # variant("ax", default=False, description="Build the AX extension.")

    depends_on("cxx", type="build")
    depends_on("cmake@3.18:", type="build")  # VDB 10+ needed newer cmake.
    depends_on("cmake@3.24:", type="build", when="@13:")
    depends_on("git", type="build", when="@develop")

    depends_on("ilmbase", when="@8:9")  # note: ilmbase has been rolled into OpenEXR 3
    depends_on("imath@3.1:", when="@13:")

    depends_on("openexr")
    depends_on("openexr@2.3", when="@8:9")
    depends_on("openexr@2.3:", when="@10")
    depends_on("openexr@3.2:", when="@13:")

    depends_on("intel-tbb")
    depends_on("intel-tbb@:2020.1", when="@:8.1")
    depends_on("intel-tbb@2021", when="@8.2:10")
    depends_on("intel-tbb@2021:", when="@13:")

    depends_on("jemalloc")
    depends_on("zlib-api")
    depends_on("c-blosc@1.17:")

    depends_on("boost+iostreams+system@1.82:", type=("build", "link"), when="@:10")
    depends_on("boost+iostreams@1.82:", type=("build", "link"), when="@13:")

    with when("+python"):
        extends("python")
        depends_on("py-numpy", type=("build", "link"))
        with when("@13:"):
            depends_on("python@3.11", type=("build", "link"))
            depends_on("py-nanobind", type=("build"))
        with when("@:10"):
            depends_on("python@3.10", type=("build", "link"))
            # pre py-nanobind they used boost python
            depends_on("boost+python+numpy")

    # This section still not ready for prime time. Seems to be very
    # picky on particular versions of llmv..  AX requires quite a few
    # things, and hasn't been properly released
    # depends_on("llvm@18.1.8", when="+ax")
    # depends_on("bison@3.7.0:", when="+ax")
    # depends_on("flex@2.6.4:", when="+ax")

    def cmake_args(self):

        args = [
            self.define("OPENVDB_BUILD_CORE", True),
            # Force the specific Spack-built Boost prefix
            self.define("Boost_ROOT", self.spec["boost"].prefix),
            self.define("Boost_NO_BOOST_CMAKE", True),
            self.define("Boost_NO_SYSTEM_PATHS", True),
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define_from_variant("OPENVDB_BUILD_VDB_PRINT", "vdb_print"),
            self.define_from_variant("OPENVDB_BUILD_VDB_LOD", "vdb_lod"),
            self.define_from_variant("OPENVDB_BUILD_VDB_RENDER", "vdb_render"),
            self.define_from_variant("OPENVDB_BUILD_PYTHON_MODULE", "python"),
            # AX removed for the time being
            # self.define_from_variant("OPENVDB_BUILD_AX", "ax"),
            # self.define_from_variant("OPENVDB_BUILD_AX_BINARIES", "ax"),
        ]

        if self.spec.satisfies("+python"):
            args.append(self.define("Python3_EXECUTABLE", self.spec["python"].command.path))

        return args

    @run_after("install")
    def fix_python_layout(self):
        """Fixes the lib64 vs lib issue for RHEL/Rocky etc"""
        spec = self.spec
        if "+python" not in spec:
            return

        # Explicitly use string paths for os.path operations
        prefix_str = str(self.prefix)
        py_ver = spec["python"].version.up_to(2)
        target_dir = os.path.join(prefix_str, "lib", f"python{py_ver}", "site-packages")

        # pattern is globally available in Spack DSL
        pattern = f"openvdb*.{dso_suffix}"
        matches = find(prefix_str, pattern, recursive=True)

        if not matches:
            if find(target_dir, pattern, recursive=True):
                return
            raise InstallError(f"Python extension 'openvdb' not found in {self.prefix}")

        mkdirp(target_dir)

        for src in matches:
            # Avoid moving if it's already in the right place
            if os.path.normpath(os.path.dirname(src)) == os.path.normpath(target_dir):
                continue

            install(src, target_dir)
            os.remove(src)

        # Cleanup lib64 remnants
        old_path = os.path.join(prefix_str, "lib64", f"python{py_ver}")
        if os.path.isdir(old_path):
            shutil.rmtree(old_path, ignore_errors=True)

    def test_python_import(self):
        """Verify that OpenVDB can create and manipulate a grid."""

        if "+python" not in self.spec:
            return

        python_exe = self.spec["python"].command.path
        py = Executable(python_exe)

        # This script creates a FloatGrid, sets a value, and checks it.
        # It tests: 1. Import, 2. C++ Binding, 3. Memory Allocation
        test_script = (
            "import openvdb as vdb; "
            "grid = vdb.FloatGrid(); "
            "grid.name = 'test_grid'; "
            "accessor = grid.getAccessor(); "
            "accessor.setValueOn((0, 0, 0), 1.0); "
            "assert grid.activeVoxelCount() == 1; "
            "print('OpenVDB Functional Test: PASSED')"
        )

        py("-c", test_script)
