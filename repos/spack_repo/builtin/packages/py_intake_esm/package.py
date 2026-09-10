# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyIntakeEsm(PythonPackage):
    """
    An intake plugin for parsing an Earth System Model (ESM) catalog and loading netCDF files
    and/or Zarr stores into Xarray datasets."
    """

    homepage = "https://intake-esm.readthedocs.io"
    git = "https://github.com/intake/intake-esm.git"
    pypi = "intake_esm/intake_esm-2025.12.12.tar.gz"

    maintainers("LydDeb")

    license("Apache-2.0", checked_by="LydDeb")

    version(
        "2025.12.12", sha256="b99d2d07347a9ea98261277960ccce8a737f683521472bc4ca879b8f71bc7ed2"
    )

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-setuptools@75.0:", type="build")
    depends_on("py-setuptools-scm@8.1:", type="build")
    depends_on("py-dask@2024.12:", type=("build", "run"))
    depends_on("py-fastprogress@1.0.0:", type=("build", "run"))
    depends_on("py-fsspec@2024.12:", type=("build", "run"))
    depends_on("py-intake@2.0.0:", type=("build", "run"))
    depends_on("py-itables", type=("build", "run"))
    depends_on("py-netcdf4@1.5.5:", type=("build", "run"))
    depends_on("py-pandas@2.1.0:", type=("build", "run"))
    depends_on("py-polars@1.24.0:1.32", type=("build", "run"))
    depends_on("py-pydantic@2.0:", type=("build", "run"))
    depends_on("py-pydap@:3.5.4,3.5.6:", type=("build", "run"))
    depends_on("py-requests@2.24.0:", type=("build", "run"))
    depends_on("py-xarray@2024.10:", type=("build", "run"))
    depends_on("py-zarr@2.12:2,3.1:", type=("build", "run"))
    depends_on("py-kerchunk@0.2.9:", type=("build", "run"))
