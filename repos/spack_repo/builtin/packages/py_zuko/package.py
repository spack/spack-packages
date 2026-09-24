# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyZuko(PythonPackage):
    """Normalizing flows in PyTorch."""

    homepage = "https://github.com/probabilists/zuko"
    pypi = "zuko/zuko-1.5.0.tar.gz"

    license("MIT")

    version("1.5.0", sha256="86ae48e3e8fe79841acbc4b2c54502ab22b2ba1a50a646ad7618303718e5c7b1")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools@61:", type="build")

    with default_args(type=("build", "run")):
        depends_on("py-numpy@1.20:")
        depends_on("py-torch@1.12:")
