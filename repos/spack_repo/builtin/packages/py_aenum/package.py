# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyAenum(PythonPackage):
    """Advanced Enumerations (compatible with Python's stdlib Enum),
    NamedTuples, and NamedConstants."""

    homepage = "https://github.com/ethanfurman/aenum"
    pypi = "aenum/aenum-2.1.2.tar.gz"

    version("3.1.16", sha256="bfaf9589bdb418ee3a986d85750c7318d9d2839c1b1a1d6fe8fc53ec201cf140")
    version("3.1.12", sha256="3e531c91860a81f885f7e6e97d219ae9772cb899580084788935dad7d9742ef0")
    version("2.1.2", sha256="a3208e4b28db3a7b232ff69b934aef2ea1bf27286d9978e1e597d46f490e4687")

    depends_on("py-setuptools", type="build")
