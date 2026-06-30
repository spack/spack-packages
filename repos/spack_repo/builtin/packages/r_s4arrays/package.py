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
        version("1.10.1", commit="a4cccbaab0d12176db3670665f0ca6c23bb900be")  # bioc 3.22
        version("1.8.1", commit="3ccac7337984c08cf086caedbef48d3d8d94b165")  # bioc 3.21
        version("1.6.0", commit="e100af0de22e3b49ce3b544c158eb327b1bd2133")  # bioc 3.20
        version("1.4.1", commit="472c245dc1c66c4eb0877b081e4a95f8eff97ba8")  # bioc 3.19
        version("1.2.1", commit="59b8f4e28d2273145411f0d5429d1f31f6b79e12")  # bioc 3.18
        version("1.0.6", commit="fbe4bb0f05465c737ef6dcd1d7def2f2e445e10b")  # bioc 3.17

    depends_on("c", type="build")

    depends_on("r@4.3.0:", type=("build", "run"))

    depends_on("r-s4vectors@0.47.6:", type=("build", "run"), when="@1.9.2:")
    depends_on("r-s4vectors", type=("build", "run"))

    depends_on("r-abind", type=("build", "run"), when="@1.1.5:")
    depends_on("r-biocgenerics@0.45.2:", type=("build", "run"))
    depends_on("r-crayon", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
