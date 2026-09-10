# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RGargle(RPackage):
    """Utilities for Working with Google APIs.

    Provides utilities for working with Google APIs
    <https://developers.google.com/apis-explorer>. This includes functions and
    classes for handling common credential types and for preparing, executing,
    and processing HTTP requests."""

    cran = "gargle"

    license("MIT")

    version("1.6.1", sha256="0c72c60e5e448ad9db6d4f224654afa1a1d459d43f31c623c8117eba29850e5c")
    version("1.5.2", sha256="4a5beb046eb50a168b4baf5d1fcd8ac20d698e7fcb6b6ef46a436ded5b039001")
    version("1.4.0", sha256="8e0f1edf5595d4fd27bd92f98af1cc0c1349975803d9d6f3ff0c25ee2440498b")
    version("1.2.1", sha256="f367e2c82f403167ae84058303a4fb0402664558a2abf0b495474a7ef1a2f020")
    version("1.2.0", sha256="4d46ca2933f19429ca5a2cfe47b4130a75c7cd9931c7758ade55bac0c091d73b")

    with default_args(type=("build", "run")):
        depends_on("r@4.1:", when="@1.6.1:")
        depends_on("r@3.6:", when="@1.5.0:")
        depends_on("r@3.5:", when="@1.2.1:")
        depends_on("r@3.3:")

        depends_on("r-cli@3.0.1:", when="@1.4.0:")
        depends_on("r-cli@3.0.0:")
        depends_on("r-fs@1.3.1:")
        depends_on("r-glue@1.3.0:")
        depends_on("r-httr@1.4.5:", when="@1.4.0:")
        depends_on("r-httr@1.4.0:")
        depends_on("r-jsonlite")
        depends_on("r-lifecycle@0.2.0:", when="@1.6.0:")
        depends_on("r-lifecycle", when="@1.4.0:")
        depends_on("r-openssl", when="@1.4.0:")
        depends_on("r-rappdirs")
        depends_on("r-rlang@1.1.0:", when="@1.4.0:")
        depends_on("r-rlang@1.0.0:", when="@1.2.1:")
        depends_on("r-rlang@0.4.9:")
        depends_on("r-withr")

        # Historical dependencies
        depends_on("r-rstudioapi", when="@:1.2.1")
