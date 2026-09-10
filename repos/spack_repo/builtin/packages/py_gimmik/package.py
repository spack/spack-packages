# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyGimmik(PythonPackage):
    """Generator of Matrix Multiplication Kernels - GiMMiK - is a tool for generation of
    high performance matrix multiplication kernel code.
    for various accelerator platforms."""

    homepage = "https://github.com/PyFR/GiMMiK"
    pypi = "gimmik/gimmik-2.2.tar.gz"

    maintainers("MichaelLaufer")

    license("BSD-3-Clause")

    version("3.2.1", sha256="048644bd71497eb07e144f2c22fdee49ba23e1cde5fb954c3c30c4e3ea23687a")
    version("3.0", sha256="45c2da7acff3201b7796ba731e4be7f3b4f39469ff1f1bc0ddf4f19c4a6af010")

    depends_on("py-setuptools", type="build")
    depends_on("py-numpy@1.7:", type=("build", "run"))
    depends_on("py-mako", type=("build", "run"))
