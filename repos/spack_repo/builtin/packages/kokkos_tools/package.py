# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class KokkosTools(CMakePackage):
    """Kokkos Profiling and Debugging Tools"""

    homepage = "https://github.com/kokkos/kokkos-tools/"
    git = "https://github.com/kokkos/kokkos-tools.git"
    url = (
        "https://github.com/kokkos/kokkos-tools/releases/download/5.2.0/kokkos-tools-5.2.0.tar.gz"
    )

    maintainers("jennfshr", "vlkale", "rbberger")
    license("Apache-2.0 WITH LLVM-exception")

    version("develop", branch="develop")

    version("5.2.0", sha256="545169f76709a7e8391b3c8bbf3cc1b03844095fe54a85946e840eab4cbfc513")

    variant("mpi", default=False, description="Enable MPI support")
    variant("papi", default=False, description="Enable PAPI support")

    depends_on("cxx", type="build")

    depends_on("kokkos")
    depends_on("mpi", when="+mpi")
    depends_on("papi", when="+papi")

    def cmake_args(self):
        # The plugins are intentionally disabled the time to properly introduce new variants
        # with associated dependencies.
        # Feel free to contribute.
        args = [
            self.define("KokkosTools_ENABLE_APEX", False),
            self.define("KokkosTools_ENABLE_CALIPER", False),
            self.define("KokkosTools_ENABLE_SYSTEMTAP", False),
            self.define("KokkosTools_ENABLE_VARIORUM", False),
            self.define("KokkosTools_ENABLE_EXAMPLES", False),
            self.define("KokkosTools_ENABLE_SINGLE", False),
            self.define("KokkosTools_ENABLE_TESTS", False),
            self.define_from_variant("KokkosTools_ENABLE_MPI", "mpi"),
            self.define_from_variant("KokkosTools_ENABLE_PAPI", "papi"),
        ]
        return args
