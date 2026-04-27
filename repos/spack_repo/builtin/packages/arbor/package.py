# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage

from spack.package import *

class Arbor(CMakePackage, CudaPackage):
    """Arbor is a high-performance library for computational neuroscience
    simulations."""

    homepage = "https://arbor-sim.org"
    git = "https://github.com/arbor-sim/arbor.git"
    url = "https://github.com/arbor-sim/arbor/archive/refs/tags/v0.12.1.tar.gz"
    license("BSD-3-Clause")
    maintainers = ("thorstenhater",)
    submodules = True

    version("master", branch="master", submodules=True)
    version("develop", branch="master", submodules=True)
    version(
        "0.12.1",
        sha256="6584ccfaef1c8f9eab6c8794d0f4f06745cbfb7c2d701815c74ed9e6a101a3dc",
        url="https://github.com/arbor-sim/arbor/archive/refs/tags/v0.12.1.tar.gz",
        submodules=True,
    )
    version(
        "0.11.0",
        sha256="6df68b308dd629df993eda40319676cd43407ae211d0846100b0cf42e8c9ad22",
        url="https://github.com/arbor-sim/arbor/archive/refs/tags/v0.11.0.tar.gz",
        submodules=True,
    )
    version(
        "0.10.0",
        sha256="6b6cc900b85fbf833fae94817b9406a0d690dc28",
        url="https://github.com/arbor-sim/arbor/releases/download/v0.10.1/arbor-v0.10.0-full.tar.gz",
        submodules=True,
    )
    version(
        "0.9.0",
        sha256="5f9740955c821aca81e23298c17ad64f33f635756ad9b4a0c1444710f564306a",
        url="https://github.com/arbor-sim/arbor/releases/download/v0.9.0/arbor-v0.9.0-full.tar.gz",
        submodules=True,
    )
    version(
        "0.8.1",
        sha256="caebf96676ace6a9c50436541c420ca4bb53f0639dcab825de6fa370aacf6baa",
        url="https://github.com/arbor-sim/arbor/releases/download/v0.8.1/arbor-v0.8.1-full.tar.gz",
    )
    version(
        "0.8.0",
        sha256="18df5600308841616996a9de93b55a105be0f59692daa5febd3a65aae5bc2c5d",
        url="https://github.com/arbor-sim/arbor/releases/download/v0.8/arbor-v0.8-full.tar.gz",
    )
    version(
        "0.7.0",
        sha256="c3a6b7193946aee882bb85f9c38beac74209842ee94e80840968997ba3b84543",
        url="https://github.com/arbor-sim/arbor/releases/download/v0.7/arbor-v0.7-full.tar.gz",
    )
    version(
        "0.6.0",
        sha256="4cd333b18effc8833428ddc0b99e7dc976804771bc85da90034c272c7019e1e8",
        url="https://github.com/arbor-sim/arbor/releases/download/v0.6/arbor-v0.6-full.tar.gz",
    )
    version(
        "0.5.2",
        sha256="290e2ad8ca8050db1791cabb6b431e7c0409c305af31b559e397e26b300a115d",
        url="https://github.com/arbor-sim/arbor/releases/download/v0.5.2/arbor-v0.5.2-full.tar.gz",
    )

    variant(
        "assertions",
        default=False,
        description="Enable arb_assert() assertions in code.",
    )
    variant("doc", default=False, description="Build documentation.")
    variant("mpi", default=False, description="Enable MPI support")
    variant("python", default=True, description="Enable Python frontend support")
    variant(
        "pystubs", default=True, when="@0.11:", description="Python stub generation"
    )
    variant(
        "vectorize",
        default=False,
        description="Enable vectorization of computational kernels",
    )
    variant("hwloc", default=False, description="support for thread pinning via HWLOC")
    variant(
        "gpu_rng",
        default=False,
        description="Use GPU generated random numbers -- not bitwise equal to CPU version",
        when="+cuda",
    )

    # https://docs.arbor-sim.org/en/latest/install/build_install.html#compilers
    conflicts("%gcc@:8")
    conflicts("%clang@:9")
    # Cray compiler v9.2 and later is Clang-based.
    conflicts("%cce@:9.1")
    conflicts("%intel")

    depends_on("cmake@3.19:", type="build")
    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    # misc dependencies
    depends_on("fmt@7.1:", when="@0.5.3:")  # required by the modcc compiler
    depends_on("fmt@9.1:", when="@0.7.1:")
    depends_on("fmt@10.2:", when="@0.9.1:")
    depends_on("fmt@10.2:", when="@0.10.0:")
    depends_on("fmt@12.0:", when="@0.12.0:")
    depends_on("googletest@1.12.1:", when="@0.7.1:")
    depends_on("pugixml@1.11:", when="@0.7.1:")
    depends_on("pugixml@1.13:", when="@0.9.1:")
    depends_on("pugixml@1.14:", when="@0.10.0:")
    depends_on("pugixml@1.15:", when="@0.12.0:")
    depends_on("nlohmann-json@3.11.3:")
    depends_on("nlohmann-json@3.12:", when="@0.12.0:")
    depends_on("random123@1.14.0:")
    with when("+cuda"):
        depends_on("cuda@10:")
        depends_on("cuda@11:", when="@0.7.1:")
        depends_on("cuda@12:", when="@0.9.1:")
        depends_on("cuda@12:", when="@0.10.0:")

    # mpi
    depends_on("mpi", when="+mpi")
    depends_on("py-mpi4py", when="+mpi+python", type=("build", "run"))

    # hwloc
    depends_on("hwloc@2:", when="+hwloc", type=("build", "run"))

    # python (bindings)
    with when("+python"):
        extends("python")
        depends_on("python@3.7:", type=("build", "run"))
        depends_on("python@3.9:", when="@0.9.1:", type=("build", "run"))
        depends_on("python@3.10:", when="@0.10.0:", type=("build", "run"))
        depends_on("python@3.10:", when="@0.11.0:", type=("build", "run"))
        depends_on("python@3.11:", when="@0.12.0:", type=("build", "run")) #
        depends_on("py-numpy", type=("build", "run"))
        depends_on("py-numpy@2.0.0:", when="@0.12.0:", type=("build", "run"))
        depends_on("py-pybind11@2.6:", type="build")
        depends_on("py-pybind11@2.8.1:", when="@0.5.3:", type="build")
        depends_on("py-pybind11@2.10.1:", when="@0.7.1:", type="build")
        depends_on("py-pybind11@2.11.1:", when="@0.9.1:", type="build")
        depends_on("py-pybind11@2.10.1:", when="@0.7.1:", type="build")
        depends_on("py-pybind11@3.0.2:", when="@0.12.0:", type="build")
        depends_on("py-pybind11-stubgen@2.5:", when="+pystubs", type="build")

    # sphinx based documentation
    with when("+doc"):
        depends_on("python@3.11:", type="build")
        depends_on("py-sphinx", type="build")
        depends_on("py-svgwrite", type="build")

    @property
    def build_targets(self):
        return ["all", "html"] if "+doc" in self.spec else ["all"]

    def cmake_args(self):
        spec = self.spec
        args = [
            self.define_from_variant("ARB_WITH_ASSERTIONS", "assertions"),
            self.define_from_variant("ARB_WITH_MPI", "mpi"),
            self.define_from_variant("ARB_WITH_PYTHON", "python"),
            self.define_from_variant("ARB_VECTORIZE", "vectorize"),
            self.define_from_variant("ARB_BUILD_PYTHON_STUBS", "pystubs"),
            self.define("ARB_ARCH", "none"),
            self.define("ARB_CXX_FLAGS_TARGET", optimization_flags(self.compiler, spec.target)),
        ]

        if self.spec.satisfies("+cuda"):
            args.extend(
                [
                    self.define("ARB_GPU", "cuda"),
                    self.define_from_variant("ARB_USE_GPU_RNG", "gpu_rng"),
                ]
            )

        return args

    @run_after("install", when="+python")
    @on_package_attributes(run_tests=True)
    def install_test(self):
        python("-c", "import arbor")
