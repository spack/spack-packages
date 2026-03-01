# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.cargo import CargoPackage

from spack.package import *


class CargoC(CargoPackage):
    """A package to build and install C-compatible libraries"""

    homepage = "https://github.com/lu-zero/cargo-c"
    url = "https://github.com/lu-zero/cargo-c/archive/refs/tags/v0.10.18.tar.gz"
    git = "https://github.com/lu-zero/cargo-c.git"

    license("MIT", checked_by="jmcarcell")

    version("0.10.18", sha256="0f2b699be7ad5cac05624701065ae521c7f6b8159bdbcb8103445fc2440d1a7e")
    version("0.10.17", sha256="a92b752f35e3ef54c992b2ba382466eb58a11020d13e62a25a4101bc055d5146")
    version("0.10.16", sha256="c0ebb3175393da5b55c3cd83ba1ae9d42d32e2aece6ceff1424239ffb68eb3e3")

    depends_on("c", type="build")

    depends_on("openssl")
    depends_on("rust@1.89:", type="build", when="@0.10.17:")
    depends_on("rust@1.88:", type="build", when="@0.10.16:")
