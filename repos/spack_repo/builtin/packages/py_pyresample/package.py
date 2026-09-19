# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPyresample(PythonPackage):
    """A package for resampling geospatial image data"""

    homepage = "https://github.com/pytroll/pyresample"
    pypi = "pyresample/pyresample-1.35.0.tar.gz"

    license("LGPL-3.0-or-later")

    version("1.35.0", sha256="95f64734d63632ca642bc7bf4bce057c2ecac60f05fafd73c881bf68403ab5bb")
    version("1.34.2", sha256="094e959e3e31a547d39ce1a940e5cdb23845a5c458a0fc244f2e4e5135e4f797")
    version("1.34.1", sha256="6e0e7ccf090bcabf4bfc8818d7ff633741fddf9784fe90b4add86f925b5b72f1")
    version("1.34.0", sha256="a0cd05327f8015862809da8704e93943890f02194d11d97ede29576f6a6730d4")

    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools-scm +toml", type="build")

    depends_on("python@3.11:", type=("build", "run"))

    depends_on("py-configobj", type=("build", "run"))
    depends_on("py-cython", type=("build", "run"))
    depends_on("py-donfig", type=("build", "run"))
    depends_on("py-numexpr", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-platformdirs", type=("build", "run"))
    depends_on("py-pykdtree", type=("build", "run"))
    depends_on("py-pyproj", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-shapely", type=("build", "run"))
    depends_on("py-versioneer", type=("build", "run"))

    # Optional functionality dependencies
    depends_on("py-dask", type=("build", "run"))
    depends_on("py-odc-geo", type=("build", "run"))
    depends_on("py-rasterio", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-xarray", type=("build", "run"))

    variant("plotting", default=False, description="Enable plotting functionality")
    variant("tests", default=False, description="Dependencies to run test suites")

    with when("+plotting"):
        depends_on("py-cartopy", type=("build", "run"))
        depends_on("py-matplotlib", type=("build", "run"))

    with when("+tests"):
        depends_on("py-cartopy", type="test")
        depends_on("py-dask", type="test")
        depends_on("py-matplotlib", type="test")
        depends_on("py-pillow", type="test")
        depends_on("py-pytest", type="test")
        depends_on("py-pytest-lazy-fixtures", type="test")
        depends_on("py-rasterio", type="test")
        depends_on("py-scipy", type="test")
        depends_on("py-xarray", type="test")
        depends_on("py-zarr", type="test")
