# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RMicrobenchmark(RPackage):
    """Accurate Timing Functions.

    Provides infrastructure to accurately measure and compare the execution
    time of R expressions."""

    cran = "microbenchmark"

    license("BSD-2-Clause")

    version("1.5.0", sha256="3d1e92a9206811ad128b28795d20a0d31da5f0c29ea7f1caaf1194ed3e49765f")
    version("1.4.10", sha256="04cc41be72708dce8d31ff1cb105d88cc9f167250ea00fe9a165c99204b9b481")
    version("1.4.9", sha256="443d2caf370ef33e4ac2773176ad9eb86f8790f43b430968ef9647699dbbffd2")
    version("1.4-7", sha256="268f13c6323dd28cc2dff7e991bb78b814a8873b4a73f4a3645f40423da984f6")

    depends_on("c", type="build")

    depends_on("r@3.2:", type=("build", "run"), when="@1.5:")
