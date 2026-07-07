# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import re

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


def submodules(package):
    submodules = [
        "projects/rocprofiler-sdk/external/googletest",
        "projects/rocprofiler-sdk/external/fmt",
        "projects/rocprofiler-sdk/external/doxygen-awesome-css",
        "projects/rocprofiler-sdk/external/ptl",
        "projects/rocprofiler-sdk/external/cereal",
        "projects/rocprofiler-sdk/external/filesystem",
        "projects/rocprofiler-sdk/external/perfetto",
        "projects/rocprofiler-sdk/external/elfio",
        "projects/rocprofiler-sdk/external/yaml-cpp",
        "projects/rocprofiler-sdk/external/json",
    ]
    return submodules


class RocprofilerSdk(CMakePackage):
    """ROCProfiler-SDK is AMD’s new and improved tooling infrastructure, providing a
    hardware-specific low-level performance analysis interface for profiling and
    tracing GPU compute applications."""

    homepage = "https://github.com/ROCm/rocprofiler-sdk"
    git = "https://github.com/ROCm/rocm-systems.git"
    url = "https://github.com/ROCm/rocprofiler-sdk/archive/refs/tags/rocm-6.3.2.tar.gz"

    tags = ["rocm"]

    maintainers("afzpatel", "srekolam", "renjithravindrankannath")
    executables = ["rocprofv3"]

    license("MIT")
    version(
        "7.2.3",
        tag="rocm-7.2.3",
        commit="c2d94761153e1033a91744842dfc66eddd631fde",
        submodules=submodules,
    )
    version(
        "7.2.1",
        tag="rocm-7.2.1",
        commit="e1a6bc5663304b9c586b3254b8920f2981057804",
        submodules=submodules,
    )
    version(
        "7.2.0",
        tag="rocm-7.2.0",
        commit="fc0010cf6a5a972d42b276df946510f30343d493",
        submodules=submodules,
    )
    version(
        "7.1.1",
        git="https://github.com/ROCm/rocprofiler-sdk.git",
        tag="rocm-7.1.1",
        commit="ff4f9a64d386454ed5f1a1360a2a5c14292f36c6",
        submodules=True,
    )
    version(
        "7.1.0",
        git="https://github.com/ROCm/rocprofiler-sdk.git",
        tag="rocm-7.1.0",
        commit="d5c0aaae36a6cb348f408c9fde8be435e29981b9",
        submodules=True,
    )
    version(
        "7.0.2",
        git="https://github.com/ROCm/rocprofiler-sdk.git",
        tag="rocm-7.0.2",
        commit="19ae05055bee5dab65854b44c047f34db2e8276c",
        submodules=True,
    )
    version(
        "7.0.0",
        git="https://github.com/ROCm/rocprofiler-sdk.git",
        tag="rocm-7.0.0",
        commit="18af6a58b74558c91ba09376d86d2401da2cf76f",
        submodules=True,
    )
    version(
        "6.4.3",
        git="https://github.com/ROCm/rocprofiler-sdk.git",
        tag="rocm-6.4.3",
        commit="fb30388fd30c073ac7baf3dad775f37c51aafcc8",
        submodules=True,
    )
    version(
        "6.4.2",
        git="https://github.com/ROCm/rocprofiler-sdk.git",
        tag="rocm-6.4.2",
        commit="e8e49fe76971000a42a5a177d9a727d16dd0ebcf",
        submodules=True,
    )
    version(
        "6.4.1",
        git="https://github.com/ROCm/rocprofiler-sdk.git",
        tag="rocm-6.4.1",
        commit="e8e49fe76971000a42a5a177d9a727d16dd0ebcf",
        submodules=True,
    )
    version(
        "6.4.0",
        git="https://github.com/ROCm/rocprofiler-sdk.git",
        tag="rocm-6.4.0",
        commit="e8e49fe76971000a42a5a177d9a727d16dd0ebcf",
        submodules=True,
    )
    version(
        "6.3.3",
        git="https://github.com/ROCm/rocprofiler-sdk.git",
        tag="rocm-6.3.3",
        commit="95a3964ee26ac45618517f24669858bdb39ea7d2",
        submodules=True,
    )
    version(
        "6.3.2",
        git="https://github.com/ROCm/rocprofiler-sdk.git",
        tag="rocm-6.3.2",
        commit="f5d3fd3d3460c74cb8935f0021e31f0bff5cb305",
        submodules=True,
    )
    version(
        "6.3.1",
        git="https://github.com/ROCm/rocprofiler-sdk.git",
        tag="rocm-6.3.1",
        commit="38ac1c8f7d62cbb702f53c7085be16bf1943369a",
        submodules=True,
    )
    version(
        "6.3.0",
        git="https://github.com/ROCm/rocprofiler-sdk.git",
        tag="rocm-6.3.0",
        commit="38ac1c8f7d62cbb702f53c7085be16bf1943369a",
        submodules=True,
    )
    version(
        "6.2.4",
        git="https://github.com/ROCm/rocprofiler-sdk.git",
        tag="rocm-6.2.4",
        commit="03fe8df3622a97161699439dfe933ef8e9e7db8a",
        submodules=True,
    )
    amdgpu_targets = ROCmPackage.amdgpu_targets

    variant(
        "amdgpu_target",
        description="AMD GPU architecture",
        values=auto_or_any_combination_of(*amdgpu_targets),
        sticky=True,
    )

    variant("internal-fmt", default=False, description="build internal fmt")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("sqlite", when="@7:")
    depends_on("elfutils")
    depends_on("libdrm")
    depends_on("pkgconfig", when="@7.1:")
    depends_on("py-pybind11", when="@7.2:")
    depends_on("gotcha", when="@7.2:")
    depends_on("fmt@:10", when="@7.2: ~internal-fmt")
    depends_on("glog", when="@7.2:")

    for ver in ["6.2.4", "6.3.0", "6.3.1", "6.3.2", "6.3.3", "6.4.0", "6.4.1", "6.4.2", "6.4.3"]:
        depends_on(f"aqlprofile@{ver}", when=f"@{ver}")
    for ver in ["7.0.0", "7.0.2", "7.1.0", "7.1.1", "7.2.0", "7.2.1", "7.2.3"]:
        depends_on(f"hsa-amd-aqlprofile@{ver}", when=f"@{ver}")

    for ver in [
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
        "7.2.3",
    ]:
        depends_on(f"hip@{ver}", when=f"@{ver}")
        depends_on(f"rocm-cmake@{ver}", when=f"@{ver}")
        for tgt in ROCmPackage.amdgpu_targets:
            depends_on(f"rccl@{ver} amdgpu_target={tgt}", when=f"@{ver} amdgpu_target={tgt}")
        depends_on(f"rocprofiler-register@{ver}", when=f"@{ver}")

    for ver in [
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
        "7.2.3",
    ]:
        for tgt in ROCmPackage.amdgpu_targets:
            depends_on(f"rocdecode@{ver} amdgpu_target={tgt}", when=f"@{ver} amdgpu_target={tgt}")

    patch(
        "https://github.com/ROCm/rocm-systems/commit/ef7253365c420ca486f074b9e9119a222e30fea0.patch?full_index=1",
        sha256="05a71386d12d7fc98a40c025dc65a804556e01f381d1101ea244f35f29edd3d8",
        when="@7.2:",
    )

    @property
    def root_cmakelists_dir(self):
        if self.spec.satisfies("@:7.1"):
            return "."
        else:
            return "projects/rocprofiler-sdk"

    def cmake_args(self):
        args = []
        if self.spec.satisfies("@7.1:"):
            args.append(self.define("ElfUtils_ROOT_DIR", self.spec["elfutils"].prefix))
        if self.spec.satisfies("@7.2:"):
            args.append(self.define("ROCPROFILER_BUILD_PYBIND11", "OFF"))
            args.append(self.define_from_variant("ROCPROFILER_BUILD_FMT", "internal-fmt"))
            args.append(self.define("ROCPROFILER_BUILD_GLOG", "OFF"))
            args.append(self.define("ROCPROFILER_BUILD_GOTCHA", "OFF"))
            args.append(self.define("ROCPROFILER_BUILD_SQLITE3", "OFF"))
        return args

    def setup_run_environment(self, env):
        if not self.spec.external:
            if self.spec.satisfies("@7:"):
                env.prepend_path("LD_LIBRARY_PATH", self.spec["hsa-amd-aqlprofile"].prefix.lib)
            else:
                env.prepend_path("LD_LIBRARY_PATH", self.spec["aqlprofile"].prefix.lib)

    @classmethod
    def determine_version(cls, exe):
        output = Executable(exe)("--version", output=str, error=str)
        match = re.search(r"rocm_version: (\d+\.\d+\.\d+)", output)
        return match.group(1) if match else None
