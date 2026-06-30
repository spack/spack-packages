# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyGitpython(PythonPackage):
    """GitPython is a python library used to interact with Git repositories."""

    homepage = "https://gitpython.readthedocs.org"
    pypi = "GitPython/GitPython-3.1.12.tar.gz"

    license("BSD-3-Clause")

    version("3.1.50", sha256="80da2d12504d52e1f998772dc5baf6e553f8d2fcfe1fcc226c9d9a2ee3372dcc")
    version("3.1.43", sha256="35f314a9f878467f5453cc1fee295c3e18e52f1b99f10f6cf5b1682e968a9e7c")

    depends_on("py-setuptools", type="build")
    depends_on("py-gitdb@4.0.1:4", type=("build", "run"))

    def url_for_version(self, version):
        url = "https://files.pythonhosted.org/packages/source/G/GitPython/GitPython-{}.tar.gz"
        if version > Version("3.1.43"):
            url = url.lower()
        return url.format(version)
