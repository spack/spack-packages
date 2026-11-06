# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPulserMyqlm(PythonPackage):
    """An extension to interface MyQLM with Pulser."""

    homepage = "https://github.com/pasqal-io/Pulser-myQLM"
    pypi = "pulser-myqlm/pulser_myqlm-0.8.3-py3-none-any.whl"

    supplier = "Organization: Pasqal Quantum Solutions / Pulser Development Team"

    maintainers("LydDeb")

    license("Apache-2.0", checked_by="LydDeb")

    version("0.8.3", sha256="40cdcbe994f7c7ad642414aa9e8eff0324ad8394a981fdeb87b624691efa4e59")

    with default_args(type=("build", "run")):
        depends_on("python@3.9:", type=("build", "run"))
        depends_on("py-numpy")
        depends_on("py-scipy")
        depends_on("py-pulser-core@1.4.0:")
        depends_on("py-pulser-simulation@1.4.0:")
        depends_on("py-myqlm@1.9.0:1.10.3,1.10.5:")
        depends_on("py-requests")
        depends_on("py-backoff@2.2:2")
