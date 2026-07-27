# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RMatrixmodels(RPackage):
    """Modelling with Sparse and Dense Matrices.

    Modelling with sparse and dense 'Matrix' matrices, using modular prediction
    and response module classes."""

    cran = "MatrixModels"

    version("0.5-4", sha256="f57af9e0a35a3fea77790e46846482c6c7de0d0ea1996a995a5924f2d41cf33c")
    version("0.5-3", sha256="c2db5406c6b0b9d348b44eea215a39c64fc087099fea1342a04d50326577f20f")
    version("0.5-1", sha256="3fc55bdfa5ab40c75bf395e90983d14c9715078c33c727c1658e4e1f36e43ea9")
    version("0.5-0", sha256="a87faf1a185219f79ea2307e6787d293e1d30bf3af9398e8cfe1e079978946ed")
    version("0.4-1", sha256="fe878e401e697992a480cd146421c3a10fa331f6b37a51bac83b5c1119dcce33")

    with default_args(type=("build", "run")):
        depends_on("r@3.6.0:", when="@0.5-1:")
        depends_on("r@3.0.1:")

        depends_on("r-matrix@1.6-0:", when="@0.5-2:")
        depends_on("r-matrix@1.4-2:", when="@0.5-1:")
        depends_on("r-matrix@1.1-5:")

    conflicts("r-matrix@1.8:")
