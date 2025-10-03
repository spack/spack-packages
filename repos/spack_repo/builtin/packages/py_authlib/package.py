# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyAuthlib(PythonPackage):
    """ The ultimate Python library in building OAuth and OpenID Connect servers. JWS, JWK, JWA, JWT are included. """

    homepage = "https://github.com/authlib/authlib"
    pypi = "authlib/authlib-1.6.5.tar.gz"

    license("BSD-3-Clause")
    version("1.6.5", sha256="6aaf9c79b7cc96c900f0b284061691c5d4e61221640a948fe690b556a6d6d10b")

    depends_on("py-setuptools", type="build")
    depends_on("py-cryptography", type=("build", "run"))