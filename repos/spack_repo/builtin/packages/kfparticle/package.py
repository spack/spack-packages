# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Kfparticle(CMakePackage):
    """KFParticle is a package for reconstruction of short-lived particles
    in heavy-ion experiments based on the Kalman filter, as used by ALICE."""

    homepage = "https://github.com/alisw/KFParticle"
    url = "https://github.com/alisw/KFParticle/archive/refs/tags/v1.1-alice10.tar.gz"
    git = "https://github.com/alisw/KFParticle.git"

    maintainers("wdconinc")

    tags = ["hep"]

    license("GPL-3.0-only", checked_by="wdconinc")

    version(
        "1.1-alice10", sha256="141e9e90adc0855584e17fe0897848b66581878addb701f7e1b4a1419bfcad4d"
    )
    version(
        "1.1-alice9", sha256="7ee1c1cc39dead3f095a5fd79b6d48224e24edb3a0f1b626b95e8ea260e2945c"
    )
    version(
        "1.1-alice8", sha256="c2717e3405eb4c3d26b5d70c33b656d6510e236f76cc5ae5c5f8705410573fe0"
    )
    version(
        "1.1-alice7",
        sha256="2c4a51bff7e6786f65482395ca5b9fe23f1b3ce09b54057e1022bc494ed931bb",
        url="https://github.com/alisw/KFParticle/archive/refs/tags/alice/v1.1-7.tar.gz",
    )
    version(
        "1.1-alice6",
        sha256="c2cda2f4bbb829e8fb69788abac6a14874e284b0ca36b26ca25464364f77e5ea",
        url="https://github.com/alisw/KFParticle/archive/refs/tags/alice/v1.1-6.tar.gz",
    )

    variant("fixtarget", default=False, description="Compile for fixed target geometry")

    depends_on("cxx", type="build")

    depends_on("cmake@3.16:", type="build", when="@1.1-alice8:")
    # cmake_minimum_required(VERSION 2.8.8) is rejected by CMake 4
    depends_on("cmake@:3", type="build", when="@:1.1-alice7")

    depends_on("root")
    depends_on("vc")

    def cmake_args(self):
        return [
            self.define("CMAKE_CXX_STANDARD", self.spec["root"].variants["cxxstd"].value),
            self.define_from_variant("FIXTARGET", "fixtarget"),
        ]
