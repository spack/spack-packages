# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyHatchDocstringDescription(PythonPackage):
    """A hatchling plugin to read the description from the package docstring"""

    homepage = "https://github.com/flying-sheep/hatch-docstring-description"
    pypi = "hatch_docstring_description/hatch_docstring_description-1.1.1.tar.gz"

    license("GPL-3.0-or-later")

    version("1.1.1", sha256="b15d93c273ba3736abc9e2c542bb42a728a6740703ff5ed85cc072ed49458ae3")

    depends_on("python@3.9:", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-hatch-vcs")

    with default_args(type=("build", "run")):
        depends_on("py-hatchling")
