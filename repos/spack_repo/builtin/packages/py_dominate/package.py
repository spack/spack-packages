# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyDominate(PythonPackage):
    """Dominate is a Python library for creating and
    manipulating HTML documents using an elegant DOM API. It
    allows you to write HTML pages in pure Python very
    concisely, which eliminates the need to learn another
    template language, and lets you take advantage of the more
    powerful features of Python."""

    homepage = "https://github.com/Knio/dominate"
    pypi = "dominate/dominate-2.6.0.tar.gz"

    license("LGPL-3.0-or-later")

    version("2.9.1", sha256="558284687d9b8aae1904e3d6051ad132dd4a8c0cf551b37ea4e7e42a31d19dc4")
    version("2.6.0", sha256="76ec2cde23700a6fc4fee098168b9dee43b99c2f1dd0ca6a711f683e8eb7e1e4")

    # https://github.com/Knio/dominate/issues/172
    depends_on("python@:3.11", when="@:2.8", type=("build", "run"))
    depends_on("py-setuptools@64:", when="@2.9:", type="build")
    depends_on("py-setuptools", type="build")
