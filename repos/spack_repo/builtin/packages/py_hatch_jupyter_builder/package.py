# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyHatchJupyterBuilder(PythonPackage):
    """A hatch plugin to help build Jupyter packages."""

    homepage = "https://github.com/jupyterlab/hatch-jupyter-builder"
    pypi = "hatch_jupyter_builder/hatch_jupyter_builder-0.8.3.tar.gz"

    license("BSD-3-Clause")

    version("0.9.1", sha256="79278198d124c646b799c5e8dca8504aed9dcaaa88d071a09eb0b5c2009a58ad")
    version("0.8.3", sha256="0dbd14a8aef6636764f88a8fd1fcc9a91921e5c50356e6aab251782f264ae960")

    depends_on("npm", type="run")

    with default_args(type=("build", "run")):
        depends_on("py-hatchling@1.17:", when="@0.9:")
        depends_on("py-hatchling@1.5:")
