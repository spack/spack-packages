# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPycompadre(PythonPackage):
    """The Compadre Toolkit provides a performance portable solution for the
    parallel evaluation of computationally dense kernels. The toolkit
    specifically targets the Generalized Moving Least Squares (GMLS) approach,
    which requires the inversion of small dense matrices. The result is a set
    of weights that provide the information needed for remap or entries that
    constitute the rows of some globally sparse matrix.
    """

    homepage = "https://github.com/sandialabs/compadre"
    git = "https://github.com/sandialabs/compadre.git"
    url = "https://github.com/sandialabs/compadre/archive/v1.3.0.tar.gz"
    maintainers("kuberry")

    version("master", branch="master")
    version("1.7.2", sha256="4b7c2944300fd025957be44a1114177dfa0aafcf9e613d830a94e020b2f1751e")
    version(
        "1.6.2",
        sha256="ad4122feed81e9f661ee86e73ad4bf53dbfb2470b389a4ea31e6c8d727c8bec8",
        deprecated=True,
    )
    version(
        "1.6.0",
        sha256="5d937f85c2e64b50955beab1ac9f1083162f5239a5f13a40ef9a9c0e6ad216c9",
        deprecated=True,
    )
    version(
        "1.5.0",
        sha256="b7dd6020cc5a7969de817d5c7f6c5acceaad0f08dcfd3d7cacfa9f42e4c8b335",
        deprecated=True,
    )
    version(
        "1.4.1",
        sha256="2e1e7d8e30953f76b6dc3a4c86ec8103d4b29447194cb5d5abb74b8e4099bdd9",
        deprecated=True,
    )
    version(
        "1.3.0",
        sha256="f711a840fd921e84660451ded408023ec3bcfc98fd0a7dc4a299bfae6ab489c2",
        deprecated=True,
    )

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("cmake@3.10:", type="build", when="@:1.4")
    depends_on("cmake@3.16:", type="build", when="@1.5:1.6")
    depends_on("cmake@3.24:", type="build", when="@1.7:")

    depends_on("kokkos-kernels@3.3.01:4", when="@:1.5")
    depends_on("kokkos-kernels@4:", when="@1.6")
    depends_on("kokkos-kernels@4.5.1:", when="@1.7:")
    requires("%clang", when="^kokkos+cuda~wrapper")

    variant(
        "build_type",
        default="Debug",
        values=("Debug", "Release", "RelWithDebInfo", "MinSizeRel"),
        description="CMake build type: Debug, Release, RelWithDebInfo, MinSizeRel",
    )
    variant("extreme_debug", default="False", description="Enable extreme debugging")
    conflicts("+extreme_debug", when="build_type=Release")
    conflicts("+extreme_debug", when="build_type=RelWithDebInfo")

    depends_on("python@3.4:", type=("build", "link", "run"), when="@:1.5")
    depends_on("python@3.6:", type=("build", "link", "run"), when="@1.6")
    depends_on("python@3.10:", type=("build", "link", "run"), when="@1.7:")

    depends_on("py-setuptools", type="build")
    depends_on("py-cython@0.23:", type="build")

    depends_on("py-pybind11", type="build", when="@:1.6")
    depends_on("py-nanobind", type="build", when="@1.7:")

    depends_on("py-numpy@:2.3", when="@:1.6")
    depends_on("py-numpy@2.1:", when="@1.7:")

    # fixes duplicate symbol issue with static library build
    patch(
        "https://github.com/sandialabs/Compadre/commit/af91a6ee3831dc951445df76053ec6315c58cb45.patch?full_index=1",
        sha256="e267b74f8ecb8dd23970848ed919d29b7d442f619ce80983e02a19f1d9582c61",
        when="@1.5.0",
    )

    # logic borrowed from Trilinos recipe
    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        spec = self.spec
        if "^kokkos+cuda+wrapper" in spec:
            if "+mpi" in spec:
                env.set("OMPI_CXX", self["kokkos-nvcc-wrapper"].kokkos_cxx)
                env.set("MPICH_CXX", self["kokkos-nvcc-wrapper"].kokkos_cxx)
                env.set("MPICXX_CXX", self["kokkos-nvcc-wrapper"].kokkos_cxx)
            else:
                env.set("CXX", self["kokkos-nvcc-wrapper"].kokkos_cxx)

        if "^kokkos+rocm" in spec:
            if "+mpi" in spec:
                env.set("OMPI_CXX", self.spec["hip"].hipcc)
                env.set("MPICH_CXX", self.spec["hip"].hipcc)
                env.set("MPICXX_CXX", self.spec["hip"].hipcc)
            else:
                env.set("CXX", self.spec["hip"].hipcc)

    @run_before("install")
    def set_cmake_from_variants(self):
        spec = self.spec
        with open("cmake_opts.txt", "w") as f:
            f.write("Kokkos_ROOT:PATH=%s\n" % spec["kokkos"].prefix)
            f.write("KokkosKernels_ROOT:PATH=%s\n" % spec["kokkos-kernels"].prefix)

            # Compadre_DEBUG is default OFF and handled from CMAKE_BUILD_TYPE beginning in v1.7.0
            f.write("CMAKE_BUILD_TYPE:STRING=%s\n" % spec.variants["build_type"].value)
            if spec.satisfies("@:1.6"):
                if spec.variants["build_type"].value.upper() == "RELEASE":
                    f.write("Compadre_DEBUG:BOOL=OFF\n")
                elif spec.variants["build_type"].value.upper() == "RELWITHDEBINFO":
                    f.write("Compadre_DEBUG:BOOL=OFF\n")
                else:
                    f.write("Compadre_DEBUG:BOOL=OFF\n")

            if spec.variants["extreme_debug"].value:
                f.write("Compadre_EXTREME_DEBUG:BOOL=ON\n")
