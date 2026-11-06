# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RRtmb(RPackage):
    """'R' Bindings for 'TMB'."""

    cran = "RTMB"

    license("GPL-2.0-or-later")

    version("2.0", sha256="a87b21eb5b30071c702b6b45866dfd2ee2aee51d78da0cbf4fdab5d7c1454635")

    depends_on("cxx", type="build")

    with default_args(type=("build", "run")):
        depends_on("r-rcpp@1.0.9:")
        depends_on("r-matrix")
        depends_on("r-tmb@1.9.7:")
        depends_on("r-mass")
        depends_on("r-rcppeigen")
