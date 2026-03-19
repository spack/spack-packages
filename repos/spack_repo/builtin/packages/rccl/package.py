# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import re

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Rccl(CMakePackage):
    """RCCL (pronounced "Rickle") is a stand-alone library
    of standard collective communication routines for GPUs,
    implementing all-reduce, all-gather, reduce, broadcast,
    and reduce-scatter."""

    homepage = "https://github.com/ROCm/rccl"
    git = "https://github.com/ROCm/rccl.git"
    url = "https://github.com/ROCm/rccl/archive/rocm-6.4.3.tar.gz"
    tags = ["rocm"]

    maintainers("srekolam", "renjithravindrankannath", "afzpatel")
    libraries = ["librccl"]
    version("7.2.0", sha256="c884d730711e433b9df88af3cdf003eeeb3df6d98e93a09475f760a2aa017078")
    version("7.1.1", sha256="eaa60bcf62feb3198553f2bcf6dcbfdfcecd0fdfabda41f1dae7d3f15fadbd68")
    version("7.1.0", sha256="50ba486bc8a466a68bff9d6c9d7b3ebf8de9426906720fa44023b5390602b3b8")
    version("7.0.2", sha256="3e4363163f5de772707c8deea349a00744200733693c76a07ac842e55b6ad19e")
    version("7.0.0", sha256="b55ecb07e82b130c9ce4fe9c969c2192a18b462f0e87ac70386e01341af6a98f")
    version(
        "6.4.3",
        tag="rocm-6.4.3",
        commit="2f7ac66cd64c68d4af8bb4562ce193778a7e470e",
        submodules=True,
    )
    version(
        "6.4.2",
        tag="rocm-6.4.2",
        commit="2f7ac66cd64c68d4af8bb4562ce193778a7e470e",
        submodules=True,
    )
    version(
        "6.4.1",
        tag="rocm-6.4.1",
        commit="e72b592201d626f16a03a7ba22502130a2846036",
        submodules=True,
    )
    version(
        "6.4.0",
        tag="rocm-6.4.0",
        commit="7b86f83d8468a577ed59d9b2a34a8d7639d36072",
        submodules=True,
    )
    version(
        "6.3.3",
        tag="rocm-6.3.3",
        commit="9a0e6a114c8f7371fa3050b413a350d6945fb7db",
        submodules=True,
    )
    version(
        "6.3.2",
        tag="rocm-6.3.2",
        commit="9a0e6a114c8f7371fa3050b413a350d6945fb7db",
        submodules=True,
    )
    version(
        "6.3.1",
        tag="rocm-6.3.1",
        commit="4ab67f5a5946d851a963b281cd9aa7b86eee752a",
        submodules=True,
    )
    version(
        "6.3.0",
        tag="rocm-6.3.0",
        commit="eef7b2918cef592a18b6e59859558e6a3f0f0614",
        submodules=True,
    )
    version("6.2.4", sha256="12a04743ed89a74b4a08aa046b6a549d385e15d6866042fd41eac8f085f50eea")
    version("6.2.1", sha256="0f5e35c7afbb21c1d49ff201b7d1ddf163d853c27c75c3eaf7b449f4dc1e2188")
    version("6.2.0", sha256="a29c94ea3b9c1a0121d7b1450cb01a697f9f9132169632312b9b0bf744d3c0e3")
    version("6.1.2", sha256="98af99c12d800f5439c7740d797162c35810a25e08e3b11b397d3300d3c0148e")
    version("6.1.1", sha256="6368275059ba190d554535d5aeaa5c2510d944b56efd85c90a1701d0292a14c5")
    version("6.1.0", sha256="c6308f6883cbd63dceadbe4ee154cc6fa9e6bdccbd2f0fda295b564b0cf01e9a")
    version("6.0.2", sha256="5c8495acba3d620b751e729d1157e7b4eea8f5e5692c50ce47c5204d3dfd443c")
    version("6.0.0", sha256="0496d5a5f2e48c92cd390ab318df31a53cf7ec590988c2574c9f3d99c38b0fa7")
    version("5.7.1", sha256="fb4c1f0084196d1226ce8a726d0f012d3890b54508a06ca87bbda619be8b90b1")
    version("5.7.0", sha256="4c2825a3e4323ef3c2f8855ef445c1a81cf1992fb37e3e8a07a50db354aa3954")

    amdgpu_targets = ROCmPackage.amdgpu_targets

    variant(
        "amdgpu_target",
        description="AMD GPU architecture",
        values=auto_or_any_combination_of(*amdgpu_targets),
        sticky=True,
    )
    variant("asan", default=False, description="Build with address-sanitizer enabled or disabled")

    patch("0004-Set-rocm-core-path-for-version-file.patch", when="@6.0:6.2")
    patch("0004-Set-rocm-core-path-for-version-file-6.3.patch", when="@6.3")
    patch("0004-Set-rocm-core-path-for-version-file-6.4.patch", when="@6.4")
    patch("0005-Add-rocm-core-roctracer-path.patch", when="@7.0")
    patch(
        "https://github.com/ROCm/rccl/commit/724680f87c8cfa1c4ffc8bfb5468fcc03e6606d9.patch?full_index=1",
        sha256="a747b2f76acf938860b4319cafb90426506d5b931ca776d094fd0eb9580ef785",
        when="@7.1",
    )
    # See https://github.com/ROCm/rocm-systems/pull/3231
    patch("memory-3231.patch", when="@7.1:")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("cmake@3.5:", type="build")
    depends_on("numactl@2:")

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
    ]:
        depends_on(f"rocm-cmake@{ver}:", type="build", when=f"@{ver}")
        depends_on(f"hip@{ver}", when=f"@{ver}")
        depends_on(f"comgr@{ver}", when=f"@{ver}")
        depends_on(f"hsa-rocr-dev@{ver}", when=f"@{ver}")
        depends_on(f"rocm-smi-lib@{ver}", when=f"@{ver}")
        depends_on(f"rocm-core@{ver}", when=f"@{ver}")

    for ver in ["6.4.0", "6.4.1", "6.4.2", "6.4.3", "7.0.0", "7.0.2", "7.1.0", "7.1.1", "7.2.0"]:
        depends_on(f"roctracer-dev@{ver}", when=f"@{ver}")
        depends_on(f"rocprofiler-register@{ver}", when=f"@{ver}")

    depends_on("googletest@1.11.0:", type="test")

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
        env.set("CXX", self.spec["hip"].hipcc)
        env.set("ROCMCORE_PATH", self.spec["rocm-core"].prefix)
        if self.spec.satisfies("+asan"):
            env.set("ASAN_OPTIONS", "detect_leaks=0")
            env.set("CFLAGS", "-fsanitize=address -shared-libasan")
            env.set("CXXFLAGS", "-fsanitize=address -shared-libasan")
            env.set("LDFLAGS", "-fuse-ld=lld")

    def cmake_args(self):
        args = [
            self.define("NUMACTL_DIR", self.spec["numactl"].prefix),
            self.define("ROCM_SMI_DIR", self.spec["rocm-smi-lib"].prefix),
            self.define("ROCM_PATH", self.spec["hip"].prefix),
            self.define("BUILD_TESTS", self.run_tests),
            self.define("ENABLE_MSCCLPP", False),
            self.define("ENABLE_MSCCL_KERNEL", False),
            # Anecdotally, memory usage is about ~8GB per job per GPU arch. The value could be
            # computed from amd_gpu_targets, except in the case of auto. Leave constant for now.
            self.define("RCCL_MAX_MEMORY", "32"),
            self.define("RCCL_MEMORY_PER_LINK_JOB", "8"),
        ]
        if "auto" not in self.spec.variants["amdgpu_target"]:
            if self.spec.satisfies("@7.1:"):
                args.append(self.define_from_variant("GPU_TARGETS", "amdgpu_target"))
            else:
                args.append(self.define_from_variant("AMDGPU_TARGETS", "amdgpu_target"))

        if self.spec.satisfies("^cmake@3.21.0:3.21.2"):
            args.append(self.define("__skip_rocmclang", True))
        if self.spec.satisfies("@7.0"):
            args.append(self.define("EXPLICIT_ROCM_VERSION", self.version))
        if self.spec.satisfies("@7.1:"):
            args.append(self.define("ROCMCORE_PATH", self.spec["rocm-core"].prefix))
        return args

    def test_unit(self):
        """Run unit tests"""
        unit_tests = which(join_path(self.prefix.bin, "rccl-UnitTests"), required=True)
        unit_tests()
