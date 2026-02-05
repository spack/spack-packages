# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Gsibec(CMakePackage):
    """GSIbec: Extracts the background error covariance (BEC) model
    capabilities from the Gridpoint Statistical Interpolation (GSI)
    atmospheric analysis system into a library of its own."""

    homepage = "https://github.com/GEOS-ESM/gsibec"
    git = "https://github.com/GEOS-ESM/gsibec.git"
    url = "https://github.com/GEOS-ESM/gsibec/archive/refs/tags/1.0.2.tar.gz"

    maintainers("mathomp4", "danholdaway")

    license("Apache-2.0")

    version("develop", branch="develop")
    version("1.4.0", sha256="aa512995c32bd4a9998584a62707abed299fe34af4e9dbf5b44aebd335376e54")
    version("1.3.1", sha256="fe7dbe7d170b47dbacc3febc42fc9877c118860b1532d70246bc73934e548185")
    version("1.2.2", sha256="c15e6a2e75e6b4b0727490bff6a52c02c7309cc48a202e393009074ecf33b06a")
    version("1.2.1", sha256="83bf12ad6603d66e2e48b50cfcb57b7acd64e0d428a597a842db978a3277baf6")
    version("1.1.3", sha256="9cac000562250487c16608e8245d97457cc1663b1793b3833be5a76ebccb4b47")
    version("1.1.2", sha256="8bdcdf1663e6071b6ad9e893a76307abc70a6de744fb75a13986e70242993ada")
    version("1.0.7", sha256="53912f1f19d46f4941b377803cc2fce89a2b50d2ece7562f8fd65215a8908158")
    version("1.0.6", sha256="10e2561685156bcfba35c7799732c77f9c05bd180888506a339540777db833dd")
    version("1.0.5", sha256="ac0cecc59e38da7eefb5a8f27975b33752fa61a4abd3bdbbfb55578ea59d95b3")
    version("1.0.4", sha256="6460e221f2a45640adab016336c070fbe3e7c4b6fc55257945bf5cdb38d5d3e2")
    version("1.0.3", sha256="f104daf55705c5093a3d984073f082017bc9166f51ded36c7f7bb8adf233c916")
    version("1.0.2", sha256="7dc02f1f499e0d9f2843440f517d6c8e5d10ea084cbb2567ec198ba06816bc8b")

    depends_on("c", type="build")
    depends_on("fortran", type="build")

    depends_on("mpi", type=("build", "run"))
    depends_on("netcdf-c +mpi", type=("build", "run"))
    depends_on("netcdf-fortran", type=("build", "run"))

    depends_on("lapack", type=("build", "run"))

    depends_on("ecbuild", type="build")
    depends_on("jedi-cmake", type="build")

    # sp is used in 1.3.x and earlier and ip in 1.4.x and later
    depends_on("ip@5", when="@1.4:", type=("build", "run"))
    depends_on("sp", when="@:1.3", type=("build", "run"))

    def cmake_args(self):
        return [
            self.define("ENABLE_MKL", self.spec.satisfies("^[virtuals=lapack] intel-oneapi-mkl"))
        ]
