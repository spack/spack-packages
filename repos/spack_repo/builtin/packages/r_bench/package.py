# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RBench(RPackage):
    """High Precision Timing of R Expressions."""

    cran = "bench"

    license("MIT")

    version("1.1.4", sha256="b822f5b7648deecc6b516dcca4e932ce92e65eb166b997b04355218aceb1d083")

    depends_on("c", type="build")

    with default_args(type=("build", "run")):
        depends_on("r@4:")
        depends_on("r-glue@1.8:")
        depends_on("r-pillar@1.10.1:")
        depends_on("r-profmem@0.6:")
        depends_on("r-rlang@1.1.4:")
        depends_on("r-tibble@3.2.1:")
