# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Snls(CMakePackage, CudaPackage, ROCmPackage):
    """Small solver for Nonlinear systems of equations"""

    homepage = "https://github.com/LLNL/SNLS"
    url = "https://github.com/llnl/SNLS/archive/refs/tags/v0.4.4.tar.gz"
    git = "https://github.com/LLNL/SNLS.git"

    maintainers("rblake-llnl")

    license("BSD-3-Clause", checked_by="rblake-llnl")

    version("develop", branch="develop")
    version("v0.4.4", sha256="dbe89167c6ab9d7a76515cb5c0413f3673272bd1fc8cd20d83ba81815241f191")
    version("v0.4.3", sha256="51c4ddf56e14c24fb7358ec13bbf3ddb1bbdfbc1eefe7126f42726e3a813b250")
    version("v0.4.2", sha256="3a4e72069df932b71a4c4f940c6bcbc2ddad20686e81178c97de9725efe9a0aa")
    version("v0.4.1", sha256="cffcfb7bb033319760fc42491eb58981190c04dcb2bb17aa6d544564854512f3")
    version("v0.4.0", sha256="dfedf72272ef8bbf41d62ae2e8f2b1e48653b1ec364a19b6a832e2dd2c19d7ea")

    variant("shared", default=True, description="build shared libs")

    depends_on("blt", type=("build"))
    depends_on("c", type=("build"))
    depends_on("cxx", type=("build"))
    depends_on("chai")
    depends_on("umpire")
    depends_on("raja")
    depends_on("camp")
    depends_on("fmt")

    def cmake_args(self):
        """
        Generate the list of CMake arguments for building SNLS
        """
        spec = self.spec
        args = [
            self.define("ENABLE_TESTS", False),
            self.define("ENABLE_GTEST", False),
            self.define("USE_BATCH_SOLVERS", True),
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define("BLT_SOURCE_DIR", spec["blt"].prefix),
            self.define("RAJA_DIR", spec["raja"].prefix.lib.cmake.raja),
            self.define("CAMP_DIR", spec["camp"].prefix.lib.cmake.camp),
            self.define("UMPIRE_DIR", spec["umpire"].prefix),
            self.define("CHAI_DIR", spec["chai"].prefix.lib.cmake.chai),
            self.define("FMT_DIR", spec["fmt"].prefix.lib64.cmake.fmt),
        ]
        return args
