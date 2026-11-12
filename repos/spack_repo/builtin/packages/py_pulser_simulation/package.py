# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPulserSimulation(PythonPackage):
    """An emulator of pulse-level sequences created with Pulser."""

    homepage = "https://github.com/pasqal-io/Pulser"
    pypi = "pulser-simulation/pulser_simulation-1.9.0-py3-none-any.whl"

    supplier = "Organization: Pulser Development Team"

    maintainers("LydDeb")

    license("Apache-2.0", checked_by="LydDeb")

    version("1.9.0", sha256="11690f5f605248059a1cee4737249cb7a5cc5f2434be1369a4baca03a22ccec2")

    with default_args(type=("build", "run")):
        depends_on("py-qutip@5")
        depends_on("py-pulser-core@1.9.0")
