# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Hoppet(AutotoolsPackage, CMakePackage):
    """A Fortran 95 package for carrying out QCD DGLAP evolution and other
    common manipulations of parton distribution functions (PDFs)."""

    homepage = "https://hoppet.hepforge.org/"
    url = "https://github.com/gavinsalam/hoppet/archive/refs/tags/hoppet-1.2.0.tar.gz"

    tags = ["hep"]
    maintainers("haralmha")

    # Version 2.0.0+ switched from custom autotools to CMake
    build_system(
        conditional("autotools", when="@:1"), conditional("cmake", when="@2:"), default="cmake"
    )

    version("2.1.4", sha256="5b363c4ce97f39cbfd558280412a6f9268624067059005d1f12ab14582fcf813")
    version("2.0.1", sha256="c95a47a4d9cdf241126614ab3f330e84a2ede7288eb3599bf2fef6b80be98030")
    version("1.2.0", sha256="6e00eb56a4f922d03dfceba7b389a3aaf51f277afa46d7b634d661e0797e8898")

    depends_on("cxx", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    with when("build_system=cmake"):
        depends_on("cmake@3.15:", type="build")
