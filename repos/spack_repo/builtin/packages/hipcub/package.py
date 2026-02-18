# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Hipcub(CMakePackage, CudaPackage, ROCmPackage):
    """Radeon Open Compute Parallel Primitives Library"""

    homepage = "https://github.com/ROCm/hipCUB"
    git = "https://github.com/ROCm/hipCUB.git"
    url = "https://github.com/ROCm/hipCUB/archive/rocm-6.4.3.tar.gz"
    tags = ["rocm"]

    license("BSD-3-Clause")

    maintainers("srekolam", "renjithravindrankannath", "afzpatel")
    version("7.1.1", sha256="2a7dc48ba7feb0f21d62844df7e1ef075249e9d2a491b76c8eb8f60335eb24b1")
    version("7.1.0", sha256="131c1168f0b690874f5bce2f20c37ce854d4de47487ad1ffd2d361445276c0b8")
    version("7.0.2", sha256="ed7ce02bbbd1ed49dfeb2ec86cae01825dc7081c98875f046a9950ac4c9c8caa")
    version("7.0.0", sha256="fc17f982514fc5f5dd45938969d47f86b59f529500da9b160a32ca9cd5bc5796")
    version("6.4.3", sha256="1246f2d23665e4c4ec58a923d96b35cbfa4079adeda8bac47ba8fad3f85437bf")
    version("6.4.2", sha256="31efcb029c6f5056c04a03e881704206e988dda949cd308ef8c474e5bb9bbaee")
    version("6.4.1", sha256="93a213a37142ae38518b6d912b89dc0ecb50e092ce84df4cb06447f1528fcc29")
    version("6.4.0", sha256="2c044ed9bf53b9410ef6de4ca578384569b0a89cac4e8604dfdde390b2918481")
    version("6.3.3", sha256="4ce22aba007c6c8a8b2231adefa7785b1869e5fdd4af29b0371a499a523c2dc6")
    version("6.3.2", sha256="4a1443c2ea12c3aa05fb65703eb309ccf8b893f9e6cbebec4ccf5502ba54b940")
    version("6.3.1", sha256="e5d100c7b8f95fe6243ad9f22170c136aa34db4e588136bec54ede7cb2e7f12f")
    version("6.3.0", sha256="a609cde18cefa90a1970049cc5630f2ec263f12961aa85993897580da2ca0456")
    version("6.2.4", sha256="06f3655b110d3d2e2ecf0aca052d3ba3f2ef012c069e5d2d82f2b75d50555f46")
    version("6.2.1", sha256="e0203e72afac4da19cb1d62896fff404ec44517141b420bd38f6e962e52ef6fd")
    version("6.2.0", sha256="8dda8b77740e722fd4cf7223476313fc873bad75d50e6cb86ff284a91d76752d")
    version("6.1.2", sha256="830a0f3231e07fcc6cd6261c4e1af2d7d0ac4862c606ecdc80c2635557ca3d9f")
    version("6.1.1", sha256="967716d67e4270c599a60b770d543ea9148948edb907a0fa4d8be3a1785c2058")
    version("6.1.0", sha256="39ac03053ecf35f1faf212e5b197b03c0104b74b0833f7cce5cf625c273ba71c")
    version("6.0.2", sha256="3f912a23dc34510cf18d9097f6eda37e01d01724975c8149c92a64c92415968c")
    version("6.0.0", sha256="8d9f6e1e3f8433a2ceae1b0efd6727c21383980077e264725d00d5fee165bd30")
    version("5.7.1", sha256="9b23a58408bc4c549d3c754196cb3e2c1a50e177ab0a286101cbea2f7f173945")
    version("5.7.0", sha256="899356867f662d9a6f3870bb4a496f605a3143c6ad4d1fa9e9faead68fa8d13b")

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
    variant("asan", default=False, description="Build with address-sanitizer enabled or disabled")
    conflicts("+cuda +rocm", msg="CUDA and ROCm support are mutually exclusive")
    conflicts("~cuda ~rocm", msg="CUDA or ROCm support is required")

    depends_on("cxx", type="build")  # generated

    depends_on("cmake@3.10.2:", type="build")

    depends_on("googletest@1.10.0:", type="test")

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
        depends_on(f"rocprim@{ver}", when=f"+rocm @{ver}")
        depends_on(f"rocm-cmake@{ver}:", type="build", when=f"@{ver}")
        depends_on(f"hip +cuda@{ver}", when=f"+cuda @{ver}")

    # fix hardcoded search in /opt/rocm and broken config mode search
    patch("find-hip-cuda-rocm-5.3.patch", when="@5.7 +cuda")

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        if self.spec.satisfies("+rocm"):
            env.set("CXX", self.spec["hip"].hipcc)
        if self.spec.satisfies("+asan"):
            self.asan_on(env)

    def cmake_args(self):
        args = [self.define("BUILD_TEST", self.run_tests)]

        if self.spec.satisfies("+rocm ^cmake@3.21.0:3.21.2"):
            args.append(self.define("__skip_rocmclang", "ON"))

        # FindHIP.cmake is still used for +cuda
        if self.spec.satisfies("+cuda"):
            args.append(self.define("CMAKE_MODULE_PATH", self.spec["hip"].prefix.lib.cmake.hip))
        if self.spec.satisfies("@:6.3.1"):
            args.append(self.define("BUILD_FILE_REORG_BACKWARD_COMPATIBILITY", True))

        return args
