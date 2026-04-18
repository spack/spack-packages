# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyUxarray(PythonPackage):
    """Xarray extension for unstructured climate and global weather data analysis and
    visualization"""

    homepage = "https://uxarray.readthedocs.io"
    pypi = "uxarray/uxarray-2024.10.0.tar.gz"
    git = "https://github.com/uxarray/uxarray.git"

    license("Apache-2.0", checked_by="climbfuji")

    maintainers("Chrismarsh")

    version("2026.2.0", sha256="296adbcdcee0eba4dea4af31e4f9b489bb7092983f0fcb14e3f45f73089446a4")
    version("2025.12.0", sha256="0be5ad31f916253d6a3167dd42b0f6ccea754443aace90ddf0e36cc16407a6d5")
    version("2025.11.0", sha256="a1976851451d3729f86e9fe9a8a899c4bf338b84af8dc265298f5a16a6400bb9")
    version("2025.10.0", sha256="b25b8e13c7f041cb4c094ad7de0addd49acd0baae18da2a75a278c3c411ca20d")
    version("2025.9.0", sha256="cdbeef657bb75518a9c4a1880ac2e2d446b1c2bdaacf15e6ce45654a2ed47f34")
    version("2025.8.0", sha256="2279e3f4c5ca78d6a896441ee98ea29a228c7b24a0571c425d1c689939794c44")
    version("2025.6.0", sha256="f354648373c2c253bce80af1339f052b651e4ecff68fff78635c843324f7d228")
    version("2025.5.1", sha256="420fab51843a26642d876c451badd4fafcbac16f1703f391abed19f6beac1a04")
    version("2025.5.0", sha256="5a52c938569212522c251fa48acbb967da4ee4f15ad3aeffcbf07f16813634b1")
    version("2025.4.0", sha256="340ab54254e0e403481ec144d056a2a82450623c7144e6cfd8d11dfae467e92d")
    version("2024.10.0", sha256="f65a9920ce085af9a38349dc5ece4f9b83bc015dc8cb738d245d343f7816fd59")

    # Build-time dependencies
    depends_on("python@3.9:", type=("build", "run"), when="@2024")
    depends_on("python@3.10:", type=("build", "run"), when="@2025:")

    depends_on("py-setuptools@60:", type="build")
    depends_on("py-setuptools-scm@8:", type="build")

    # "Minimal" run-time dependencies
    depends_on("py-antimeridian", type=("build", "run"))
    depends_on("py-cartopy", type=("build", "run"))
    # With older versions of py-dask (2021.6.2):
    #    @derived_from(pd.core.strings.StringMethods)
    #                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    #    AttributeError: module 'pandas.core.strings' has no attribute 'StringMethods'
    # With py-dask@2023.4.1:
    #      return get(descriptor, obj, type(obj))
    #                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    #      TypeError: descriptor '__call__' for 'type' objects doesn't apply to a 'property' object
    # https://github.com/dask/dask/issues/11038
    depends_on("py-dask@2024.7.1: +dataframe", type=("build", "run"))

    depends_on("py-datashader", type=("build", "run"))
    depends_on("py-geoviews", type=("build", "run"))
    depends_on("py-holoviews", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-matplotlib-inline", type=("build", "run"))
    depends_on("py-netcdf4", type=("build", "run"))
    depends_on("py-numba", type=("build", "run"))

    depends_on("py-numpy@:2.3", type=("build", "run"), when="@:2025")
    depends_on("py-numpy@:2.4", type=("build", "run"), when="@2026:")

    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-pyarrow", type=("build", "run"))
    depends_on("arrow +parquet", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-shapely", type=("build", "run"))
    depends_on("py-spatialpandas", type=("build", "run"))
    depends_on("py-geopandas", type=("build", "run"))
    depends_on("py-xarray", type=("build", "run"))
    depends_on("py-hvplot", type=("build", "run"))
    depends_on("py-healpix", type=("build", "run"), when="@2025.4.0:")
    depends_on("py-polars", type=("build", "run"), when="@2025.4.0:")
    depends_on("py-pytest", type=("build", "run"))
