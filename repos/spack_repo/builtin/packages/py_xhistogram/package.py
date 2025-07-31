# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyXhistogram(PythonPackage):
    """Fast, flexible, label-aware histograms for numpy and xarray."""

    homepage = "https://github.com/xgcm/xhistogram"
    pypi = "xhistogram/xhistogram-0.3.2.tar.gz"

    license("MIT")

    version("0.3.2", sha256="56b0751e1469eaed81710f644c8ba5c574b51883baa2feee26a95f2f708f91a1")

    depends_on("py-setuptools", type="build")
    depends_on("py-versioneer", type="build")
    depends_on("py-versioneer@0.29:", type="build", when="^python@3.12:")

    depends_on("py-xarray@0.12:", type=("build", "run"))
    depends_on("py-dask@2.3:+array", type=("build", "run"))
    depends_on("py-numpy@1.17:", type=("build", "run"))

    # compatibility with python 3.12
    patch("https://github.com/xgcm/xhistogram/commit/6eef6c697d95ea70883a5ff6ee2f3e7188eaa4c5.patch",
          sha256="2a508aded3ac57dfe7c87ff3e27124400daf04391759009fea209ce5cb0067fe",
          when="^python@3.12")
