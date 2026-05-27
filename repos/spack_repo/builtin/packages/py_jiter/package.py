# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyJiter(PythonPackage):
    """Fast iterable JSON parser."""

    homepage = "https://github.com/pydantic/jiter/"
    pypi = "jiter/jiter-0.5.0.tar.gz"

    license("MIT", checked_by="qwertos")

    version("0.13.0", sha256="f2839f9c2c7e2dffc1bc5929a510e14ce0a946be9365fd1219e7ef342dae14f4")
    version("0.5.0", sha256="1d916ba875bcab5c5f7d927df998c4cb694d27dceddf3392e58beaf10563368a")

    depends_on("python@3.9:", when="@0.10:", type=("build", "run"))
    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-maturin@1.9.4:1", when="@0.11:", type="build")
    depends_on("py-maturin@1", type="build")
    depends_on("rust@1.73:", type=("build", "run"))
