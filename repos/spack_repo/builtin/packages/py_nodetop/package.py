# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyNodetop(PythonPackage):
    """See what a cluster actually has free, and why a queue that looks fine
    will not take a job. Supports Slurm, PBS, LSF, Grid Engine, Kubernetes and
    ssh pools, with no runtime dependencies."""

    homepage = "https://github.com/PursuitOfDataScience/nodetop"
    pypi = "nodetop/nodetop-0.7.0.tar.gz"

    maintainers("PursuitOfDataScience")

    license("MIT")

    version("0.7.0", sha256="821ba861ebe0c7dcd7e56f0e52b95c0f53155b8c1df1cbf31a7991671a122774")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-setuptools@77:", type="build")
