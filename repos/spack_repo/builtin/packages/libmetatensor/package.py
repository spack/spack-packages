# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage, generator

from spack.package import *


class Libmetatensor(CMakePackage):
    """Self-describing sparse tensor data format for atomistic machine learning and beyond."""

    homepage = "https://docs.metatensor.org"
    url = "https://github.com/metatensor/metatensor/releases/download/metatensor-core-v0.0.0/metatensor-core-cxx-0.0.0.tar.gz"
    git = "https://github.com/metatensor/metatensor.git"

    maintainers("HaoZeke", "Luthaf", "RMeli")
    license("BSD-3-Clause", checked_by="HaoZeke")

    version("0.1.19", sha256="2d319186057cf6da8fe39cc4f961baccce59c4486223113ce554632ae7765e26")
    version("0.1.17", sha256="42119e11908239915ccc187d7ca65449b461f1d4b5af4d6df1fb613d687da76a")

    variant("shared", default=True, description="Build shared library version")

    generator("ninja")

    depends_on("cmake@3.16:", type="build")
    depends_on("cmake@3.22:", type="build", when="@0.1.18:")
    depends_on("rust@1.74.0:", type="build")
    depends_on("c", type="build")
    depends_on("cxx", type="build")

    def cmake_args(self):
        args = [
            self.define("METATENSOR_INSTALL_BOTH_STATIC_SHARED", "OFF"),
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
        ]
        return args
