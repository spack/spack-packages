# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Rocdecode(CMakePackage):
    """rocDecode is a high performance video decode SDK for AMD hardware"""

    homepage = "https://github.com/ROCm/rocDecode"
    git = "https://github.com/ROCm/rocDecode.git"
    url = "https://github.com/ROCm/rocDecode/archive/refs/tags/rocm-6.4.3.tar.gz"

    tags = ["rocm"]

    maintainers("afzpatel", "srekolam", "renjithravindrankannath")

    license("MIT")
    version("7.1.1", sha256="76e7a27eb49b262ed68c2c8f13a20aba8700113087bc58068c396979e6051596")
    version("7.1.0", sha256="ccd8d7fe8010214a00d75ac0299747ad9ebf25849f2575cb096b814ec071d952")
    version("7.0.2", sha256="4d8c49236135105f252fe6ccd8652a440b4646129cad8595eead49cc7d34aa96")
    version("7.0.0", sha256="f0c1dd260bf091c44d15718008630d0b882b8f444f4740c9d8edcbbed1e759fe")
    version("6.4.3", sha256="dd485e1cf24eb6f7315c32afcd2eb639a64dfb100a747bdbef3aa3235c4e3fa9")
    version("6.4.2", sha256="43c3bc2fe71c150bd6e646c95f834002df80d0bc6489082731c0be68fb785eac")
    version("6.4.1", sha256="35e364cec1405c76cfbb91215e1a327efea1e60340d8c8df12c0e5b2f0e1321e")
    version("6.4.0", sha256="d82c17687cc8ccac67fe2d401edd25c9825b38777b7a7b4100f84658838a1e50")
    version("6.3.3", sha256="e72f53674527b7a6c3cba3b7555fee32117f0875107fd9e632a2ec1d5ce03489")
    version("6.3.2", sha256="39ff3c21c81a73910dcfe6a147edaddecc21575a3077f0f99971c8d2f6d0e7d5")
    version("6.3.1", sha256="94da1a61167abaf3f983ae5d62bffb22bb8ba3eb1c9d9fc7c68ed9a066aa4e52")
    version("6.3.0", sha256="931f49ff86fa34929b03cec8e7becde78d0c49c1c3a23a13203fecd2b392b242")
    version("6.2.4", sha256="37aaa1299cfc517ddaf60b0e8a5cf06d672f59e8acc0da3862b40b810d4931cb")
    version("6.2.1", sha256="d4a636415d61fef94f97197cb9ebbff59e3a18dc4850612ee142e3e14a35e6d4")
    version("6.2.0", sha256="fe0d7c19a4e65b93405566511880b94f25ef68c830d0088f9458da9baea1d4f9")
    version("6.1.2", sha256="67a13aeaa495e06683124de5908e61cf2be3beff79b13d858897344aa809775e")
    version("6.1.1", sha256="5914c91e433ec7e8511b8a9017d165a0589c1aff9f5527b413d0b3a32a3cc318")
    version("6.1.0", sha256="8316dbde87f1fea782af6216c8d013e866542329a673fb24a668335c6169ef8f")

    amdgpu_targets = ROCmPackage.amdgpu_targets

    variant(
        "amdgpu_target",
        description="AMD GPU architecture",
        values=auto_or_any_combination_of(*amdgpu_targets),
        sticky=True,
    )

    depends_on("libva", type="build", when="@6.2:")
    depends_on("libdrm", type="build", when="@6.4:")
    depends_on("ffmpeg", when="@7.0:")

    for ver in [
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
        depends_on(f"hip@{ver}", when=f"@{ver}")

    for ver in ["6.4.0", "6.4.1", "6.4.2", "6.4.3", "7.0.0", "7.0.2", "7.1.0", "7.1.1"]:
        depends_on(f"llvm-amdgpu@{ver}", when=f"@{ver}")

    patch("0001-add-amdgpu-drm-include.patch", when="@6.4")

    def patch(self):
        if self.spec.satisfies("@:7.0"):
            filter_file(
                r"${ROCM_PATH}/llvm/bin/clang++",
                "{0}/bin/clang++".format(self.spec["llvm-amdgpu"].prefix),
                "CMakeLists.txt",
                string=True,
            )
            filter_file(
                r"${ROCM_PATH}/lib/llvm/bin/clang++",
                "{0}/bin/clang++".format(self.spec["llvm-amdgpu"].prefix),
                "CMakeLists.txt",
                string=True,
            )

    def cmake_args(self):
        args = []
        if "auto" not in self.spec.variants["amdgpu_target"]:
            args.append(self.define_from_variant("AMDGPU_TARGETS", "amdgpu_target"))
        if self.spec.satisfies("@6.3.0:"):
            args.append(self.define("LIBVA_INCLUDE_DIR", self.spec["libva"].prefix.include))
        if self.spec.satisfies("@6.4.0:"):
            args.append(
                self.define("CMAKE_C_COMPILER", f"{self.spec['llvm-amdgpu'].prefix}/bin/amdclang")
            )
            args.append(
                self.define(
                    "CMAKE_CXX_COMPILER", f"{self.spec['llvm-amdgpu'].prefix}/bin/amdclang++"
                )
            )
        if self.spec.satisfies("@6.4"):
            args.append(self.define("AMDGPU_DRM_INCLUDE_DIRS", self.spec["libdrm"].prefix.include))
        if self.spec.satisfies("@7.0:"):
            args.append(
                self.define("LIBDRM_AMDGPU_INCLUDE_DIR", self.spec["libdrm"].prefix.include)
            )
            args.append(self.define("LIBDRM_AMDGPU_LIBRARY", self.spec["libdrm"].prefix.lib))
        return args
