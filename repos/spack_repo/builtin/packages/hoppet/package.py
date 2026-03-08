# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems import autotools, cmake
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
    version("2.1.3", sha256="9373818e296dafefbd77e73effac4901cc20c1936dd43bb4cbaf4a3b69283b1d")
    version("2.1.2", sha256="d5a0feb801174546b3f0a1e1ad76c3afe8002ec736d3ac9117f27bdab3b8706d")
    version("2.1.1", sha256="99440483f2b4bd89d942adc9f2651052efbdf1a380121a89278b683fdc547899")
    version("2.1.0", sha256="f65b85ec08cbe5c075cf781b758234ae0fa01651f4d1fe1c4a6467954592b867")
    version("2.0.1", sha256="c95a47a4d9cdf241126614ab3f330e84a2ede7288eb3599bf2fef6b80be98030")
    version("2.0.0", sha256="daf8c09b3c73bd9cb003b18ccb0d4a2d479eb9a718f51e4c14e78e59250f1a55")
    version("1.2.0", sha256="6e00eb56a4f922d03dfceba7b389a3aaf51f277afa46d7b634d661e0797e8898")

    depends_on("cxx", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    with when("build_system=cmake"):
        depends_on("cmake@3.15:", type="build")
