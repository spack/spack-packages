# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTreeSitterC(PythonPackage):
    """Python bindings to the C-grammar provided by tree-sitter"""

    homepage = "https://tree-sitter.github.io/py-tree-sitter/"
    pypi = "tree_sitter_c/tree_sitter_c-0.24.1.tar.gz"
    git = "https://github.com/tree-sitter/tree-sitter-c"

    version("0.24.1", sha256="7d2d0cda0b8dda428c81440c1e94367f9f13548eedca3f49768bde66b1422ad6")

    depends_on("py-tree-sitter")
    depends_on("python@3.10:", type=("build", "link", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("c", type="build")
