# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPythonGitlab(PythonPackage):
    """Python wrapper for the GitLab API"""

    homepage = "https://github.com/gpocentek/python-gitlab"
    pypi = "python_gitlab/python_gitlab-6.4.0.tar.gz"

    license("LGPL-3.0-or-later")

    version("8.2.0", sha256="de874dc538db6dceb48929f4c8fb55d6064dd19cb3ffdad1100190f835c5b674")
    version("6.4.0", sha256="55ed94fb47932124b7f9df8e72b29352d3d0ee01ecf44f081dd070f4bad8700d")
    version("3.15.0", sha256="c9e65eb7612a9fbb8abf0339972eca7fd7a73d4da66c9b446ffe528930aff534")
    version("3.9.0", sha256="5fc5e88f81f366e11851cb8b4b9a5b827491ce20ba7585446b74c9b097726ba3")
    version("2.10.1", sha256="7afa7d7c062fa62c173190452265a30feefb844428efc58ea5244f3b9fc0d40f")
    version("1.8.0", sha256="a6b03bc53f6e2e22b88d5ff9772b1bb360570ec82752f1def3d6eb60cda093e7")
    version("0.19", sha256="88b65591db7a10a0d9979797e4e654a113e2b93b3a559309f6092b27ab93934a")
    version("0.18", sha256="d60d67c82fedd8c3e4f0bb8b5241bf2df32307c98fdf2f02a94850e21db2d804")
    version("0.17", sha256="f79337cd8b2343195b7ac0909e0483624d4235cca78fc76196a0ee4e109c9a70")
    version("0.16", sha256="2c50dc0bd3ed7c6b1edb6e556b0f0109493ae9dfa46e3bffcf3e5e67228d7d53")

    with default_args(type="build"):
        depends_on("py-setuptools@61:", when="@4:")
        depends_on("py-setuptools")

    with default_args(type=("build", "run")):
        depends_on("python@3.10:", when="@7:")
        depends_on("python@3.9:", when="@5:")
        depends_on("python@3.7:", when="@3:")

        depends_on("py-requests@2.32:", when="@4.6:")
        depends_on("py-requests@2.25:", when="@2.10.1:")
        depends_on("py-requests@2.22:", when="@2:")
        depends_on("py-requests@2.4.2:", when="@1.4:")
        depends_on("py-requests@1:")

        depends_on("py-requests-toolbelt@1:", when="@4.6:")
        depends_on("py-requests-toolbelt@0.10.1:", when="@3.13:")
        depends_on("py-requests-toolbelt@0.9.1:", when="@2.6:")

        # Historical dependencies
        depends_on("py-typing-extensions@4:", when="@3.14:3 ^python@:3.7")
        depends_on("py-six", when="@:1")

    def url_for_version(self, version):
        if self.spec.satisfies("@4.5:"):
            name = "python_gitlab"
        else:
            name = "python-gitlab"
        return f"https://files.pythonhosted.org/packages/source/p/{name}/{name}-{version}.tar.gz"
