# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTreeMath(PythonPackage):
    """Mathematical operations for JAX pytrees."""

    homepage = "https://github.com/google/tree-math"
    pypi = "tree-math/tree-math-0.2.0.tar.gz"

    license("Apache-2.0")

    version("0.2.1", sha256="77613c2360e067b16c0738b32e7d64aa5e1167e609ca1a32b6fa05dcb0d330bb")
    version("0.2.0", sha256="fced2b436fa265b4e24ab46b5768d7b03a4a8d0b75de8a5ab110abaeac3b5772")

    depends_on("py-setuptools", type="build")
    depends_on("py-jax", type=("build", "run"))
