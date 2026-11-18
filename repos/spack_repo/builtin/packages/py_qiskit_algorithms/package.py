# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyQiskitAlgorithms(PythonPackage):
    """Qiskit Algorithms: A library of quantum computing algorithms"""

    homepage = "https://github.com/qiskit-community/qiskit-algorithms"
    pypi = "qiskit_algorithms/qiskit_algorithms-0.3.1.tar.gz"

    supplier = "Organization: Qiskit Algorithms Development Team"

    maintainers("LydDeb")

    license("Apache-2.0", checked_by="LydDeb")

    version("0.3.1", sha256="cba9c573d47c0f9508745a5a2794298084ec4f8833781b426fa9b2cea0fca794")

    depends_on("python@3.8:", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-setuptools")

    with default_args(type=("build", "run")):
        depends_on("py-qiskit@0.44:")
        depends_on("py-scipy@1.4:")
        depends_on("py-numpy@1.17:")
