# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPathvalidate(PythonPackage):
    """pathvalidate is a Python library to sanitize/validate a string such as
    filenames/file-paths/etc.
    """

    homepage = "https://github.com/thombashi/pathvalidate"
    pypi = "pathvalidate/pathvalidate-3.3.1.tar.gz"

    license("MIT")

    version("3.3.1", sha256="b18c07212bfead624345bb8e1d6141cdcf15a39736994ea0b94035ad2b1ba177")

    with default_args(type="build"):
        depends_on("py-setuptools@64:")
        depends_on("py-setuptools-scm@8:")
