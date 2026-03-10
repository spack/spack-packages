# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPytablewriter(PythonPackage):
    """pytablewriter is a Python library to write a table in various formats."""

    homepage = "https://github.com/thombashi/pytablewriter"
    pypi = "pytablewriter/pytablewriter-1.2.1.tar.gz"

    license("MIT")

    version("1.2.1", sha256="7bd0f4f397e070e3b8a34edcf1b9257ccbb18305493d8350a5dbc9957fced959")

    variant("html", default=False, description="Install dependencies needed for HTML support")

    with default_args(type="build"):
        depends_on("py-setuptools@64:")
        depends_on("py-setuptools-scm@8:")

    with default_args(type=("build", "run")):
        depends_on("py-dataproperty@1.1:1")
        depends_on("py-mbstrdecoder@1")
        depends_on("py-pathvalidate@2.3:3")
        depends_on("py-tabledata@1.3.1:1")
        depends_on("py-tcolorpy@0.0.5:0")
        depends_on("py-typepy@1.3.2:1+datetime")

        with when("+html"):
            depends_on("py-dominate@2.1.5:2")
