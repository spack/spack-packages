# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Proteus(CMakePackage, CudaPackage, ROCmPackage):
    """
    Proteus: A Programmable Just-In-Time (JIT) Compiler based on LLVM.
    It embeds seamlessly into existing C++ codebases and accelerates
    CUDA, HIP, and host-only C/C++ applications.
    """

    homepage = "https://github.com/Olympus-HPC/proteus"
    url = "https://github.com/Olympus-HPC/proteus/archive/refs/tags/v2026.07.0.tar.gz"
    git = "https://github.com/Olympus-HPC/proteus.git"

    maintainers("ZwFink", "ggeorgakoudis")

    license("Apache-2.0 WITH LLVM-exception")

    version("main", branch="main")
    version(
        "2026.07.0",
        sha256="4131ed4fc932784d3a5a978fd48475a92c2acc439cb3511eccd7d799016650f2",
    )
    version(
        "2026.05.0",
        sha256="ddccebbdda332a05ff259976ebad54822f4e412e293629035fdfea023d57246f",
    )
    version(
        "2026.03.0",
        sha256="4268c210883de1ca8afaa985cd1429505bbe130fc6cbdbb16bce16598063aa8c",
    )
    version(
        "2026.01.0",
        sha256="3045ecec79ae46bc73a9cc5c01e1f4545b5ad25dbf0c9b67cce6890a8f93bc46",
    )

    # Variants to control build options.
    variant(
        "shared",
        default=False,
        description="Build Proteus as a shared library (BUILD_SHARED)",
    )
    variant("tests", default=False, description="Enable building of tests (ENABLE_TESTS)")
    variant(
        "developer_flags",
        default=False,
        description="Enable developer flags (ENABLE_DEVELOPER_COMPILER_FLAGS)",
    )
    variant("mpi", default=False, description="Enable MPI support")
    variant("impl_headers", default=False, description="Install implementation headers")

    # Disallow enabling both CUDA and HIP at the same time.
    conflicts(
        "+cuda +rocm",
        msg="Proteus cannot be built with both +cuda and +rocm simultaneously",
    )
    # Require the Clang compiler since tests use the Proteus LLVM plugin.
    requires("%clang@18:20", when="+tests")

    # Build Dependencies.
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.18:", type="build")

    # Proteus LLVM and Clang dependencies.
    # CUDA enabled.
    depends_on("llvm@18:20 +clang targets=all", when="+cuda")

    # ROCm enabled, use the AMDGPU LLVM build.
    depends_on("llvm-amdgpu@6.2:", when="+rocm")

    # Host-only (no CUDA or HIP).
    depends_on("llvm@18:20+clang", when="~rocm ~cuda")

    requires("%[virtuals=c,cxx] llvm-amdgpu", when="+rocm")
    requires("%[virtuals=c,cxx] llvm", when="+cuda")

    # CUDA and HIP dependencies.
    depends_on("cuda@12:", when="+cuda")
    depends_on("hip@6.2:", when="+rocm")

    # MPI dependency.
    depends_on("mpi", when="+mpi")

    def cmake_args(self):
        # Enforce clang when building tests
        if "+tests" in self.spec and not self.spec.satisfies("%clang"):
            raise InstallError(
                "Building Proteus with +tests requires the Clang compiler, "
                f"but spec: {self.spec} is using the compiler: {self.spec.compiler}."
            )

        args = []

        # Helper to find LLVM/Clang config: prefer whichever provider is present
        if "llvm-amdgpu" in self.spec:
            llvm_provider = self.spec["llvm-amdgpu"]
        elif "llvm" in self.spec:
            llvm_provider = self.spec["llvm"]
        else:
            raise InstallError("Proteus requires an LLVM provider (llvm or llvm-amdgpu)")

        args.append(self.define("LLVM_INSTALL_DIR", llvm_provider.prefix))

        # BUILD_SHARED (default static).
        args.append(self.define_from_variant("BUILD_SHARED", "shared"))

        # ENABLE_TESTS.
        args.append(self.define_from_variant("ENABLE_TESTS", "tests"))

        # PROTEUS_ENABLE_HIP / PROTEUS_ENABLE_CUDA.
        args.append(self.define_from_variant("PROTEUS_ENABLE_HIP", "rocm"))
        args.append(self.define_from_variant("PROTEUS_ENABLE_CUDA", "cuda"))

        # ENABLE_DEVELOPER_COMPILER_FLAGS.
        args.append(self.define_from_variant("ENABLE_DEVELOPER_COMPILER_FLAGS", "developer_flags"))

        # MPI support.
        args.append(self.define_from_variant("PROTEUS_ENABLE_MPI", "mpi"))

        # Install implementation headers if requested.
        args.append(self.define_from_variant("PROTEUS_INSTALL_IMPL_HEADERS", "impl_headers"))

        return args
