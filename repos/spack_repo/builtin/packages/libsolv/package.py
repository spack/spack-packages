# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Libsolv(CMakePackage):
    """Library for solving packages and reading repositories."""

    homepage = "https://en.opensuse.org/OpenSUSE:Libzypp_satsolver"
    url = "https://github.com/openSUSE/libsolv/archive/refs/tags/0.7.34.tar.gz"

    maintainers("charmoniumQ")

    license("BSD-3-Clause")

    version("0.7.34", sha256="fd9c8a75d3ca09d9ff7b0d160902fac789b3ce6f9fb5b46a7647895f9d3eaf05")
    version("0.7.24", sha256="62743265222a729c7fe94c40f7b90ccc1ac5568f5ee6df46884e7ce3c16c78c7")
    version("0.7.22", sha256="968aef452b5493751fa0168cd58745a77c755e202a43fe8d549d791eb16034d5")

    variant("shared", default=True, description="Build shared libraries")
    variant("conda", default=False, description="Include solv/conda.h")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("expat", type="link")
    depends_on("zlib-api", type="link")

    def cmake_args(self):
        return [
            self.define("ENABLE_STATIC", self.spec.satisfies("~shared")),
            self.define("DISABLE_DYNAMIC", self.spec.satisfies("~shared")),
            self.define_from_variant("ENABLE_CONDA", "conda"),
        ]
