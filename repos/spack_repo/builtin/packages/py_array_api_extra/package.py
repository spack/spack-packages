# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyArrayApiExtra(PythonPackage):
    """Extra array functions built on top of the array API standard."""

    homepage = "https://github.com/data-apis/array-api-extra"
    pypi = "array_api_extra/array_api_extra-0.11.4.tar.gz"

    license("MIT")

    version("0.11.4", sha256="66236f72aaa4cdf97a3c5581696e3a9c89513714612a9bc6010e19fad1a22012")

    with default_args(type="build"):
        depends_on("py-meson-python")

    with default_args(type=("build", "run")):
        depends_on("python@3.11:")

        depends_on("py-array-api-compat@0.15:1")
