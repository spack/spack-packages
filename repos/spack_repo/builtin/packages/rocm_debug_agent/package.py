# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.rocm import ROCmLibrary

from spack.package import *


class RocmDebugAgent(ROCmLibrary, CMakePackage):
    """Radeon Open Compute (ROCm) debug agent"""

    homepage = "https://github.com/ROCm/rocr_debug_agent"
    git = "https://github.com/ROCm/rocr_debug_agent.git"
    url = "https://github.com/ROCm/rocr_debug_agent/archive/rocm-6.2.4.tar.gz"
    tags = ["rocm"]

    maintainers("srekolam", "renjithravindrankannath", "afzpatel")
    libraries = ["librocm-debug-agent"]

    version("7.2.1", sha256="7dfd3363e07fcec65fb8f66c442e0cd601621cb5e086f311205ac3e65c9f9b6c")
    version("7.2.0", sha256="42b7e7afe16913e67b7af1358ddbe7772bff1ffe61f4d60960062288b6287c2c")
    version("7.1.1", sha256="2e8ab39ab68fe6eccaa9494b984faa7fb7edfb12e3f7e1b38dfe146e5b914d10")
    version("7.1.0", sha256="21224ffe5019f1e2a160cad587b0448e550954accce9fd051a915c3f95b54e5b")
    version("7.0.2", sha256="72ef89af0ec15edf43a99a3e76a420d501fa0871825c9baecd9dff1fc4d021dd")
    version("7.0.0", sha256="5d822964855979c5063e0ec9554596463d37cdf5f3501550887c034beb3adcc8")
    version("6.4.3", sha256="4be5783e3df89e8c3e35c5690d9414ca8a0b695081352bb945bb533e01de1d65")
    version("6.4.2", sha256="8b42dee486f959795acbac7f8bf287718edbb14393e6262c3dcec97f0697d949")
    version("6.4.1", sha256="0e9fc4626e16eea1c701b5206349fceab4ec596a1d22738977e779f673a26769")
    version("6.4.0", sha256="699af72a1ff7edf3cff6ef293469345538da06aaedefb3540dd61f55ea862330")
    version("6.3.3", sha256="27407c5cabec3d9757ffe5eb729639ccb3ad3b086f57f101854b73479a6f0f51")
    version("6.3.2", sha256="578aa08b10a456eebd2b548afd86339bd5a5df807611ffd20cc3006eaae74836")
    version("6.3.1", sha256="0e28a9febf3b95cc6bbf8eae91091bf22a8f49fe9558171251f8f9afe666f9d7")
    version("6.3.0", sha256="c8c3461395b2fc1e136d61eb5a36ba9f3f751eb00cb9d830f498de2e5d4299d5")
    version("6.2.4", sha256="a4f213a9e28a1e82543135c0b6d16c5a252186f83fc842f980631943f7e11398")
    version("6.2.1", sha256="933223ff6e0aefb54917f4102ac6679dcd67e25ade4bce5e49f5212f45e3bae5")
    version("6.2.0", sha256="a4b839c47b8a1cd8d00c3577eeeea04d3661210eb8124e221d88bcbedc742363")
    version("6.1.2", sha256="c7cb779915a3d61e39d92cef172997bcf5eae720308f6d9c363a2cbc71b5621c")
    version("6.1.1", sha256="c631281b346bab9ec3607c59404f548f7cba084a05e9c9ceb3c3579c48361ad1")
    version("6.1.0", sha256="f52700563e490d662b505693d485272d73521aabff306107586dd1149fb4a70e")
    version("6.0.2", sha256="da8da1241a6cbb9d0b2a3b81829faf632225a7a27ca881c9715b9f05bca54c89")
    version("6.0.0", sha256="705be2c2bd0f5c7d1e286eb9b94045b2bd017ff323f07bca9aa7c81f2d168524")
    version("5.7.1", sha256="3b8d2835935da98f41e7cfc5b808c596ac06dd705b9a07bb70283e002f8dea6a")
    version("5.7.0", sha256="d9344ed02e82a01140f2162e901e6a519e5fee6b498e2f49417730ee2660c5c1")

    variant("asan", default=False, description="Build with address-sanitizer enabled or disabled")

    conflicts("+asan", when="os=rhel9")
    conflicts("+asan", when="os=centos7")
    conflicts("+asan", when="os=centos8")

    depends_on("cxx", type="build")  # generated
    depends_on("c", type="build")

    depends_on("cmake@3:", type="build")
    depends_on("elfutils@0.188:", type="link")

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
        "7.2.0",
        "7.2.1",
    ]:
        depends_on(f"hsa-rocr-dev@{ver}", when=f"@{ver}")
        depends_on(f"rocm-dbgapi@{ver}", when=f"@{ver}")
        depends_on(f"hip@{ver}", when=f"@{ver}")
        depends_on(f"rocm-core@{ver}", when=f"@{ver}")

    # https://github.com/ROCm/rocr_debug_agent/pull/4
    patch("0001-Drop-overly-strict-Werror-flag.patch")
    patch("0002-add-hip-architecture.patch", when="@:6.3")

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.set("CC", f"{self.spec['llvm-amdgpu'].prefix}/bin/clang")
        env.set("CXX", f"{self.spec['llvm-amdgpu'].prefix}/bin/clang++")
        if self.spec.satisfies("+asan"):
            env.set("ASAN_OPTIONS", "detect_leaks=0")
            env.set("CFLAGS", "-fsanitize=address -shared-libasan")
            env.set("CXXFLAGS", "-fsanitize=address -shared-libasan")
            env.set("LDFLAGS", "-fuse-ld=lld")

    def cmake_args(self):
        spec = self.spec
        args = [self.define("CMAKE_MODULE_PATH", spec["hip"].prefix.lib.cmake.hip)]
        return args
