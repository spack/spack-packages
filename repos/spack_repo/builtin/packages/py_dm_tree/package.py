# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import tempfile

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyDmTree(PythonPackage):
    """tree is a library for working with nested data structures. In a
    way, tree generalizes the builtin map() function which only
    supports flat sequences, and allows to apply a function to each
    leaf preserving the overall structure."""

    homepage = "https://github.com/deepmind/tree"
    pypi = "dm-tree/dm_tree-0.1.5.tar.gz"

    maintainers("aweits")

    license("Apache-2.0")

    version("0.1.9", sha256="a4c7db3d3935a5a2d5e4b383fc26c6b0cd6f78c6d4605d3e7b518800ecd5342b")
    version("0.1.8", sha256="0fcaabbb14e7980377439e7140bd05552739ca5e515ecb3119f234acee4b9430")
    version("0.1.7", sha256="30fec8aca5b92823c0e796a2f33b875b4dccd470b57e91e6c542405c5f77fd2a")

    depends_on("cxx", type="build")

    # Based on PyPI wheel availability
    depends_on("python@3.10:3.13", when="@0.1.9:", type=("build", "run"))
    depends_on("python@:3.11", when="@0.1.8", type=("build", "run"))
    depends_on("python@:3.10", when="@0.1.6:0.1.7", type=("build", "run"))

    depends_on("python@3.10:", type=("build", "run"), when="@0.1.9:")
    depends_on("py-setuptools", type="build")
    depends_on("cmake@3.24:", when="@0.1.9:", type="build")
    depends_on("cmake@3.12:", when="@0.1.7:", type="build")
    depends_on("py-pybind11@2.10.1:", when="@0.1.8:")
    depends_on("abseil-cpp cxxstd=14", when="@0.1.8:")
    depends_on("py-absl-py@0.6.1:", type=("build", "run"), when="@0.1.9:")
    depends_on("py-attrs@18.2.0:", type=("build", "run"), when="@0.1.9:")
    with default_args(type=("build", "run"), when="@0.1.9:"):
        depends_on("py-numpy@1.21:")
        depends_on("py-numpy@1.21.2:", when="^python@3.10:")
        depends_on("py-numpy@1.23.3:", when="^python@3.11:")
        depends_on("py-numpy@1.26.0:", when="^python@3.12:")
        depends_on("py-numpy@2.1.0:", when="^python@3.13:")
    depends_on("py-wrapt@1.11.2:", type=("build", "run"), when="@0.1.9:")

    patch(
        "https://github.com/google-deepmind/tree/commit/63f25d4e05440ccbd4ba662be5f3f6eb460d29d8.patch?full_index=1",
        sha256="77dbd895611d412da99a5afbf312c3c49984ad02bd0e56ad342b2002a87d789c",
        when="@0.1.8",
    )
    conflicts("%gcc@13:", when="@:0.1.7")

    # This is set later
    tmp_path = None

    @run_after("install")
    def clean(self):
        remove_linked_tree(PyDmTree.tmp_path)

    def url_for_version(self, version):
        if version <= Version("0.1.8"):
            return super().url_for_version(version).replace("_", "-")
        else:
            return super().url_for_version(version)

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
