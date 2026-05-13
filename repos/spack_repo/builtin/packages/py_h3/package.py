# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyH3(PythonPackage):
    """Uber's hierarchical hexagonal geospatial indexing system."""

    homepage = "https://github.com/uber/h3-py"
    git = "https://github.com/uber/h3-py.git"
    pypi = "h3/h3-4.4.2.tar.gz"

    maintainers("LydDeb")

    license("Apache-2.0", checked_by="LydDeb")

    version("4.4.2", sha256="b25ab9f339e40b10dcb5e2e6988d07672e780a4950d79c25380d308cdf14f82f")

    depends_on("c", type="build")

    depends_on("python@3.8:", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-scikit-build-core")
        depends_on("py-cython")
