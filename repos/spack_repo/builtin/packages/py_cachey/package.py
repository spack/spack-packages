# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyCachey(PythonPackage):
    """Cachey is a package for caching of analytic computations."""

    homepage = "http://github.com/dask/cachey/"
    pypi = "cachey/cachey-0.2.1.tar.gz"

    maintainers("Markus92")

    license("BSD-3-Clause", checked_by="Markus92")

    version("0.2.1", sha256="0310ba8afe52729fa7626325c8d8356a8421c434bf887ac851e58dcf7cf056a6")

    depends_on("python@3.6:", type=("build", "run"))

    depends_on("py-setuptools", type="build")

    depends_on("py-heapdict", type=("build", "run"))
