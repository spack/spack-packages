# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.opam import OpamPackage

from spack.package import *


class OpamNum(OpamPackage):
    """The legacy Num library for arbitrary-precision
    integer and rational arithmetic"""

    has_code = False

    maintainers("green-br")

    version("1.6")

    depends_on("c", type="build")  # generated
    depends_on("opam", type=("build", "run"))

    opam_name = "num"
