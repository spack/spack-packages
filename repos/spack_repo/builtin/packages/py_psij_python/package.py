# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPsijPython(PythonPackage):
    """PSI/J is an abstraction layer over cluster schedulers to write scheduler
    agnostic HPC applications."""

    homepage = "https://www.exaworks.org/"
    git = "https://github.com/exaworks/psij-python.git"
    pypi = "psij-python/psij-python-0.9.9.tar.gz"

    maintainers("andre-merzky")

    license("MIT")

    version("0.9.9", sha256="79d527e43a5bb0df00818b956cc4dec064b59c38e4f8557e8533f901cb47d68f")

    # Build dependencies (in order listed in pyproject.toml)
    depends_on("py-setuptools", type="build")

    # Install dependencies (in order listed in pyproject.toml or setup.cfg/py)
    depends_on("py-psutil@5.9:6.1.1", type=("build", "run"), when="@0.9.9:")
    depends_on("py-pystache@0.6.0:", type=("build", "run"))
    depends_on("py-typeguard@3.0.1:", type=("build", "run"), when="@0.9.8:")
    depends_on("py-packaging@24.0:24.2", type=("build", "run"), when="@0.9.9:")
