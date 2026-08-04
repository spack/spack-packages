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

    version("0.10.24", sha256="91c6e0be34aa0ad26b7ef21ce21a390c95635e4e6e00b7a6ff07323f9af8550b")
    version("0.10.23", sha256="17679af6c00a70ce1d70668023e993045539afdc7ab0ca1a081aa8ef6993a595")
    version("0.10.22", sha256="a7b00539437932f2a17a72b97d9c2142367a2d70ee20f9f1692a8b13c7255332")
    version("0.10.21", sha256="819b62a61e5271924dffd122b7c713e446e5d65f3e630bbe9b90d4d46513d8fa")
    version("0.10.20", sha256="9bdf7c10b44466a7c01dc4ed152da5031793cca9e0c8009d73223a32522cf2c3")
    version("0.10.19", sha256="4136fbb1c25b1afdf1aaf473d00e532b73bbe02c7c53cb44965aff41ed328d20")
    version("0.10.18", sha256="0f2b699be7ad5cac05624701065ae521c7f6b8159bdbcb8103445fc2440d1a7e")
    version("0.10.17", sha256="a92b752f35e3ef54c992b2ba382466eb58a11020d13e62a25a4101bc055d5146")
    version("0.10.16", sha256="c0ebb3175393da5b55c3cd83ba1ae9d42d32e2aece6ceff1424239ffb68eb3e3")

    depends_on("c", type="build")

    depends_on("openssl")
    depends_on("pkgconfig", type="build")
    depends_on("rust@1.95:", type="build", when="@0.10.24:")
    depends_on("rust@1.94:", type="build", when="@0.10.23:")
    depends_on("rust@1.93:", type="build", when="@0.10.22:")
    depends_on("rust@1.92:", type="build", when="@0.10.21:")
    depends_on("rust@1.91:", type="build", when="@0.10.20:")
    depends_on("rust@1.90:", type="build", when="@0.10.19:")
    depends_on("rust@1.89:", type="build", when="@0.10.17:")
    depends_on("rust@1.88:", type="build", when="@0.10.16:")
