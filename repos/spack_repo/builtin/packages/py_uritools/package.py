# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyUritools(PythonPackage):
    """Provides RFC 3986 compliant functions for parsing, classifying and composing URIs and URI
    references, largely replacing the Python Standard Library's urllib.parse module."""

    homepage = "https://github.com/tkem/uritools/"
    pypi = "uritools/uritools-7.0.1.tar.gz"

    maintainers("ebagrenrut")

    license("MIT")

    version("7.0.1", sha256="abf09f899b925fad05407d7f39061318c6be62cce065db727a024daadf96eebf")

    with default_args(type="build"):
        depends_on("py-setuptools@80:")
        depends_on("py-setuptools-scm@8.2:")

    depends_on("python@3.11:", type=("build", "run"))
