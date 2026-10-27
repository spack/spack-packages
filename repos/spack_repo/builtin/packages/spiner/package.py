# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Spiner(CMakePackage):
    """Spiner:
    Performance portable routines for generic, tabulated, multi-dimensional data"""

    homepage = "https://github.com/lanl/spiner"
    git = "https://github.com/lanl/spiner.git"

    maintainers("rbberger")

    license("BSD-3-Clause")

    version("main", branch="main")
    version("1.7.0", commit="5ebeb5cf76ce9f65471d888280e74353f63cdccb", tag="v1.7.0")
    version("1.6.4", commit="3c0ea89be32065b3be9f897652acc7a7d81e133a", tag="1.6.4")

    with default_args(deprecated=True):
        version("1.6.3", commit="c379f5d2cce9625a60b149192ec43c8cff7b74b1", tag="1.6.3")
        version("1.6.2", commit="a0f4a214f42fe1e9aeb757f4cdeb7cd2b6eb65f7", tag="1.6.2")
        version("1.6.1", commit="24df4e52e98ca4b82539016268eec367d5b7d184", tag="1.6.1")
        version("1.6.0", commit="bf7ab6043d1253c7cad9bf7ba54c48194df730d6", tag="1.6.0")

    # When overriding/overloading varaints, the last variant is always used, except for
    # "when" clauses. Therefore, call the whens FIRST then the non-whens.
    # https://spack.readthedocs.io/en/latest/packaging_guide.html#overriding-variants
    variant("kokkos", default=False, description="Enable kokkos")

    variant("hdf5", default=False, description="Enable hdf5")
    variant("mpi", default=False, description="Support parallel hdf5")

    variant("python", default=False, description="Python, Numpy & Matplotlib Support")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("cmake@3.23:", when="@1.6.0:", type="build")
    depends_on("catch2@3.7.1:", when="@1.6.3:", type="test")
    depends_on("catch2@2.13.4:2.13.9", type="test")
    depends_on("ports-of-call@1.5.1:", when="@1.6.0:")
    depends_on("ports-of-call@2.0.0:", when="@1.7.0:")
    depends_on("ports-of-call@main", when="@main")

    depends_on("kokkos@3.3.00:", when="+kokkos")
    requires("^kokkos+cuda_constexpr", when="+kokkos ^kokkos+cuda")
    requires("^kokkos+cuda_lambda", when="+kokkos ^kokkos@4+cuda")

    depends_on("hdf5+hl~mpi", when="+hdf5~mpi")
    depends_on("hdf5+hl+mpi", when="+hdf5+mpi")

    depends_on("python", when="+python")
    depends_on("py-numpy", when="+python")
    depends_on("py-matplotlib", when="+python")

    conflicts("+mpi", when="~hdf5")

    def cmake_args(self):
        use_kokkos_option = "SPINER_TEST_USE_KOKKOS"

        args = [
            self.define("BUILD_TESTING", self.run_tests),
            self.define("SPINER_BUILD_TESTS", self.run_tests),
            self.define(
                "SPINER_TEST_USE_KOKKOS", self.run_tests and self.spec.satisfies("+kokkos")
            ),
            self.define_from_variant(use_kokkos_option, "kokkos"),
            self.define_from_variant("SPINER_USE_HDF", "hdf5"),
        ]
        if self.spec.satisfies("^kokkos+cuda"):
            args.append(
                self.define(
                    "CMAKE_CUDA_ARCHITECTURES", self.spec["kokkos"].variants["cuda_arch"].value
                )
            )
        if self.spec.satisfies("^kokkos+rocm") and not self.spec.satisfies(
            "^kokkos+rocm %cxx=llvm-amdgpu"
        ):
            args.append(self.define("CMAKE_CXX_COMPILER", self.spec["hip"].hipcc))
            args.append(self.define("CMAKE_C_COMPILER", self.spec["hip"].hipcc))
        if self.spec.satisfies("%cxx=llvm ^kokkos+cuda~wrapper %cxx=llvm") or self.spec.satisfies(
            "%cxx=llvm-amdgpu ^kokkos+rocm~wrapper %cxx=llvm-amdgpu"
        ):
            # explicitly disable launch compiler in these cases to avoid not getting
            # Spack wrapper rpaths
            args.append(self.define("Kokkos_LAUNCH_COMPILER", False))
        return args
