# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Snls(CMakePackage):
    """Small Non-Linear Solver for solving non-linear systems of equations"""

    homepage = "https://github.com/llnl/SNLS"
    url = "https://github.com/llnl/SNLS/archive/refs/tags/v0.4.4.tar.gz"
    git = "https://github.com/llnl/SNLS.git"

    maintainers("rcarson3")

    license("BSD-3-Clause", checked_by="rblake-llnl")

    version("develop", branch="develop")
    version(
        "v0.4.4",
        sha256="dbe89167c6ab9d7a76515cb5c0413f3673272bd1fc8cd20d83ba81815241f191",
        url="https://github.com/llnl/SNLS/archive/refs/tags/v0.4.4.tar.gz",
    )
    version(
        "v0.4.3",
        sha256="51c4ddf56e14c24fb7358ec13bbf3ddb1bbdfbc1eefe7126f42726e3a813b250",
        url="https://github.com/llnl/SNLS/archive/refs/tags/v0.4.3.tar.gz",
    )
    version(
        "v0.4.2",
        sha256="3a4e72069df932b71a4c4f940c6bcbc2ddad20686e81178c97de9725efe9a0aa",
        url="https://github.com/llnl/SNLS/archive/refs/tags/v0.4.2.tar.gz",
    )
    version(
        "v0.4.1",
        sha256="cffcfb7bb033319760fc42491eb58981190c04dcb2bb17aa6d544564854512f3",
        url="https://github.com/llnl/SNLS/archive/refs/tags/v0.4.1.tar.gz",
    )
    version(
        "v0.4.0",
        sha256="dfedf72272ef8bbf41d62ae2e8f2b1e48653b1ec364a19b6a832e2dd2c19d7ea",
        url="https://github.com/llnl/SNLS/archive/refs/tags/v0.4.0.tar.gz",
    )

    variant("shared", default=True, description="build shared libs")
    variant("tests", default=False, description="Build with tests enabled")
    variant("batch_solver", default=True, description="enable batch solver")
    variant(
        "cxxstd",
        default="17",
        values=("17", "20"),
        description="C++ standard to build with",
    )

    depends_on("blt", type=("build"))
    depends_on("c", type=("build"), when="+tests")
    depends_on("cxx", type=("build"))
    depends_on("chai", when="+batch_solver")
    depends_on("umpire", when="+batch_solver")
    depends_on("raja", when="+batch_solver")
    depends_on("camp", when="+batch_solver")
    depends_on("fmt", when="+batch_solver")

    @property
    def cxx_std(self):
        return self.spec.variants.get("cxxstd").value

    def cmake_args(self):
        """
        Generate the list of CMake arguments for building SNLS
        """
        spec = self.spec
        args = [
            self.define_from_variant("ENABLE_TESTS", "tests"),
            self.define_from_variant("ENABLE_GTEST", "tests"),
            self.define_from_variant("USE_BATCH_SOLVERS", "batch_solver"),
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define("BLT_CXX_STD", f"c++{self.cxx_std}"),
            self.define("BLT_SOURCE_DIR", spec["blt"].prefix),
            self.define("RAJA_DIR", spec["raja"].prefix),
            self.define("CAMP_DIR", spec["camp"].prefix),
            self.define("UMPIRE_DIR", spec["umpire"].prefix),
            self.define("CHAI_DIR", spec["chai"].prefix),
            self.define("FMT_DIR", spec["fmt"].prefix),
        ]
        return args
