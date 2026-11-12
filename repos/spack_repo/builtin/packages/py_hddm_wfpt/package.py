# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyHddmWfpt(PythonPackage):
    """HDDM is a python module that implements Hierarchical Bayesian estimation
    of Drift Diffusion Models."""

    homepage = "https://github.com/lnccbrown/hddm-wfpt"
    pypi = "hddm_wfpt/hddm_wfpt-0.1.7.tar.gz"

    license("BSD-2-Clause")

    version("0.1.7", sha256="f55a21a5e7cce14a1185ba68b4fca0933741f7df14a51d1e9f34667fe6632d82")

    with default_args(type="build"):
        depends_on("c")
        depends_on("cxx")

        depends_on("py-setuptools")
        depends_on("py-cython@3:")

    with default_args(type=("build", "run")):
        depends_on("python@3.10:3.14")

        depends_on("py-numpy@2:")
        depends_on("py-scipy@1.15.2:")
