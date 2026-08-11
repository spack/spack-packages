# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RRsubread(RPackage):
    """Mapping, quantification and variant analysis of sequencing data"""

    bioc = "Rsubread"

    with default_args(get_full_repo=True):
        version("2.26.0", commit="2c0bab403dc79708587393438b0634a0dc79a929")  # bioc 3.23
        version("2.22.1", commit="f06e38b33a12e2403dd467e4c7969596b6126741")  # bioc 3.21
        version("2.16.0", commit="62b92c9ed3fc2be89ed9f29e3db1809d1e115dbc")
        version("2.14.2", commit="863bd98c6523b888da59335a6acb516d2676d412")  # bioc 3.17

    depends_on("c", type="build")

    depends_on("r", type=("build", "run"))

    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-r-utils", type=("build", "run"))
    depends_on("zlib-api", type=("build", "run"))
