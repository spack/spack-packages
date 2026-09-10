# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Spiner(CMakePackage):
    """Spiner:
    Performance portable routines for generic, tabulated, multi-dimensional data"""

    homepage = "https://github.com/lanl/spiner"
    url = "https://github.com/lanl/spiner/archive/refs/tags/v1.7.0.tar.gz"
    git = "https://github.com/lanl/spiner.git"

    maintainers("rbberger")

    license("BSD-3-Clause")

    version("main", branch="main")
    version("1.7.0", sha256="effe6844fd895c4790eeebcb3f3bc7b3d4a7380554acfcc528d8d8296e88a9ba")
    version("1.6.4", sha256="a51de69e438f5e3893958736d246c41ca87fd6442ee1e0a9cc5d442861ac5404")
    version("1.6.3", sha256="f78c50e0b4d7c4fd3f380432f12a528941e2bee5171d6f200e9a52bbcea940e9")
    version("1.6.2", sha256="91fb403ce3b151fbdf8b6ff5aed0d8dde1177749f5633951027b100ebc7080d3")
    version("1.6.1", sha256="52774322571d3b9b0dc3c6b255257de9af0e8e6170834360f2252c1ac272cbe7")
    version("1.6.0", sha256="afa5526d87c78c1165ead06c09c5c2b9e4a913687443e5adff7b709ea4dd7edf")

    def url_for_version(self, version):
        if version < Version("1.7"):
            return f"https://github.com/lanl/spiner/archive/refs/tags/{version}.tar.gz"
        else:
            return f"https://github.com/lanl/spiner/archive/refs/tags/v{version}.tar.gz"

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
    requires("^kokkos+cuda_lambda+cuda_constexpr", when="+kokkos ^kokkos+cuda")

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
        if self.spec.satisfies("^kokkos+rocm"):
            args.append(self.define("CMAKE_CXX_COMPILER", self.spec["hip"].hipcc))
            args.append(self.define("CMAKE_C_COMPILER", self.spec["hip"].hipcc))
        if self.spec.satisfies("^kokkos+cuda"):
            args.append(self.define("CMAKE_CXX_COMPILER", self["kokkos"].kokkos_cxx))
        return args
