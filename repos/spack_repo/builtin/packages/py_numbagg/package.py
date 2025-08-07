# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyNumbagg(PythonPackage):
    """N-D labeled arrays and datasets in Python"""

    homepage = "https://github.com/numbagg/numbagg"
    pypi = "numbagg/numbagg-0.9.0.tar.gz"

    license("BSD-3-Clause")

    version("0.9.0", sha256="45ba41077b7a621e35eaa4c294d90b22e75e8513b8c211f59d2b9be840fc1175")

    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools-scm", type="build")

    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-numba", type=("build", "run"))
