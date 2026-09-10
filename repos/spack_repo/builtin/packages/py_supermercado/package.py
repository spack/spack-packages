# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySupermercado(PythonPackage):
    """supermercado extends the functionality of mercantile with additional commands"""

    pypi = "supermercado/supermercado-0.3.0.tar.gz"
    git = "https://github.com/mapbox/supermercado"

    license("MIT", checked_by="Chrismarsh")

    version("0.3.0", sha256="d8cc7519cb25f1142ee0e7c9e40b9be9a5688c3ac1f90a87d165286c3bfe44b6")

    depends_on("py-setuptools@68:", type="build")
    depends_on("python@3.10:")
