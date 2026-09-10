# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyDataproperty(PythonPackage):
    """Python library for extract property from data."""

    homepage = "https://github.com/thombashi/DataProperty"
    pypi = "dataproperty/dataproperty-1.1.0.tar.gz"

    license("MIT")

    version("1.1.0", sha256="b038437a4097d1a1c497695c3586ea34bea67fdd35372b9a50f30bf044d77d04")

    with default_args(type="build"):
        depends_on("py-setuptools@64:")
        depends_on("py-setuptools-scm@8:")

    with default_args(type=("build", "run")):
        depends_on("py-mbstrdecoder@1")
        depends_on("py-typepy@1.3.2:1+datetime")
