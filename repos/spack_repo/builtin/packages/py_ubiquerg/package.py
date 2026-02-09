# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyUbiquerg(PythonPackage):
    """Tools for work (erg) everywhere (ubique)."""

    homepage = "https://github.com/pepkit/ubiquerg"
    pypi = "ubiquerg/ubiquerg-0.6.2.tar.gz"

    license("BSD-2-Clause")

    version("0.6.3", sha256="025509c4ec77a5cde8e8be66dabfef2ca6e3cd99da3cb15066c66a6f2bc3b9b5")
    version("0.6.2", sha256="a9b1388799d4c366f956e0c912819099ad8f6cd0e5d890923cdde197f80d14cf")

    depends_on("py-setuptools", type="build")
