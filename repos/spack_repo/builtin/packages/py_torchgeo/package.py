# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTorchgeo(PythonPackage):
    """TorchGeo: datasets, samplers, transforms, and pre-trained models for geospatial data."""

    homepage = "https://github.com/microsoft/torchgeo"
    pypi = "torchgeo/torchgeo-0.1.0.tar.gz"
    git = "https://github.com/microsoft/torchgeo.git"

    license("MIT")
    maintainers("adamjstewart", "calebrob6", "ashnair1")

    version("main", branch="main")
    version("0.9.0", sha256="93858ccd1cd9cc25b022572dabcd94a024160529a3bd7fc75dc28e995240ca6c")
    version("0.8.1", sha256="2de05fd510264569f28a8d92737cac85d34dd3c14e01aec99e6f2edb7d297248")
    version("0.8.0", sha256="a367127b8a6b6f94cff979972169271c70ca9d8237d68576c5ec38de34e5cbe7")
    version("0.7.2", sha256="0597455c689c61fd1bdffc79357646292aac98681279a1d05536317a0d094b69")
    version("0.7.1", sha256="05f645868a6dff083d4d0529662bde1b502e1f33ef260ebc735065e05d84176e")
    version("0.7.0", sha256="4ba0e96ea826080f393b1bb719a3f8c364637112710b1ac38c56b9590a638e29")
    version("0.6.2", sha256="82f49f0d18d2c22cc70fc0690641e8dd60e4904a9c50d32c79ebd5020ac10fa7")
    version("0.6.1", sha256="38c930917ea341d05a7a611ff74c017f29482df7455d50e287ea79dec7d0a14b")

    variant("datasets", default=False, description="Install optional dataset dependencies")
    variant("docs", default=False, description="Install documentation dependencies")
    variant(
        "models", default=False, description="Install optional model dependencies", when="@0.8:"
    )
    variant("style", default=False, description="Install style checking tools")
    variant("tests", default=False, description="Install testing tools")

    # Required dependencies
    with default_args(type="build"):
        depends_on("py-setuptools@77.0.1:", when="@0.7.1:")
        depends_on("py-setuptools@61:")

    with default_args(type=("build", "run")):
        depends_on("python@3.12:", when="@0.9:")
        depends_on("python@3.11:", when="@0.7:")
        depends_on("python@3.10:")
        depends_on("py-einops@0.3:")
        depends_on("py-geopandas@0.13:", when="@0.9:")
        depends_on("py-geopandas@0.12.1:", when="@0.8:")
        depends_on("py-jsonargparse@4.35:+signatures", when="@0.9:")
        depends_on("py-jsonargparse@4.25:+signatures")
        depends_on("py-kornia@0.8.2:", when="@0.8:")
        depends_on("py-kornia@0.7.4:", when="@0.7:")
        depends_on("py-kornia@0.7.3:")
        depends_on("py-lightly@1.4.5:")
        depends_on("py-lightning@2:")
        depends_on("py-matplotlib@3.7.3:", when="@0.9:")
        depends_on("py-matplotlib@3.6:", when="@0.7:")
        depends_on("py-matplotlib@3.5:")
        depends_on("py-numpy@1.26:", when="@0.9:")
        depends_on("py-numpy@1.24:", when="@0.8:")
        depends_on("py-numpy@1.23.2:", when="@0.7:")
        depends_on("py-numpy@1.21.2:")
        depends_on("py-pandas@2.1.1:", when="@0.9:")
        depends_on("py-pandas@1.5:", when="@0.7:")
        depends_on("py-pandas@1.3.3:")
        depends_on("pil@10:", when="@0.9:")
        depends_on("pil@9.2:", when="@0.7:")
        depends_on("pil@8.4:")
        depends_on("py-pyproj@3.6.1:", when="@0.9:")
        depends_on("py-pyproj@3.4:", when="@0.7:")
        depends_on("py-pyproj@3.3:")
        depends_on("py-rasterio@1.4.3:", when="@0.8:")
        # https://github.com/torchgeo/torchgeo/pull/2969
        depends_on("py-rasterio@1.3.11:", when="@0.7:")
        depends_on("py-rasterio@1.3:")
        depends_on("py-segmentation-models-pytorch@0.5:", when="@0.7.1:")
        # https://github.com/microsoft/torchgeo/pull/2740
        depends_on("py-segmentation-models-pytorch@0.3.3:0.4", when="@0.7.0")
        depends_on("py-segmentation-models-pytorch@0.2:0.4", when="@0.6")
        depends_on("py-shapely@2.0.2:", when="@0.9:")
        depends_on("py-shapely@2:", when="@0.8:")
        depends_on("py-shapely@1.8.5:", when="@0.7:")
        depends_on("py-shapely@1.8:")
        depends_on("py-timm@1.0.3:", when="@0.8:")
        depends_on("py-timm@0.9.2:", when="@0.7:")
        depends_on("py-timm@0.4.12:")
        depends_on("py-torch@2.2:", when="@0.9:")
        depends_on("py-torch@2:", when="@0.7:")
        depends_on("py-torch@1.13:")
        depends_on("py-torchmetrics@1.2:", when="@0.7:")
        depends_on("py-torchmetrics@0.10:")
        depends_on("py-torchvision@0.17:", when="@0.9:")
        depends_on("py-torchvision@0.15.1:", when="@0.7:")
        depends_on("py-torchvision@0.14:")
        depends_on("py-typing-extensions@4.8:", when="@0.9:")
        depends_on("py-typing-extensions@4.5:", when="@0.7:")

        # Historical dependencies
        depends_on("py-fiona@1.8.22:", when="@0.7")
        depends_on("py-fiona@1.8.21:", when="@0.6")

    # Optional dependencies
    with when("+datasets"), default_args(type="run"):
        depends_on("py-h5py@3.10:", when="@0.9:")
        depends_on("py-h5py@3.8:", when="@0.7:")
        depends_on("py-h5py@3.6:")
        depends_on("py-laspy@2.5.3:", when="@0.7.2:")
        depends_on("py-laspy@2:")
        depends_on("py-netcdf4@1.6.5:", when="@0.9:")
        depends_on("py-netcdf4@1.6.1:", when="@0.7:")
        depends_on("py-pandas+parquet", when="@0.7:")
        depends_on("py-pycocotools@2.0.8:", when="@0.9:")
        depends_on("py-pycocotools@2.0.7:")
        depends_on("py-requests@2.25:", when="@0.9:")
        depends_on("py-requests@2.23:", when="@0.8:")
        depends_on("py-rioxarray@0.14.1:", when="@0.8:")
        depends_on("py-scikit-image@0.22:", when="@0.9:")
        depends_on("py-scikit-image@0.20:", when="@0.7:")
        depends_on("py-scikit-image@0.19:")
        depends_on("py-scipy@1.11.2:", when="@0.9:")
        depends_on("py-scipy@1.9.2:", when="@0.7:")
        depends_on("py-scipy@1.7.2:")
        depends_on("py-webdataset@0.2.4:", when="@0.7:")
        depends_on("py-xarray@0.17:", when="@0.8:")
        depends_on("py-xarray@0.12.3:", when="@0.7:")

        # Required to download SpaceNet datasets.
        depends_on("awscli-v2")
        # Required to download Source Cooperative datasets.
        depends_on("azcopy")
        # bz2 required to extract .tar.bz2 files, zlib required to extract .tar.gz files.
        depends_on("python+bz2+zlib")
        # JPEG, JPEG2000, TIFF, compressed PNG support required for file I/O in several datasets.
        depends_on("py-pillow+jpeg+jpeg2000+tiff+zlib", when="^[virtuals=pil] py-pillow")
        depends_on("py-pillow-simd+jpeg+jpeg2000+tiff+zlib", when="^[virtuals=pil] py-pillow-simd")
        # GDAL and libtiff are both dependencies of rasterio.
        # Sentinel 2 dataset requires OpenJPEG to read .jp2 files.
        depends_on("gdal+openjpeg")
        # JPEG required for GDAL to read JPEG files
        # LIBDEFLATE, ZLIB, and ZSTD required for compressed file I/O.
        depends_on("libtiff+jpeg+libdeflate+zlib+zstd")

        # Historical dependencies
        depends_on("opencv@4.5.5.64:", when="@0.7:0.8.0")
        depends_on("opencv@4.5.4:", when="@0.6")
        depends_on("opencv+imgcodecs+jpeg+png+python3+tiff", when="@:0.8.0")
        # Required to download Google Drive datasets.
        depends_on("py-gdown", when="@:0.8 ^py-torchvision@0.17.1:")
        depends_on("py-pyvista@0.34.2:", when="@0.6")
        depends_on("py-rtree@1.0.1:", when="@0.7")
        depends_on("py-rtree@1:", when="@0.6")

    with when("+docs"), default_args(type="run"):
        depends_on("py-ipywidgets@7:")
        depends_on("py-myst-parser@0.18:", when="@0.8.1:")
        depends_on("py-nbsphinx@0.8.5:")
        depends_on("py-pydata-sphinx-theme@0.14:", when="@0.8.1:")
        depends_on("py-pytorch-sphinx-theme", when="@:0.8.0")
        depends_on("py-sphinx@5.3:", when="@0.8.1:")
        depends_on("py-sphinx@4:5", when="@:0.8.0")
        depends_on("pandoc")

    with when("+models"), default_args(type="run"):
        depends_on("py-microsoft-aurora@1.6:")

    with when("+style"), default_args(type="run"):
        depends_on("prettier@3:")
        depends_on("py-mypy@1.16:", when="@0.8.1:")
        depends_on("py-mypy@0.900:")
        depends_on("py-pandas-stubs@2.1.1:", when="@0.9:")
        depends_on("py-pandas-stubs@1.5:", when="@0.8.1:")
        depends_on("py-ruff@0.9:", when="@0.7:")
        depends_on("py-ruff@0.2:")
        depends_on("py-types-requests@2.25:", when="@0.9:")
        depends_on("py-types-requests@2.23:", when="@0.8.1:")
        depends_on("py-types-shapely@2.0.2:", when="@0.9:")
        depends_on("py-types-shapely@2:", when="@0.8.1:")

    with when("+tests"), default_args(type="run"):
        depends_on("py-nbmake@1.3.3:")
        depends_on("py-packaging@21:", when="@0.9:")
        depends_on("py-packaging@20.9:", when="@0.7.2:")
        depends_on("py-pytest@7.3.2:", when="@0.9:")
        depends_on("py-pytest@7.3:")
        depends_on("py-pytest-cov@4:")
        depends_on("py-pytest-socket@0.3.4:", when="@0.9:")

    # https://github.com/torchgeo/torchgeo/pull/3052
    conflicts("py-lightning@2.5.5:2.5")
    # https://github.com/microsoft/torchgeo/pull/2484
    conflicts("py-lightning@=2.5.0")
    # https://github.com/Lightning-AI/pytorch-lightning/issues/19977
    conflicts("py-lightning@2.3")
    # https://github.com/torchgeo/torchgeo/pull/3311
    conflicts("py-pandas@3:", when="@:0.8.0")
    # https://github.com/rasterio/rasterio/issues/3196
    conflicts("py-rasterio@1.4.0:1.4.2")
