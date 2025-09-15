# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyCfXarray(PythonPackage):
    """A convenience wrapper for using CF attributes on xarray objects."""

    homepage = "https://cf-xarray.readthedocs.io/"
    pypi = "cf_xarray/cf_xarray-0.9.0.tar.gz"

    license("Apache-2.0")

    version("0.10.6", sha256="159236eca465453784ee7efa2a430d5e2092978db8a5d4d8b591f61d0639cb89")
    version("0.10.5", sha256="4aa629cd9e8c3e53253270e48a6080e62065b78c4e597f01c80b5f5b372d2331")
    version("0.10.4", sha256="047dd732cc7f154c7aa9d5c00b77c64e2c538258f0b6e7565a4b2c7715ee8aba")
    version("0.10.3", sha256="009143716ae1f49dc5d37624d7b6e1b0ec424b0a892a84f8f0a85e0970dc3453")
    version("0.10.2", sha256="9d2391cb3f4a2572fa42a3ab3cfdb6e6949ac0cd12b9652d607c1054d68a4412")
    version("0.10.1", sha256="dd0fc3091feef78f319cea32ec3b78ea5468a7e80e4b96243de8eda24f8b727c")
    version("0.10.0", sha256="7b45319fc315175854c9e701a84ebb795eb4b2764a2d05bd2d9d3ea87d004d18")
    version("0.9.0", sha256="01213bdc5ed4d41eeb5da179d99076f49a905b1995daef2a0c7ec402b148675c")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("python@3.10:", type=("build", "run"), when="@0.9.5:")
    depends_on("py-setuptools@45:", type="build")
    depends_on("py-setuptools-scm@6.2:+toml", type="build")
    depends_on("py-xarray@2023.09.0:", type=("build", "run"), when="@0.10.2:")
    depends_on("py-xarray@2022.03.0:", type=("build", "run"), when="@0.9:0.10.1")
