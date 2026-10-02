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
    version("1.7.0", sha256="1d787cc5f52fc2123bb69e6e2ee53b268b258abe4ed5be99e53706bcb250175c")
    version("1.6.0", sha256="cd011e67c284b7f94d0f1c6ff8bf5309535fa26a895b0db2df83290c47dae55b")
    version("1.5.1", sha256="95fea9daec6c2d5f0453159dbcd5efb26cb23997f0981e49fe9793a2fd342313")
    version("1.5.0", sha256="a2e2d7f0c1f340ab2597f2b9c02563f0057419a53287fbf4cdf1a7934bc6d60b")
    version("1.4.2", sha256="d6714428a9c5204c1c44a2b246f228effaddc688f812277f229f4acdbcfeb7c5")
    version("1.4.1", sha256="ecd871717c372a6983f643c0178dda44bc017d6b32b9258dbf3775af95f580ce")
    version("1.4.0", sha256="6836fa10f9ce62ea61cf1bdc3283d7ad0c305836cc5a08c4edfd30695708e788")
    version("1.3.1", sha256="8997ddc56a1d3078b44a1e2933adc0a7fbf678bd19bade3ae015bc0e13d40d3b")
    version("1.3.0", sha256="fa247539a559881ffe574a70227d3c72551e7c4a9fb29b0945578d6a840d1c87")

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
    with when("@1.3"):
        depends_on("python@3.8:3.10", type=("build", "run"))
        depends_on("py-mpi4py@3:", type=("build", "run"))
        depends_on("py-numpy@1.20:1", type=("build", "run"))
        depends_on("py-scipy@0.14:", type=("build", "run"))
        depends_on("pil@6:", type=("build", "run"))
        depends_on("py-torchvision@0.8:", type=("build", "run"))
        depends_on("py-torch@1.8:2.0.1", type=("build", "run"))

    with when("@1.4"):
        depends_on("python@3.8:3.11", type=("build", "run"))
        depends_on("py-mpi4py@3:", type=("build", "run"))
        depends_on("py-numpy@1.22:1", type=("build", "run"))
        depends_on("py-scipy@1.10:", type=("build", "run"))
        depends_on("pil@6:", type=("build", "run"))
        depends_on("py-torchvision@0.12:", type=("build", "run"))
        depends_on("py-torch@1.11:2.3.2", type=("build", "run"))

    with when("@1.5"):
        depends_on("python@3.9:3.12", type=("build", "run"))
        depends_on("py-mpi4py@3:", type=("build", "run"))
        depends_on("py-numpy@1.22:1", type=("build", "run"))
        depends_on("py-scipy@1.10:", type=("build", "run"))
        depends_on("pil@6:", type=("build", "run"))
        depends_on("py-typing-extensions", type=("build", "run"))
        depends_on("py-torchvision@0.15.2:0.21.1", type=("build", "run"))
        depends_on("py-torch@2.0:2.6.1", type=("build", "run"))

    with when("@1.6"):
        depends_on("python@3.10:", type=("build", "run"))
        depends_on("py-mpi4py@3:", type=("build", "run"))
        depends_on("py-scipy@1.14:", type=("build", "run"))
        depends_on("pil@6:", when=("+examples"), type=("build", "run"))
        depends_on("py-typing-extensions", type=("build", "run"))
        depends_on("py-torchvision@0.15:", type=("build", "run"))
        depends_on("py-torch@2.0:2.8.0", type=("build", "run"))

    with when("@1.7"):
        depends_on("python@3.10:", type=("build", "run"))
        depends_on("py-mpi4py@3.0.0:", type=("build", "run"))
        depends_on("py-scipy@1.14:", type=("build", "run"))
        depends_on("pil", when="+examples", type=("build", "run"))
        depends_on("py-torchvision@0.15:", type=("build", "run"))
        depends_on("py-torch@2.0:2.9", type=("build", "run"))

    with when("@1.8"):
        depends_on("python@3.11:", type=("build", "run"))
        depends_on("py-mpi4py@3.1:", type=("build", "run"))
        depends_on("py-scipy@1.14:", type=("build", "run"))
        depends_on("pil@6:", when=("+examples"), type=("build", "run"))
        depends_on("py-torchvision@0.18:", type=("build", "run"))
        depends_on("py-torch@2.3:2.11.0", type=("build", "run"))

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

    # additional variants till 1.8
    with when("@:1.8"):
        depends_on("py-docutils@0.16:", when="+docutils", type=("build", "link", "run"))
        depends_on("py-h5py@2.8.0:", when="+hdf5", type=("build", "link", "run"))
        depends_on("py-netcdf4@1.5.6:", when="+netcdf", type=("build", "link", "run"))
        depends_on("py-zarr", when="+zarr", type=("build", "link", "run"))
        depends_on("py-pre-commit@1.18.3:", when="+dev", type=("build", "link", "run"))
        depends_on("py-scikit-learn@0.24.0:", when="+examples", type=("build", "link", "run"))
        depends_on("py-matplotlib@3.1.0:", when="+examples", type=("build", "link", "run"))

    conflicts("+cuda+rocm")
