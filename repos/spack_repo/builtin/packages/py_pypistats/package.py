# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPypistats(PythonPackage):
    """Python interface to PyPI Stats API."""

    homepage = "https://github.com/hugovk/pypistats"
    pypi = "pypistats/pypistats-1.11.0.tar.gz"

    license("MIT")

    version("1.11.0", sha256="99059cabd3b9dc60fea8553aa03fe9c5eeca8dcb3486830f05b6cfed2f0ebf2a")

    with default_args(type="build"):
        depends_on("py-hatch-vcs")
        depends_on("py-hatchling@1.27:")

    with default_args(type=("build", "run")):
        depends_on("py-httpx@0.19:")
        depends_on("py-platformdirs")
        depends_on("py-prettytable@3.12:")
        depends_on("py-pytablewriter@0.63:+html")
        depends_on("py-python-dateutil")
        depends_on("py-python-slugify")
        depends_on("py-termcolor@2.1:")
        depends_on("py-tomli", when="^python@:3.10")
