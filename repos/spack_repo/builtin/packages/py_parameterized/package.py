# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyParameterized(PythonPackage):
    """Parameterized testing with any Python test framework."""

    homepage = "https://github.com/wolever/parameterized"
    pypi = "parameterized/parameterized-0.8.1.tar.gz"

    version("0.9.0", sha256="7fc905272cefa4f364c1a3429cbbe9c0f98b793988efb5bf90aac80f08db09b1")
    version("0.8.1", sha256="41bbff37d6186430f77f900d777e5bb6a24928a1c46fb1de692f8b52b8833b5c")

    depends_on("py-setuptools@57:", type="build")

    with when("@0.9.0:"):
        depends_on("python@3.7:")
        depends_on("py-setuptools@61.2:", type="build")
