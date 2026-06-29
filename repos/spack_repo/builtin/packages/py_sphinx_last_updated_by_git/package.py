# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySphinxLastUpdatedByGit(PythonPackage):
    """Get the "last updated" time for each Sphinx page from Git."""

    homepage = "https://github.com/mgeier/sphinx-last-updated-by-git/"
    pypi = "sphinx-last-updated-by-git/sphinx_last_updated_by_git-0.3.8.tar.gz"

    license("BSD-2-Clause")

    version("0.3.8", sha256="c145011f4609d841805b69a9300099fc02fed8f5bb9e5bcef77d97aea97b7761")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-sphinx@1.8:", type=("build", "run"))
