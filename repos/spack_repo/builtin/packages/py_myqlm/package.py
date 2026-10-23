# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMyqlm(PythonPackage):
    """
    myQLM is the quantum software stack developed by Bull, for writing, simulating, optimizing,
    and executing quantum program.
    """

    homepage = "https://www.bull.com/en/solutions/quantum-computing"

    pypi = "myqlm/myqlm-1.13.5-py3-none-any.whl"

    supplier = "Organization: Bull SAS"

    maintainers("LydDeb")

    version("1.13.5", sha256="ffe2f297662d40910c4199292314f0f51d4a31028605217196b8488a86f56f48")

    with default_args(type="run"):
        depends_on("py-qat-comm@1.9.0")
        depends_on("py-qat-core@1.13.1")
        depends_on("py-qat-analog@0.8.0")
        depends_on("py-qat-devices@0.6.0")
        depends_on("py-qat-fusion@0.4.0")
        depends_on("py-qat-lang@3.4.0")
        depends_on("py-qat-anapli@0.3.0")
        depends_on("py-qat-variational@1.8.0")
        depends_on("py-qat-pbo@1.7.0")
        depends_on("py-qat-nnize@1.5.0")
        depends_on("py-qat-synthopline@0.6.0")
        depends_on("py-qat-hardware@1.7.2")
        depends_on("py-qat-quops@1.6.0")
        depends_on("py-qlmaas@1.13.4")
        depends_on("py-myqlm-clinalg@0.5.1")
        depends_on("py-myqlm-contrib@1.11.0")
        depends_on("py-myqlm-fermion@1.4.0")
        depends_on("py-qat-linalg-util@1.1.0")
        depends_on("py-myqlm-simulators@1.11.0")
