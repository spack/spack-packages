# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyVesinTorch(PythonPackage):
    """Computing neighbor lists for atomistic system."""

    homepage = "https://luthaf.fr/vesin/latest/index.html"
    pypi = "vesin-torch/vesin-torch-0.3.7.tar.gz"

    import_modules = ["vesin.torch"]

    maintainers("HaoZeke", "luthaf", "rmeli")
    license("BSD-3-Clause", checked_by="HaoZeke")

    version("0.3.7", sha256="37504d17c9850ec696d1b2c1ce65d6735a35a3e1becdf3f94f1be7de1521512e")

    # pyproject.toml
    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-setuptools@77:", type="build")
    depends_on("py-wheel@0.41:", type="build")
    depends_on("cmake@3.16:", type="build")
    # setup.py
    depends_on("py-torch@2.3:", type=("build", "run"))
