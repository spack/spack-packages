# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMffpy(PythonPackage):
    """Reader and Writer for Philips' MFF file format."""

    homepage = "https://github.com/BEL-Public/mffpy"
    pypi = "mffpy/mffpy-0.6.3.tar.gz"

    license("Apache-2.0")

    version("0.11.0", sha256="daaf3d018e7bb4a6827e4bb32d7877a3cc78e1bc97c2b0f3d1027e7ae1724eef")
    version("0.6.3", sha256="fceaf59f5fccb26b6e8a0363579d27e53db547493af353737a24983d95dc012d")

    with default_args(type="build"):
        depends_on("py-setuptools")

    with default_args(type=("build", "run")):
        depends_on("python@3.6:")

        depends_on("py-lxml@4.8:", when="@0.8:")
        depends_on("py-pytz@2019.2:")
        depends_on("py-numpy@1.15.1:")
        depends_on("py-deprecated@1.2.12:")
