# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyQrisp(PythonPackage):
    """A high-level quantum programming language"""

    homepage = "https://github.com/fraunhoferfokus/Qrisp"
    pypi = "qrisp/qrisp-0.5.4.tar.gz"

    supplier = "Person: Raphael Seidel"

    maintainers("LydDeb")

    license("EPL-2.0", checked_by="LydDeb")

    version("0.5.4", sha256="faa39059eec8eb50a937378a752c5781023ff07a0974d9880c0bd924a75661bb")

    depends_on("python@3.8:", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-setuptools")

    with default_args(type=("build", "run")):
        depends_on("py-qiskit@0.44.0:")
        depends_on("py-matplotlib@3.5.1:")
        depends_on("py-scipy@1.10.0:")
        depends_on("py-numba")
        depends_on("py-networkx")
        depends_on("py-tqdm")
        depends_on("py-dill")
        depends_on("py-flask")
        depends_on("py-waitress")
        depends_on("py-pyyaml")
        depends_on("py-requests")
        depends_on("py-psutil")
