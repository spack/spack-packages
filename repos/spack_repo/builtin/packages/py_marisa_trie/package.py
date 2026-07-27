# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMarisaTrie(PythonPackage):
    """Static memory-efficient and fast Trie-like structures for Python."""

    homepage = "https://github.com/pytries/marisa-trie"
    pypi = "marisa_trie/marisa_trie-1.3.1.tar.gz"

    license("MIT AND (BSD-2-Clause OR LGPL-2.1-or-later)")

    version("1.3.1", sha256="97107fd12f30e4f8fea97790343a2d2d9a79d93697fe14e1b6f6363c984ff85b")

    depends_on("cxx", type="build")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools@77:", type="build")
    depends_on("py-cython@3.1.3:", type="build")
