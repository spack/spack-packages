# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySlurmwatch(PythonPackage):
    """Live, process-isolated CPU, memory and GPU telemetry for running Slurm
    jobs, in the terminal."""

    homepage = "https://github.com/PursuitOfDataScience/slurmwatch"
    pypi = "slurmwatch/slurmwatch-1.2.4.tar.gz"

    maintainers("PursuitOfDataScience")

    license("MIT")

    version("1.2.4", sha256="28257c1df87f91ffc63bec9ca9c6e7f6c0d09e8ffade09f1553ed446cd5989dc")

    depends_on("python@3.10:", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-setuptools@77:")
        depends_on("py-setuptools-scm@8:")

    with default_args(type=("build", "run")):
        depends_on("py-textual@0.86:8")
        depends_on("py-rich@13:")
        depends_on("py-pynvml@11.5:11")
