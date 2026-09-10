# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyJsonpointer(PythonPackage):
    """Library to resolve JSON Pointers according to RFC 6901"""

    homepage = "https://github.com/stefankoegl/python-json-pointer"
    pypi = "jsonpointer/jsonpointer-2.0.tar.gz"

    license("BSD-3-Clause")

    version("3.0.0", sha256="2b2d729f2091522d61c3b31f82e11870f60b68f43fbc705cb76bf4b832af59ef")
    version("2.0", sha256="c192ba86648e05fdae4f08a17ec25180a9aef5008d973407b581798a83975362")
    version("1.9", sha256="39403b47a71aa782de6d80db3b78f8a5f68ad8dfc9e674ca3bb5b32c15ec7308")

    depends_on("python@3.7:", type="build", when="@3:")
    depends_on("py-setuptools", type="build")
