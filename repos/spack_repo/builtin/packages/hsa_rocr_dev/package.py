# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import re

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class HsaRocrDev(CMakePackage):
    """This repository includes the user mode API nterfaces and libraries
    necessary for host applications to launch computer kernels to available
    HSA ROCm kernel agents.AMD Heterogeneous System Architecture HSA -
    Linux HSA Runtime for Boltzmann (ROCm) platforms."""

    homepage = "https://github.com/ROCm/ROCR-Runtime"
    git = "https://github.com/ROCm/ROCR-Runtime.git"
    url = "https://github.com/ROCm/ROCR-Runtime/archive/rocm-6.2.4.tar.gz"
    tags = ["rocm"]

    maintainers("srekolam", "renjithravindrankannath", "haampie", "afzpatel")
    libraries = ["libhsa-runtime64"]

    version("7.1.1", sha256="4c5b58afa1e11461954bd005a10ebf29941c120f1d6a7863954597f5eacfc605")
    version("7.1.0", sha256="383fa8e1776c3ee527cdddc9f9ac6f7134c3fcd8758eae9be8bd3a8b7fdca9b1")
    version("7.0.2", sha256="9c2020f7a42d60fe9775865ab58464078007926a3b01f1ca8128557c89e7a566")
    version("7.0.0", sha256="9ea2cbcf343f643ede6e16d82fbd0303771e1978759b2e546d0efc0df3263e4c")
    version("6.4.3", sha256="3b23bed04cbed72304d31d69901eb76afa2099c7ac37f055348dfcda2d25e41a")
    version("6.4.2", sha256="8ad5dbf7cb0f728b8e515f46a41db24ed3b99ca894ccdd9f4d9bac969e9e35bb")
    version("6.4.1", sha256="f72d100a46a2dd9f4c870cef156604777f1bdb1841df039d14bf37b19814b9da")
    version("6.4.0", sha256="ff740e8c8f2229c6dc47577363f707b1a44ea4254f8ad74f8f0a669998829535")
    version("6.3.3", sha256="aa2e30d3d68707d6df4840e954bb08cc13cd312cec1a98a64d97adbe07262f50")
    version("6.3.2", sha256="aaecaa7206b6fa1d5d7b8f7c1f7c5057a944327ba4779448980d7e7c7122b074")
    version("6.3.1", sha256="547ceeeda9a41cdffa21e57809dc5834f94938a0a2809c283aebcbcf01901df0")
    version("6.3.0", sha256="8fd6bcd6a5afd0ae5a59e33b786a525f575183d38c34049c2dab6b9270a1ca3b")
    version("6.2.4", sha256="b7aa0055855398d1228c39a6f4feb7d7be921af4f43d82855faf0b531394bb9b")
    version("6.2.1", sha256="dbe477b323df636f5e3221471780da156c938ec00dda4b50639aa8d7fb9248f4")
    version("6.2.0", sha256="c98090041fa56ca4a260709876e2666f85ab7464db9454b177a189e1f52e0b1a")
    version("6.1.2", sha256="6eb7a02e5f1e5e3499206b9e74c9ccdd644abaafa2609dea0993124637617866")
    version("6.1.1", sha256="72841f112f953c16619938273370eb8727ddf6c2e00312856c9fca54db583b99")
    version("6.1.0", sha256="50386ebcb7ff24449afa2a10c76a059597464f877225c582ba3e097632a43f9c")
    version("6.0.2", sha256="e7ff4d7ac35a2dd8aad1cb40b96511a77a9c23fe4d1607902328e53728e05c28")
    version("6.0.0", sha256="99e8fa1af52d0bf382f28468e1a345af1ff3452c35914a6a7b5eeaf69fc568db")
    version("5.7.1", sha256="655e9bfef4b0b6ad3f9b89c934dc0a8377273bb0bccbda6c399ac5d5d2c1c04c")
    version("5.7.0", sha256="2c56ec5c78a36f2b847afd4632cb25dbf6ecc58661eb2ae038c2552342e6ce23")

    variant("shared", default=True, description="Build shared or static library")
    variant("image", default=True, description="build with or without image support")
    variant("asan", default=False, description="Build with address-sanitizer enabled or disabled")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("cmake@3:", type="build")
    depends_on("pkgconfig", type="build")

    # Note, technically only necessary when='@3.7: +image', but added to all
    # to work around https://github.com/spack/spack/issues/23951
    depends_on("xxd", when="+image", type="build")
    depends_on("elf", type="link")
    depends_on("numactl")
    depends_on("pkgconfig")
    depends_on("libdrm", when="@6.3:")

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
    ]:
        depends_on(f"hsakmt-roct@{ver}", when=f"@{ver}")

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
        depends_on(f"llvm-amdgpu@{ver}", when=f"@{ver}")
        depends_on(f"rocm-core@{ver}", when=f"@{ver}")

    for ver in [
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
        depends_on(f"rocprofiler-register@{ver}", when=f"@{ver}")

    @property
    def root_cmakelists_dir(self):
        if self.spec.satisfies("@6.3:"):
            return "."
        else:
            return "src"

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
        if self.spec.satisfies("@5.7: +asan"):
            numa_inc = self.spec["numactl"].prefix.include
            numa_lib = self.spec["numactl"].prefix.lib
            env.set("CC", f"{self.spec['llvm-amdgpu'].prefix}/bin/clang")
            env.set("CXX", f"{self.spec['llvm-amdgpu'].prefix}/bin/clang++")
            env.set("ASAN_OPTIONS", "detect_leaks=0")
            env.set("CFLAGS", f"-fsanitize=address -shared-libasan -I{numa_inc} -L{numa_lib}")
            env.set("CXXFLAGS", f"-fsanitize=address -shared-libasan -I{numa_inc} -L{numa_lib}")
            env.set("LDFLAGS", "-fuse-ld=lld")

    def cmake_args(self):
        spec = self.spec

        # hsa-rocr-dev wants the directory containing the header files, but
        # libelf adds an extra path (include/libelf) compared to elfutils
        libelf_include = os.path.dirname(
            find_headers("libelf", spec["elf"].prefix.include, recursive=True)[0]
        )

        args = [
            self.define("LIBELF_INCLUDE_DIRS", libelf_include),
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define_from_variant("IMAGE_SUPPORT", "image"),
            self.define("CMAKE_INSTALL_LIBDIR", "lib"),
        ]

        # device libs is bundled with llvm-amdgpu (default) or standalone
        if self.spec.satisfies("^rocm-device-libs"):
            bitcode_dir = spec["rocm-device-libs"].prefix.amdgcn.bitcode
        else:
            bitcode_dir = spec["llvm-amdgpu"].prefix.amdgcn.bitcode

        args.append(self.define("BITCODE_DIR", bitcode_dir))

        if self.spec.satisfies("@5.7.0:"):
            args.append(self.define_from_variant("ADDRESS_SANITIZER", "asan"))
        if self.spec.satisfies("@6.0"):
            args.append(self.define("ROCM_PATCH_VERSION", "60000"))
        if self.spec.satisfies("@6.1"):
            args.append(self.define("ROCM_PATCH_VERSION", "60100"))
        if self.spec.satisfies("@6.2"):
            args.append(self.define("ROCM_PATCH_VERSION", "60200"))
        if self.spec.satisfies("@6.3"):
            args.append(self.define("ROCM_PATCH_VERSION", "60300"))
        if self.spec.satisfies("@6.3.2:"):
            args.append(self.define("SHARED_LIBS", "ON"))
            args.append(self.define("BUILD_SHARED_LIBS", "ON"))
        return args
