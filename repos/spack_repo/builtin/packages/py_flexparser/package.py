# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyFlexparser(PythonPackage):
    """A flexible and extensible text parsing library for Python."""

    homepage = "https://github.com/hgrecco/flexparser"
    pypi = "flexparser/flexparser-0.4.tar.gz"

    license("BSD-3-Clause")

    version("0.4", sha256="266d98905595be2ccc5da964fe0a2c3526fbbffdc45b65b3146d75db992ef6b2")

    depends_on("py-hatchling", type="build")
    depends_on("py-hatch-vcs", type="build")

    depends_on("py-typing-extensions", type=("build", "run"))
