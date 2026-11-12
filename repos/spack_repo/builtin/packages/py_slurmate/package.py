# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySlurmate(PythonPackage):
    """Interactive TUI wizard and CLI that builds and submits Slurm batch
    scripts, offering only the partitions, QOS, GPUs and modules the cluster
    actually has."""

    homepage = "https://github.com/PursuitOfDataScience/slurmate"
    pypi = "slurmate/slurmate-0.8.0.tar.gz"

    maintainers("PursuitOfDataScience")

    license("MIT")

    version("0.8.0", sha256="51ca42f705e4f9e3a04a5394467038f25c829c93d53833cfc30d8353bd4a2906")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-setuptools@77:", type="build")

    with default_args(type=("build", "run")):
        depends_on("py-questionary@2:")
        depends_on("py-prompt-toolkit@3")
        depends_on("py-rich@13:")
        depends_on("py-tomli@2:", when="^python@:3.10")
