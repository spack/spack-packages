# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMyqlmInterop(PythonPackage):
    """myQLM-interop package"""

    homepage = "https://www.bull.com/en/solutions/quantum-computing"
    pypi = "myqlm-interop/myqlm_interop-2.1.0-py3-none-any.whl"

    supplier = "Organization: Bull SAS"

    maintainers("LydDeb")

    version("2.1.0", sha256="44ad6170e72817e00298cc1782efb39f700a7c6d7492341fda97c4d29c5a2ea0")

    with default_args(type="run"):
        depends_on("py-qat-lang@2.2.0:")
        depends_on("py-numpy@2:")
        depends_on("py-ply")
