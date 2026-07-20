# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyDatashader(PythonPackage):
    """Datashader is a data rasterization pipeline for automating the process of creating
    meaningful representations of large amounts of data"""

    homepage = "https://datashader.org"
    pypi = "datashader/datashader-0.16.3.tar.gz"
    git = "https://github.com/holoviz/datashader.git"

    license("BSD-3-Clause", checked_by="climbfuji")

    version("0.18.2", sha256="53ef0bc35b9ba1034bdf290a2e28babf0fa2b075a3e5a822c79dcde12183d1ff")
    version("0.18.1", sha256="ad9390a9178eb03493fb67649f6570d59ccb371cf663533e0672a1826bb436b0")
    version("0.16.3", sha256="9d0040c7887f7a5a5edd374c297402fd208a62bf6845e87631b54f03b9ae479d")

    # pyproject.toml
    depends_on("python@3.9:", type=("build", "run"))
    depends_on("python@3.10:", type=("build", "run"), when="@0.18.1:")

    depends_on("py-hatchling", type="build")
    depends_on("py-hatch-vcs", type="build")

    depends_on("py-param", type=("build", "run"))
    depends_on("py-pyct", type=("build", "run"))

    depends_on("py-colorcet", type="run")
    depends_on("py-multipledispatch", type="run")
    depends_on("py-numba", type="run")
    depends_on("py-numpy", type="run")
    depends_on("py-pandas", type="run")
    depends_on("py-pillow", type="run")
    depends_on("py-requests", type="run")
    depends_on("py-scipy", type="run")
    depends_on("py-toolz", type="run")
    depends_on("py-packaging", type="run")
    depends_on("py-xarray", type="run")
    depends_on("py-dask", type="run")

    # https://github.com/holoviz/hvplot/issues/1471
    depends_on("py-dask@2025.1:", type="run", when="@0.17:")
