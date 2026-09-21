# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Gyselalibxx(CMakePackage):
    """Gyselalib++ is a collection of C++ components for writing
    gyrokinetic semi-Lagrangian codes and similar."""

    homepage = "https://gyselax.github.io/gyselalibxx/"
    git = "https://github.com/gyselax/gyselalibxx.git"
    url = "https://github.com/gyselax/gyselalibxx/archive/refs/tags/v0.8.0.tar.gz"

    maintainers("EmilyBourne", "tpadioleau")

    license("MIT", checked_by="tpadioleau")

    version("develop", branch="devel", no_cache=True)
    version("0.8.0", sha256="86f695324cde542eb746e6016678c87c22c82557944b34f644153ac907a924ae")

    depends_on("cxx", type="build")
    depends_on("cmake@3.25:4", type="build")

    depends_on("ddc +fft +pdi +splines")
    depends_on("ddc@0.15", when="@0.8:")
    depends_on("ginkgo@1.8:1")
    depends_on("gmgpolar@2.3.1:2")
    depends_on("kokkos@4.4.1:5")
    depends_on("kokkos-kernels@4.5.1:5")
    depends_on("koliop@0.2", when="@0.8:")
    depends_on("lapack")
    depends_on("mpi")
    depends_on("paraconf@1")
    depends_on("pdi@1.10.1:1")

    depends_on("googletest@1.12:1 +gmock", type="test")
    depends_on("pdiplugin-decl-hdf5@1.10.1:1 +mpi", type="test")
    depends_on("pdiplugin-mpi@1.10.1:1", type="test")
    depends_on("pdiplugin-set-value@1.10.1:1", type="test")
    depends_on("python@3.11:3", type="test")
    depends_on("py-dask@2026.3:2026", type="test")
    depends_on("py-h5py@3.16:3", type="test")
    depends_on("py-matplotlib@3.11:3", type="test")
    depends_on("py-numpy@2.4:2", type="test")
    depends_on("py-pyyaml@6", type="test")
    depends_on("py-xarray@2026.4:2026", type="test")

    requires(
        "^kokkos +cuda_constexpr",
        when="^kokkos +cuda",
        msg="Gyselalib++ relies on the constexpr support of nvcc",
    )

    def cmake_args(self):
        args = [
            self.define("GYSELALIBXX_BUILD_SIMULATIONS", self.run_tests),
            self.define("GYSELALIBXX_BUILD_TESTING", self.run_tests),
            self.define("GYSELALIBXX_COMPILE_SOURCE", True),
            self.define("GYSELALIBXX_ENABLE_DEPRECATED", True),
        ]

        if self.spec.satisfies("^kokkos+cuda"):
            args.append(self.define("CMAKE_CXX_FLAGS", "-fno-ipa-sra"))

        if self.spec.satisfies("^kokkos+rocm"):
            args.append(self.define("CMAKE_CXX_COMPILER", self.spec["hip"].hipcc))
        else:
            args.append(self.define("CMAKE_CXX_COMPILER", self["kokkos"].kokkos_cxx))

        return args
