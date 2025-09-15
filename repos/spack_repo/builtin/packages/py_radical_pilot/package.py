# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyRadicalPilot(PythonPackage):
    """RADICAL-Pilot is a Pilot system specialized in executing applications
    composed of many computational tasks on high performance computing (HPC)
    platforms."""

    homepage = "https://radical-cybertools.github.io"
    git = "https://github.com/radical-cybertools/radical.pilot.git"
    pypi = "radical_pilot/radical_pilot-1.92.0.tar.gz"

    maintainers("andre-merzky")

    license("MIT")

    version("develop", branch="devel")
    version("1.92.0", sha256="5c65df02ec097f71648259db8ed8638580ea8e4c1c7f360879afff7f99e56134")

    depends_on("py-radical-utils@1.90:1.99", type=("build", "run"), when="@1.90:")
    depends_on("py-radical-gtod@1.90:1.99", type=("build", "run"), when="@1.90:")
    depends_on("py-requests", type=("build", "run"), when="@1.90:")
    depends_on("py-psij-python", type=("build", "run"), when="@1.48:")
    depends_on("py-dill", type=("build", "run"), when="@1.14:")
    depends_on("py-setproctitle", type=("build", "run"))
    depends_on("py-setuptools", type="build")
