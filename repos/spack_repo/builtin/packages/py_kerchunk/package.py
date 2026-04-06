# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyKerchunk(PythonPackage):
    """Kerchunk is a library that provides a unified way to represent a variety of chunked,
    compressed data formats (e.g. NetCDF, HDF5, GRIB), allowing efficient access to the data
    from traditional file systems or cloud object storage. It also provides a flexible way
    to create virtual datasets from multiple files. It does this by extracting the byte ranges,
    compression information and other information about the data and storing this metadata in a
    new, separate object. This means that you can create a virtual aggregate dataset over
    potentially many source files, for efficient, parallel and cloud-friendly in-situ access
    without having to copy or translate the originals. It is a gateway to in-the-cloud massive
    data processing while the data providers still insist on using legacy formats for archival
    storage."""

    homepage = "https://github.com/fsspec/kerchunk"
    pypi = "kerchunk/kerchunk-0.2.9.tar.gz"

    license("MIT", checked_by="Chrismarsh")
    maintainers("Chrismarsh")

    version("0.2.9", sha256="86a54da9a57a94fd6fb97be786e2d83182d3d8e4fd7c0ea2b67cde3d0641df7d")

    depends_on("python@3.11:", type=("build", "run"))
    depends_on("py-setuptools@42:", type="build")
    depends_on("py-setuptools-scm@7:", type="build")

    depends_on("py-fsspec@2025.2.0:", type=("build", "run"))
    depends_on("py-numcodecs", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-ujson", type=("build", "run"))
    depends_on("py-zarr@3.0.1:", type=("build", "run"))
