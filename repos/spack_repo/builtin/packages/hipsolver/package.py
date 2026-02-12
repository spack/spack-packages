# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import re

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Hipsolver(CMakePackage, CudaPackage, ROCmPackage):
    """hipSOLVER is a LAPACK marshalling library, with multiple supported backends.
    It sits between the application and a 'worker' LAPACK library, marshalling
    inputs into the backend library and marshalling results back to the application.
    hipSOLVER exports an interface that does not require the client to change,
    regardless of the chosen backend. Currently, hipSOLVER supports rocSOLVER
    and cuSOLVER as backends."""

    homepage = "https://github.com/ROCm/hipSOLVER"
    git = "https://github.com/ROCm/hipSOLVER.git"
    url = "https://github.com/ROCm/hipSOLVER/archive/rocm-6.4.3.tar.gz"
    tags = ["rocm"]

    maintainers("cgmb", "srekolam", "renjithravindrankannath", "afzpatel")
    libraries = ["libhipsolver"]

    license("MIT")
    version("7.1.1", sha256="bd664e3cd43bfcc7e94d5a387c27262c4b218d6d2e71e086992b174349dd1c10")
    version("7.1.0", sha256="19b87cd27b9048964e94a77bb8c07a23ecfd5f96a73a91eebd1d365487bad2bf")
    version("7.0.2", sha256="eac1a691bdc00ceb50580c1dab6cbffd6c7d579ebbad145857f58c4de84a3cae")
    version("7.0.0", sha256="5ea1e0250651da458158432409bd4c06a53224902e17ea26f3b941aed15ee8aa")
    version("6.4.3", sha256="403c2d0aacc3ea2dea5f6d61aca058337d448a224891b887ae1601ce68af8d15")
    version("6.4.2", sha256="5c1afee73157d042fd1dcae1ac416ea6f6f62207d7cb08595942b9f016673631")
    version("6.4.1", sha256="86ac30d5cf741a254485ed54c7f51e4c9bc9803cda31dab8e86f11b39742b28e")
    version("6.4.0", sha256="d6cf798c5f2d1d00a442f7a3f07c6f3a9e4ce5b3be36608aac7c97175dac9eb0")
    version("6.3.3", sha256="529263f9abe5b7485bbabedc3993630abaa0d5fd547c4add0993d1cb0d71e226")
    version("6.3.2", sha256="885c999da8e4aa0b4cb9584bc0fc0d6a8c8d56f5e7ee6d211c608003eff22aa7")
    version("6.3.1", sha256="793074ebaa4a3b16dc6e4d2a54ecbb259f1e0ec7fdcd7f885da622a1d1478b76")
    version("6.3.0", sha256="a0443f0b894cedd5af59af4fadcb3c38daa728ca32c13b9741fb19e2d828a089")
    version("6.2.4", sha256="4dc564498361cb1bac17dcfeaf0f2b9c85320797c75b05ee33160a133f5f4a15")
    version("6.2.1", sha256="614e3c0bc11bfa84acd81d46db63f3852a750adaaec094b7701ab7b996cc8e93")
    version("6.2.0", sha256="637577a9cc38e4865894dbcd7eb35050e3de5d45e6db03472e836b318602a84d")
    version("6.1.2", sha256="406a8e5b82daae2fc03e0a738b5a054ade01bb41785cee4afb9e21c7ec91d492")
    version("6.1.1", sha256="01d4553458f417824807c069cacfc65d23f6cac79536158473b4356986c8fafd")
    version("6.1.0", sha256="3cb89ca486cdbdfcb1a07c35ee65f60219ef7bc62a5b0f94ca1a3206a0106495")
    version("6.0.2", sha256="8215e55c3a5bc9c7eeb141cefdc6a6eeba94d8bc3aeae9e685ab7904965040d4")
    version("6.0.0", sha256="385849db02189d5e62096457e52ae899ae5c1ae7d409dc1da61f904d8861b48c")
    version("5.7.1", sha256="5592e965c0dc5722931302289643d1ece370220af2c7afc58af97b3395295658")
    version("5.7.0", sha256="0e35795bfbcb57ed8e8437471209fb7d230babcc31d9a4a0b3640c3ee639f4a7")

    # default to an 'auto' variant until amdgpu_targets can be given a better default than 'none'
    amdgpu_targets = ROCmPackage.amdgpu_targets
    variant(
        "amdgpu_target",
        description="AMD GPU architecture",
        values=disjoint_sets(("auto",), amdgpu_targets)
        .with_default("auto")
        .with_error(
            "the values 'auto' and 'none' are mutually exclusive with any of the other values"
        )
        .with_non_feature_values("auto", "none"),
        sticky=True,
    )
    variant("rocm", default=True, description="Enable ROCm support")
    conflicts("+cuda +rocm", msg="CUDA and ROCm support are mutually exclusive")
    conflicts("~cuda ~rocm", msg="CUDA or ROCm support is required")

    variant(
        "build_type",
        default="Release",
        values=("Release", "Debug", "RelWithDebInfo"),
        description="CMake build type",
    )
    variant("asan", default=False, description="Build with address-sanitizer enabled or disabled")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    depends_on("cmake@3.5:", type="build")
    depends_on("suite-sparse", type="build")
    depends_on("hip +cuda", when="+cuda")

    for ver in [
        "5.7.0",
        "5.7.1",
        "6.0.0",
        "6.0.2",
        "6.1.0",
        "6.1.1",
        "6.1.2",
        "6.2.0",
        "6.2.1",
        "6.2.4",
        "6.3.0",
        "6.3.1",
        "6.3.2",
        "6.3.3",
        "6.4.0",
        "6.4.1",
        "6.4.2",
        "6.4.3",
        "7.0.0",
        "7.0.2",
        "7.1.0",
        "7.1.1",
    ]:
        depends_on(f"rocm-cmake@{ver}", when=f"+rocm @{ver}")
        depends_on(f"rocblas@{ver}", when=f"+rocm @{ver}")
        depends_on(f"rocsolver@{ver}", when=f"+rocm @{ver}")

    for tgt in ROCmPackage.amdgpu_targets:
        depends_on(f"rocblas amdgpu_target={tgt}", when=f"+rocm amdgpu_target={tgt}")
        depends_on(f"rocsolver amdgpu_target={tgt}", when=f"+rocm amdgpu_target={tgt}")

    depends_on("googletest@1.10.0:", type="test")
    depends_on("netlib-lapack@3.7.1:", type="test")
    patch("001-suite-sparse-include-path.patch", when="@6.1.0")
    patch("0001-suite-sparse-include-path-6.1.1.patch", when="@6.1.1:6.2")

    def check(self):
        exe = join_path(self.build_directory, "clients", "staging", "hipsolver-test")
        exe = which(exe)
        exe(["--gtest_filter=-*known_bug*"])

    @classmethod
    def determine_version(cls, lib):
        match = re.search(r"lib\S*\.so\.\d+\.\d+\.(\d)(\d\d)(\d\d)", lib)
        if match:
            ver = "{0}.{1}.{2}".format(
                int(match.group(1)), int(match.group(2)), int(match.group(3))
            )
        else:
            ver = None
        return ver

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        if self.spec.satisfies("+asan"):
            self.asan_on(env)

    def cmake_args(self):
        args = [
            self.define("BUILD_CLIENTS_SAMPLES", "OFF"),
            self.define("BUILD_FORTRAN_BINDINGS", "OFF"),
            self.define("BUILD_CLIENTS_TESTS", self.run_tests),
            self.define("SUITE_SPARSE_PATH", self.spec["suite-sparse"].prefix),
            self.define("CMAKE_INSTALL_LIBDIR", "lib"),
        ]

        args.append(self.define_from_variant("USE_CUDA", "cuda"))
        # FindHIP.cmake is still used for +cuda
        if self.spec.satisfies("+cuda"):
            args.append(self.define("CMAKE_MODULE_PATH", self.spec["hip"].prefix.lib.cmake.hip))
        else:
            args.append(self.define("ROCBLAS_PATH", self.spec["rocblas"].prefix))
        if self.spec.satisfies("@5.2.0:6.3.1"):
            args.append(self.define("BUILD_FILE_REORG_BACKWARD_COMPATIBILITY", True))
        libloc = self.spec["suite-sparse"].prefix.lib64
        if not os.path.isdir(libloc):
            libloc = self.spec["suite-sparse"].prefix.lib
        args.append(self.define("SUITE_SPARSE_LIBDIR", libloc))
        return args
