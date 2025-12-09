# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySnoop(PythonPackage):
    """snoop is a powerful set of Python debugging tools. It's primarily meant
    to be a more featureful and refined version of PySnooper. It also includes
    its own version of icecream and some other nifty stuff."""

    pypi = "snoop/snoop-0.6.0.tar.gz"

    license("MIT", checked_by="jmlapre")

    version("0.6.0", sha256="c615eddf84d8907f893dec7fde38768aa4b1d88d92d63055b6cfc07e5cde37ec")
    version("0.4.3", sha256="2e0930bb19ff0dbdaa6f5933f88e89ed5984210ea9f9de0e1d8231fa5c1c1f25")

    depends_on("python@3.8:", when="@0.6:")
    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools-scm+toml", type="build")
    depends_on("py-six", when="@:0.5", type=("build", "run"))
    depends_on("py-cheap-repr@0.4.0:", type=("build", "run"))
    depends_on("py-executing", type=("build", "run"))
    depends_on("py-asttokens", type=("build", "run"))
    depends_on("py-pygments", type=("build", "run"))
