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
    git = "https://github.com/gavinsalam/hoppet.git"

    tags = ["hep"]
    maintainers("haralmha")

    build_system(
        conditional("autotools", when="@:1"), conditional("cmake", when="@2:"), default="cmake"
    )

    version("2.3.0", sha256="d631c63baeb66977a4fa6c79c4603fe05db1b8f6b352121f72f019183bf05ecc")
    version("2.2.2", sha256="b750b2b9a8eb532d7bf2c8928710762fc28fb2b4c5c1f403fd6a1af35d8c983f")
    version("2.1.4", sha256="5b363c4ce97f39cbfd558280412a6f9268624067059005d1f12ab14582fcf813")
    version("2.0.1", sha256="c95a47a4d9cdf241126614ab3f330e84a2ede7288eb3599bf2fef6b80be98030")
    version("1.2.0", sha256="6e00eb56a4f922d03dfceba7b389a3aaf51f277afa46d7b634d661e0797e8898")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")
