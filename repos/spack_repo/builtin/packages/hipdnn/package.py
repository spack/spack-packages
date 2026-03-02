# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage, generator
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Hipdnn(CMakePackage):
    """hipDNN is a graph-based deep learning library for AMD GPUs that leverages a flexible
    plugin architecture to provide optimized implementations and utilities
    for various routines"""

    homepage = "https://github.com/ROCm/hipDNN"
    url = "https://github.com/ROCm/rocm-libraries/archive/refs/tags/rocm-7.1.1.tar.gz"
    git = "https://github.com/ROCm/hipDNN.git"

    maintainers("srekolam", "afzpatel", "renjithravindrankannath")
    tags = ["rocm"]
    libraries = ["libmiopen_legacy_plugin", "libhipdnn_backend"]

    license("MIT")

    version("7.2.0", sha256="8ad5f4a11f1ed8a7b927f2e65f24083ca6ce902a42021a66a815190a91ccb654")
    version("7.1.1", sha256="2c00694c6131192354b0e785e4dcb06a302e4b7891ec50ca30927e05ba7b368b")

    amdgpu_targets = ROCmPackage.amdgpu_targets
    variant(
        "amdgpu_target",
        description="AMD GPU architecture",
        values=auto_or_any_combination_of(*amdgpu_targets),
        sticky=True,
    )
    variant("asan", default=False, description="Build with address-sanitizer enabled or disabled")
    variant("plugins", default=True, description="Build with  plugins enabled or disabled")
    variant("frontend", default=True, description="Build with front-end  enabled or disabled")

    generator("ninja")
    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("cmake@3.13.4:", type="build")
    depends_on("nlohmann-json")
    depends_on("flatbuffers")
    depends_on("spdlog")
    depends_on("googletest")

    for ver in ["7.1.1", "7.2.0"]:
        depends_on(f"rocm-cmake@{ver}:", type="build", when=f"@{ver}")
        depends_on(f"hip@{ver}", when=f"@{ver}")
        depends_on(f"llvm-amdgpu@{ver}", when=f"@{ver}")
        depends_on(f"miopen-hip@{ver}", when=f"@{ver}")

    patch("0001-change-the-install-prefix-of-hipdnn-for-spack-builds.patch", when="@7.1")

    def patch(self):
        filter_file(
            r"${ROCM_PATH}/llvm/bin",
            "{0}/bin".format(self.spec["llvm-amdgpu"].prefix),
            "projects/hipdnn/cmake/ClangToolChain.cmake",
            string=True,
        )
        filter_file(
            r"${ROCM_PATH}/llvm/lib",
            "{0}/lib".format(self.spec["llvm-amdgpu"].prefix),
            "projects/hipdnn/cmake/ClangToolChain.cmake",
            string=True,
        )
        if self.spec.satisfies("@7.2:"):
            filter_file(
                r"${ROCM_PATH}${DEFAULT_ROCM_LLVM_ROOT}",
                self.spec["llvm-amdgpu"].prefix,
                "projects/hipdnn/cmake/ClangToolChain.cmake",
                string=True,
            )

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

    @property
    def root_cmakelists_dir(self):
        return "projects/hipdnn"

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        if self.spec.satisfies("@7.1:"):
            env.set("CC", f"{self.spec['llvm-amdgpu'].prefix}/bin/clang")
            env.set("CXX", f"{self.spec['llvm-amdgpu'].prefix}/bin/clang++")
        if self.spec.satisfies("+asan"):
            env.set("ASAN_OPTIONS", "detect_leaks=0")
            env.set("CFLAGS", "-fsanitize=address -shared-libasan")
            env.set("CXXFLAGS", "-fsanitize=address -shared-libasan")
            env.set("LDFLAGS", "-fuse-ld=lld")

    def cmake_args(self):
        spec = self.spec
        args = [
            self.define_from_variant("BUILD_ADDRESS_SANITIZER", "asan"),
            self.define_from_variant("HIP_DNN_BUILD_PLUGINS", "plugins"),
            self.define_from_variant("HIP_DNN_BUILD_FRONTEND", "frontend"),
            self.define(
                "HIP_DNN_NLOHMANN_JSON_INCLUDE_DIR",
                "{0}/include".format(spec["nlohmann-json"].prefix),
            ),
            self.define(
                "HIP_DNN_FLATBUFFERS_INCLUDE_DIR", "{0}/include".format(spec["flatbuffers"].prefix)
            ),
            self.define("HIP_DNN_SPDLOG_INCLUDE_DIR", "{0}/include".format(spec["spdlog"].prefix)),
            self.define("HIPDNN_NO_DOWNLOAD", "ON"),
            self.define("HIP_DNN_SKIP_TESTS", not self.run_tests),
        ]
        if "auto" not in self.spec.variants["amdgpu_target"]:
            args.append(self.define_from_variant("GPU_TARGETS", "amdgpu_target"))
        if spec.satisfies("@7.2:"):
            args.append(self.define("CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT", "OFF"))
            args.append(self.define("CMAKE_MAKE_PROGRAM", spec["ninja"].prefix.bin.ninja))
            args.append(self.define("ROCM_LLVM_BIN_DIR", spec["llvm-amdgpu"].prefix.bin))
        return args
