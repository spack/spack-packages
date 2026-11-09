# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyQiskit(PythonPackage):
    """
    An open-source SDK for working with quantum computers at the level of extended quantum
    circuits, operators, and primitives.
    """

    homepage = "https://www.ibm.com/quantum/qiskit"
    pypi = "qiskit/qiskit-2.5.1.tar.gz"

    supplier = "Organization: Qiskit Development Team"

    maintainers("LydDeb")

    license("Apache-2.0", checked_by="LydDeb")

    version("2.5.1", sha256="923e11f02c6720da4f9435cbfc78b6d2c4a106198175a16d32ae730eaa007fa6")
    version("1.4.6", sha256="e004df4eb0a4bba61e75e6b1d71813341b35f04ccb49673fe62df3ff7f79ba2b")

    with default_args(type="build"):
        depends_on("py-setuptools@77.0:")
        depends_on("py-setuptools-rust@1.13.0:")

    with default_args(type=("build", "run")):
        depends_on("python@3.10:")
        depends_on("py-numpy@2")
        depends_on("py-numpy@1.17:2", when="@1")
        depends_on("py-scipy@1.14:")
        depends_on("py-scipy@1.5:", when="@1")
        depends_on("py-rustworkx@0.15:")
        depends_on("py-dill@0.3:")
        depends_on("py-stevedore@3:")
        depends_on("py-typing-extensions")
        depends_on("py-sympy@1.3:", when="@1")
        depends_on("py-python-dateutil@2.8.0:", when="@1")
