# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RHttr2(RPackage):
    """Perform HTTP Requests and Process the Responses.

    Tools for creating and modifying HTTP requests, then performing them and
    processing the results. 'httr2' is a modern re-imagining of 'httr' that
    uses a pipe-based interface and solves more of the problems that API
    wrapping packages face."""

    cran = "httr2"

    license("MIT")

    version("1.2.2", sha256="a5e7128fe26e083839d85c2969412c7fafaca6140b5601156c0c3472cc5c45e1")
    version("1.0.2", sha256="d1f8e37f74a59f4e1b3b886e5f453336ba14251e500acdccc8f4f7d2b9300048")
    version("0.2.2", sha256="5d1ab62541f7817112519f0f9d00d6a2555bab5b2da7f5c6d579b0c307d7f2bf")

    depends_on("gmake", type="build")

    with default_args(type=("build", "run")):
        depends_on("r@4.1:", when="@1.2:")
        depends_on("r@4.0:", when="@1.0.2:")
        depends_on("r@3.4:")
        depends_on("r-cli@3.0.0:")
        depends_on("r-curl@6.4.0:", when="@1.2:")
        depends_on("r-curl@5.1.0:", when="@1.0.0:")
        depends_on("r-curl")
        depends_on("r-glue")
        depends_on("r-lifecycle", when="@1.0.0:")
        depends_on("r-magrittr")
        depends_on("r-openssl")
        depends_on("r-r6")
        depends_on("r-rappdirs")
        depends_on("r-rlang@1.1.0:", when="@1.0.0:")
        depends_on("r-rlang@1.0.0:")
        depends_on("r-vctrs@0.6.3:", when="@1.0.0:")
        depends_on("r-withr")
