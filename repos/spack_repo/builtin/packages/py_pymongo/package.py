# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPymongo(PythonPackage):
    """The PyMongo distribution contains tools for interacting with
    MongoDB database from Python. The bson package is an implementation
    of the BSON format for Python. The pymongo package is a native
    Python driver for MongoDB. The gridfs package is a gridfs
    implementation on top of pymongo."""

    pypi = "pymongo/pymongo-3.9.0.tar.gz"

    license("Apache-2.0", checked_by="wdconinc")

    version("4.10.1", sha256="a9de02be53b6bb98efe0b9eda84ffa1ec027fcb23a2de62c4f941d9a2f2f3330")

    depends_on("c", type="build")  # generated

    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools@65:", type="build")
    depends_on("py-hatchling@1.24:", type="build")
    depends_on("py-hatch-requirements-txt@0.4.1:", type="build")
    depends_on("py-dnspython@1.16.0:2", type="build")
