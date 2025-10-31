# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class ProdUtil(CMakePackage):
    """
    Product utilities for the NCEP models.

    This is part of NOAA's NCEPLIBS project."""

    homepage = "https://github.com/NOAA-EMC/NCEPLIBS-prod_util"
    url = "https://github.com/NOAA-EMC/NCEPLIBS-prod_util/archive/refs/tags/v1.2.2.tar.gz"
    git = "https://github.com/NOAA-EMC/NCEPLIBS-prod_util"

    maintainers("AlexanderRichert-NOAA", "Hang-Lei-NOAA", "edwardhartnett")

    version("develop", branch="develop")
    version("2.1.2", sha256="af2e0163152b3afbc5a51ce5260265c3fb38e195900f4f90bff52cecb2bbf773")
    version("2.1.1", sha256="2f7507fa378a44f42b971f60de8152387c311bfa9c5c05a274c87b43a143aacd")
    version("2.1.0", sha256="fa7df4a82dae269ffb347b9007376fb0d9979c17c4974814ea82204b12d70ea5")

    depends_on("c", type="build")
    depends_on("fortran", type="build")

    depends_on("w3emc")

    def check(self):
        with working_dir(self.build_directory):
            make("test")
