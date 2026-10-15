# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RH5mread(RPackage):
    """A fast HDF5 reader"""

    bioc = "h5mread"

    with default_args(get_full_repo=True):
        version("1.4.1", commit="13dfc9b2293de730d6a6a79dc345bc59b4b05b04")  # bioc 3.23
        version("1.2.1", commit="b3770761af5669f989d4a6f6ab365b8f69c3740b")  # bioc 3.22
        version("1.0.1", commit="1719e5241bb5c9aa70b6f7fe020e8e10b14f8ee8")  # bioc 3.21

    depends_on("c", type="build")

    depends_on("r@4.5:", type="build")

    depends_on("r-biocgenerics", type=("build", "run"))

    depends_on("r-iranges", type=("build", "run"))

    depends_on("r-s4arrays", type=("build", "run"))

    depends_on("r-s4vectors@0.50.2:", type=("build", "run"), when="@1.4.1:")
    depends_on("r-s4vectors", type=("build", "run"))

    depends_on("r-sparsearray", type=("build", "run"))

    depends_on("r-rhdf5", type=("build", "run"))

    depends_on("r-rhdf5filters", type=("build", "run"))

    depends_on("curl", type=("build", "link"))

    depends_on("gmake", type="build")

    # > h5mread.so: undefined symbol: H5Treclaim
    conflicts("^r-rhdf5@2.28:2.54", when="@1.4")

    # > fatal error: hdf5_hl.h: No such file or directory
    conflicts("^r-rhdf5@2.24:2.26")
