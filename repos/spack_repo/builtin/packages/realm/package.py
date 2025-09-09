# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Realm(CMakePackage, CudaPackage, ROCmPackage):
    """Realm is a distributed, event–based tasking runtime for building
    high-performance applications that span clusters of CPUs, GPUs, and other
    accelerators. It began life as the low-level substrate underneath the Legion
    programming system but is now maintained as a standalone project for developers
    who want direct, fine-grained control of parallel and heterogeneous
    machines."""

    homepage = "https://legion.stanford.edu/realm/"
    git = "https://github.com/StanfordLegion/realm.git"
    url = "https://github.com/StanfordLegion/realm/archive/refs/tags/v25.6.1-rc.3.tar.gz"

    license("Apache-2.0")

    maintainers("rbberger")

    version("main", branch="main")
    version(
        "25.6.1-rc.3", sha256="fa100b8b55009941017a24e37a2834142f3af3a4abcd937e6be51099f747ebe6"
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("cmake@3.22:", when="@25.03.0:", type="build")

    # TODO: Need to spec version of MPI v3 for use of the low-level MPI transport
    # layer. At present the MPI layer is still experimental and we discourge its
    # use for general (not legion development) use cases.
    depends_on("mpi", when="network=mpi")
    depends_on("ucx", when="network=ucx")
    depends_on("ucc", when="network=ucx")
    depends_on("ucc+cuda+nccl", when="network=ucx +cuda")
    depends_on("ucc+rocm+rccl", when="network=ucx +rocm")
    depends_on("hdf5", when="+hdf5")
    depends_on("hwloc", when="+hwloc")

    # Propagate CUDA architectures
    for arch in CudaPackage.cuda_arch_values:
        depends_on(f"ucc cuda_arch={arch}", when=f"network=ucx +cuda cuda_arch={arch}")
        depends_on(
            f"kokkos+cuda+cuda_lambda cuda_arch={arch}", when=f"+kokkos+cuda cuda_arch={arch}"
        )

    for arch in ROCmPackage.amdgpu_targets:
        depends_on(f"ucc amdgpu_target={arch}", when=f"network=ucx +rocm amdgpu_target={arch}")
        depends_on(f"kokkos+rocm amdgpu_target={arch}", when=f"+rocm amdgpu_target={arch}")

    depends_on("kokkos@4:", when="+kokkos")
    depends_on("kokkos+openmp", when="+kokkos+openmp")
    depends_on("kokkos~openmp", when="+kokkos~openmp")
    depends_on("kokkos+cmake_lang", when="+kokkos+cuda")
    depends_on("kokkos+cmake_lang", when="+kokkos+rocm")

    depends_on("python@3.8:", when="+python")

    depends_on("papi", when="+papi")

    # A C++ standard variant to work-around some odd behaviors with apple-clang
    # but this might be helpful for other use cases down the road. Legion's
    # current development policy is C++11 or greater so we capture that aspect
    # here.
    cpp_stds = ("17", "20")
    variant("cxxstd", default="17", description="C++ standard", values=cpp_stds, multi=False)

    # Network transport layer: the underlying data transport API should be used for
    # distributed data movement.  For Legion, gasnet is the currently the most
    # mature.  We have many users that default to using no network layer for
    # day-to-day development thus we default to 'none'.  MPI support is new and
    # should be considered as a beta release.
    variant(
        "network",
        default="none",
        values=("gasnet", "mpi", "ucx", "none"),
        description="The network communications/transport layer to use.",
        multi=False,
    )

    depends_on("gasnet+pic", when="network=gasnet")

    # configs based on https://github.com/StanfordLegion/gasnet
    depends_on("gasnet+mpi_compat+pshm conduits=smp", when="network=gasnet conduit=smp")
    depends_on("gasnet+mpi_compat~pshm conduits=mpi", when="network=gasnet conduit=mpi")
    depends_on(
        "gasnet+mpi_compat+pshm conduits=ibv ibv_max_hcas=4", when="network=gasnet conduit=ibv"
    )
    depends_on(
        "gasnet+mpi_compat+pshm conduits=ofi ofi_provider=cxi ofi_spawner=pmi pmi=cray",
        when="network=gasnet conduit=ofi-slingshot11",
    )

    with when("network=gasnet"):
        variant(
            "conduit",
            default="smp",
            values=("smp", "aries", "ibv", "udp", "mpi", "ucx", "ofi-slingshot11"),
            description="The GASNet conduit(s) to enable.",
            sticky=True,
            multi=False,
        )

    with when("network=ucx"):
        variant(
            "ucx_backends",
            default="p2p",
            values=("p2p", "mpi"),
            description="UCX Bootstraps to build and install",
            multi=True,
        )
        requires("ucx_backends=p2p", msg="p2p backend is always enabled")

    variant("shared", default=False, description="Build shared libraries.")

    variant(
        "log_level",
        default="warning",
        # Note: these values are dependent upon those used in the cmake config.
        values=("spew", "debug", "info", "print", "warning", "error", "fatal", "none"),
        description="Set the compile-time logging level.",
        multi=False,
    )

    with when("+cuda"):
        variant(
            "cuda_dynamic_load",
            default=False,
            description="Enable dynamic loading of CUDA libraries.",
        )
        variant(
            "cuda_unsupported_compiler",
            default=False,
            description="Disable nvcc version check (--allow-unsupported-compiler).",
        )

    variant("hdf5", default=False, description="Enable support for HDF5.")
    variant("hwloc", default=False, description="Use hwloc for topology awareness.")
    variant(
        "kokkos", default=False, description="Enable support for interoperability with Kokkos."
    )
    variant(
        "libdl", default=True, description="Enable support for dynamic object/library loading."
    )
    variant("openmp", default=False, description="Enable support for OpenMP.")
    variant("papi", default=False, description="Enable PAPI performance measurements.")
    variant("python", default=False, description="Enable Python support.")
    requires("+shared", when="+python")

    variant(
        "max_dims",
        values=int,
        default="3",
        description="Set max number of dimensions for logical regions.",
    )

    variant(
        "sysomp", default=False, description="Use system OpenMP implementation instead of Realm's"
    )

    def cmake_args(self):
        spec = self.spec
        from_variant = self.define_from_variant
        options = [
            self.define("REALM_ENABLE_INSTALL", True),
            self.define("REALM_INSTALL", True),  # remove once inconsistency is fixed
            from_variant("REALM_CXX_STANDARD", "cxxstd"),
            from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define("REALM_ENABLE_UCX", spec.satisfies("network=ucx")),
            self.define("REALM_INSTALL_UCX_BOOTSTRAPS", spec.satisfies("network=ucx")),
            self.define(
                "UCX_BOOTSTRAP_ENABLE_MPI", spec.satisfies("network=ucx ucx_backends=mpi")
            ),
            self.define("REALM_ENABLE_GASNETEX", spec.satisfies("network=gasnet")),
            self.define("REALM_ENABLE_MPI", spec.satisfies("network=mpi")),
            from_variant("REALM_ENABLE_CUDA", "cuda"),
            from_variant("REALM_ENABLE_HIP", "rocm"),
            from_variant("REALM_ENABLE_HDF5", "hdf5"),
            from_variant("REALM_ENABLE_HWLOC", "hwloc"),
            from_variant("REALM_ENABLE_KOKKOS", "kokkos"),
            from_variant("REALM_ENABLE_LIBDL", "libdl"),
            from_variant("REALM_ENABLE_OPENMP", "openmp"),
            from_variant("REALM_ENABLE_PAPI", "papi"),
            from_variant("REALM_ENABLE_PYTHON", "python"),
            from_variant("REALM_CUDA_DYNAMIC_LOAD", "cuda_dynamic_load"),
            self.define("REALM_OPENMP_SYSTEM_RUNTIME", spec.satisfies("+openmp +sysomp")),
        ]

        options.append(f"-DREALM_LOG_LEVEL={str.upper(spec.variants['log_level'].value)}")

        if spec.satisfies("+cuda"):
            options.append(
                self.define("CMAKE_CUDA_ARCHITECTURES", spec.variants["cuda_arch"].value)
            )
            if spec.satisfies("+cuda_unsupported_compiler"):
                options.append("-DCUDA_NVCC_FLAGS:STRING=--allow-unsupported-compiler")

        if spec.satisfies("+kokkos"):
            if spec.satisfies("+cuda+cuda_unsupported_compiler ^kokkos+cuda %cxx=clang"):
                # Keep CMake CUDA compiler detection happy
                options.append(
                    self.define("CMAKE_CUDA_FLAGS", "--allow-unsupported-compiler -std=c++17")
                )

        maxdims = int(spec.variants["max_dims"].value)
        # TODO: sanity check if maxdims < 0 || > 9???
        options.append(f"-DREALM_MAX_DIM={maxdims}")

        return options
