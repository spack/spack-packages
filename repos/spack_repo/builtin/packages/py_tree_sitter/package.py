# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage, depends_on

from spack.package import *


class PyTreeSitter(PythonPackage):
    """Python bindings to the tree-sitter library"""

    homepage = "https://tree-sitter.github.io/py-tree-sitter/"
    pypi = "tree-sitter/tree-sitter-0.24.0.tar.gz"
    git = "https://github.com/tree-sitter/py-tree-sitter.git"

    maintainers("JohnGouwar")

    version("master", branch="master", submodules=True)
    version("0.25.0", commit="9c78f3b8d10f81b97fbb2181c9333323d6375480", submodules=True)
    version("0.24.0", sha256="abd95af65ca2f4f7eca356343391ed669e764f37748b5352946f00f7fc78e734")

    depends_on("python@3.10:", type=("build", "link", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("c", type="build")
