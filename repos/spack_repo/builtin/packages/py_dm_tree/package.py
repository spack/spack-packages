# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class PyDmTree(CMakePackage):
    """tree is a library for working with nested data structures. In a way, tree generalizes the
    builtin map() function which only supports flat sequences, and allows to apply a function to
    each leaf preserving the overall structure."""

    homepage = "https://github.com/deepmind/tree"
    url = "https://files.pythonhosted.org/packages/source/d/dm_tree/dm-tree-0.1.8.tar.gz"
    root_cmakelists_dir = "tree"

    maintainers("aweits")

    license("Apache-2.0")

    version("0.1.9", sha256="a4c7db3d3935a5a2d5e4b383fc26c6b0cd6f78c6d4605d3e7b518800ecd5342b")

    with default_args(deprecated=True):
        version("0.1.8", sha256="0fcaabbb14e7980377439e7140bd05552739ca5e515ecb3119f234acee4b9430")
        version("0.1.7", sha256="30fec8aca5b92823c0e796a2f33b875b4dccd470b57e91e6c542405c5f77fd2a")

    extends("python")

    with default_args(type="build"):
        depends_on("cxx")
        depends_on("cmake@3.24:", when="@0.1.9:")
        depends_on("cmake@3.12:")
        # 0.1.7 uses FetchContent for pybind11.
        depends_on("py-pybind11@2.10.1:", when="@0.1.8:")

    with default_args(type=("build", "run")):
        depends_on("python@3.10:", when="@0.1.9:")
        # Based on PyPI wheel availability
        depends_on("python@:3.11", when="@:0.1.8")
        depends_on("python@:3.10", when="@:0.1.7")

    depends_on("abseil-cpp cxxstd=14", type="link", when="@0.1.8:")
    depends_on("py-attrs@18.2.0:", type="run", when="@0.1.9:")
    depends_on("py-wrapt@1.11.2:", type="run", when="@0.1.9:")

    # Avoid FetchContent for pybind11 and abseil-cpp in 0.1.8.
    patch(
        "https://github.com/google-deepmind/tree/commit/63f25d4e05440ccbd4ba662be5f3f6eb460d29d8.patch?full_index=1",
        sha256="77dbd895611d412da99a5afbf312c3c49984ad02bd0e56ad342b2002a87d789c",
        when="@0.1.8",
    )
    # Add missing an install(...) to CMakeLists.txt
    # https://github.com/google-deepmind/tree/pull/136
    patch("add-cmake-install-0.1.9.patch", when="@0.1.9")
    patch("add-cmake-install-0.1.8.patch", when="@0.1.8")
    patch("add-cmake-install-0.1.7.patch", when="@0.1.7")

    conflicts("%gcc@13:", when="@:0.1.7")

    def url_for_version(self, version):
        if version <= Version("0.1.8"):
            return super().url_for_version(version).replace("_", "-")
        else:
            return super().url_for_version(version)

    def cmake_args(self):
        return [
            self.define("USE_SYSTEM_ABSEIL", True),
            self.define("USE_SYSTEM_PYBIND11", True),
            self.define("PYTHON_INSTALL_DIR", join_path(python_platlib, "tree")),
        ]
