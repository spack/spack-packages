# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RSparsearray(RPackage):
    """High-performance sparse data representation and manipulation in R."""

    bioc = "SparseArray"

    with default_args(get_full_repo=True):
        version("1.12.2", commit="dd96584c2f1284fe00041e392b5bed5749b4e42d")  # bioc 3.23
        version("1.11.13", commit="65383c02f986832b1416c6ad39da800d8ced05df")
        version("1.10.10", commit="ae957c5c70aacacb712d2449d9edeab2362c7904")
        version("1.9.2", commit="62a3a8c1957f2584b3ed0989ae02bb2ae1f3bc80")
        version("1.8.1", commit="ca78384f77def2f2e068739e8b43688eed3bb9da")  # bioc 3.21

    depends_on("c", type="build")

    depends_on("r@4.3:", type=("build", "run"))
    depends_on("r@4.5:", type=("build", "run"), when="@1.11:")

    depends_on("r-biocgenerics@0.43.1:", type=("build", "run"))

    depends_on("r-iranges", type=("build", "run"))

    depends_on("r-matrix", type=("build", "run"))

    depends_on("r-matrixgenerics@1.11.1:", type=("build", "run"))

    depends_on("r-matrixstats", type=("build", "run"))

    depends_on("r-s4arrays@1.11.1:", type=("build", "run"), when="@1.11.5:")
    depends_on("r-s4arrays@1.9.3:", type=("build", "run"), when="@1.9.2:")
    depends_on("r-s4arrays@1.5.11:", type=("build", "run"))

    depends_on("r-s4vectors@0.43.2:", type=("build", "run"))

    depends_on("r-xvector", type=("build", "run"))

    # <=1.10 calls DATAPTR without a declaration; GCC 14+ errors on this
    conflicts("%gcc@14: ^r@4.6:", when="@:1.10")
