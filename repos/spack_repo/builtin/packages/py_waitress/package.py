# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyWaitress(PythonPackage):
    """Waitress: a production-quality pure-Python WSGI server with very acceptable performance."""

    homepage = "https://github.com/Pylons/waitress/"
    pypi = "waitress/waitress-2.1.2.tar.gz"

    license("ZPL-2.1")

    version("3.0.2", sha256="682aaaf2af0c44ada4abfb70ded36393f0e307f4ab9456a215ce0020baefc31f")
    version("3.0.1", sha256="ef0c1f020d9f12a515c4ec65c07920a702613afcad1dbfdc3bcec256b6c072b3")

    depends_on("py-setuptools@41:", type="build")
