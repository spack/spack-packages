# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyChardet(PythonPackage):
    """Universal encoding detector for Python 3"""

    homepage = "https://github.com/chardet/chardet"
    pypi = "chardet/chardet-3.0.4.tar.gz"

    license("MIT", when="@7:")
    license("LGPL-2.1-or-later", when="@:6")

    version("7.0.1", sha256="6fce895c12c5495bb598e59ae3cd89306969b4464ec7b6dd609b9c86e3397fe3")
    version("7.0.0", sha256="5272ea14c48cb5f38e87e698c641a7ea2a8b1db6c42ea729527fbe8bd621f39c")
    version("6.0.0", sha256="aaa00ede13dd39a582de2b1254221a1f3e1c77e7738036431b6cb7e6a05b4f19")
    version("5.2.0", sha256="1b3b6ff479a8c414bc3fa2c0852995695c4a026dcd6d0633b2dd092ca39c1cf7")
    version("5.1.0", sha256="0d62712b956bc154f85fb0a266e2a3c5913c2967e00348701b32411d6def31e5")
    version("5.0.0", sha256="0368df2bfd78b5fc20572bb4e9bb7fb53e2c094f60ae9993339e8671d0afb8aa")
    version("4.0.0", sha256="0d6f53a15db4120f2b08c94f11e7d93d2c911ee118b6b30a04ec3ee8310179fa")
    version("3.0.4", sha256="84ab92ed1c4d4f16916e05906b6b75a6c0fb5db821cc65e70cbd64a3e2a5eaae")
    version("3.0.2", sha256="4f7832e7c583348a9eddd927ee8514b3bf717c061f57b21dbe7697211454d9bb")
    version("2.3.0", sha256="e53e38b3a4afe6d1132de62b7400a4ac363452dc5dfcf8d88e8e0cce663c68aa")

    with default_args(type="build"):
        depends_on("py-hatch-vcs", when="@6:")
        depends_on("py-hatchling", when="@6:")

        # Historical dependencies
        depends_on("py-pytest-runner", when="@3")
        depends_on("py-setuptools", when="@:5")
