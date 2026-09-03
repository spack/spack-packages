# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyHeat(PythonPackage):
    """Heat is a distributed tensor framework built on PyTorch and mpi4py. It provides
    highly optimized algorithms and data structures for tensor computations using
    CPUs, GPUs (CUDA/ROCm), and distributed cluster systems. It is designed to
    handle massive arrays that exceed the memory and computational limits of a
    single machine."""

    homepage = "https://github.com/helmholtz-analytics/heat/"
    pypi = "heat/heat-1.3.0.tar.gz"

    maintainers("ClaudiaComito", "JuanPedroGHM", "LeonKaem")

    license("MIT")

    version("1.8.0", sha256="f0d64e122c88a44ca27ad60d91cdb7250f97c71c971913302ed90d838d7fd253")

    variant("docutils", default=False, description="Use the py-docutils package")
    variant("hdf5", default=False, description="Use the py-h5py package needed for HDF5 support")
    variant(
        "netcdf", default=False, description="Use the py-netcdf4 package needed for NetCDF support"
    )
    variant(
        "zarr", default=False, description="Use the py-zarr package for Zarr support"
    )
    variant("dev", default=False, description="Use the py-pre-commit package")
    variant(
        "examples",
        default=False,
        description="Use py-scikit-learn and py-matplotlib for the example tests",
    )
    variant("cuda", default=False, description="build Py_Torch dependency with cuda support")
    variant("rocm", default=False, description="build Py_Torch dependency with rocm support")

    depends_on("py-setuptools", type="build")

    # dependencies per major version, sourced from setup.py or pyproject.toml
    with when("@1.8"):
        depends_on("python@3.11:", type=("build", "run"))
        depends_on("py-mpi4py@3.1:", type=("build", "run"))
        depends_on("py-scipy@1.14:", type=("build", "run"))
        depends_on("pil@6:", when=("+examples"), type=("build", "run"))
        depends_on("py-torchvision@0.18:", type=("build", "run"))
        depends_on("py-torch@2.3:2.11.0", type=("build", "run"))

    # specify differences cuda vs rocm
    with when("+cuda"):
        depends_on("py-torch+cuda", type=("build", "run"))

    with when("+rocm"):
        depends_on("py-torch+rocm", type=("build", "run"))

    # additional variants
    depends_on("py-docutils@0.16:", when="+docutils", type=("build", "link", "run"))
    depends_on("py-h5py@2.8.0:", when="+hdf5", type=("build", "link", "run"))
    depends_on("py-netcdf4@1.5.6:", when="+netcdf", type=("build", "link", "run"))
    depends_on("py-zarr", when="+zarr", type=("build", "link", "run"))
    depends_on("py-pre-commit@1.18.3:", when="+dev", type=("build", "link", "run"))
    depends_on("py-scikit-learn@0.24.0:", when="+examples", type=("build", "link", "run"))
    depends_on("py-matplotlib@3.1.0:", when="+examples", type=("build", "link", "run"))

    conflicts("+cuda+rocm")
