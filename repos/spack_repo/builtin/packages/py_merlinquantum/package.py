# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMerlinquantum(PythonPackage):
    """Quantum neural network models using photonic circuits - Preview"""

    homepage = "https://merlinquantum.ai"
    pypi = "merlinquantum/merlinquantum-0.4.0-py3-none-any.whl"

    supplier = "Organization: quandelaOSS"

    maintainers("LydDeb")

    license("MIT", checked_by="LydDeb")

    version("0.4.0", sha256="c496fe9b1c6ecabb8155b1589a255f5d69095166592481c09e00007a6840ae05")

    depends_on("python@3.10:", type=("build", "run"))

    with default_args(type=("build", "run")):
        depends_on("py-torch@2:2.13")
        depends_on("py-perceval-quandela@1.2.1:")
        depends_on("py-numpy@2.2.6:")
        depends_on("py-pandas")
        depends_on("py-scikit-learn@1.7.2:1.9")
