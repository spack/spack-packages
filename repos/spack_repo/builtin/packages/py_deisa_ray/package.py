# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyDeisaRay(PythonPackage):
    """In Situ Analytics with Ray backend."""

    homepage = "https://github.com/deisa-project/deisa-ray"
    pypi = "deisa_ray/deisa_ray-0.1.7.tar.gz"

    license("MIT")

    version("0.1.7", sha256="b2d0d020882a3ee557df2ddbcc33715fedb7dd848e0248591778909b7d133705")

    depends_on("py-hatchling", type="build")
    depends_on("python@3.12:", type=("build", "run"))
    depends_on("py-dask@2025.5.0 +dataframe", type=("build", "run"))
    depends_on("py-ray@2.48: +default", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-h5py@3.15.1:", type=("build", "run"))
    depends_on("py-zarr@3.1.5:", type=("build", "run"))
    depends_on("py-xarray", type=("build", "run"))
    depends_on("py-h5netcdf", type=("build", "run"))
    depends_on("py-deisa-core@0.5:", type=("build", "run"))
