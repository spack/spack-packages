# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPygithub(PythonPackage):
    """Typed interactions with the GitHub API v3"""

    homepage = "https://pygithub.readthedocs.io/"
    pypi = "PyGithub/PyGithub-1.54.1.tar.gz"

    license("LGPL-3.0-only")

    version("2.8.1", sha256="341b7c78521cb07324ff670afd1baa2bf5c286f8d9fd302c1798ba594a5400c9")
    version("2.1.1", sha256="ecf12c2809c44147bce63b047b3d2e9dac8a41b63e90fcb263c703f64936b97c")
    version("1.59.1", sha256="c44e3a121c15bf9d3a5cc98d94c9a047a5132a9b01d22264627f58ade9ddc217")
    version("1.55", sha256="1bbfff9372047ff3f21d5cd8e07720f3dbfdaf6462fcaed9d815f528f1ba7283")

    depends_on("python@3.6:", type=("build", "run"))
    depends_on("python@3.7:", type=("build", "run"), when="@1.57:")
    depends_on("python@3.8:", type=("build", "run"), when="@2.8.1:")

    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools@64:", type="build", when="@2.8.1:")
    depends_on("py-setuptools-scm", type="build", when="@1.58.1:")
    depends_on("py-setuptools-scm@7:", type="build", when="@2.8.1:")
    depends_on("py-pynacl@1.4.0:", type=("build", "run"))
    depends_on("py-python-dateutil", type=("build", "run"), when="@2.1.0:")
    depends_on("py-requests@2.14.0:", type=("build", "run"))
    depends_on("py-pyjwt@2.4.0:", type=("build", "run"))
    depends_on("py-pyjwt@2.4.0: +crypto", type=("build", "run"), when="@1.58.1:")
    depends_on("py-typing-extensions@4:", type=("build", "run"), when="@2.1.0:")
    depends_on("py-typing-extensions@4.5:", type=("build", "run"), when="@2.8.1:")
    depends_on("py-urllib3@1.26.0:", type=("build", "run"), when="@2.1.0:")
    depends_on("py-deprecated", type=("build", "run"), when="@:2.1.1")

    # DetailedHTTPError: GET
    # https://files.pythonhosted.org/packages/source/P/PyGithub/PyGithub-2.8.1.tar.gz
    # returned 404: Not Found
    def url_for_version(self, version):
        if version == Version("2.8.1"):
            return "https://files.pythonhosted.org/packages/c1/74/e560bdeffea72ecb26cff27f0fad548bbff5ecc51d6a155311ea7f9e4c4c/pygithub-2.8.1.tar.gz"
        else:
            return f"https://files.pythonhosted.org/packages/source/P/PyGithub/PyGithub-{version}.tar.gz"
