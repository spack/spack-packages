# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyQoolqit(PythonPackage):
    """A Python library for developing algorithms in the Rydberg Analog Model."""

    homepage = "https://github.com/pasqal-io/qoolqit"
    pypi = "qoolqit/qoolqit-1.3.0.tar.gz"

    supplier = "Organization: Pasqal SAS"

    maintainers("LydDeb")

    license("MIT", checked_by="LydDeb")

    version("1.3.0", sha256="ee3c818d7f047212a0919c3040a0dca64abc419c2a6cdd9b4666eb5b335a863e")

    with default_args(type=("build", "run")):
        depends_on("python@3.10:", type=("build", "run"))
        depends_on("py-networkx@3.4:")
        depends_on("py-numpy@2:")
        depends_on("py-pulser@1.9.0: +torch")
