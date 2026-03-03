# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySphinxThemeBuilder(PythonPackage):
    """A tool for authoring Sphinx themes with a simple (opinionated) workflow."""

    homepage = "https://sphinx-theme-builder.readthedocs.io/en/latest"
    pypi = "sphinx-theme-builder/sphinx_theme_builder-0.2.0b2.tar.gz"
    git = "https://github.com/pradyunsg/sphinx-theme-builder"

    license("MIT")

    version("0.3.2", sha256="40b4bc2275b04d76781722c2e597770159e512f166986e1ceca1580a693f27bb")
    version(
        "0.2.0b2",
        sha256="e9cd98c2bb35bf414fe721469a043cdcc10f0808d1ffcf606acb4a6282a6f288",
        deprecated=True,
    )

    depends_on("py-flit-core@3.2:3", type="build")

    with default_args(type=("build", "run")):
        # https://github.com/pradyunsg/sphinx-theme-builder/pull/51
        depends_on("python@:3.13", when="@:0.2")

        depends_on("py-pyproject-metadata@0.10:", when="@0.3:")
        depends_on("py-pyproject-metadata")
        depends_on("py-packaging")
        depends_on("py-rich")
        depends_on("py-nodeenv")
        depends_on("py-setuptools")
        depends_on("py-tomli", when="^python@:3.10")
        depends_on("py-diagnostic@2:", when="@0.3:")

    def url_for_version(self, version):
        url = "https://files.pythonhosted.org/packages/source/s/sphinx-theme-builder/{}-{}.tar.gz"
        if version == Version("0.2.0b2"):
            name = "sphinx-theme-builder"
        else:
            name = "sphinx_theme_builder"
        return url.format(name, version)
