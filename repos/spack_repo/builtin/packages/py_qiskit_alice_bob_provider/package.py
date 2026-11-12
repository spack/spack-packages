# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyQiskitAliceBobProvider(PythonPackage):
    """Provider for running Qiskit circuits on Alice & Bob QPUs and simulators"""

    homepage = "https://github.com/Alice-Bob-SW/qiskit-alice-bob-provider"
    pypi = "qiskit_alice_bob_provider/qiskit_alice_bob_provider-1.2.0.tar.gz"

    supplier = "Organization: Alice & Bob"

    maintainers("LydDeb")

    license("Apache-2.0", checked_by="LydDeb")

    version("1.2.0", sha256="c8e0453d6b74d6e6f7ade37b285ea0f93f6c88d04ba6a2f225ac567fb07e9a22")

    depends_on("python@3.9:3.13", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-setuptools@42:")

    with default_args(type=("build", "run")):
        depends_on("py-ipython")
        depends_on("py-ipywidgets")
        depends_on("py-pydantic@2.0:")
        depends_on("py-requests@1.26:")
        depends_on("py-qiskit@1.3.1:2")
        depends_on("py-qiskit-aer@0.16.1:0.17")
        depends_on("py-qiskit-qir-alice-bob-fork@0.5.0")
        depends_on("py-tenacity")
