# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyVllm(PythonPackage, CudaPackage, ROCmPackage):
    """A high-throughput and memory-efficient inference and serving engine for LLMs."""

    homepage = "https://vllm.ai/"
    pypi = "vllm/vllm-0.16.0.tar.gz"

    maintainers("thomas-bouvier")

    version("0.16.0", sha256="1f684bb31fbef59d862e2fe666e23a41f1d39d93f86215ce1ce1db89a8f5665b")

    # Fix compilation on x86 without AVX512
    # https://github.com/vllm-project/vllm/pull/34052
    patch("fix-mla-decode-avx2.patch", when="@0.16.0")

    variant("cuda", default=False, description="Use CUDA")
    variant("rocm", default=False, description="Use ROCm")

    conflicts("+cuda+rocm")

    conflicts(
        "cuda_arch=none",
        when="+cuda",
        msg="Must specify CUDA compute capabilities of your GPU, see "
        "https://developer.nvidia.com/cuda-gpus",
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("numactl", type="build")

    depends_on("python@3.10:3.13", type=("build", "run"))
    depends_on("py-setuptools@77.0.3:80", type="build")
    depends_on("py-setuptools-scm@8:", type="build")
    depends_on("py-packaging@24.2:", type="build")
    depends_on("cmake@3.26.1:", type="build")
    depends_on("ninja", type="build")
    depends_on("py-jinja2", type="build")
    depends_on("py-grpcio-tools", type="build")

    # PyTorch is imported at build time to read metadata
    # vLLM 0.16.0 expects TORCH_SUPPORTED_VERSION_CUDA == 2.9.1, but the CPU build
    # tracks newer torch.
    depends_on("py-torch@2.10.0", when="@0.16.0 ~cuda~rocm", type="build")
    depends_on("py-torch~cuda~rocm", when="~cuda~rocm", type="build")

    with when("+cuda"):
        depends_on("py-torch@2.9.1", when="@0.16.0", type="build")
        # cuDNN / cuSPARSELt / kineto must be enabled in py-torch itself,
        # otherwise vLLM's CMake reports USE_CUDNN=0, USE_CUSPARSELT=0 and
        # kineto_LIBRARY-NOTFOUND.
        depends_on("py-torch +cuda +cudnn +cusparselt +kineto +nccl", type="build")
        # Propagate CUDA arch to py-torch and nccl
        for cuda_arch in CudaPackage.cuda_arch_values:
            depends_on(
                "py-torch cuda_arch=%s" % cuda_arch,
                when="cuda_arch=%s" % cuda_arch,
                type="build",
            )
            depends_on(
                "nccl cuda_arch=%s" % cuda_arch,
                when="cuda_arch=%s" % cuda_arch,
                type="build",
            )

    # CUTLASS source. vLLM's CMakeLists.txt pins CUTLASS_REVISION to v4.2.1 for
    # v0.16.0 and uses FetchContent_Declare(cutlass SOURCE_DIR ...), which needs
    # the full source tree (not just an install prefix with headers). We drop
    # the source into the build tree via a Spack resource and point
    # VLLM_CUTLASS_SRC_DIR at it in setup_build_environment.
    resource(
        name="cutlass",
        url="https://github.com/NVIDIA/cutlass/archive/refs/tags/v4.2.1.tar.gz",
        sha256="a4513ba33ae82fd754843c6d8437bee1ac71a6ef1c74df886de2338e3917d4df",
        destination=".",
        placement="cutlass-src",
        when="@0.16.0 +cuda",
    )

    # TODO: vLLM 0.16.0 also FetchContents the following at configure time and
    # will fail without network:
    #   - flashmla       (env override: FLASH_MLA_SRC_DIR)
    #   - qutlass        (env override: QUTLASS_SRC_DIR)
    #   - vllm-flash-attn(env override: VLLM_FLASH_ATTN_SRC_DIR)
    #   - triton_kernels (env override: TRITON_KERNELS_SRC_DIR)
    # Add resource() entries for each and export the corresponding env vars
    # in setup_build_environment if/when offline builds are required.

    # Common deps https://github.com/vllm-project/vllm/blob/v0.15.1/requirements/common.txt
    depends_on("py-regex", type=("build", "run"))
    depends_on("py-cachetools", type=("build", "run"))
    depends_on("py-psutil", type=("build", "run"))
    depends_on("py-sentencepiece", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-requests@2.26:", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-blake3", type=("build", "run"))
    depends_on("py-py-cpuinfo", type=("build", "run"))
    depends_on("py-transformers@4.56:4", type=("build", "run"))
    depends_on("py-tokenizers@0.21.1:", type=("build", "run"))
    depends_on("py-protobuf@6.33.5:", type=("build", "run"))
    depends_on("py-fastapi@0.115: +standard", type=("build", "run"))
    depends_on("py-aiohttp@3.13.3:", type=("build", "run"))
    depends_on("py-openai@1.99.1:", type=("build", "run"))
    depends_on("py-pydantic@2.12:", type=("build", "run"))
    depends_on("py-prometheus-client@0.18:", type=("build", "run"))
    depends_on("py-pillow", type=("build", "run"))
    depends_on("py-prometheus-fastapi-instrumentator@7:", type=("build", "run"))
    depends_on("py-tiktoken@0.6:", type=("build", "run"))
    depends_on("py-lm-format-enforcer@0.11.3", type=("build", "run"))
    depends_on("py-llguidance@1.3", type=("build", "run"))
    depends_on("py-outlines-core@0.2.11", type=("build", "run"))
    depends_on("py-diskcache@5.6.3", type=("build", "run"))
    depends_on("py-lark@1.2.2", type=("build", "run"))
    depends_on("py-xgrammar@0.1.29", type=("build", "run"))
    depends_on("py-typing-extensions@4.10:", type=("build", "run"))
    depends_on("py-filelock@3.16.1:", type=("build", "run"))
    depends_on("py-partial-json-parser", type=("build", "run"))
    depends_on("py-pyzmq@25:", type=("build", "run"))
    depends_on("py-msgspec", type=("build", "run"))
    depends_on("py-gguf@0.17:", type=("build", "run"))
    depends_on("py-mistral-common@1.9.0: +image", type=("build", "run"))
    depends_on("py-opencv-python@4.13: +headless", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-six@1.16:", when="^python@3.12:", type=("build", "run"))
    depends_on("py-einops", type=("build", "run"))
    depends_on("py-compressed-tensors@0.13.0", type=("build", "run"))
    depends_on("py-depyf@0.20.0", type=("build", "run"))
    depends_on("py-cloudpickle", type=("build", "run"))
    depends_on("py-watchfiles", type=("build", "run"))
    depends_on("py-python-json-logger", type=("build", "run"))
    depends_on("py-pybase64", type=("build", "run"))  # not sure
    depends_on("py-cbor2", type=("build", "run"))
    depends_on("py-ijson", type=("build", "run"))  # not sure
    depends_on("py-setproctitle", type=("build", "run"))
    depends_on("py-openai-harmony@0.0.3:", type=("build", "run"))
    depends_on("py-anthropic@0.71:", type=("build", "run"))
    depends_on("py-model-hosting-container-standards@0.1.13:0", type=("build", "run"))
    depends_on("py-mcp", type=("build", "run"))
    depends_on("py-grpcio", type=("build", "run"))
    depends_on("py-grpcio-reflection", type=("build", "run"))

    # Optional dependencies
    with default_args(type=("build", "link", "run")):
        depends_on("cuda", when="+cuda")

    with when("+rocm"):
        depends_on("hip")

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        # Override version to avoid setuptools_scm requiring a git repo
        # and to bypass get_vllm_version() device-detection logic
        env.set("VLLM_VERSION_OVERRIDE", str(self.spec.version))

        if self.spec.satisfies("+cuda"):
            env.set("VLLM_TARGET_DEVICE", "cuda")
            env.set("CUDA_HOME", self.spec["cuda"].prefix)

            # Point vLLM's CMake at the cutlass source tree fetched by the
            # resource() above. Must be a real directory containing
            # CMakeLists.txt (not a Spec object or an install prefix).
            env.set(
                "VLLM_CUTLASS_SRC_DIR",
                join_path(self.stage.source_path, "cutlass-src"),
            )

            # PyTorch and vLLM CMakeLists.txt expect TORCH_CUDA_ARCH_LIST and
            # emit a warning if CMAKE_CUDA_ARCHITECTURES is used instead.
            # Convert Spack's "80" -> "8.0", "120" -> "12.0", etc.
            arches = self.spec.variants["cuda_arch"].value
            torch_arch = ";".join("{}.{}".format(a[:-1], a[-1]) for a in arches)
            env.set("TORCH_CUDA_ARCH_LIST", torch_arch)
        elif self.spec.satisfies("+rocm"):
            env.set("VLLM_TARGET_DEVICE", "rocm")
            env.set("ROCM_HOME", self.spec["rocm"].prefix)
        else:
            env.set("VLLM_TARGET_DEVICE", "cpu")

        numa_inc = self.spec["numactl"].prefix.include
        numa_lib = self.spec["numactl"].prefix.lib
        env.append_flags("CXXFLAGS", f"-I{numa_inc}")
        env.append_flags("LDFLAGS", f"-L{numa_lib}")
