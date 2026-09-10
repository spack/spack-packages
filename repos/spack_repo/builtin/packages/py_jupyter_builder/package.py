# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyJupyterBuilder(PythonPackage):
    """Build tools for JupyterLab (and remixes).."""

    homepage = "https://github.com/jupyterlab/jupyter-builder"
    pypi = "jupyter_builder/jupyter_builder-1.2.2.tar.gz"
    git = "https://github.com/jupyterlab/jupyter-builder.git"

    supplier = "Organization: JupyterLab"

    maintainers("jeremyfix")

    license("BSD-3-Clause", checked_by="jeremyfix")

    version("1.2.2", sha256="b6cea88f58e44b2c5eba96f28d2e0d16fd453d3ca6dc9c4492ff8a1f2e97f601")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-hatchling@1.21.1:", type=("build", "run"))
    depends_on("py-hatch-nodejs-version@0.3.2:", type=("build", "run"))
