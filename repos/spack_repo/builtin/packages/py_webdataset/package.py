# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyWebdataset(PythonPackage):
    """Python-based I/O for deep learning problems."""

    homepage = "https://github.com/webdataset/webdataset"
    pypi = "webdataset/webdataset-0.1.62.tar.gz"

    license("BSD-3-Clause")
    maintainers("adamjstewart")

    version("1.0.2", sha256="7f0498be827cfa46cc5430a58768a24e2c6a410676a61be1838f53d61afdaab4")

    depends_on("py-setuptools@45:", type="build")

    with default_args(type=("build", "run")):
        depends_on("python@3.10:")
        depends_on("py-braceexpand")
        depends_on("py-numpy")
        depends_on("py-pyyaml")
