# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Legion(CMakePackage, CudaPackage, ROCmPackage):
    """Legion is a data-centric parallel programming system for writing
    portable high performance programs targeted at distributed heterogeneous
    architectures. Legion presents abstractions which allow programmers to
    describe properties of program data (e.g. independence, locality). By
    making the Legion programming system aware of the structure of program
    data, it can automate many of the tedious tasks programmers currently
    face, including correctly extracting task- and data-level parallelism
    and moving data around complex memory hierarchies. A novel mapping
    interface provides explicit programmer controlled placement of data in
    the memory hierarchy and assignment of tasks to processors in a way
    that is orthogonal to correctness, thereby enabling easy porting and
    tuning of Legion applications to new architectures."""

    homepage = "https://legion.stanford.edu/"
    git = "https://github.com/StanfordLegion/legion.git"

    license("Apache-2.0")

    maintainers("pmccormick", "streichler", "elliottslaughter", "rbberger")
    tags = ["e4s"]
    version("26.03.0", tag="legion-26.03.0", commit="b95c7bfdbdf564eac57f9ace73c394acea4ac216")
    version("25.12.0", tag="legion-25.12.0", commit="6f710cb46590b04ad299362819fdecb3a4e429ca")
    version("25.09.0", tag="legion-25.09.0", commit="8759d840099a138b5f395e86c841848520b34b73")
    version("25.06.0", tag="legion-25.06.0", commit="d8e35c48d089014b0f764181b7b90278a7558b21")
    version("25.03.0", tag="legion-25.03.0", commit="04716e3b3686d4af71e6a4398dfbe8cd869c057b")
    version("24.12.0", tag="legion-24.12.0", commit="2f087ebe433a19f9a3abd05382f951027933bad9")
    version("24.09.0", tag="legion-24.09.0", commit="4a03402467547b99530042cfe234ceec2cd31b2e")
    version("24.06.0", tag="legion-24.06.0", commit="3f27977943626ef23038ef0049b7ad1b389caad1")
    version("24.03.0", tag="legion-24.03.0", commit="c61071541218747e35767317f6f89b83f374f264")
    version("23.12.0", tag="legion-23.12.0", commit="8fea67ee694a5d9fb27232a7976af189d6c98456")
    version("23.09.0", tag="legion-23.09.0", commit="7304dfcf9b69005dd3e65e9ef7d5bd49122f9b49")
    version("23.06.0", tag="legion-23.06.0", commit="7b5ff2fb9974511c28aec8d97b942f26105b5f6d")
    version("stable", branch="stable")
    version("master", branch="master")

    # Old control replication commits used by FleCSI releases, prior to 24.03.0
    version("cr-20230307", commit="435183796d7c8b6ac1035a6f7af480ded750f67d", deprecated=True)

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build", when="+fortran")

    depends_on("cmake@3.16:", when="@21.03.0:24.12.0", type="build")
    depends_on("cmake@3.22:", when="@25.03.0:", type="build")

    depends_on("realm", when="@25.09.0:")
    depends_on("realm+shared", when="@25.09.0: +shared")
    depends_on("realm+kokkos", when="@25.09.0: +kokkos")
    depends_on("realm+hdf5", when="@25.09.0: +hdf5")
    depends_on("realm+hwloc", when="@25.09.0: +hwloc")
    depends_on("realm+openmp", when="@25.09.0: +openmp")
    depends_on("realm+sysomp", when="@25.09.0: +sysomp")
    depends_on("realm+cuda", when="@25.09.0: +cuda")
    depends_on("realm+rocm", when="@25.09.0: +rocm")
    depends_on("realm+cuda_unsupported_compiler", when="@25.09.0: +cuda_unsupported_compiler")

    depends_on("realm@26:", when="@26:")
    depends_on("realm@25:", when="@25.09.0:")

    for d in range(1, 10):
        depends_on(f"realm max_dims={d}", when=f"@25.09.0: max_dims={d}")

    # force same compiler as kokkos if static build
    depends_on("kokkos %gcc", when="+kokkos~shared %gcc")
    depends_on("kokkos %clang", when="+kokkos~shared %clang")

    # TODO: Need to spec version of MPI v3 for use of the low-level MPI transport
    # layer. At present the MPI layer is still experimental and we discourge its
    # use for general (not legion development) use cases.
    depends_on("mpi", when="@:25.06.0 network=mpi")
    depends_on(
        "mpi", when="@:25.06.0 network=gasnet"
    )  # MPI is required to build gasnet (needs mpicc).
    depends_on("ucx", when="@:25.06.0 network=ucx")
    depends_on("ucc", when="@25.03.0:25.06.0 network=ucx")
    depends_on("ucc+cuda+nccl", when="network=ucx +cuda @25.03.0:25.06.0")
    depends_on("ucc+rocm+rccl", when="network=ucx +rocm @25.03.0:25.06.0")
    depends_on("ucx", when="conduit=ucx @:25.06.0")
    depends_on("mpi", when="conduit=mpi @:25.06.0")
    depends_on("cuda@10.0:11.9", when="+cuda_unsupported_compiler @21.03.0:23.03.0")
    depends_on("cuda@10.0:11.9", when="+cuda @21.03.0:23.03.0")
    depends_on("cuda@11.7:12.8", when="+cuda_unsupported_compiler @23.06.0:24.12.0")
    depends_on("cuda@11.7:12.8", when="+cuda @23.06.0:24.12.0")
    depends_on("hip@5.1:5.7", when="+rocm @23.03.0:23.12.0")
    depends_on("hip@5.1:", when="+rocm")
    depends_on("hdf5", when="+hdf5")
    depends_on("hwloc", when="+hwloc")
    depends_on("libfabric", when="@:25.06.0 network=gasnet conduit=ofi-slingshot11")

    depends_on("gasnet", when="@25.09.0: ^realm network=gasnet")

    # Kokkos
    depends_on("kokkos", when="@:25.06.0,stable +kokkos")
    depends_on("kokkos", when="+kokkos~shared")

    # OpenMP backend
    depends_on("kokkos+openmp", when="@:25.06.0,stable +kokkos+openmp")
    depends_on("kokkos~openmp", when="@:25.06.0,stable +kokkos~openmp")

    # cuda-centric
    cuda_arch_list = CudaPackage.cuda_arch_values
    for arch in cuda_arch_list:
        # UCX transport dependency when using CUDA
        depends_on(
            f"ucc cuda_arch={arch}", when=f"@25.03.0:25.06.0 network=ucx +cuda cuda_arch={arch}"
        )
        depends_on(
            f"kokkos+cuda+cuda_lambda+wrapper cuda_arch={arch}",
            when=f"@:25.06.0 +kokkos+cuda cuda_arch={arch} %gcc",
        )
        depends_on(
            f"kokkos+cuda+cuda_lambda~wrapper cuda_arch={arch}",
            when=f"@:25.06.0 +kokkos+cuda cuda_arch={arch} %clang",
        )
        depends_on(f"realm cuda_arch={arch}", when=f"@25.09.0: +cuda cuda_arch={arch}")

    # https://github.com/spack/spack/issues/37232#issuecomment-1553376552
    patch("hip-offload-arch.patch", when="@23.03.0 +rocm")

    def patch(self):
        if self.spec.satisfies("@25.09.0:"):
            # conflicts with Realm FindGASNet.cmake
            force_remove("cmake/FindGASNet.cmake")
        if self.spec.satisfies("@:25.06.0 network=gasnet conduit=ofi-slingshot11") and (
            self.spec.satisfies("^[virtuals=mpi] cray-mpich+wrappers")
            or self.spec.satisfies("^[virtuals=mpi] mpich netmod=ofi ^libfabric fabrics=cxi")
            or self.spec.satisfies("^[virtuals=mpi] openmpi fabrics=ofi ^libfabric fabrics=cxi")
        ):
            filter_file(
                r"--with-mpi-cc=cc",
                f"--with-mpi-cc={self.spec['mpi'].mpicc}",
                "stanfordgasnet/gasnet/configs/config.ofi-slingshot11.release",
                string=True,
            )

    # HIP specific
    variant(
        "hip_hijack",
        default=False,
        description="Hijack application calls into the HIP runtime",
        when="+rocm",
    )
    variant(
        "hip_target",
        default="ROCM",
        values=("ROCM", "CUDA"),
        description="API used by HIP",
        multi=False,
        when="+rocm",
    )

    for arch in ROCmPackage.amdgpu_targets:
        depends_on(
            f"ucc amdgpu_target={arch}",
            when=f"@25.03.0:25.06.0 network=ucx +rocm amdgpu_target={arch}",
        )
        depends_on(
            f"kokkos+rocm amdgpu_target={arch}",
            when=f"@:25.06.0 +kokkos+rocm amdgpu_target={arch}",
        )
        depends_on(f"realm amdgpu_target={arch}", when=f"@25.09.0: +rocm amdgpu_target={arch}")

    depends_on("kokkos+rocm", when="@:25.06.0 +kokkos+rocm")

    # https://github.com/StanfordLegion/legion/#dependencies
    depends_on("python@3.8:", when="+python")
    depends_on("py-cffi", when="+python")
    depends_on("py-numpy", when="+python")
    depends_on("py-pip", when="+python", type="build")
    depends_on("py-setuptools", when="+python", type="build")

    depends_on("papi", when="@:25.06.0 +papi")
    depends_on("zlib-api", when="+zlib")

    # A C++ standard variant to work-around some odd behaviors with apple-clang
    # but this might be helpful for other use cases down the road.  Legion's
    # current development policy is C++17 or greater so we capture that aspect
    # here.
    cpp_stds = (conditional("11", "14", when="@:24.03.0"), "17", "20")
    variant("cxxstd", default="17", description="C++ standard", values=cpp_stds, multi=False)

    # Network transport layer: the underlying data transport API should be used for
    # distributed data movement.  For Legion, GASNet and UCX are the most
    # mature.  We have many users that default to using no network layer for
    # day-to-day development thus we default to 'none'.  MPI support is new and
    # should be considered as a beta release.
    variant(
        "network",
        default="none",
        values=("gasnet", "mpi", "ucx", "none"),
        description="The network communications/transport layer to use.",
        multi=False,
        when="@:25.06.0",
    )

    # Add Gasnet tarball dependency in spack managed manner
    # TODO: Provide less mutable tag instead of branch
    resource(
        name="stanfordgasnet",
        git="https://github.com/StanfordLegion/gasnet.git",
        destination="stanfordgasnet",
        branch="master",
        when="@:25.06.0 network=gasnet",
    )

    # We default to automatically embedding a gasnet build. To override this
    # point the package a pre-installed version of GASNet-Ex via the gasnet_root
    # variant.
    #
    # make sure we have a valid directory provided for gasnet_root...
    def validate_gasnet_root(value):
        if value == "none":
            return True

        if not os.path.isdir(value):
            print("gasnet_root:", value, "-- no such directory.")
            return False
        else:
            return True

    with when("@:25.06.0 network=gasnet"):
        variant(
            "gasnet_root",
            default="none",
            values=validate_gasnet_root,
            description="Path to a pre-installed version of GASNet (prefix directory).",
            multi=False,
        )
        variant(
            "conduit",
            default="none",
            values=("none", "aries", "ibv", "udp", "mpi", "ucx", "ofi-slingshot11"),
            description="The GASNet conduit(s) to enable.",
            sticky=True,
            multi=False,
        )
        conflicts(
            "conduit=none", msg="the 'conduit' variant must be set to a value other than 'none'"
        )
        variant("gasnet_debug", default=False, description="Build gasnet with debugging enabled.")

    variant("shared", default=False, description="Build shared libraries.")

    variant(
        "bounds_checks", default=False, description="Enable bounds checking in Legion accessors."
    )

    variant(
        "privilege_checks",
        default=False,
        description="Enable runtime privildge checks in Legion accessors.",
    )

    variant(
        "output_level",
        default="warning",
        # Note: these values are dependent upon those used in the cmake config.
        values=("spew", "debug", "info", "print", "warning", "error", "fatal", "none"),
        description="Set the compile-time logging level.",
        multi=False,
    )

    variant("spy", default=False, description="Enable detailed logging for Legion Spy debugging.")

    # note: we will be dependent upon spack's latest-and-greatest cuda version...
    variant("cuda", default=False, description="Enable CUDA support.")
    variant(
        "cuda_hijack",
        default=False,
        description="Hijack application calls into the CUDA runtime (+cuda).",
    )
    variant(
        "cuda_unsupported_compiler",
        default=False,
        description="Disable nvcc version check (--allow-unsupported-compiler).",
    )
    conflicts("+cuda_hijack", when="~cuda")

    variant("fortran", default=False, description="Enable Fortran bindings.")
    requires("+bindings", when="+fortran")

    variant("hdf5", default=False, description="Enable support for HDF5.")

    variant("hwloc", default=False, description="Use hwloc for topology awareness.")

    variant(
        "kokkos", default=False, description="Enable support for interoperability with Kokkos."
    )

    variant(
        "bindings", default=False, description="Build runtime language bindings (excl. Fortran)."
    )

    variant(
        "libdl", default=True, description="Enable support for dynamic object/library loading."
    )

    variant("openmp", default=False, description="Enable support for OpenMP within Legion tasks.")

    variant(
        "papi",
        default=False,
        description="Enable PAPI performance measurements.",
        when="@:25.06.0",
    )

    variant("python", default=False, description="Enable Python support.")
    requires("+bindings", when="+python")
    requires("+shared", when="+python")

    variant("zlib", default=True, description="Enable zlib support.")

    variant(
        "redop_complex", default=False, description="Use reduction operators for complex types."
    )
    requires("+redop_complex", when="+bindings")
    variant(
        "redop_half",
        default=False,
        description="Use reduction operators for half precision types.",
    )

    variant(
        "max_dims",
        values=int,
        default="3",
        description="Set max number of dimensions for logical regions.",
    )
    variant(
        "max_fields",
        values=int,
        default="512",
        description="Maximum number of fields allowed in a logical region.",
    )
    variant(
        "max_num_nodes",
        values=int,
        default="1024",
        description="Maximum number of nodes supported by Legion.",
    )
    variant("prof", default=False, description="Install Rust Legion prof")

    depends_on("rust@1.74:", type="build", when="@21.03.0:24.12.0 +prof")
    depends_on("rust@1.84:", type="build", when="@25.03.0: +prof")

    variant("gc", default=False, description="Enable garbage collector logging")
    variant(
        "sysomp", default=False, description="Use system OpenMP implementation instead of Realm's"
    )

    def flag_handler(self, name, flags):
        if name == "cxxflags":
            if self.spec.satisfies("%oneapi@2025:") or self.spec.satisfies("%cxx=clang@20:"):
                flags.append("-Wno-error=missing-template-arg-list-after-template-kw")
        return (flags, None, None)

    def cmake_args(self):
        spec = self.spec
        from_variant = self.define_from_variant
        options = [
            from_variant("CMAKE_CXX_STANDARD", "cxxstd"),
            from_variant("BUILD_SHARED_LIBS", "shared"),
            from_variant("Legion_BOUNDS_CHECKS", "bounds_checks"),
            from_variant("Legion_PRIVILEGE_CHECKS", "privilege_checks"),
            from_variant("Legion_SPY", "spy"),
            from_variant("Legion_USE_Fortran", "fortran"),
            from_variant("Legion_USE_HDF5", "hdf5"),
            from_variant("Legion_USE_HWLOC", "hwloc"),
            from_variant("Legion_USE_Kokkos", "kokkos"),
            from_variant("Legion_USE_LIBDL", "libdl"),
            from_variant("Legion_USE_OpenMP", "openmp"),
            from_variant("Legion_USE_PAPI", "papi"),
            from_variant("Legion_USE_Python", "python"),
            from_variant("Legion_USE_ZLIB", "zlib"),
            from_variant("Legion_BUILD_BINDINGS", "bindings"),
            from_variant("Legion_REDOP_COMPLEX", "redop_complex"),
            from_variant("Legion_REDOP_HALF", "redop_half"),
        ]

        if spec.satisfies("network=gasnet"):
            options.append("-DLegion_NETWORKS=gasnetex")
            if spec.variants["gasnet_root"].value != "none":
                gasnet_dir = spec.variants["gasnet_root"].value
                options.append("-DGASNet_ROOT_DIR=%s" % gasnet_dir)
            else:
                gasnet_dir = join_path(self.stage.source_path, "stanfordgasnet", "gasnet")
                options.append("-DLegion_EMBED_GASNet=ON")
                options.append("-DLegion_EMBED_GASNet_LOCALSRC=%s" % gasnet_dir)

            gasnet_conduit = spec.variants["conduit"].value

            if "-" in gasnet_conduit:
                gasnet_conduit, gasnet_system = gasnet_conduit.split("-")
                options.append("-DGASNet_CONDUIT=%s" % gasnet_conduit)
                options.append("-DGASNet_SYSTEM=%s" % gasnet_system)
            else:
                options.append("-DGASNet_CONDUIT=%s" % gasnet_conduit)

            if spec.satisfies("+gasnet_debug"):
                options.append("-DLegion_EMBED_GASNet_CONFIGURE_ARGS=--enable-debug")
        elif spec.satisfies("network=mpi"):
            options.append("-DLegion_NETWORKS=mpi")
        elif spec.satisfies("network=ucx"):
            options.append("-DLegion_NETWORKS=ucx")
        else:
            options.append("-DLegion_EMBED_GASNet=OFF")

        options.append(f"-DLegion_OUTPUT_LEVEL={str.upper(spec.variants['output_level'].value)}")

        if spec.satisfies("+cuda"):
            cuda_arch = spec.variants["cuda_arch"].value
            options.append(self.define("Legion_USE_CUDA", True))
            options.append(self.define("Legion_GPU_REDUCTIONS", True))
            options.append(self.define("Legion_CUDA_ARCH", cuda_arch))
            options.append(self.define("Legion_HIJACK_CUDART", spec.satisfies("+cuda_hijack")))
            options.append(from_variant("CMAKE_CUDA_STANDARD", "cxxstd"))

            if spec.satisfies("+cuda_unsupported_compiler"):
                options.append(self.define("CMAKE_CUDA_FLAGS", "--allow-unsupported-compiler"))
                options.append(
                    self.define("CUDA_NVCC_FLAGS", "--allow-unsupported-compiler")
                )  # TODO: still needed?

        if spec.satisfies("+rocm"):
            options.append(self.define("Legion_USE_HIP", True))
            options.append(self.define("Legion_GPU_REDUCTIONS", True))
            options.append(from_variant("Legion_HIP_TARGET", "hip_target"))
            options.append(from_variant("Legion_HIP_ARCH", "amdgpu_target"))
            options.append(from_variant("Legion_HIJACK_HIP", "hip_hijack"))
            options.append(from_variant("CMAKE_HIP_STANDARD", "cxxstd"))
            if spec.satisfies("@23.03.0:23.12.0"):
                options.append(self.define("HIP_PATH", f"{spec['hip'].prefix}/hip"))
            else:
                options.append(self.define("ROCM_PATH", spec["hip"].prefix))

        # for shared libraries, realm_kokkos.so will be self contained.
        # however, in the static case we need to use the same compiler/wrapper as kokkos globally.
        if self.spec.satisfies("~shared+kokkos ^kokkos+wrapper"):
            options.append(self.define("CMAKE_CXX_COMPILER", self["kokkos"].kokkos_cxx))
        elif self.spec.satisfies("~shared+kokkos ^kokkos~cmake_lang+rocm"):
            options.append(self.define("CMAKE_CXX_COMPILER", self.spec["hip"].hipcc))

        maxdims = int(spec.variants["max_dims"].value)
        # TODO: sanity check if maxdims < 0 || > 9???
        options.append("-DLegion_MAX_DIM=%d" % maxdims)

        maxfields = int(spec.variants["max_fields"].value)
        if maxfields <= 0:
            maxfields = 512
        # make sure maxfields is a power of two.  if not,
        # find the next largest power of two and use that...
        if maxfields & (maxfields - 1) != 0:
            while maxfields & maxfields - 1:
                maxfields = maxfields & maxfields - 1
            maxfields = maxfields << 1
        options.append("-DLegion_MAX_FIELDS=%d" % maxfields)

        maxnodes = int(spec.variants["max_num_nodes"].value)
        if maxnodes <= 0:
            maxnodes = 1024
        # make sure maxnodes is a power of two.  if not,
        # find the next largest power of two and use that...
        if maxnodes & (maxnodes - 1) != 0:
            while maxnodes & maxnodes - 1:
                maxnodes = maxnodes & maxnodes - 1
            maxnodes = maxnodes << 1
        options.append("-DLegion_MAX_NUM_NODES=%d" % maxnodes)

        # This disables Legion's CMake build system's logic for targeting the native
        # CPU architecture in favor of Spack-provided compiler flags
        options.append("-DBUILD_MARCH:STRING=")

        if spec.satisfies("+openmp +sysomp"):
            options.append("-DLegion_OpenMP_SYSTEM_RUNTIME=ON")

        if spec.satisfies("+gc"):
            options.append("-DCMAKE_CXX_FLAGS=-DLEGION_GC")

        return options

    def build(self, spec, prefix):
        super().build(spec, prefix)
        if spec.satisfies("+prof"):
            with working_dir(join_path(self.stage.source_path, "tools", "legion_prof_rs")):
                cargo = which("cargo", required=True)
                cargo("install", "--root", "out", "--path", ".", "--all-features", "--locked")

    def install(self, spec, prefix):
        super().install(spec, prefix)
        if spec.satisfies("+prof"):
            with working_dir(join_path(self.stage.source_path, "tools", "legion_prof_rs")):
                install_tree("out", prefix)

    @run_after("install")
    def cache_test_sources(self):
        """Copy the example source files after the package is installed to an
        install test subdirectory for use during `spack test run`."""
        cache_extra_test_sources(self, [join_path("examples", "local_function_tasks")])

    def test_run_local_function_tasks(self):
        """Build and run external application example"""

        test_dir = join_path(
            self.test_suite.current_test_cache_dir, "examples", "local_function_tasks"
        )

        if not os.path.exists(test_dir):
            raise SkipTest(f"{test_dir} must exist")

        cmake_args = [
            f"-DCMAKE_C_COMPILER={self.compiler.cc}",
            f"-DCMAKE_CXX_COMPILER={self.compiler.cxx}",
            f"-DLegion_DIR={join_path(self.prefix, 'share', 'Legion', 'cmake')}",
        ]

        with working_dir(test_dir):
            cmake = self.spec["cmake"].command
            cmake(*cmake_args)

            make = which("make", required=True)
            make()

            exe = which("local_function_tasks", required=True)
            exe()
