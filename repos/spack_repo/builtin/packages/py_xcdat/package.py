# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage
from spack.package import *


class PyXcdat(PythonPackage):
    """xCDAT is an extension of xarray for climate data analysis on structured grids. It serves as a modern successor to the Community Data Analysis Tools (CDAT) library."""

    homepage = "https://xcdat.readthedocs.io/en/latest"

    url = "https://github.com/xCDAT/xcdat/archive/refs/tags/v0.9.0.tar.gz"

    maintainers("LydDeb")

    license("Apache-2.0", checked_by="LydDeb")

    version("0.9.0", sha256="a36b46fe6317fabbac96ed2d4d1c6596a4f11d5069a88f85f683c08cd849faeb")
    version("0.8.0", sha256="8df894c9776f8dfc0d01370242f6e519a6de77889a87d0e9159ec9e2c105e389")
    version("0.7.3", sha256="ad78929782f9fa6ed51525a5517aa7d232060b00dbdb5573e75d72319776e99a")
    version("0.7.2", sha256="c16f7ce865388fa0ed963dd61fab032f72d483c2f0b61e745ca0e60d919024f4")
    version("0.7.1", sha256="b3ff94c5de06f0e560df64569ec36873965ef1239b991651142ae69f399676d7")

    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools@42:", type="build", when="@0.7.3:")
    depends_on("py-dask", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-xarray@2024.03.0:", type=("build", "run"), when="@0.7.3:")
    depends_on("py-xarray@2023.2.0:", type=("build", "run"), when="@0.7.1:0.7.2")
    depends_on("py-cf-xarray@0.10.3:", type=("build", "run"), when="@0.9")
    depends_on("py-cf-xarray@0.9.1:", type=("build", "run"), when="@0.7.3:")
    depends_on("py-cftime", type=("build", "run"), when="@0.7.3:")
    depends_on("py-netcdf4", type=("build", "run"), when="@0.7.3:")
    depends_on("py-numpy@2", type=("build", "run"), when="@0.7.3:")
    depends_on("py-numpy@1.23.0:", type=("build", "run"), when="@0.7.1:0.7.2")
    depends_on("py-python-dateutil", type=("build", "run"), when="@0.7.3:")
    depends_on("py-scipy", type=("build", "run"), when="@0.9")
    depends_on("py-sparse", type=("build", "run"), when="@0.9")
    depends_on("py-xesmf", type=("build", "run"))
    depends_on("py-xesmf@0.8.7:", type=("build", "run"), when="@0.7.3:")
    depends_on("py-xgcm", type=("build", "run"), when="@0.7.3:")
