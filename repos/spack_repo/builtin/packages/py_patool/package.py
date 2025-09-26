# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPatool(PythonPackage):
    """portable archive file manager"""

    homepage = "https://wummel.github.io/patool/"
    pypi = "patool/patool-1.12.tar.gz"
    git = "https://github.com/wummel/patool.git"

    license("GPL-3.0-or-later")

    version("4.0.1", sha256="41f7ee21be337a5baf07b2cb4796e9d94397ab741d2379c622f98fc001099802")
    version("1.12", sha256="e3180cf8bfe13bedbcf6f5628452fca0c2c84a3b5ae8c2d3f55720ea04cb1097")

    depends_on("python@3.11:", type=("build", "run"), when="@4:")
    depends_on("python@3.5:", type=("build", "run"))

    depends_on("py-setuptools-reproducible", type="build", when="@4.0.1:")

    # Historical dependencies
    depends_on("py-setuptools", type="build", when="@:4.0.0")
