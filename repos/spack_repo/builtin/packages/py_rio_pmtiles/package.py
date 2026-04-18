# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyRioPmtiles(PythonPackage):
    """Library and utilities to write and read PMTiles archives,
    cloud-optimized archives of map tiles."""

    homepage = "https://docs.protomaps.com/"
    pypi = "rio_pmtiles/rio_pmtiles-1.0.3.tar.gz"
    git = "https://github.com/protomaps/PMTiles"

    license("BSD-3-Clause", checked_by="Chrismarsh")

    version("1.2.0", sha256="b1ca2264afab0b37d62631976b25ef1cc611d62502ef1b8e3d2b584007763f83")
    version("1.0.3", sha256="bd4c1bc94c292cdc6d06f0d50837ce18fa2e6e49f4811fa0f58588735bd65f26")

    depends_on("py-setuptools", type="build")
    depends_on("py-click")
    depends_on("py-cligj@0.5:")
    depends_on("py-mercantile")
    depends_on("py-pmtiles@3")
    depends_on("py-pyroaring@1")
    depends_on("py-rasterio@1")
    depends_on("py-shapely@2")
    depends_on("py-supermercado")
    depends_on("py-tqdm@4")
