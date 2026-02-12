# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySetuptoolsRust(PythonPackage):
    """Setuptools rust extension plugin."""

    homepage = "https://github.com/PyO3/setuptools-rust"
    pypi = "setuptools-rust/setuptools_rust-1.11.1.tar.gz"

    license("MIT")

    version("1.12.0", sha256="d94a93f0c97751c17014565f07bdc324bee45d396cd1bba83d8e7af92b945f0c")
    version("1.11.1", sha256="7dabc4392252ced314b8050d63276e05fdc5d32398fc7d3cce1f6a6ac35b76c0")
    version("1.9.0", sha256="704df0948f2e4cc60c2596ad6e840ea679f4f43e58ed4ad0c1857807240eab96")
    version("1.8.1", sha256="94b1dd5d5308b3138d5b933c3a2b55e6d6927d1a22632e509fcea9ddd0f7e486")
    version("1.7.0", sha256="c7100999948235a38ae7e555fe199aa66c253dc384b125f5d85473bf81eae3a3")
    version("1.6.0", sha256="c86e734deac330597998bfbc08da45187e6b27837e23bd91eadb320732392262")
    version("1.5.1", sha256="0e05e456645d59429cb1021370aede73c0760e9360bbfdaaefb5bced530eb9d7")
    version("1.4.1", sha256="18ff850831f58ee21d5783825c99fad632da21e47645e9427fd7dec048029e76")
    version("1.2.0", sha256="0a4ada479e8c7e3d8bd7cb56e1a29acc2b2bb98c2325051b0cdcb57d7f056de8")
    version("0.12.1", sha256="647009e924f0ae439c7f3e0141a184a69ad247ecb9044c511dabde232d3d570e")

    depends_on("py-setuptools@62.4:", when="@1.4.0:", type=("build", "run"))
    depends_on("py-setuptools@46.1:", type=("build", "run"))
    depends_on("py-setuptools", type=("build", "run"))
    depends_on("py-setuptools-scm", when="@1.7.0:", type="build")
    depends_on("py-semantic-version@2.8.2:2", when="@1.2.0:", type=("build", "run"))
    depends_on("py-semantic-version@2.6.0:", type=("build", "run"))
    depends_on("rust", type="run")

    # Historical dependencies
    depends_on("py-typing-extensions@3.7.4.3:", when="@1.2.0:1.7.0", type=("build", "run"))
    depends_on("py-setuptools-scm+toml@6.3.2:", when="@1.2.0:1.4.1", type="build")
    depends_on("py-setuptools-scm+toml@3.4.3:", when="@:1.1", type="build")
    depends_on("py-tomli@1.2.1:", when="@:1.9 ^python@:3.10", type=("build", "run"))
    depends_on("py-toml@0.9.0:", type=("build", "run"), when="@0.12.1")

    def url_for_version(self, version):
        if version >= Version("1.10.0"):
            name = "setuptools_rust"
        else:
            name = "setuptools-rust"
        return f"https://files.pythonhosted.org/packages/source/s/setuptools-rust/{name}-{version}.tar.gz"
