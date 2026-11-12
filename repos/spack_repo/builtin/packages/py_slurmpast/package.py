# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySlurmpast(PythonPackage):
    """Post-mortem dashboard for finished Slurm jobs: how they actually ran,
    why they failed, and what the next submission should request."""

    homepage = "https://github.com/PursuitOfDataScience/slurmpast"
    pypi = "slurmpast/slurmpast-0.9.0.tar.gz"

    maintainers("PursuitOfDataScience")

    license("MIT")

    version("0.9.0", sha256="01440a312f78d212b91ce1b47ca804d6d8bf2481380495eef1616a5dfcd54323")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-setuptools@77:", type="build")

    with default_args(type=("build", "run")):
        depends_on("py-textual@0.86:8")
        depends_on("py-rich@13.3.3:")
