# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyDirscape(PythonPackage):
    """Shows every storage area you can reach on an HPC cluster, how full each
    one is, and what changed since the last run. Sizes come from GPFS, Lustre,
    CephFS and XFS quotas, so a run takes seconds. No runtime dependencies."""

    homepage = "https://github.com/PursuitOfDataScience/dirscape"
    pypi = "dirscape/dirscape-0.1.0.tar.gz"

    maintainers("PursuitOfDataScience")

    license("MIT")

    version("0.1.0", sha256="58f5ae7a6aa16d93d0d25dea086c72f6748fcbdcafe669f47b0f31178153dcc0")

    depends_on("python@3.6:", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-setuptools@64:")
        depends_on("py-setuptools-scm@8:")
