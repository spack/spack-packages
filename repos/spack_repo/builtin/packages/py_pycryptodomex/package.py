# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPycryptodomex(PythonPackage):
    """Cryptographic library for Python."""

    homepage = "https://www.pycryptodome.org/"
    pypi = "pycryptodomex/pycryptodomex-3.23.0.tar.gz"

    license("BSD-2-Clause")

    version("3.23.0", sha256="71909758f010c82bc99b0abf4ea12012c98962fbf0583c2164f8b84533c2e4da")

    depends_on("python", type=("build", "link", "run"))
    depends_on("c", type="build")
    depends_on("py-setuptools", type="build")
