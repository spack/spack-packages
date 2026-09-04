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

    version("0.28.0", sha256="ac96dd0ec5be9c13f2aa4bfb50498c4727110406f6e4980b58a4097e4d18634a")
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

    depends_on("python@3.10:3.14", type=("build", "run"), when="@0.20:")
    depends_on("python@3.10:3.13", type=("build", "run"), when="@:0.19")
    depends_on("py-setuptools@77.0.3:80", type="build")
    depends_on("py-setuptools-scm@8:", type="build")
    depends_on("py-seuptools-rust@1.9.0:", type="build", when="@0.22:")
    depends_on("py-packaging@24.2:", type="build")
    depends_on("cmake@3.26.1:", type="build")
    depends_on("ninja", type="build")
    depends_on("py-jinja2", type="build")
    depends_on("py-grpcio-tools", type="build", when="@:0.17")

    # PyTorch is imported at build time to read metadata
    depends_on("py-torch@2.13.0 +gloo", when="@0.28.0 ~cuda~rocm", type="build")
    depends_on("py-torch@2.10.0 +gloo", when="@0.16.0 ~cuda~rocm", type="build")
    depends_on("py-torch~cuda~rocm", when="~cuda~rocm", type="build")

    with when("+cuda"):
        depends_on("py-torch@2.9.1 +gloo", when="@0.16.0", type="build")
        # cuDNN / cuSPARSELt / kineto must be enabled in py-torch itself,
        # otherwise vLLM's CMake reports USE_CUDNN=0, USE_CUSPARSELT=0 and
        # kineto_LIBRARY-NOTFOUND.
        depends_on("py-torch +cuda +cudnn +cusparselt +kineto +nccl", type="build")
        # vLLM's CUDA kernels import triton.language.target_info (added in
        # triton 3.x). Without this, vLLM logs "No module named
        # 'triton.language.target_info'" and skips its Triton kernels.
        depends_on("py-triton@3.5.0:", type=("build", "run"))
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
    depends_on("py-transformers@5.5.3:", type=("build", "run"), when="@0.24:")
    depends_on("py-transformers@4.56:4", type=("build", "run"))
    depends_on("py-huggingface-hub@1.27:", type=("build", "run"), when="@0.28:")
    depends_on("py-tokenizers@0.21.1:", type=("build", "run"))
    depends_on("py-safetensors@0.6.2:", type=("build", "run"), when="@0.22:")
    depends_on("py-protobuf@5.29.6:", type=("build", "run"))
    conflicts("^py-protobuf@6.30")
    conflicts("^py-protobuf@6.31")
    conflicts("^py-protobuf@6.32")
    conflicts("^py-protobuf@6.33.0:6.33.4")
    depends_on("py-fastapi@0.133:0.136 +standard", type=("build", "run"), when="@0.24:")
    depends_on("py-fastapi@0.115: +standard", type=("build", "run"))
    depends_on("py-starlette@1.0.1:", type=("build", "run"), when="@0.24:")
    depends_on("py-aiohttp@3.13.3:", type=("build", "run"))
    depends_on("py-openai@2:", type=("build", "run"), when="@0.19:")
    depends_on("py-openai@1.99.1:", type=("build", "run"))
    depends_on("py-pydantic@2.12:", type=("build", "run"))
    depends_on("py-prometheus-client@0.18:", type=("build", "run"))
    depends_on("py-pillow", type=("build", "run"))
    depends_on("py-prometheus-fastapi-instrumentator@8:", type=("build", "run"), when="@0.24:")
    depends_on("py-prometheus-fastapi-instrumentator@7:", type=("build", "run"))
    depends_on("py-tiktoken@0.6:", type=("build", "run"))
    depends_on("py-lm-format-enforcer@0.11.3", type=("build", "run"))
    depends_on("py-llguidance@1.7", type=("build", "run"), when="@0.22:")
    depends_on("py-llguidance@1.3", type=("build", "run"))
    depends_on("py-outlines-core@0.2.14", type=("build", "run"), when="@0.20:")
    depends_on("py-outlines-core@0.2.11", type=("build", "run"))
    depends_on("py-lark@1.2.2", type=("build", "run"))
    depends_on("py-xgrammar@0.2.1:", type=("build", "run"), when="@0.24:")
    depends_on("py-xgrammar@0.1.29", type=("build", "run"))
    depends_on("py-typing-extensions@4.10:", type=("build", "run"))
    depends_on("py-filelock@3.16.1:", type=("build", "run"))
    depends_on("py-partial-json-parser", type=("build", "run"))
    depends_on("py-json-schema@4.23:", type=("build", "run"), when="@0.24:")
    depends_on("py-pyzmq@25:", type=("build", "run"))
    depends_on("py-msgspec", type=("build", "run"))
    depends_on("py-mistral-common@1.11.6: +image", type=("build", "run"), when="@0.27:")
    depends_on("py-mistral-common@1.9.0: +image", type=("build", "run"))
    depends_on("py-opencv-python@4.13: +headless", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-six@1.16:", when="^python@3.12:", type=("build", "run"))
    depends_on("py-einops", type=("build", "run"))
    depends_on("py-compressed-tensors@0.17.0", type=("build", "run"), when="@0.23:")
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
    depends_on("py-model-hosting-container-standards@0.1.14:0", type=("build", "run"), when="@0.21:")
    depends_on("py-model-hosting-container-standards@0.1.13:0", type=("build", "run"))
    depends_on("py-mcp", type=("build", "run"))
    depends_on("py-opentelemetry-sdk@1.27:", type=("build", "run"), when="@0.17:")
    depends_on("py-opentelemetry-api@1.27:", type=("build", "run"), when="@0.17:")
    depends_on("py-opentelemetry-exporter-otlp@1.27:", type=("build", "run"), when="@0.17:")
    depends_on("py-opentelemetry-semantic-conventions-ai@0.4.1:", type=("build", "run"), when="@0.17:")

    # Historical dependencies
    depends_on("py-gguf@0.17:", type=("build", "run"), when="@:0.23")
    depends_on("py-diskcache@5.6.3", type=("build", "run"), when="@:0.25")
    depends_on("py-grpcio", type=("build", "run"), when="@:0.17")
    depends_on("py-grpcio-reflection", type=("build", "run"), when="@:0.17")

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

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        # Triton JIT-compiles its CUDA driver (driver.c / cuda_utils.c) at
        # runtime using the system gcc, and that compile needs cuda.h.
        # Triton's build only knows about its own include dir, not CUDA's,
        # so without CUDA_HOME / CPATH the JIT fails with
        # "fatal error: cuda.h: No such file or directory".
        if self.spec.satisfies("+cuda"):
            cuda_home = self.spec["cuda"].prefix
            env.set("CUDA_HOME", cuda_home)
            env.prepend_path("CPATH", join_path(str(cuda_home), "include"))
