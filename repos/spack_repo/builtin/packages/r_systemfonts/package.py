# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RSystemfonts(RPackage):
    """System Native Font Finding.

    Provides system native access to the font catalogue. As font handling
    varies between systems it is difficult to correctly locate installed fonts
    across different operating systems. The 'systemfonts' package provides
    bindings to the native libraries on Windows, macOS and Linux for finding
    font files that can then be used further by e.g. graphic devices. The main
    use is intended to be from compiled code but 'systemfonts' also provides
    access from R."""

    cran = "systemfonts"

    license("MIT")

    version("1.3.2", sha256="828a1780e540bd05107cd0a1ddfac6727de8aef1d6d82b43591dabaf753dd135")
    version("1.3.1", sha256="4392cbf7f97d335b61f7a70257faead2d45a3beeb76249d75a41e9ed82e4456d")
    version("1.1.0", sha256="1941069bd20320284ec026a38c53cb736be60bda431303ceaf8fd27ae13fb644")
    version("1.0.4", sha256="ef766c75b942f147d382664a00d6a4930f1bfe0cce9d88943f571682a85a84c0")
    version("1.0.3", sha256="647c99d5ea6f90a49768ea7b10b39816af6be85168475273369fd973a20dbbba")
    version("1.0.1", sha256="401db4d9e78e3a5e00b7a0b4fbad7fbb1c584734469b65fe5b7ebe1851c7a797")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    with default_args(type=("build", "run")):
        depends_on("r@3.2.0:")
        depends_on("r-base64enc", when="@1.2.3:")
        depends_on("r-jsonlite", when="@1.2:")
        depends_on("r-lifecycle", when="@1.1:")
        depends_on("r-cpp11@0.2.1:")

    depends_on("fontconfig")
    depends_on("freetype")
