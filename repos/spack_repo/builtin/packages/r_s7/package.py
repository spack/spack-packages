# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RS7(RPackage):
    """The S7 package is a new OOP system designed to be a successor to S3 and S4."""

    homepage = "https://rconsortium.github.io/S7/"
    cran = "S7"

    license("MIT", checked_by="snehring")

    version("0.2.1", sha256="f026ec13aa4d0613720c483e2b6ec28251f4d4b7cc6624cab689ecfcac189a5b")
    version("0.2.0", sha256="b8675a7fac7a396e524b21cd353ef0823d2acf76088b5f229d2a55a182a4d49b")
    version("0.1.1", sha256="dce9613f389d3c49bf70e2dc57852b79b6e70474abb92887e13cb3d50d2a7b64")
    version("0.1.0", sha256="83bd800c959520955a70b6efdc8467a38cc53ceaff598947e98b65eddd77cdc1")

    depends_on("c", type="build")
