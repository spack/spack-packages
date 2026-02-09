# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySimsimd(PythonPackage):
    """Portable mixed-precision BLAS-like vector math library for x86 and ARM"""

    homepage = "https://github.com/ashvardanian/simsimd"
    pypi = "simsimd/simsimd-6.5.3.tar.gz"

    license("Apache-2.0")

    version("6.5.8", sha256="0c78cedddf85e9ffa7bc4fdb2e57ebae89ed55367f05acb2c7e1b9c3db6e2ff7")
    version("6.5.3", sha256="5ff341e84fe1c46e7268ee9e31f885936b29c38ce59f423433aef5f4bb5bfd18")

    depends_on("c", type="build")

    depends_on("py-setuptools@42:", type="build")
