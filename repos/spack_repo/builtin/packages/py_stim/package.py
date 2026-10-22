# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyStim(PythonPackage):
    """A fast library for analyzing with quantum stabilizer circuits."""

    homepage = "https://github.com/quantumlib/stim"
    pypi = "stim/stim-1.16.0.tar.gz"

    supplier = "Person: Craig Gidney"

    maintainers("LydDeb")

    license("Apache-2.0", checked_by="LydDeb")

    version("1.16.0", sha256="9092a996429dcf616d8d4ca01fec886b7b310caf9425a39fcfe499005636bd52")

    with default_args(type="build"):
        depends_on("cxx")
        depends_on("py-setuptools")
        depends_on("py-pybind11@2.11.1:2")

    with default_args(type=("build", "run")):
        depends_on("py-numpy")
