# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyNumpyIndexed(PythonPackage):
    """This package contains functionality for indexed operations on numpy ndarrays,
    providing efficient vectorized functionality such as grouping and set operations."""

    homepage = "https://github.com/EelcoHoogendoorn/Numpy_arraysetops_EP"
    url = (
        "https://pypi.io/packages/py2.py3/n/numpy_indexed/numpy_indexed-0.3.7-py2.py3-none-any.whl"
    )

    version("0.3.7", sha256="3e9f8f5ca453e49809618b3717b8ce07551b616a4ae43069c46aaad286386a9e")

    depends_on("py-setuptools", type="build")

    depends_on("python@3.5:", type=("build", "run"))

    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-future", type=("build", "run"))
