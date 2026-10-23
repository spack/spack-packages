# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMyqlmSimulators(PythonPackage):
    """myQLM-fermion package"""

    homepage = "https://www.bull.com/en/solutions/quantum-computing"
    pypi = "myqlm-simulators/myqlm_simulators-1.11.0-py3-none-any.whl"

    supplier = "Organization: Bull SAS"

    maintainers("LydDeb")

    version("1.11.0", sha256="024393ef02b4520048d63d6430896f54146398cc3384f23eefe8b1fd4bd8260d")

    with default_args(type="run"):
        depends_on("py-qat-core")
        depends_on("py-qat-lang")
        depends_on("py-qat-variational")
        depends_on("py-numpy@2")
