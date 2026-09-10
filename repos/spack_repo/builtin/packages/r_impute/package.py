# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RImpute(RPackage):
    """impute: Imputation for microarray data.

    Imputation for microarray data (currently KNN only)"""

    bioc = "impute"

    with default_args(get_full_repo=True):
        # This package didn't change since version 1.32.0 (bioc 2.11).
        # The latest 1.86.0 is provided just not to scare the users, although it is also spurious.

        version("1.86.0", commit="9d2f1a82ab21cbda0f76f735c07a141c7361dedc")  # bioc 3.23
        version("1.74.0", commit="6dc26573263e337d4b521f006701f022bbad21b9", deprecated=True)
        version("1.72.0", commit="638ac916464f5a392b947ef5bb426b8445d27325", deprecated=True)
        version("1.70.0", commit="970b2c28d908e26369b01dddf36dab2f8916d4af", deprecated=True)
        version("1.68.0", commit="fa4e4d883e609633c49d865a44acd6a79954eaac", deprecated=True)
        version("1.64.0", commit="31a5636f4dfbb1fd61386738786a0de048a620c2", deprecated=True)
        version("1.58.0", commit="dc17173df08d965a0d0aac9fa4ad519bd99d127e", deprecated=True)
        version("1.56.0", commit="6c037ed4dffabafceae684265f86f2a18751b559", deprecated=True)
        version("1.54.0", commit="efc61f5197e8c4baf4ae881fb556f0312beaabd8", deprecated=True)
        version("1.52.0", commit="7fa1b917a5dd60f2aaf52d9aae1fcd2c93511d63", deprecated=True)
        version("1.50.1", commit="31d1cc141797afdc83743e1d95aab8a90ee19b71", deprecated=True)
        version("1.32.0", commit="d9a48a7491e4ed39eb7e8cf5f28172301b58de47")

    depends_on("c", type="build")  # it is fortran-only, but c compiler is used for linking
    depends_on("fortran", type="build")

    depends_on("r@2.10:", type=("build", "run"))
