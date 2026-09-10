# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RGensa(RPackage):
    """Generalized Simulated Annealing.

    Performs search for global minimum of a very complex non-linear objective
    function with a very large number of optima."""

    cran = "GenSA"

    version("1.1.15", sha256="68970dc3b463986b5b7130acbd42a5ae5a85835d004fb54f81b3ef5c2fccf925")
    version("1.1.14", sha256="66e455bb0e66d3c04af84d9dddc9b89f40b4cf9fe9ad1cf0714bcf30aa1b6837")
    version("1.1.8", sha256="375e87541eb6b098584afccab361dc28ff09d03cf1d062ff970208e294eca216")
    version("1.1.7", sha256="9d99d3d0a4b7770c3c3a6de44206811272d78ab94481713a8c369f7d6ae7b80f")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("r@2.12.0:", type=("build", "run"))
    # Rf_allocLang() was only added in r@4.4.1.
    depends_on("r@4.4.1:", type=("build", "run"), when="@1.1.15:")

    # Versions <= 1.1.14 use SET_TYPEOF, which was removed from Rinternals.h in r@4.6.0
    conflicts("r@4.6:", when="@:1.1.14")

    def patch(self):
        if self.spec.satisfies("@:1.1.8 ^r@4.4.0:"):
            # Utils.h relied on transitively including R_ext/BLAS.h from R_ext/Applic.h
            # r@4.4.0 removed this, so patch in BLAS.h header to allow for compilation
            with working_dir("src"):
                filter_file(
                    r"#include <R_ext/Applic.h>",
                    "#include <R_ext/Applic.h>\n#include <R_ext/BLAS.h>",
                    "Utils.h",
                )
