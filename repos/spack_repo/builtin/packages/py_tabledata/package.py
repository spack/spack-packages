# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTabledata(PythonPackage):
    """tabledata is a Python library to represent tabular data."""

    homepage = "https://github.com/thombashi/tabledata"
    pypi = "tabledata/tabledata-1.3.4.tar.gz"

    license("MIT")

    version("1.3.4", sha256="e9649cab129d718f3bff4150083b77f8a78c30f6634a30caf692b10fdc60cb97")

    with default_args(type="build"):
        depends_on("py-setuptools@64:")
        depends_on("py-setuptools-scm@8:")

    with default_args(type=("build", "run")):
        depends_on("py-dataproperty@1.0.1:1")
        depends_on("py-typepy@1.2:1")
