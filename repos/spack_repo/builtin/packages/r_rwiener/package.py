# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RRwiener(RPackage):
    """Provides Wiener process distribution functions, namely the Wiener first
    passage time density, CDF, quantile and random functions. Additionally
    supplies a modelling function (wdm) and further methods for the resulting
    object."""

    cran = "RWiener"

    license("GPL-2.0-or-later")

    version("1.3-3", sha256="f8ae38071aef62928355aafbcd3f194933f23f394d41022a96644be7a97bd929")

    depends_on("c", type="build")

    with default_args(type=("build", "run")):
        depends_on("r@3:")
