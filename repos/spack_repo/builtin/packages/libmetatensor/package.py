# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Libmetatensor(CMakePackage):
    """Self-describing sparse tensor data format for atomistic machine learning and beyond."""

    homepage = "https://docs.metatensor.org"
    url = "https://github.com/metatensor/metatensor/releases/download/metatensor-core-v0.1.14/metatensor-core-cxx-0.1.14.tar.gz"
    git = "https://github.com/metatensor/metatensor.git"

    maintainers("HaoZeke", "luthaf", "rmeli")
    license("BSD-3-Clause", checked_by="HaoZeke")

    version("0.1.14", sha256="dc6cdd9cf0113e2f012ecf68b81cc7cfc71bef3d2020b41574de8fa403dba646")

    variant("static", default=False, description="Build both shared and static library versions")

    generator("ninja")

    depends_on("cmake@3.16:", type="build")
    depends_on("rust@1.74.0:", type="build")
    depends_on("c", type="build")
    depends_on("cxx", type="build")

    def cmake_args(self):
        args = [self.define_from_variant("METATENSOR_INSTALL_BOTH_STATIC_SHARED", "static")]
        return args
