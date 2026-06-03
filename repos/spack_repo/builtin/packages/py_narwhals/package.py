# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyNarwhals(PythonPackage):
    """Extremely lightweight compatibility layer between dataframe libraries"""

    homepage = "https://github.com/narwhals-dev/narwhals"
    pypi = "narwhals/narwhals-1.8.1.tar.gz"

    license("MIT")

    version("2.19.0", sha256="14fd7040b5ff211d415a82e4827b9d04c354e213e72a6d0730205ffd72e3b7ff")
    version("2.3.0", sha256="b66bc4ab7b6746354f60c4b3941e3ce60c066588c35360e2dc6c063489000a16")
    version("1.38.0", sha256="0a356a21ad00de0db0e631332a823a6a6755544bd10b8e68a02d75029c71392e")
    version("1.8.1", sha256="97527778e11f39a1e5e2113b8fbb9ead788be41c0337f21852e684e378f583e8")

    depends_on("python@3.9:", type=("build", "run"), when="@1.43:")
    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-hatchling", type=("build"))
