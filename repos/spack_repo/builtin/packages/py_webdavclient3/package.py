# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyWebdavclient3(PythonPackage):
    """WebDAV client, based on original package
    https://github.com/designerror/webdav-client-python
    but uses requests instead of PyCURL."""

    homepage = "https://github.com/ezhov-evgeny/webdav-client-python-3"
    pypi = "webdavclient3/webdavclient3-3.14.7.tar.gz"
    git = "https://github.com/ezhov-evgeny/webdav-client-python-3.git"

    maintainers("wdconinc")

    license("MIT", checked_by="wdconinc")

    version("3.14.7", sha256="6c04252b579bc015cec78081480c63eadf1030f382768248777c6203f059b3f5")

    with default_args(type="build"):
        depends_on("py-setuptools")
        depends_on("py-wheel")

    with default_args(type=("build", "run")):
        depends_on("py-requests")
        depends_on("py-lxml")
        depends_on("py-python-dateutil")
