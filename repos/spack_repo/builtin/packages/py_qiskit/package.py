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

    with default_args(type="build"):
        depends_on("py-setuptools@77.0:")
        depends_on("py-setuptools-rust@1.13.0:")

    with default_args(type=("build", "run")):
        depends_on("python@3.10:")
        depends_on("py-numpy@2")
        depends_on("py-scipy@1.14:")
        depends_on("py-rustworkx@0.15:")
        depends_on("py-dill@0.3:")
        depends_on("py-stevedore@3:")
        depends_on("py-typing-extensions")
