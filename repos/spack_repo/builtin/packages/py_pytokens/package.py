# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPytokens(PythonPackage):
    """A Fast, spec compliant Python 3.14+ tokenizer that runs on older Pythons."""

    homepage = "https://github.com/tusharsadhwani/pytokens"
    pypi = "pytokens/pytokens-0.4.1.tar.gz"

    license("MIT")

    version("0.4.1", sha256="292052fe80923aae2260c073f822ceba21f3872ced9a68bb7953b348e561179a")

    with default_args(type="build"):
        depends_on("c")
        depends_on("py-setuptools@69:")
        depends_on("py-mypy")

    depends_on("python", type=("build", "link", "run"))
