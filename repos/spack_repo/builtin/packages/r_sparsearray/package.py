# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RSparsearray(RPackage):
    """The SparseArray package provides array-like containers for efficient
    in-memory representation of multidimensional sparse data in R (arrays and
    matrices). The package defines the SparseArray virtual class and two concrete
    subclasses: COO_SparseArray and SVT_SparseArray. Each subclass uses its own
    internal representation of the nonzero multidimensional data: the "COO layout"
    and the "SVT layout", respectively. SVT_SparseArray objects mimic as much as
    possible the behavior of ordinary matrix and array objects in base R. In
    particular, they suppport most of the "standard matrix and array API" defined
    in base R and in the matrixStats package from CRAN."""

    bioc = "SparseArray"

    license("Artistic-2.0")

    version("1.10.10", commit="ae957c5c70aacacb712d2449d9edeab2362c7904")

    depends_on("c", type="build")

    with default_args(type=("build", "run")):
        depends_on("r@4.3:")
        depends_on("r-matrix")
        depends_on("r-biocgenerics@0.43.1:")
        depends_on("r-matrixgenerics@1.11.1:")
        depends_on("r-s4vectors@0.43.2:")
        depends_on("r-s4arrays@1.10.1:")
        depends_on("r-xvector")
