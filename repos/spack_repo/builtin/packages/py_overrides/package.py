# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyOverrides(PythonPackage):
    """A decorator to automatically detect mismatch when overriding a method."""

    homepage = "https://github.com/mkorpela/overrides"
    pypi = "overrides/overrides-7.3.1.tar.gz"

    license("Apache-2.0")

    version("7.7.0", sha256="55158fa3d93b98cc75299b1e67078ad9003ca27945c76162c1c0766d6f91820a")
    version("7.3.1", sha256="8b97c6c1e1681b78cbc9424b138d880f0803c2254c5ebaabdde57bb6c62093f2")

    depends_on("py-setuptools", type="build")
