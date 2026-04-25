# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyDaskJobqueue(PythonPackage):
    """Dask is a flexible parallel computing library for analytics."""

    homepage = "https://github.com/dask/dask-jobqueue"
    pypi = "dask_jobqueue/dask_jobqueue-0.9.0.tar.gz"

    maintainers("chrismarsh")

    license("BSD-3-Clause")

    version("0.9.0", sha256="494ef64b7bb3848c7d72ed334c288030caca6a09dca54cfaa3f395f4ba7f5c47")

    depends_on("py-setuptools", type="build")
    depends_on("py-versioneer", type="build")

    depends_on("python@3.10:", type=("build", "run"))

    # requirements.txt
    depends_on("py-dask@2022.2.0:", type=("build", "run"))
    depends_on("py-distributed@2022.2.0:", type=("build", "run"))
