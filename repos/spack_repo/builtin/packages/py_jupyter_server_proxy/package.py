# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyJupyterServerProxy(PythonPackage):
    """
    Jupyter Server Proxy lets you run arbitrary external processes
    (such as RStudio, Shiny Server, Syncthing, PostgreSQL, Code Server, etc)
    alongside your notebook server and provide authenticated web access to them
    using a path like /rstudio next to others like /lab.
    """

    homepage = "https://github.com/jupyterhub/jupyter-server-proxy"
    pypi = "jupyter-server-proxy/jupyter_server_proxy-4.4.0.tar.gz"

    license("BSD-3-Clause")

    version("4.4.0", sha256="e5732eb9c810c0caa997f90a2f15f7d09af638e7eea9c67eb5c43e9c1f0e1157")
    version("3.2.2", sha256="54690ea9467035d187c930c599e76065017baf16e118e6eebae0d3a008c4d946")

    depends_on("python@3.8:", type=("build", "run"), when="@4:")
    depends_on("py-hatch-jupyter-builder@0.8.3:", type="build", when="@4.1.1:")
    depends_on("py-hatchling@1.18.0:", type="build", when="@4.1.1:")
    depends_on("py-jupyterlab@4.0.6:4", type="build", when="@4.1:")
    depends_on("py-jupyterlab@3", type="build", when="@:3")

    depends_on("py-aiohttp", type=("build", "run"))
    depends_on("py-importlib-metadata@4.8.3:", type=("build", "run"), when="@4: ^python@:3.9")
    depends_on("py-jupyter-server@1.24:", type=("build", "run"), when="@4.2:")
    depends_on("py-jupyter-server@1:", type=("build", "run"), when="@:4.1")
    depends_on("py-simpervisor@1:", type=("build", "run"), when="@4.1:")
    depends_on("py-simpervisor@0.4:", type=("build", "run"), when="@:4.0")
    depends_on("py-tornado@6.1:", type=("build", "run"), when="@4.2:")
    depends_on("py-traitlets@5.1:", type=("build", "run"), when="@4.1.1:")

    # Historical dependencies
    depends_on("py-jupyter-packaging@0.7.9:0.7", type="build", when="@:3")
    depends_on("py-setuptools@40.8.0:", type="build", when="@:3")

    def url_for_version(self, version):
        if version >= Version("3.2.3"):
            name = "jupyter_server_proxy"
        else:
            name = "jupyter-server-proxy"
        return f"https://files.pythonhosted.org/packages/source/j/jupyter-server-proxy/{name}-{version}.tar.gz"
