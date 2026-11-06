# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyRichToolkit(PythonPackage):
    """Rich toolkit for building command-line applications."""

    homepage = "https://github.com/patrick91/rich-toolkit"
    pypi = "rich_toolkit/rich_toolkit-0.20.6.tar.gz"

    license("MIT")

    version("0.20.6", sha256="04768f19438df877c6279e6e668ab0d88b5fff5c7ef3ac302838d97f7b03472e")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-hatchling", type="build")
    depends_on("py-rich@13.7.1:", type=("build", "run"))
    depends_on("py-click@8.1.7:", type=("build", "run"))
    depends_on("py-typing-extensions@4.12.2:", type=("build", "run"))
