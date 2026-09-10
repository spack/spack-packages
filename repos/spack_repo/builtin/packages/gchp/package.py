# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import shutil

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Gchp(CMakePackage):
    """GEOS-Chem High Performance model of atmospheric chemistry"""

    homepage = "https://gchp.readthedocs.io/"
    url = "https://github.com/geoschem/GCHP/archive/13.4.0.tar.gz"
    git = "https://github.com/geoschem/GCHP.git"
    maintainers("lizziel", "laestrada")

    license("MIT")

    version("14.7.1", commit="503642dfe2b02c219e69fed52e027faea1a0063d", submodules=True)
    version("14.7.0", commit="3216f281670dc124f2649dedfa60293eba38a8de", submodules=True)
    version("14.6.3", commit="1f5d79a54a55a716c2707c607794441ff5cc5c30", submodules=True)
    version("14.6.2", commit="54bf9e48fcb0e2b7968382052f8c86ee115d6c0c", submodules=True)
    version("14.6.1", commit="c4591eb9953c732d81026976e494352da90b17a9", submodules=True)
    version("14.6.0", commit="fbb215f11977f6a0a4e7cc1c27843e3409f1360c", submodules=True)
    version("14.5.3", commit="915abefbe20a628a7c00becda0306a7c29eff6cb", submodules=True)
    version("14.5.2", commit="59fcade5dbeb924c86d00d5cef539e8181c89e23", submodules=True)
    version("14.5.1", commit="5b7a4a7d39d9bd2da894ca9d7af4e0040475f1d4", submodules=True)
    version("14.5.0", commit="a9e7c3f073921a0c31327332fd29facc8b31db99", submodules=True)
    version("14.4.3", commit="e499969f3831261e1fd15774b9fc68d01d012ba2", submodules=True)
    version("14.4.2", commit="856010810a7b32d3df695a4802dd65868f9a5a8b", submodules=True)
    version("14.4.1", commit="966d10d6c95236e53cc93fa334715d235d325b76", submodules=True)
    version("14.4.0", commit="cfbebef856dfb5aaa2504116d50bef65484a98e8", submodules=True)
    version("14.3.1", commit="495766f538ab82d775cc7b12fcf320712b04550b", submodules=True)
    version("14.3.0", commit="14cb7564fde9c9457b638ceb4d091ffec578f0b8", submodules=True)
    version("14.2.3", commit="3a1a52faac1179a7fa8ac405481221667be4ef91", submodules=True)
    version("14.2.2", commit="074494ee693714a16a7f93ffb8d354a07150e34d", submodules=True)
    version("14.2.1", commit="6413378b92167be9dd6d564a17f058b77f1a0091", submodules=True)
    version("14.2.0", commit="2c5417bb0b3b351e2298d07e885685c7e0298c47", submodules=True)
    version("14.1.1", commit="0345abf5cb237a72e0fc33873263f6618ff3e16b", submodules=True)
    version("14.1.0", commit="c6d533b7481be2dca303e53380238074f1c0cf01", submodules=True)
    version("14.0.2", commit="7973fb683095ccee24c9ca006ef95421b85d1781", submodules=True)
    version("14.0.1", commit="a1be697c01c507abcd4645598fea795293414b87", submodules=True)
    version("14.0.0", commit="e7a5aaf226ed41c43ef38b42ff8aace4a4307104", submodules=True)
    version("13.4.0", commit="d8c6d4d8db1c5b0ba54d4893185d999a619afc58", submodules=True)
    version("13.3.4", commit="efb2346381648ffff04ce441d5d61d7fec0c53fe", submodules=True)
    version("13.2.1", commit="9dc2340cac684971fa961559a4dc3d8818326ab8", submodules=True)
    version("13.1.2", commit="106b8f783cafabd699e53beec3a4dd8aee45234b", submodules=True)
    version("13.1.1", commit="a17361a78aceab947ca51aa1ecd3391beaa3fcb2", submodules=True)
    version("13.1.0", commit="4aca45370738e48623e61e38b26d981d3e20be76", submodules=True)
    version("13.0.2", commit="017ad7276a801ab7b3d6945ad24602eb9927cf01", submodules=True)
    version("13.0.1", commit="f40a2476fda901eacf78c0972fdb6c20e5a06700", submodules=True)
    version("13.0.0", commit="1f5a5c5630c5d066ff8306cbb8b83e267ca7c265", submodules=True)
    version("dev", branch="dev", submodules=True)

    patch("for_aarch64.patch", when="target=aarch64:")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    depends_on("esmf@8.0.1", when="@:13")
    depends_on("esmf@8.0.0:", when="@14.0")
    depends_on("esmf@8.1.0:", when="@14.1")
    depends_on("esmf@8.4.2:", when="@14.2:14.6")
    depends_on("esmf@8.6.1:", when="@14.7:")
    depends_on("udunits@2", when="@14.7:")
    depends_on("mpi@3")
    depends_on("netcdf-fortran")
    depends_on("cmake@3.24:")
    depends_on("libfabric", when="+ofi")
    depends_on("m4")

    variant("omp", default=False, description="OpenMP parallelization")
    variant("real8", default=True, description="REAL*8 precision")
    variant("apm", default=False, description="APM Microphysics (Experimental)")
    variant("rrtmg", default=False, description="RRTMG radiative transfer model")
    variant("luo", default=False, description="Luo et al 2019 wet deposition scheme")
    variant("tomas", default=False, description="TOMAS Microphysics (Experimental)")
    variant("ofi", default=False, description="Build with Libfabric support")

    def cmake_args(self):
        args = [
            self.define("RUNDIR", self.prefix),
            self.define_from_variant("OMP", "omp"),
            self.define_from_variant("USE_REAL8", "real8"),
            self.define_from_variant("APM", "apm"),
            self.define_from_variant("RRTMG", "rrtmg"),
            self.define_from_variant("LUO_WETDEP", "luo"),
            self.define_from_variant("TOMAS", "tomas"),
        ]
        return args

    def install(self, spec, prefix):
        super().install(spec, prefix)
        # Preserve source code in prefix for two reasons:
        # 1. Run directory creation occurs independently of code compilation,
        # possibly multiple times depending on user needs,
        # and requires the preservation of some of the source code structure.
        # 2. Run configuration is relatively complex and can result in error
        # messages that point to specific modules / lines of the source code.
        # Including source code thus facilitates runtime debugging.
        shutil.move(self.stage.source_path, join_path(prefix, "source_code"))

        # Ensure that the bin directory gets installed
        install_tree(join_path(self.build_directory, "bin"), prefix.bin)
