# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySphinxGithubChangelog(PythonPackage):
    """Build a sphinx changelog from GitHub Releases."""

    homepage = "https://github.com/ewjoachim/sphinx-github-changelog"
    pypi = "sphinx_github_changelog/sphinx_github_changelog-1.7.2.tar.gz"

    maintainers("adamjstewart")

    license("MIT")

    version("1.7.2", sha256="79f11f30ec5b1ae52a1742a6dc702644203b164732a1af4b049ebe522ff484e4")

    with default_args(type="build"):
        depends_on("py-hatchling")
        depends_on("py-uv-dynamic-versioning")

    with default_args(type=("build", "run")):
        depends_on("py-docutils")
        depends_on("py-requests")
        depends_on("py-sphinx")
