# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMditPyPlugins(PythonPackage):
    """Collection of core plugins for markdown-it-py"""

    homepage = "https://github.com/executablebooks/mdit-py-plugins/"
    git = "https://github.com/executablebooks/mdit-py-plugins/"
    pypi = "mdit-py-plugins/mdit_py_plugins-0.4.2.tar.gz"

    license("MIT")

    version("0.6.1", sha256="a2bca0f039f39dbd35fb74ae1b5f998608c437463371f0ff7f49a19a17a114d0")
    version("0.5.0", sha256="f4918cb50119f50446560513a8e311d574ff6aaed72606ddae6d35716fe809c6")
    version("0.4.2", sha256="5f2cd1fdb606ddf152d37ec30e46101a60512bc0e5fa1a7002c36647b09e26b5")
    version("0.3.5", sha256="eee0adc7195e5827e17e02d2a258a2ba159944a0748f59c5099a4a27f78fcf6a")
    version("0.3.1", sha256="3fc13298497d6e04fe96efdd41281bfe7622152f9caa1815ea99b5c893de9441")
    version("0.2.8", sha256="5991cef645502e80a5388ec4fc20885d2313d4871e8b8e320ca2de14ac0c015f")

    with default_args(type="build"):
        depends_on("py-flit-core@3.4:3", when="@0.3:")

        # Historical dependencies
        depends_on("py-setuptools", when="@:0.2")

    with default_args(type=("build", "run")):
        depends_on("python@3.10:", when="@0.6:")
        depends_on("python@3.8:3", when="@0.4:0.5")
        depends_on("python@3.7:3", when="@0.3")
        depends_on("python@3.6:3", when="@:0.2")
        depends_on("py-markdown-it-py@2:4", when="@0.5:")
        depends_on("py-markdown-it-py@1:3", when="@0.4")
        depends_on("py-markdown-it-py@1:2", when="@0.3")
        depends_on("py-markdown-it-py@1:1", when="@0.2")

    def url_for_version(self, version):
        prefix = self.url.rsplit("/", maxsplit=1)[0]
        package = "mdit-py-plugins" if version < Version("2.0.0") else "mdit_py_plugins"
        return f"{prefix}/{package}-{version}.tar.gz"
