# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyQiskitQirAliceBobFork(PythonPackage):
    """Qiskit to QIR translator"""

    homepage = "https://github.com/Alice-Bob-SW/qiskit-qir"
    pypi = "qiskit_qir_alice_bob_fork/qiskit_qir_alice_bob_fork-0.6.1.tar.gz"

    supplier = "Organization: Alice & Bob"

    maintainers("LydDeb")

    license("MIT", checked_by="LydDeb")

    version("0.6.1", sha256="d675a9e900809a85c5da8935145273ca789259e3fd093e8b8be86f3fa17ba356")
    version("0.5.0", sha256="4294e275ae12a13a3ab5ad189961d408b89ba470d7bb4a24b16bb5dc2e372c56")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-wheel@0.38.1:", type="build")

    with default_args(type="build"):
        depends_on("py-setuptools@42:")

    with default_args(type=("build", "run")):
        depends_on("py-qiskit@2.4.0:2", when="@0.6")
        depends_on("py-qiskit@1", when="@0.5")
        depends_on("py-pyqir@0.10")
