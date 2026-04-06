# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyCbor2(PythonPackage):
    """CBOR (de)serializer with extensive tag support"""

    pypi = "cbor2/cbor2-5.6.5.tar.gz"

    license("MIT")

    version("5.6.5", sha256="b682820677ee1dbba45f7da11898d2720f92e06be36acec290867d5ebf3d7e09")

    # https://github.com/agronholm/cbor2/blob/5.6.5/pyproject.toml
    depends_on("py-setuptools@61:", type="build")
    depends_on("py-setuptools-scm@6.4:", type="build")
