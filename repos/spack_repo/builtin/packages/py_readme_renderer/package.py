# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyReadmeRenderer(PythonPackage):
    """readme_renderer is a library for rendering "readme" descriptions
    for Warehouse."""

    homepage = "https://github.com/pypa/readme_renderer"
    pypi = "readme_renderer/readme_renderer-24.0.tar.gz"

    version("44.0", sha256="8712034eabbfa6805cacf1402b4eeb2a73028f72d1166d6f5cb7f9c047c5d1e1")
    version("37.3", sha256="cd653186dfc73055656f090f227f5cb22a046d7f71a841dfa305f55c9a513273")
    version("24.0", sha256="bb16f55b259f27f75f640acf5e00cf897845a8b3e4731b5c1a436e4b8529202f")
    version("16.0", sha256="c46b3418ddef3c3c3f819a4a9cfd56ede15c03d12197962a7e7a89edf1823dd5")

    depends_on("python@3.9:", type=("build", "run"), when="@44:")
    depends_on("python@3.7:", type=("build", "run"), when="@35:37")
    depends_on("py-setuptools@40.8:", type="build", when="@33:")
    depends_on("py-setuptools", type="build", when="@:32")

    depends_on("py-nh3@0.2.14:", type=("build", "run"), when="@42:")
    depends_on("py-docutils@0.21.2:", type=("build", "run"), when="@44:")
    depends_on("py-docutils@0.13.1:", type=("build", "run"), when="@:43")
    depends_on("py-pygments@2.5.1:", type=("build", "run"), when="@25:")
    depends_on("py-pygments", type=("build", "run"), when="@:24")

    # Historical dependencies
    depends_on("py-bleach@2.1.0:", type=("build", "run"), when="@:41")
    depends_on("py-six", type=("build", "run"), when="@:29")
