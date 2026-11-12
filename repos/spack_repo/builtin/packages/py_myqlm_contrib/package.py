# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMyqlmContrib(PythonPackage):
    """Modules developed by the myQLM community"""

    homepage = "https://www.bull.com/en/solutions/quantum-computing"
    pypi = "myqlm-contrib/myqlm_contrib-1.11.0-py3-none-any.whl"

    supplier = "Organization: Bull SAS"

    maintainers("LydDeb")

    version("1.11.0", sha256="3e1a395d0e84d7239f2ba530c20490839a531444780d08b47a2cd30b5fc206a2")

    with default_args(type="run"):
        depends_on("py-qat-comm")
        depends_on("py-qat-core")
        depends_on("py-networkx")
