# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyArrayApiCompat(PythonPackage):
    """A wrapper around NumPy and other array libraries to make them compatible
    with the Array API standard"""

    homepage = "https://github.com/data-apis/array-api-compat/"
    pypi = "array_api_compat/array_api_compat-1.14.0.tar.gz"

    license("MIT")

    version("1.15.0", sha256="53c5f922491bf15f62847afafc4e39eedfae57d218988fefb8cce39c2a9b3dea")
    version("1.14.0", sha256="c819ba707f5c507800cb545f7e6348ff1ecc46538381d9ad9b371ffc9cd6d784")

    depends_on("python@3.10:", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-meson-python", when="@1.15:")

        # Historical
        depends_on("py-setuptools", when="@:1.14")
        depends_on("py-setuptools-scm", when="@:1.14")
