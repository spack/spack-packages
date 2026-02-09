# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyInquirer(PythonPackage):
    """Collection of common interactive command line user interfaces, based on Inquirer.js."""

    homepage = "https://github.com/magmax/python-inquirer"
    pypi = "inquirer/inquirer-3.1.3.tar.gz"

    license("MIT")

    version("3.1.4", sha256="958dbd5978f173630756a6ed6243acf931e750416eb7a6ed3a0ff13af0fdfcb5")
    version("3.1.3", sha256="aac309406f5b49d4b8ab7c6872117f43bf082a552dc256aa16bc95e16bb58bec")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-poetry-core@1:", type="build")
    depends_on("py-blessed@1.19:", type=("build", "run"))
    depends_on("py-readchar@3.0.6:", type=("build", "run"))
    depends_on("py-python-editor@1.0.4:", type=("build", "run"))
