# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RS4arrays(RPackage):
    """The S4Arrays package defines the Array virtual class to be
    extended by other S4 classes that wish to implement a container
    with an array-like semantic."""

    bioc = "S4Arrays"

    with default_args(get_full_repo=True):
        version("1.12.0", commit="b1246fd0b81ac137623ee1c0d6587a59e8ad1073")  # bioc 3.23
        version("1.8.1", commit="3ccac7337984c08cf086caedbef48d3d8d94b165")  # bioc 3.21

    depends_on("c", type="build")

    depends_on("r@4.3.0:", type=("build", "run"))

    depends_on("r-abind", type=("build", "run"), when="@1.1.5:")
    depends_on("r-biocgenerics@0.45.2:", type=("build", "run"))
    depends_on("r-crayon", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))

    depends_on("r-s4vectors@0.47.6:", type=("build", "run"), when="@1.9.2:")
    depends_on("r-s4vectors", type=("build", "run"))

    depends_on("r-matrix", type=("build", "run"))
