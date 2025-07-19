# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyXcdat(PythonPackage):
    """xCDAT is an extension of xarray for climate data analysis on structured grids.
    It serves as a modern successor to the Community Data Analysis Tools (CDAT) library."""

    homepage = "https://xcdat.readthedocs.io/en/latest"

    url = "https://github.com/xCDAT/xcdat/archive/refs/tags/v0.9.0.tar.gz"

    maintainers("LydDeb")

    license("Apache-2.0", checked_by="LydDeb")

    version("0.9.0", sha256="a36b46fe6317fabbac96ed2d4d1c6596a4f11d5069a88f85f683c08cd849faeb")

    depends_on("py-setuptools@42:", type="build")
    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-cf-xarray@0.10.3:", type=("build", "run"))
    depends_on("py-cftime", type=("build", "run"))
    depends_on("py-dask", type=("build", "run"))
    depends_on("py-netcdf4", type=("build", "run"))
    depends_on("py-numpy@2", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-python-dateutil", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-sparse", type=("build", "run"))
    depends_on("py-xarray@2024.03.0:", type=("build", "run"))
    depends_on("py-xesmf@0.8.7:", type=("build", "run"))
    depends_on("py-xgcm", type=("build", "run"))
