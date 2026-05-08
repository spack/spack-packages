# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage, generator

from spack.package import *


class Aotriton(CMakePackage):
    """Ahead of Time (AOT) Triton Math Library."""

    homepage = "https://github.com/ROCm/aotriton"
    git = "https://github.com/ROCm/aotriton.git"
    url = "https://github.com/ROCm/aotriton/archive/refs/tags/0.8.2b.tar.gz"

    maintainers("afzpatel", "srekolam", "renjithravindrankannath")

    license("MIT")
    version(
        "0.11.1b",
        tag="0.11.1b",
        commit="98371989e8a23267e284c94e95156a139e4b33c4",
        submodules=True,
    )
    version(
        "0.11b", tag="0.11b", commit="972223c501ffc22068bb035ac5d64cf54318d895", submodules=True
    )
    version(
        "0.10b", tag="0.10b", commit="6fca155f4deeb8d9529326f7b69f350aeeb93477", submodules=True
    )
    version(
        "0.9.2b", tag="0.9.2b", commit="b388d223d8c7213545603e00f6f3148c54d1f525", submodules=True
    )
    version(
        "0.9.1b", tag="0.9.1b", commit="6f72f6943c9da89d6f0e420c29a5d33a122185cf", submodules=True
    )
    version("0.9b", tag="0.9b", commit="f539cf9c2bf99dca8d0170d156c3f6f0b7b5cce5", submodules=True)
    version(
        "0.8.2b", tag="0.8.2b", commit="b24f43a9771622faa157155568b9a200c3b49e41", submodules=True
    )
    version(
        "0.8.1b", tag="0.8.1b", commit="3a80554a88ae3b1bcf4b27bc74ad9d7b913b58f6", submodules=True
    )
    version("0.8b", tag="0.8b", commit="6f8cbcac8a92775291bb1ba8f514d4beb350baf4", submodules=True)

    generator("ninja")
    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("py-setuptools@40.8:", type="build")
    depends_on("py-filelock", type=("build", "run"))

    depends_on("cmake@3.26:", type="build")
    depends_on("python", type="build")
    depends_on("z3", type="link")
    depends_on("zlib-api", type="link")
    depends_on("xz", type="link")
    depends_on("pkgconfig", type="build")

    # build llvm version with mlir with the commit that matches inside the llvm-hash.txt
    depends_on("aotriton-llvm@0.10", when="@0.10b:")
    depends_on("aotriton-llvm@0.9", when="@0.9b")
    depends_on("aotriton-llvm@0.8", when="@0.8b")

    conflicts("^openssl@3.3.0")

    # https://github.com/ROCm/aotriton/blob/main/README.md?plain=1#L24
    conflicts("%gcc@:11.3", when="@0.9b:", msg="The binary delivery is compiled with gcc13")

    # ROCm dependencies
    depends_on("hip", type="build")
    depends_on("llvm-amdgpu", type="build")
    depends_on("comgr", type="build")
    depends_on("hsa-rocr-dev", type="build")

    def patch(self):
        if self.spec.satisfies("^hip"):
            filter_file(
                "/opt/rocm/llvm/bin/ld.lld",
                f"{self.spec['llvm-amdgpu'].prefix}/bin/ld.lld",
                "third_party/triton/third_party/amd/backend/compiler.py",
                string=True,
            )

        if self.spec.satisfies("@:0.9b"):
            filter_file(
                r"LLVM_INCLUDE_DIRS",
                f"{self.spec['aotriton-llvm'].prefix}/include",
                "third_party/triton/python/setup.py",
                string=True,
            )
            filter_file(
                r"LLVM_LIBRARY_DIR",
                f"{self.spec['aotriton-llvm'].prefix}/lib",
                "third_party/triton/python/setup.py",
                string=True,
            )
            filter_file(
                r"LLVM_SYSPATH",
                f"{self.spec['aotriton-llvm'].prefix}",
                "third_party/triton/python/setup.py",
                string=True,
            )
        if self.spec.satisfies("@0.10b:"):
            filter_file(
                r"LLVM_INCLUDE_DIRS",
                f"{self.spec['aotriton-llvm'].prefix}/include",
                "third_party/triton/setup.py",
                string=True,
            )
            filter_file(
                r"LLVM_LIBRARY_DIR",
                f"{self.spec['aotriton-llvm'].prefix}/lib",
                "third_party/triton/setup.py",
                string=True,
            )
            filter_file(
                r"LLVM_SYSPATH",
                f"{self.spec['aotriton-llvm'].prefix}",
                "third_party/triton/setup.py",
                string=True,
            )

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        """Set environment variables used to control the build"""
        if self.spec.satisfies("%clang"):
            env.set(
                "TRITON_HIP_LLD_PATH", join_path(self.spec["llvm-amdgpu"].prefix, "bin", "ld.lld")
            )

    def cmake_args(self):
        args = []
        args.append(self.define("AOTRITON_GPU_BUILD_TIMEOUT", 0))
        args.append(self.define("AOTRITON_NOIMAGE_MODE", "ON"))
        # So libaotriton_v2.so and extensions find libamdhip64.so at runtime and
        # during binary cache relocation (avoids "libamdhip64.so.6 => not found").
        args.append(self.define("CMAKE_INSTALL_RPATH", self.spec["hip"].prefix.lib))
        args.append(self.define("CMAKE_INSTALL_RPATH_USE_LINK_PATH", True))
        # So libaotriton_v2.so and extensions find shared libs at runtime and
        # during binary cache relocation (avoids "=> not found" for e.g.
        # libamdhip64.so.6, libz.so.1, libhsa-runtime64.so.1, libc++abi.so.1,
        # libunwind.so.1).
        rpath_dirs = [
            self.spec["hip"].prefix.lib,
            self.spec["hsa-rocr-dev"].prefix.lib,
            self.spec["zlib-api"].prefix.lib,
            self.spec["aotriton-llvm"].prefix.lib,
        ]
        args.append(self.define("CMAKE_INSTALL_RPATH", rpath_dirs))
        if self.spec.satisfies("@0.11b"):
            args.append(self.define("AOTRITON_USE_TORCH", "OFF"))
        return args
