# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyChoreographer(PythonPackage):
    """Devtools Protocol implementation for chrome."""

    homepage = "https://github.com/plotly/choreographer"
    pypi = "choreographer/choreographer-1.0.10.tar.gz"

    license("MIT")

    version("1.0.10", sha256="7adf84a0d6a6054386d5cce013fdcadb2426479e49c9b0cb06af7d3712ed263c")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools@65:", type="build")
    depends_on("py-setuptools-git-versioning", type="build")

    depends_on("py-logistro@1.0.11:", type=("build", "run"))
    depends_on("py-simplejson@3.19.3:", type=("build", "run"))
