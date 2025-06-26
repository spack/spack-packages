# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems import cmake, meson
from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.meson import MesonPackage

from spack.package import *


class MctcLib(MesonPackage, CMakePackage):
    """Modular computation toolchain library for quantum chemistry file IO"""

    homepage = "https://github.com/grimme-lab/mctc-lib"
    url = "https://github.com/grimme-lab/mctc-lib/releases/download/v0.0.0/mctc-lib-0.0.0.tar.xz"
    git = "https://github.com/grimme-lab/mctc-lib"

    maintainers("awvwgk")

    license("Apache-2.0")

    build_system("cmake", "meson", default="meson")

    version("main", branch="main")

    version("0.4.2", sha256="ce1e962c79d871d3705be590aef44f07ca296843b85e164307290f8324769406")
    version("0.4.1", sha256="57fe4610c4fa21d0b797f88b68481c7be1e7d291daa12063caed51bee779b88a")
    version(
        "0.4.0-intel-2021-ubuntu-latest",
        sha256="b838a983137db1c223359e9b9d68cf04533b82f0e7390d485713676700c07cae",
    )
    version(
        "0.4.0-gnu-12-ubuntu-latest",
        sha256="1ead2810a0295484b5fc78a9b017f9e14152fda66ad0cecdf24e733ec2a38498",
    )
    version(
        "0.4.0-gnu-12-macos-latest",
        sha256="fc337b2b46bd664446b866d1c7a1d5cdfb1837e66d114e0d9fc6fbc1e7b47be5",
    )
    version(
        "0.4.0-gnu-10-ubuntu-latest",
        sha256="74fb14b1b2f7410cbeed0ebb854acf484989462baff46d9268f6591e83c992e7",
    )
    version("0.4.0", sha256="43f6988fc5a2c8d2d8397c6ef8d55f745c9869dd94a7dc9c099a0e1b7f423e40")
    version("0.3.2", sha256="8c4ebdf9d81272f0dfa0bfa6c7fecd51f1f3d83d3629c719298d9f349de6ee0b")
    version("0.3.1", sha256="a5032a0bbbbacc952037c5215b71aa6b438767a84bafb60fda25ba43c8835513")
    version("0.3.0", sha256="81f3edbf322e6e28e621730a796278498b84af0f221f785c537a315312059bf0")

    variant("json", default=False, description="Enable support for JSON")

    depends_on("fortran", type="build")  # generated

    depends_on("meson@0.57.2:", type="build", when="build_system=meson")

    depends_on("json-fortran@8:", when="+json")
    depends_on("pkgconfig", type="build")


class CMakeBuilder(cmake.CMakeBuilder):
    def cmake_args(self):
        return [self.define_from_variant("WITH_JSON", "json")]


class MesonBuilder(meson.MesonBuilder):
    def meson_args(self):
        return ["-Djson={0}".format("enabled" if "+json" in self.spec else "disabled")]
