# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.python import PythonPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

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

    # Spack-built torch has no vendored libgomp; the REQUIRED find_library(gomp)
    # fallback then fails configure even though OPEN_MP is unused and -fopenmp
    # already supplies OpenMP flags.
    patch("no-required-gomp.patch", when="@0.28.0")

    conflicts("+cuda+rocm")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("numactl", type="build")

    depends_on("python@3.10:3.14", type=("build", "run"), when="@0.20:")
    depends_on("python@3.10:3.13", type=("build", "run"), when="@:0.19")
    depends_on("py-setuptools@77.0.3:80", type="build")
    depends_on("py-setuptools-scm@8:", type="build")
    depends_on("py-setuptools-rust@1.9.0:", type="build", when="@0.22:")
    depends_on("py-packaging@24.2:", type="build")
    depends_on("cmake@3.26.1:", type="build")
    depends_on("ninja", type="build")
    depends_on("py-jinja2", type="build")
    depends_on("py-grpcio-tools", type="build", when="@:0.17")

    # https://github.com/vllm-project/vllm/blob/v0.16.0/requirements
    depends_on("py-torchvision", type=("build", "run"))
    depends_on("py-torchaudio", type=("build", "run"))

    # find_package(Torch) triggers torch's Caffe2Config.cmake, which does
    # find_package(Protobuf) at configure time. py-torch is a build-only dep,
    # so its own protobuf dep is not put on CMAKE_PREFIX_PATH here; declare
    # protobuf explicitly so CMake can find it.
    depends_on("protobuf", when="^py-torch~custom-protobuf", type="build")

    with when("~cuda~rocm"):
        # PyTorch is imported at build time to read metadata
        depends_on("py-torch@2.13.0 +kineto +gloo", type="build", when="@0.28.0")
        depends_on("py-torch@2.10.0 +kineto +gloo", type="build", when="@0.16.0")
        depends_on("sleef", type=("build", "run", "link"))
        # oneDNN source. vLLM's cmake/cpu_extension.cmake fetches oneDNN via
        # FetchContent and compiles private headers from src/ (e.g.
        # common/memory_desc.hpp). An install prefix is not enough; drop the
        # source into the build tree and point FETCHCONTENT_SOURCE_DIR_ONEDNN
        # at it in setup_build_environment.
        resource(
            name="onednn",
            url="https://github.com/oneapi-src/oneDNN/archive/refs/tags/v3.13.tar.gz",
            sha256="f90a34cc3f1a5af511570d72f4437205efdf97e1d28c576418daa7ef1a34daaa",
            destination=".",
            placement="onednn-src",
            when="@0.28.0:",
        )

    with when("+cuda"):
        # Keep the CUDA version compatible with the *driver* on the target
        # machines: several kernels are PTX-only fallbacks (FA2 ships
        # "8.0+PTX", Marlin "8.0+PTX", scaled_mm_c2x "8.9+PTX") and are
        # JIT-compiled by the driver at runtime. PTX from a toolkit newer
        # than the driver fails with cudaErrorUnsupportedPtxVersion.
        depends_on("cuda", type=("build", "link", "run"))
        conflicts(
            "cuda_arch=none",
            msg="Must specify CUDA compute capabilities of your GPU, see "
            "https://developer.nvidia.com/cuda-gpus",
        )

        depends_on("py-torch@2.9.1 +gloo", when="@0.16.0", type="build")
        depends_on("py-torch +cuda +gloo +cudnn +cusparselt +kineto +nccl", type="build")
        depends_on("py-triton@3.5.0:", type=("build", "run"))
        depends_on("py-flashinfer@0.6.16.post3", type="run", when="@0.28.0")
        depends_on("py-pybind11", type="build", when="@0.28.0")

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

        # CUTLASS source. vLLM's CMakeLists.txt pins a CUTLASS_REVISION per
        # release (v4.2.1 for v0.16.0, v4.4.2 for v0.28.0) and uses
        # FetchContent_Declare(cutlass SOURCE_DIR ...), which needs the full
        # source tree (not just an install prefix with headers). We drop the
        # source into the build tree via a Spack resource and point
        # VLLM_CUTLASS_SRC_DIR at it in setup_build_environment.
        resource(
            name="cutlass",
            url="https://github.com/NVIDIA/cutlass/archive/refs/tags/v4.4.2.tar.gz",
            sha256="ef62816841b8cbcd0ed3ec45d3ab56cf67d569a0f39329b43eeeebea86f58473",
            destination=".",
            placement="cutlass-src",
            when="@0.28.0",
        )
        resource(
            name="cutlass",
            url="https://github.com/NVIDIA/cutlass/archive/refs/tags/v4.2.1.tar.gz",
            sha256="a4513ba33ae82fd754843c6d8437bee1ac71a6ef1c74df886de2338e3917d4df",
            destination=".",
            placement="cutlass-src",
            when="@0.16.0",
        )

        # vLLM FetchContent-clones the external projects below at configure
        # time (cmake/external_projects/*.cmake), each pinned to a fixed git
        # commit. Stage the pinned trees as Spack resources instead, so builds
        # are checksummed and work without network access.
        resource(
            name="triton",
            url="https://github.com/triton-lang/triton/archive/refs/tags/v3.5.1.tar.gz",
            sha256="03d7c41f6f2dc1dfa3445776c4a893dc34b1e0ece42b953f036c071ff6409b80",
            destination=".",
            placement="triton-src",
            when="@0.28.0",
        )
        resource(
            name="deepgemm",
            url="https://github.com/deepseek-ai/DeepGEMM/archive/8b1392b978f5a03c828dd1711090d7fb50958b8a.tar.gz",  # noqa: E501
            sha256="d5181fff7d29c8c7386a1a7f656e764663502ed878e228d5ec8fa5eff2feb67f",
            destination=".",
            placement="deepgemm-src",
            when="@0.28.0",
        )
        resource(
            name="deepgemm-cutlass",
            url="https://github.com/NVIDIA/cutlass/archive/f3fde58372d33e9a5650ba7b80fc48b3b49d40c8.tar.gz",  # noqa: E501
            sha256="2e5890306557bd87136e1d6914e4ee42536050b9116433848175520fd15991f2",
            destination=".",
            placement={
                "include": "deepgemm-src/third-party/cutlass/include",
                "tools/util/include": "deepgemm-src/third-party/cutlass/tools/util/include",
            },
            when="@0.28.0",
        )
        resource(
            name="deepgemm-fmt",
            url="https://github.com/fmtlib/fmt/archive/553ec11ec06fbe0beebfbb45f9dc3c9eabd83d28.tar.gz",  # noqa: E501
            sha256="c314292789d28c3c3b420e75a7b2d1706f685f7fb63289128d46aeaea2c6be71",
            destination=".",
            placement={"include": "deepgemm-src/third-party/fmt/include"},
            when="@0.28.0",
        )
        resource(
            name="fmha-sm100",
            url="https://github.com/vllm-project/MSA/archive/087c161814d4d9c735b46c21212a09e5f8eb92fa.tar.gz",  # noqa: E501
            sha256="32efbae22ce41f85adf01dfd3ad98494a774591b10d00ea558a94d34170d579a",
            destination=".",
            placement="msa-src",
            when="@0.28.0",
        )
        resource(
            name="fmha-sm100-cutlass",
            url="https://github.com/NVIDIA/cutlass/archive/eb61c911471867a5fd2466bfd8f29306cea6ebf8.tar.gz",  # noqa: E501
            sha256="ffe392246cc3517017c4b91d14bbcb28aae28d26d1847b333371eb13bfec52eb",
            destination=".",
            placement={
                "include": "msa-src/python/fmha_sm100/cutlass/include",
                "tools/util/include": "msa-src/python/fmha_sm100/cutlass/tools/util/include",
            },
            when="@0.28.0",
        )
        resource(
            name="flashmla",
            url="https://github.com/vllm-project/FlashMLA/archive/a8f794d1251cbfd88a5011445dd5582289c727e4.tar.gz",  # noqa: E501
            sha256="36b9409fabb373f13d5b5b841125e71f5e11875283e752c43df5ee47f5def96b",
            destination=".",
            placement="flashmla-src",
            when="@0.28.0",
        )
        resource(
            name="flashmla-cutlass",
            url="https://github.com/NVIDIA/cutlass/archive/147f5673d0c1c3dcf66f78d677fd647e4a020219.tar.gz",  # noqa: E501
            sha256="9f6c53320a85b4a570975e557918cde65168cd311f081920446c238437347dc6",
            destination=".",
            placement={
                "include": "flashmla-src/csrc/cutlass/include",
                "tools/util/include": "flashmla-src/csrc/cutlass/tools/util/include",
            },
            when="@0.28.0",
        )
        resource(
            name="flashkda",
            url="https://github.com/vllm-project/FlashKDA/archive/053de1b716ef3255873e02d2d28f4adf09951978.tar.gz",  # noqa: E501
            sha256="9665899dcbca31c8d9af55b9ff126b7a9c15710f1c12505d03cfba39d6c243d5",
            destination=".",
            placement="flashkda-src",
            when="@0.28.0",
        )
        resource(
            name="flashkda-cutlass",
            url="https://github.com/NVIDIA/cutlass/archive/5c149f52a436782210263fb2f19b354443a61c6a.tar.gz",  # noqa: E501
            sha256="fbf35b9d16a3c2c7384a4a044a5407d1dea334d74b3152357c1fa246bc07c6dc",
            destination=".",
            placement={
                "include": "flashkda-src/cutlass/include",
                "examples/common": "flashkda-src/cutlass/examples/common",
                "tools/util/include": "flashkda-src/cutlass/tools/util/include",
            },
            when="@0.28.0",
        )
        # QuTLASS needs no vendored submodule resource: it uses the
        # CUTLASS_INCLUDE_DIR cache variable, which CUTLASS's own CMakeLists
        # sets to the cutlass-src tree staged above.
        resource(
            name="qutlass",
            url="https://github.com/IST-DASLab/qutlass/archive/e74319e3405ce6d71965732880f5dc1f52371f64.tar.gz",  # noqa: E501
            sha256="39dda9c3626e024f00cd0afbe54971edce79fa12f0842d79022c8e23303faea3",
            destination=".",
            placement="qutlass-src",
            when="@0.28.0",
        )
        resource(
            name="tml-fa4",
            url="https://github.com/vllm-project/tml-fa4/archive/b206834606ed5b5f21f8eed6b0683f528ea9cf7d.tar.gz",  # noqa: E501
            sha256="7f42421e89a030e10c5a336dcfc405e16565a106698da855ddbcfa86dd0e602e",
            destination=".",
            placement="tml-fa4-src",
            when="@0.28.0",
        )
        resource(
            name="flash-attention",
            url="https://github.com/vllm-project/flash-attention/archive/f3e1a4f74c99145c0717709860bf765de1703779.tar.gz",  # noqa: E501
            sha256="088552752435faf7902d6c64aa41cb297f3d2354d81aa992d6be8bb074eed7cf",
            destination=".",
            placement="flash-attn-src",
            when="@0.28.0",
        )
        resource(
            name="flash-attention-cutlass",
            url="https://github.com/NVIDIA/cutlass/archive/62750a2b75c802660e4894434dc55e839f322277.tar.gz",  # noqa: E501
            sha256="78816d6c6d97793b5b59ef2a702174cb85b78dfcefc8fe2489964de2e42f17d2",
            destination=".",
            placement={
                "include": "flash-attn-src/csrc/cutlass/include",
                "tools/util/include": "flash-attn-src/csrc/cutlass/tools/util/include",
            },
            when="@0.28.0",
        )

    with when("+rocm"):
        depends_on("hip")

    # Common deps https://github.com/vllm-project/vllm/blob/v0.16.0/requirements/common.txt
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
    depends_on("py-transformers@4.56:4", type=("build", "run"), when="@:0.19.0")
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
    depends_on("py-llguidance@1.3", type=("build", "run"), when="@:0.21")
    depends_on("py-outlines-core@0.2.14", type=("build", "run"), when="@0.20:")
    depends_on("py-outlines-core@0.2.11", type=("build", "run"), when="@:0.19")
    depends_on("py-lark@1.2.2", type=("build", "run"))
    depends_on("py-xgrammar@0.2.1:0", type=("build", "run"), when="@0.24:")
    depends_on("py-xgrammar@0.1.29", type=("build", "run"), when="@:0.17.1")
    depends_on("py-typing-extensions@4.10:", type=("build", "run"))
    depends_on("py-filelock@3.16.1:", type=("build", "run"))
    depends_on("py-partial-json-parser", type=("build", "run"))
    depends_on("py-jsonschema@4.23:", type=("build", "run"), when="@0.24:")
    depends_on("py-pyzmq@25:", type=("build", "run"))
    depends_on("py-msgspec", type=("build", "run"))
    depends_on("py-mistral-common@1.11.6: +image", type=("build", "run"), when="@0.27:")
    depends_on("py-mistral-common@1.9.0: +image", type=("build", "run"))
    depends_on("py-opencv-python@4.13: +headless", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-six@1.16:", when="^python@3.12:", type=("build", "run"))
    depends_on("py-einops", type=("build", "run"))
    depends_on("py-compressed-tensors@0.17.0", type=("build", "run"), when="@0.23:")
    depends_on("py-compressed-tensors@0.13.0", type=("build", "run"), when="@:0.18")
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
    depends_on(
        "py-model-hosting-container-standards@0.1.14:0", type=("build", "run"), when="@0.21:"
    )
    depends_on("py-model-hosting-container-standards@0.1.13:0", type=("build", "run"), when="@:0.20")
    depends_on("py-mcp", type=("build", "run"))
    depends_on("py-opentelemetry-sdk@1.27:", type=("build", "run"), when="@0.17:")
    depends_on("py-opentelemetry-api@1.27:", type=("build", "run"), when="@0.17:")
    # This dependency brings exporters pinned at version @1.15, causing concretization errors
    #depends_on("py-opentelemetry-exporter-otlp@1.27:", type=("build", "run"), when="@0.17:")
    depends_on(
        "py-opentelemetry-semantic-conventions-ai@0.4.1:", type=("build", "run"), when="@0.17:"
    )

    # Historical dependencies
    depends_on("py-gguf@0.17:", type=("build", "run"), when="@:0.23")
    depends_on("py-diskcache@5.6.3", type=("build", "run"), when="@:0.25")
    depends_on("py-grpcio", type=("build", "run"), when="@:0.17")
    depends_on("py-grpcio-reflection", type=("build", "run"), when="@:0.17")

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        # Override version to avoid setuptools_scm requiring a git repo.
        # Include the device local-version label (e.g. +cpu) so runtime
        # platform detection works without VLLM_TARGET_DEVICE: views do not
        # apply setup_run_environment, and upstream checks version for "cpu".
        if self.spec.satisfies("+cuda"):
            device = "cuda"
        elif self.spec.satisfies("+rocm"):
            device = "rocm"
        else:
            device = "cpu"
        env.set("VLLM_VERSION_OVERRIDE", f"{self.spec.version}+{device}")
        env.set("VLLM_TARGET_DEVICE", device)

        if self.spec.satisfies("+cuda"):
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

            # Redirect the external projects vLLM FetchContent-clones at
            # configure time (cmake/external_projects/*.cmake) to the source
            # trees staged by the resource() directives above, using each
            # project's documented local-source override.
            if self.spec.satisfies("@0.28.0"):
                src = self.stage.source_path
                env.set(
                    "TRITON_KERNELS_SRC_DIR",
                    join_path(src, "triton-src", "python", "triton_kernels", "triton_kernels"),
                )
                # The DeepGEMM _C driver (tools/build_deepgemm_C.py) calls $CXX
                # directly with a hardcoded include list that has no pybind11
                # entry; CXXFLAGS cannot reach it, but gcc/clang honor CPATH.
                # See the py-pybind11 depends_on above.
                env.prepend_path("CPATH", self.spec["py-pybind11"].prefix.include)
                env.set("DEEPGEMM_SRC_DIR", join_path(src, "deepgemm-src"))
                env.set("FMHA_SM100_SRC_DIR", join_path(src, "msa-src"))
                env.set("FLASH_MLA_SRC_DIR", join_path(src, "flashmla-src"))
                env.set("FLASH_KDA_SRC_DIR", join_path(src, "flashkda-src"))
                env.set("QUTLASS_SRC_DIR", join_path(src, "qutlass-src"))
                env.set("TML_FA4_SRC_DIR", join_path(src, "tml-fa4-src"))
                # Not VLLM_FLASH_ATTN_SRC_DIR: with it, vLLM installs the FA4
                # CuteDSL kernels as a symlink into the build stage instead of
                # copying the files, leaving a dangling symlink after stage
                # cleanup. The FetchContent cache variable below (passed via
                # the CMAKE_ARGS env var, forwarded by vLLM's setup.py) keeps
                # the copy-based install while still skipping the download.
                env.set(
                    "CMAKE_ARGS",
                    "-DFETCHCONTENT_SOURCE_DIR_VLLM-FLASH-ATTN=%s"
                    % join_path(src, "flash-attn-src"),
                )
        elif self.spec.satisfies("+rocm"):
            env.set("ROCM_HOME", self.spec["rocm"].prefix)
        else:
            env.set(
                "FETCHCONTENT_SOURCE_DIR_ONEDNN",
                join_path(self.stage.source_path, "onednn-src"),
            )

        numa_inc = self.spec["numactl"].prefix.include
        numa_lib = self.spec["numactl"].prefix.lib
        env.append_flags("CXXFLAGS", f"-I{numa_inc}")
        env.append_flags("LDFLAGS", f"-L{numa_lib}")

        if self.spec.satisfies("~cuda~rocm"):
            # Keep -I/-L only. Putting -lsleef in LDFLAGS breaks CMake's nested
            # oneDNN C ABI try_compile (CMAKE_SIZEOF_VOID_P unset -> "64 bit
            # platforms only"). Torch already links sleef; the extension inherits it.
            sleef_inc = self.spec["sleef"].prefix.include
            sleef_lib = self.spec["sleef"].prefix.lib
            env.append_flags("CXXFLAGS", f"-I{sleef_inc}")
            env.append_flags("LDFLAGS", f"-L{sleef_lib}")

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        # Also set for `spack load` / env activate. Views alone do not apply
        # this; the +cpu/+cuda/+rocm version label above is the reliable signal.
        if self.spec.satisfies("+cuda"):
            env.set("VLLM_TARGET_DEVICE", "cuda")
        elif self.spec.satisfies("+rocm"):
            env.set("VLLM_TARGET_DEVICE", "rocm")
        else:
            env.set("VLLM_TARGET_DEVICE", "cpu")

        # Triton JIT-compiles its CUDA driver (driver.c / cuda_utils.c) at
        # runtime using the system gcc, and that compile needs cuda.h.
        # Triton's build only knows about its own include dir, not CUDA's,
        # so without CUDA_HOME / CPATH the JIT fails with
        # "fatal error: cuda.h: No such file or directory".
        if self.spec.satisfies("+cuda"):
            cuda_home = self.spec["cuda"].prefix
            env.set("CUDA_HOME", cuda_home)
            env.prepend_path("CPATH", join_path(str(cuda_home), "include"))
