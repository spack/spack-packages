# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyXgcm(PythonPackage):
    """General Circulation Model Postprocessing with xarray."""

    homepage = "https://github.com/xgcm/xgcm"
    pypi = "xgcm/xgcm-0.8.1.tar.gz"

    maintainers("LydDeb")

    license("MIT", checked_by="LydDeb")

    version("0.8.1", sha256="fc733bf1ed5c1e286dddd182d37dabbdc1e01207dd15089f62be2021e29b0459")

    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools-scm", type="build")
    depends_on("py-xarray@0.20.0:", type=("build", "run"))
    depends_on("py-dask", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-future", type=("build", "run"))
