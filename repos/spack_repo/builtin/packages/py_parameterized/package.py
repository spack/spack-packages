# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyParameterized(PythonPackage):
    """Parameterized testing with any Python test framework."""

    homepage = "https://github.com/wolever/parameterized"
    pypi = "parameterized/parameterized-0.7.1.tar.gz"

    version("0.7.5", sha256="b5e6af67b9e49485e30125b1c8f031ffa81a265ca08bfa73f31551bf03cf68c4")
    version("0.7.1", sha256="6a94dbea30c6abde99fd4c2f2042c1bf7f980e48908bf92ead62394f93cf57ed")

    depends_on("py-setuptools", type="build")
