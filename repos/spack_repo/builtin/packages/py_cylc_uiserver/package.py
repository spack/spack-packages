# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyCylcUiserver(PythonPackage):
    """Cylc UI Server."""

    homepage = "https://github.com/cylc/cylc-uiserver/"
    pypi = "cylc-uiserver/cylc-uiserver-1.9.1.tar.gz"
    git = "https://github.com/cylc/cylc-uiserver.git"

    maintainers("climbfuji")

    license("GPL-3.0-or-later")

    version(
        "1.9.1",
        sha256="106551a19cbd5de85e8a59a549e1846598ee37e22171bd127a1676dccacc2792",
        url="https://files.pythonhosted.org/packages/source/c/cylc-uiserver/cylc_uiserver-1.9.1.tar.gz",
    )
    version(
        "1.7.1",
        sha256="a841437b43873e198ffad0a496ee95efb14a6fd8eadb0b9182827ebac24dfdc7",
        url="https://files.pythonhosted.org/packages/source/c/cylc-uiserver/cylc_uiserver-1.7.1.tar.gz",
    )

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("python@3.12:", when="@1.8:", type=("build", "run"))
    depends_on("py-wheel", type="build")
    depends_on("py-setuptools@40.9.0:", type="build")

    depends_on("py-cylc-flow@8.6.4:8.6", when="@1.9.1", type=("build", "run"))
    depends_on("py-cylc-flow@8.5", when="@1.7.1", type=("build", "run"))

    depends_on("py-ansimarkup@1.0.0:", type=("build", "run"))
    depends_on("py-cherrypy", when="@1.9.1", type=("build", "run"))
    depends_on("py-graphene", type=("build", "run"))
    depends_on("py-jupyter-server@2.13:", type=("build", "run"))
    depends_on("py-packaging", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-psutil", type=("build", "run"))
    depends_on("py-tornado@6.5.0:", type=("build", "run"))
    depends_on("py-traitlets@5.2.1:", type=("build", "run"))
    depends_on("py-pyzmq", type=("build", "run"))
