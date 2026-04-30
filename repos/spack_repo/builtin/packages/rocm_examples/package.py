# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class RocmExamples(CMakePackage):
    """A collection of examples for the ROCm software stack"""

    homepage = "https://github.com/ROCm/rocm-examples"
    git = "https://github.com/ROCm/rocm-examples.git"
    url = "https://github.com/ROCm/rocm-examples/archive/refs/tags/rocm-6.2.1.tar.gz"

    tags = ["rocm"]

    maintainers("srekolam", "renjithravindrankannath", "afzpatel")

    license("MIT")

    version("7.2.1", sha256="34457fc665f814ec3a0a5f83edabccc18c293825f0d421b5d9e101b7494da637")
    version("7.2.0", sha256="74c516f08cc0067c85ac5c29f25831a6e74c0cc0f0c07e80798dc827efefbde5")
    version("7.1.1", sha256="7475c4eaca103395ecae93cc5fa51b77884d06ebe990e71383c53a91bc1b089f")
    version("7.1.0", sha256="d64a82ba472126bb426c54abd1b2516479a375db895171bbc4024a7c8d0f4e94")
    version("7.0.2", sha256="02ca88ec6ce584b6710f295c2ab2df61d38a6a5e4950082863186922be40f062")
    version("7.0.0", sha256="a06dd85c3b55e62626884b9fe477393729ab5cbf7fb45c432df49bb3d918c0fe")
    version("6.4.3", sha256="febace4c74256c9dc29b3ef71227dad615701263aa4825fd4b1bb00145e59122")
    version("6.4.2", sha256="c9aa4d24a7542d029185fe382a0382bd208b2984813ebb854c352b78daf9fb80")
    version("6.4.1", sha256="ceece00ac0cb3431e032ce52eb660667fdfdcc64c1c7e9bb15ac1177fa20db83")
    version("6.4.0", sha256="af2be5806982a72c726cf052c512493cc004bfa98d0136fbf8fed2754a4f4b80")
    version("6.3.3", sha256="5e5bdffb4bf56d30c5f8dd8fda95d162362d17e446396e6b6a3afe8d293039f3")
    version("6.3.2", sha256="7a71dcfec782338af1d838f86b692974368e362de8ad85d5ec26c23b0afbab9e")
    version("6.3.1", sha256="c5093cd6641de478b940d2e36d6723f7ef1ccad3f4f96caf0394def2e6c7e325")
    version("6.3.0", sha256="809b5212d86d182586d676752b192967aee3bde6df8bbbe67558b221d63f5c7c")
    version("6.2.4", sha256="510931103e4a40b272123b5c731d2ea795215c6171810beb1d5335d73bcc9b03")
    version("6.2.1", sha256="2e426572aa5f5b44c7893ea256945c8733b79db39cca84754380f40c8b44a563")
    version("6.2.0", sha256="6fb1f954ed32b5c4085c7f071058d278c2e1e8b7b71118ee5e85cf9bbc024df0")

    amdgpu_targets = ROCmPackage.amdgpu_targets

    variant(
        "amdgpu_target",
        description="AMD GPU architecture",
        values=auto_or_any_combination_of(*amdgpu_targets),
        sticky=True,
    )

    variant("rocm", default=True, description="Build with ROCm")
    variant("cuda", default=False, description="Build with CUDA")

    conflicts("+cuda +rocm", msg="CUDA and ROCm support are mutually exclusive")
    conflicts("~cuda ~rocm", msg="CUDA or ROCm support is required")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("glfw", type="build")
    depends_on("mesa", type="build", when="+cuda")

    for ver in [
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
        depends_on(f"hip@{ver}", when=f"@{ver}")
        depends_on(f"hipify-clang@{ver}", when=f"@{ver}")
        for tgt in ROCmPackage.amdgpu_targets:
            depends_on(f"hipcub@{ver} amdgpu_target={tgt}", when=f"@{ver} amdgpu_target={tgt}")
            depends_on(f"hipsolver@{ver} amdgpu_target={tgt}", when=f"@{ver} amdgpu_target={tgt}")
            depends_on(f"hipblas@{ver} amdgpu_target={tgt}", when=f"@{ver} amdgpu_target={tgt}")
            depends_on(
                f"hiprand@{ver} amdgpu_target={tgt}", when=f"@{ver} +rocm amdgpu_target={tgt}"
            )
            depends_on(
                f"rocblas@{ver} amdgpu_target={tgt}", when=f"@{ver} +rocm amdgpu_target={tgt}"
            )
            depends_on(
                f"rocthrust@{ver} amdgpu_target={tgt}", when=f"@{ver} +rocm amdgpu_target={tgt}"
            )
            depends_on(
                f"rocsparse@{ver} amdgpu_target={tgt}", when=f"@{ver} +rocm amdgpu_target={tgt}"
            )
            depends_on(
                f"rocsolver@{ver} amdgpu_target={tgt}", when=f"@{ver} +rocm amdgpu_target={tgt}"
            )

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
        "7.2.0",
        "7.2.1",
    ]:
        for tgt in ROCmPackage.amdgpu_targets:
            depends_on(f"hipfft@{ver} amdgpu_target={tgt}", when=f"@{ver} amdgpu_target={tgt}")
            depends_on(
                f"rocfft@{ver} amdgpu_target={tgt}", when=f"@{ver} +rocm amdgpu_target={tgt}"
            )

    for ver in ["7.2.0", "7.2.1"]:
        for tgt in ROCmPackage.amdgpu_targets:
            depends_on(f"hipsparse@{ver} amdgpu_target={tgt}", when=f"@{ver} amdgpu_target={tgt}")
            depends_on(f"hip-tensor@{ver} amdgpu_target={tgt}", when=f"@{ver} amdgpu_target={tgt}")
            depends_on(f"rocwmma@{ver} amdgpu_target={tgt}", when=f"@{ver} amdgpu_target={tgt}")
            depends_on(
                f"rocprofiler-sdk@{ver} amdgpu_target={tgt}", when=f"@{ver} amdgpu_target={tgt}"
            )

    depends_on("hip+cuda", when="+cuda")
    depends_on("hipcub+cuda", when="+cuda")
    depends_on("hipsolver+cuda", when="+cuda")
    depends_on("hipblas+cuda", when="+cuda")
    depends_on("hipfft+cuda", when="@6.3: +cuda")

    patch(
        "https://github.com/ROCm/rocm-examples/commit/669fc3e90ce95567464e80d7925f45cb525c81db.patch?full_index=1",
        sha256="ee0eec2140732513d077cca2a46a8257ed785315208dd3e917e4c8e424cfa63e",
        when="@6.4+cuda",
    )
    patch("add_hip_include_cuda.patch", when="@6.4+cuda")
    patch("add_mesa_include.patch", when="@6.4+cuda")
    patch("disable_hiptensor_rocprof-sdk.patch", when="@7.2")

    def patch(self):
        filter_file(
            r"${ROCM_ROOT}/bin/hipify-perl",
            f"{self.spec['hipify-clang'].prefix}/bin/hipify-perl",
            "HIP-Basic/hipify/CMakeLists.txt",
            string=True,
        )

    def cmake_args(self):
        args = []
        if self.spec.satisfies("+rocm"):
            args.append(
                self.define(
                    "OFFLOAD_BUNDLER_COMMAND",
                    f"{self.spec['llvm-amdgpu'].prefix}/bin/clang-offload-bundler",
                )
            )
            args.append(
                self.define("LLVM_MC_COMMAND", f"{self.spec['llvm-amdgpu'].prefix}/bin/llvm-mc")
            )
            args.append(
                self.define("LLVM_DIS_COMMAND", f"{self.spec['llvm-amdgpu'].prefix}/bin/llvm-dis")
            )
        if self.spec.satisfies("+cuda"):
            args.append(self.define("GPU_RUNTIME", "CUDA"))
            args.append(self.define("CMAKE_MODULE_PATH", self.spec["hip"].prefix.lib.cmake.hip))
            args.append(self.define("ROCM_ROOT", self.spec["hip"].prefix))
            args.append(self.define("HIP_ROOT_DIR", self.spec["hip"].prefix))
            args.append(self.define("MESA_INCLUDE_DIR", self.spec["mesa"].prefix.include))
            args.append(
                self.define(
                    "CUDA_DRIVER_LIB",
                    f"{self.spec['cuda'].prefix}/targets/x86_64-linux/lib/stubs/libcuda.so",
                )
            )
            # TODO: enable reduction for +cuda
            args.append(self.define("REDUCTION_BUILD_EXAMPLES", False))
            args.append(self.define("REDUCTION_BUILD_TESTING", False))
            args.append(self.define("REDUCTION_BUILD_BENCHMARKS", False))
        return args
