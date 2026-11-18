# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyFelis(PythonPackage):
    """Felis documentation and samples"""

    homepage = "https://github.com/Alice-Bob-SW/felis"

    url = "https://github.com/Alice-Bob-SW/felis/archive/refs/tags/v1.2.0.tar.gz"

    supplier = "Organization: Alice & Bob"

    maintainers("LydDeb")

    license("Apache-2.0", checked_by="LydDeb")

    version("1.2.0", sha256="6d3b3480eaccbe41b9a548f0b92322361d67dda483a64493a5f4f65f512b39ec")

    depends_on("python@3.9:3.13", type=("build", "run"))

    with default_args(type=("build", "run")):
        depends_on("py-matplotlib@3.9")
        depends_on("py-pylatexenc@2.10")
        depends_on("py-qiskit-algorithms@0.3")
        depends_on("py-qiskit-alice-bob-provider@1.2")
        depends_on("py-qrisp@0.5.4:0.5")
        depends_on("py-scikit-learn@1.6")
        depends_on("py-tqdm@4.67")
        depends_on("py-tweedledum")
