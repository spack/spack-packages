# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import tempfile

from spack_repo.builtin.build_systems import cmake, python
from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyDmTree(CMakePackage, PythonPackage):
    """tree is a library for working with nested data structures. In a
    way, tree generalizes the builtin map() function which only
    supports flat sequences, and allows to apply a function to each
    leaf preserving the overall structure."""

    homepage = "https://github.com/deepmind/tree"
    pypi = "dm-tree/dm_tree-0.1.5.tar.gz"

    maintainers("aweits")

    license("Apache-2.0")

    version("0.1.9", sha256="a4c7db3d3935a5a2d5e4b383fc26c6b0cd6f78c6d4605d3e7b518800ecd5342b")

    # horrible build system
    with default_args(deprecated=True):
        version("0.1.8", sha256="0fcaabbb14e7980377439e7140bd05552739ca5e515ecb3119f234acee4b9430")
        version("0.1.7", sha256="30fec8aca5b92823c0e796a2f33b875b4dccd470b57e91e6c542405c5f77fd2a")

    build_system(
        conditional("python_pip", when="@:0.1.8"),
        conditional("cmake", when="@0.1.9:"),  # it's hard to pass cmake args through setup.py.
        default="cmake",
    )

    extends("python", when="build_system=cmake")

    with default_args(type="build"):
        depends_on("cxx")
        depends_on("py-setuptools", when="@:0.1.8")
        depends_on("cmake@3.24:", when="@0.1.9:")
        depends_on("cmake@3.12:", when="@0.1.7:")
        depends_on("py-pybind11@2.10.1:", when="@0.1.8:")

    with default_args(type=("build", "run")):
        depends_on("python@3.10:", when="@0.1.9:")
        # Based on PyPI wheel availability
        depends_on("python@:3.13", when="@:0.1.9")
        depends_on("python@:3.11", when="@:0.1.8")
        depends_on("python@:3.10", when="@:0.1.7")

    depends_on("abseil-cpp cxxstd=14", when="@0.1.8:", type="link")
    depends_on("py-attrs@18.2.0:", type="run", when="@0.1.9:")
    depends_on("py-wrapt@1.11.2:", type="run", when="@0.1.9:")

    patch(
        "https://github.com/google-deepmind/tree/commit/63f25d4e05440ccbd4ba662be5f3f6eb460d29d8.patch?full_index=1",
        sha256="77dbd895611d412da99a5afbf312c3c49984ad02bd0e56ad342b2002a87d789c",
        when="@0.1.8",
    )
    # Add missing an install(...) to CMakeLists.txt
    patch("add-cmake-install.patch", when="@0.1.9")

    conflicts("%gcc@13:", when="@:0.1.7")

    # This is set later
    tmp_path = None

    @run_after("install", when="@:0.1.8")
    def clean(self):
        remove_linked_tree(PyDmTree.tmp_path)

    def url_for_version(self, version):
        if version <= Version("0.1.8"):
            return super().url_for_version(version).replace("_", "-")
        else:
            return super().url_for_version(version)

    @when("@:0.1.8")
    def patch(self):
        PyDmTree.tmp_path = tempfile.mkdtemp(prefix="spack")
        env["TEST_TMPDIR"] = PyDmTree.tmp_path
        env["HOME"] = PyDmTree.tmp_path
        args = [
            # Don't allow user or system .bazelrc to override build settings
            "'--nohome_rc',\n",
            "'--nosystem_rc',\n",
            # Bazel does not work properly on NFS, switch to /tmp
            "'--output_user_root={0}',\n".format(PyDmTree.tmp_path),
            "'build',\n",
            # Spack logs don't handle colored output well
            "'--color=no',\n",
            "'--jobs={0}',\n".format(make_jobs),
            # Enable verbose output for failures
            "'--verbose_failures',\n",
            "'--spawn_strategy=local',\n",
            # bazel uses system PYTHONPATH instead of spack paths
            "'--action_env', 'PYTHONPATH={0}',\n".format(env["PYTHONPATH"]),
        ]
        filter_file("'build',", " ".join(args), "setup.py")


class CMakeBuilder(cmake.CMakeBuilder):
    def cmake_args(self):
        return [
            self.define("USE_SYSTEM_ABSEIL", True),
            self.define("USE_SYSTEM_PYBIND11", True),
            self.define("PYTHON_INSTALL_DIR", join_path(python_platlib, "tree")),
        ]

    @run_before("build")
    def make_tree_dir(self):
        mkdir(join_path(self.build_directory, "tree"))

    @property
    def root_cmakelists_dir(self):
        return "tree"


class PythonPipBuilder(python.PythonPipBuilder):
    pass
