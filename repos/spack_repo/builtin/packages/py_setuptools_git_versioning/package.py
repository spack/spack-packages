# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySetuptoolsGitVersioning(PythonPackage):
    """Use git repo data for building a version number according PEP-440"""

    homepage = "https://setuptools-git-versioning.readthedocs.io/"
    pypi = "setuptools_git_versioning/setuptools_git_versioning-3.0.0.tar.gz"

    maintainers("angus-g")

    license("MIT")

    version("3.0.1", sha256="c8a599bacf163b5d215552b5701faf5480ffc4d65426a5711a010b802e1590eb")
    version("1.13.3", sha256="9dfc59a31dcadcae04bcddc50534ccfc07a25a3180ab5cc1b1e3730217971c63")

    depends_on("py-setuptools", type=("build", "run"))
    depends_on("py-toml@0.10.2:", when="^python@:3.10", type=("build", "run"))
    depends_on("py-packaging", type=("build", "run"))

    depends_on("git", type="run")

    def url_for_version(self, version):
        sep = "_" if version >= Version("3.0.0") else "-"
        return f"https://files.pythonhosted.org/packages/source/s/setuptools{sep}git{sep}versioning/setuptools_git_versioning-{version}.tar.gz"
