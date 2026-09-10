# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyJmespath(PythonPackage):
    """JSON Matching Expressions."""

    homepage = "https://github.com/jmespath/jmespath.py"
    pypi = "jmespath/jmespath-0.9.4.tar.gz"

    license("MIT")

    version("1.1.0", sha256="472c87d80f36026ae83c6ddd0f1d05d4e510134ed462851fd5f754c8c3cbb88d")
    version("1.0.1", sha256="90261b206d6defd58fdd5e85f478bf633a2901798906be2ad389150c5c60edbe")
    version("0.10.0", sha256="b85d0567b8666149a93172712e68920734333c0ce7e89b78b3e987f71e5ed4f9")
    version("0.9.4", sha256="bde2aef6f44302dfb30320115b17d030798de8c4110e28d5cf6cf91a7a31074c")

    depends_on("py-setuptools", type="build")

    with default_args(type=("build", "run")):
        depends_on("python@3.9:", when="@1.1:")
        depends_on("python@3.7:", when="@1:")
