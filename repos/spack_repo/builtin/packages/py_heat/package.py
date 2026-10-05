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

    maintainers("LeonKaem", "ClaudiaComito", "JuanPedroGHM")

    license("MIT")

    version("1.9.0", sha256="cd5aacd7b8dccb2c47b7c088260503ae1eb1a3138048a4b687f48746f1a7f749")
    version("1.8.0", sha256="f0d64e122c88a44ca27ad60d91cdb7250f97c71c971913302ed90d838d7fd253")

    variant(
        "examples",
        default=False,
        description="include packages need for the examples",
    )
    variant("dev", default=False, description="include packages needed for development")
    variant(
        "docutils",
        default=False,
        description="adding packages for working with documentation",
    )
    variant(
        "hdf5",
        default=False,
        description="Use the py-h5py package needed for HDF5 support",
    )
    variant(
        "netcdf",
        default=False,
        description="Use the py-netcdf4 package needed for NetCDF support",
    )
    variant(
        "zarr",
        default=False,
        description="Use the py-zarr package for Zarr support",
        when="@1.6:",
    )
    variant("pandas", default=False, description="use pandas for analysis", when="@1.9:")

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

        # variants
        depends_on("py-docutils@0.16:", when="+docutils", type=("build", "link", "run"))
        depends_on("py-h5py@2.8.0:", when="+hdf5", type=("build", "link", "run"))
        depends_on("py-netcdf4@1.5.6:", when="+netcdf", type=("build", "link", "run"))
        depends_on("py-zarr", when="+zarr", type=("build", "link", "run"))
        depends_on("py-pre-commit@1.18.3:", when="+dev", type=("build", "link", "run"))
        depends_on("py-scikit-learn@0.24.0:", when="+examples", type=("build", "link", "run"))
        depends_on("py-matplotlib@3.1.0:", when="+examples", type=("build", "link", "run"))

    with when("@1.9"):
        depends_on("python@3.12:", type=("build", "run"))
        depends_on("py-mpi4py@3.1:", type=("build", "run"))
        depends_on("py-scipy@1.15:1.18.0", type=("build", "run"))
        depends_on("py-torchvision@0.21:0.29.1", type=("build", "run"))
        depends_on("py-torch@2.6:2.14.1", type=("build", "run"))
        depends_on("py-numpy@2.2.0:2.5.0", type=("build", "run"))
        depends_on("py-packaging@25.0:", type=("build", "run"))

        depends_on("py-zarr@:3.2", when=("+zarr"), type=("build", "link", "run"))
        depends_on("py-h5py@3.11:", when=("+hdf5"), type=("build", "link", "run"))
        depends_on("py-netcdf4@1.7:", when=("+netcdf"), type=("build", "link", "run"))
        depends_on("py-pandas@2.3.0:", when=("+pandas"), type=("build", "link", "run"))

        with when("+examples"):
            depends_on("pil@6:", type=("build", "run"))
            depends_on("py-scikit-learn@1.6.0:1.9.0", type=("build", "link", "run"))
            depends_on("py-matplotlib@3.8.0:", type=("build", "link", "run"))
            depends_on("py-jupyter", type=("build", "link", "run"))
            depends_on("py-ipyparallel", type=("build", "link", "run"))
            depends_on("py-h5py@3.11:", type=("build", "link", "run"))

        with when("+dev"):
            depends_on("py-pre-commit", type=("build", "link", "run"))
            depends_on("py-ruff", type=("build", "link", "run"))
            depends_on("py-mypy", type=("build", "link", "run"))
            depends_on("py-pytest", type=("build", "link", "run"))
            depends_on("py-coverage", type=("build", "link", "run"))
            # runnning tests
            depends_on("py-h5py@3.11", type=("build", "link", "run"))
            depends_on("py-netcdf4@1.7:", type=("build", "link", "run"))
            depends_on("py-zarr@3.0:3.2", type=("build", "link", "run"))
            depends_on("py-pandas@2.3.0:", type=("build", "link", "run"))
            depends_on("py-scikit-learn@1.6.0:1.9.0", type=("build", "link", "run"))

        with when("+docutils"):
            depends_on("py-sphinx", type=("build", "link", "run"))
            depends_on("py-sphinx-rtd-theme", type=("build", "link", "run"))
            depends_on("py-sphinx-autoapi", type=("build", "link", "run"))
            depends_on("py-nbsphinx", type=("build", "link", "run"))
            depends_on("py-sphinx-copybutton", type=("build", "link", "run"))
            depends_on("py-myst-parser", type=("build", "link", "run"))
            depends_on("py-sphinxcontrib-mermaid", type=("build", "link", "run"))
            depends_on("py-sphinx-design", type=("build", "link", "run"))
            depends_on("py-pydata-sphinx-theme", type=("build", "link", "run"))

    # specify differences cuda vs rocm
    with when("+cuda"):
        depends_on("py-torch+cuda", type=("build", "run"))

    with when("+rocm"):
        depends_on("py-torch+rocm", type=("build", "run"))

    conflicts("+cuda+rocm")
