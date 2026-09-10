# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPyogrio(PythonPackage):
    """Vectorized spatial vector file format I/O using GDAL/OGR"""

    homepage = "https://pypi.org/project/pyogrio"
    pypi = "pyogrio/pyogrio-0.9.0.tar.gz"
    git = "https://github.com/geopandas/pyogrio.git"

    maintainers("climbfuji", "adamjstewart")

    license("MIT", checked_by="climbfuji")

    version("0.11.1", sha256="e1441dc9c866f10d8e6ae7ea9249a10c1f57ea921b1f19a5b0977ab91ef8082c")
    version("0.11.0", sha256="a7e0a97bc10c0d7204f6bf52e1b928cba0554c35a907c32b23065aed1ed97b3f")
    version("0.10.0", sha256="ec051cb568324de878828fae96379b71858933413e185148acb6c162851ab23c")
    version("0.9.0", sha256="6a6fa2e8cf95b3d4a7c0fac48bce6e5037579e28d3eb33b53349d6e11f15e5a8")

    # pyproject.toml
    with default_args(type="build"):
        depends_on("py-setuptools")
        depends_on("py-cython@0.29:")
        depends_on("py-versioneer@0.28+toml")

    with default_args(type=("build", "run")):
        depends_on("py-certifi")
        depends_on("py-numpy")
        depends_on("py-packaging")

    # setup.py
    depends_on("gdal@2.4:", type=("build", "link", "run"))
