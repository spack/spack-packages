# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyAsyncLru(PythonPackage):
    """Simple lru_cache for asyncio"""

    homepage = "https://github.com/wikibusiness/async_lru"
    pypi = "async-lru/async_lru-2.0.5.tar.gz"

    license("MIT")

    version("2.3.0", sha256="89bdb258a0140d7313cf8f4031d816a042202faa61d0ab310a0a538baa1c24b6")
    version("2.0.5", sha256="481d52ccdd27275f42c43a928b4a50c3bfb2d67af4e78b170e3e0bb39c66e5bb")
    version("1.0.3", sha256="c2cb9b2915eb14e6cf3e717154b40f715bf90e596d73623677affd0d1fbcd32a")
    version("1.0.2", sha256="baa898027619f5cc31b7966f96f00e4fc0df43ba206a8940a5d1af5336a477cb")

    depends_on("python@3.10:", when="@2.0.5:", type=("build", "run"))
    depends_on("python@3.9:", when="@2.0.5:", type=("build", "run"))
    depends_on("python@3.6:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    depends_on("py-typing-extensions@4:", when="@2: ^python@:3.10", type=("build", "run"))

    def url_for_version(self, version):
        url = "https://files.pythonhosted.org/packages/source/a/{0}/{0}-{1}.tar.gz"
        if version >= Version("2.0.5") or version <= Version("1.0.2"):
            name = "async_lru"
        else:
            name = "async-lru"
        return url.format(name, version)
