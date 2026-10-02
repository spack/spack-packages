# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMyqlmFermion(PythonPackage):
    """myQLM-fermion package"""

    homepage = "https://www.bull.com/en/solutions/quantum-computing"
    pypi = "myqlm-fermion/myqlm_fermion-1.4.0-py3-none-any.whl"

    supplier = "Organization: Bull SAS"

    maintainers("LydDeb")

    version("1.4.0", sha256="e8f4521900294256057faacb89bab0c718274b78af3bb27d30aa8bbda41e2a55")

    with default_args(type="run"):
        depends_on("py-qat-core")
        depends_on("py-qat-lang")
        depends_on("py-anytree")
        depends_on("py-bitstring")
        depends_on("py-numpy@2")
        depends_on("py-scipy")
        depends_on("py-tqdm")
