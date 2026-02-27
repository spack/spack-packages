# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyDeisaDask(PythonPackage):
    """Deisa: Dask-Enabled In Situ Analytics."""

    homepage = "https://github.com/deisa-project/deisa-dask"
    pypi = "deisa_dask/deisa_dask-0.3.0.tar.gz"

    version("0.3.0", sha256="615483d3c21e05c1cdf0564db0245f7f6ba979e75c25a0292d3d42fcc4cf6d23")

    depends_on("py-setuptools", type="build")
    depends_on("python@3.10:", type="build")
    depends_on("py-deisa-core@0.1.0", type=("build", "run"))
    depends_on("py-dask", type=("build", "run"))
    depends_on("py-distributed", type=("build", "run"))
