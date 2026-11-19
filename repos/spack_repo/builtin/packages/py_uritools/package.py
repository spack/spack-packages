# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyUritools(PythonPackage):
    """Provides RFC 3986 compliant functions for parsing, classifying and composing URIs and URI
    references, largely replacing the Python Standard Library's urllib.parse module."""

    homepage = "https://github.com/tkem/uritools/"
    pypi = "uritools/uritools-7.0.0.tar.gz"

    maintainers("ebagrenrut")

    license("MIT")

    version("7.0.0", sha256="110b773e3f8fbaebcdcbe1377d04e418b1985adf69deeca4ed569f3e328cbf48")

    with default_args(type="build"):
        depends_on("py-setuptools@80:")
        depends_on("py-setuptools-scm@8.2:")

    depends_on("python@3.11:", type=("build", "run"))
