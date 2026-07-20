# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyAuthlib(PythonPackage):
    """The ultimate Python library in building OAuth and OpenID Connect servers.
    JWS, JWK, JWA, JWT are included."""

    homepage = "https://github.com/authlib/authlib"
    pypi = "authlib/authlib-1.6.5.tar.gz"

    license("BSD-3-Clause")
    version("1.6.7", sha256="dbf10100011d1e1b34048c9d120e83f13b35d69a826ae762b93d2fb5aafc337b")
    version("1.6.5", sha256="6aaf9c79b7cc96c900f0b284061691c5d4e61221640a948fe690b556a6d6d10b")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    # in setup.py
    depends_on("py-cryptography@3.2:", type=("build", "run"))
