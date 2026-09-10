# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Topcom(AutotoolsPackage):
    """TOPCOM is a C++ package for computing triangulations of point
    configurations and oriented matroids. It can enumerate all triangulations,
    circuits, and cocircuits up to symmetry, using lock-free multi-threading
    for efficient performance on modern multi-core systems."""

    homepage = "https://www.wm.uni-bayreuth.de/de/team/rambau_joerg/TOPCOM/"
    url = "https://www.wm.uni-bayreuth.de/de/team/rambau_joerg/TOPCOM-Downloads/TOPCOM-1_1_2.tgz"

    maintainers("d-torrance")

    license("GPL-3.0-or-later", checked_by="d-torrance")

    version("1.1.2", sha256="4fb10754ee5b76056441fea98f2c8dee5db6f2984d8c14283b49239ad4378ab6")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("gmp")

    def url_for_version(self, version):
        return f"https://www.wm.uni-bayreuth.de/de/team/rambau_joerg/TOPCOM-Downloads/TOPCOM-{version.underscored}.tgz"
