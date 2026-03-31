# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyToolz(PythonPackage):
    """A set of utility functions for iterators, functions, and dictionaries"""

    homepage = "https://github.com/pytoolz/toolz/"
    pypi = "toolz/toolz-0.9.0.tar.gz"

    license("BSD-3-Clause")

    version("1.1.0", sha256="27a5c770d068c110d9ed9323f24f1543e83b2f300a687b7891c1a6d56b697b5b")
    version("0.12.0", sha256="88c570861c440ee3f2f6037c4654613228ff40c93a6c25e0eba70d17282c6194")
    version("0.9.0", sha256="929f0a7ea7f61c178bd951bdae93920515d3fbdbafc8e6caf82d752b9b3b31c9")

    with default_args(type="build"):
        depends_on("py-setuptools")
        depends_on("py-setuptools@77:", when="@1.1.0:")

        depends_on("py-setuptools-git-versioning@2.0:", when="@1.1.0:")

    with default_args(type=("build", "run")):
        depends_on("python@3.9:", when="@1.1.0:")
        depends_on("python@3.5:", when="@0.11.0:")
