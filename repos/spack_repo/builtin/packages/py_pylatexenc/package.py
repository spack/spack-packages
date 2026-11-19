# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPylatexenc(PythonPackage):
    """Simple LaTeX parser providing latex-to-unicode and unicode-to-latex conversion"""

    homepage = "https://github.com/phfaist/pylatexenc"
    pypi = "pylatexenc/pylatexenc-2.11.tar.gz"

    supplier = "Person: Philippe Faist"

    maintainers("LydDeb")

    license("MIT", checked_by="LydDeb")

    version("2.11", sha256="305a072a99ce736246049c9da05841b9d718c0f7ea8888f5f596cf15cb621053")
    version("2.10", sha256="3dd8fd84eb46dc30bee1e23eaab8d8fb5a7f507347b23e5f38ad9675c84f40d3")

    with default_args(type="build"):
        depends_on("py-setuptools")
