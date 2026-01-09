# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyDeisa(PythonPackage):
    """Deisa common library. Contains the definition of a common interface that may be
    used with Dask and Ray."""

    homepage = "https://github.com/deisa-project/deisa"
    pypi = "deisa/deisa-0.3.0.tar.gz"

    version("0.3.0", sha256="15e6747457e8801355d2227a8b59263da32e60474a4fed7f3b188e3782a8c702")

    depends_on("py-setuptools", type="build")
    depends_on("py-dask", type=("build", "run"))
    depends_on("py-distributed", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-deisa-dask@0.3.0", type=("build", "run"))
    depends_on("py-ray", type=("build", "run"))
