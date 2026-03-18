# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyVllm(PythonPackage):
    """A high-throughput and memory-efficient inference and serving engine for LLMs."""

    homepage = "https://vllm.ai/"
    url = "https://github.com/vllm-project/vllm/archive/v0.15.1.tar.gz"

    maintainers("thomas-bouvier")

    version("0.15.1", sha256="74ff0f8e7df3d36c76760ed779aaac011bdf4c518877e07f9abad06291fe0f25")

    variant("cuda", default=False, description="Use CUDA")
    variant("rocm", default=False, description="Use ROCm")

    conflicts("+cuda+rocm")

    depends_on("python@3.10:3.13", type=("build", "run"))
    depends_on("py-setuptools@77.0.3:80", type="build")
    depends_on("py-setuptools-scm@8:", type="build")
    depends_on("py-packaging@24.2:", type="build")
    depends_on("cmake@3.26.1:", type="build")
    depends_on("ninja", type="build")
    depends_on("py-jinja2", type="build")
    depends_on("py-grpcio-tools@1.78.0", type="build")  # exact version
    depends_on("py-torch@2.10.0", when="@0.15.1", type="build")  # exact version

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
    depends_on("py-protobuf@6.33.5:", type=("build", "run"))  # to be updated
    depends_on("py-fastapi@0.115: +standard", type=("build", "run"))  # missing variant
    depends_on("py-aiohttp@3.13.3:", type=("build", "run"))  # to be updated
    depends_on("py-openai@1.99.1:", type=("build", "run"))  # to be updated
    depends_on("py-pydantic@2.12:", type=("build", "run"))
    depends_on("py-prometheus-client@0.18:", type=("build", "run"))
    depends_on("pil", type=("build", "run"))
    depends_on("py-prometheus-fastapi-instrumentator@7:", type=("build", "run"))  # to be added
    depends_on("py-tiktoken@0.6:", type=("build", "run"))
    depends_on("py-lm-format-enforcer@0.11.3", type=("build", "run"))
    depends_on("py-llguidance@1.3:", type=("build", "run"))
    depends_on("py-outlines-core@0.2.11", type=("build", "run"))
    depends_on("py-diskcache@5.6.3", type=("build", "run"))
    depends_on("py-lark@1.2.2", type=("build", "run"))
    depends_on("py-xgrammar@0.1.29", type=("build", "run"))
    depends_on("py-typing-extensions@4.10:", type=("build", "run"))
    depends_on("py-filelock@3.16.1:", type=("build", "run"))
    depends_on("py-partial-json-parser", type=("build", "run"))
    depends_on("py-pyzmq", type=("build", "run"))
    depends_on("py-msgspec", type=("build", "run"))
    depends_on("py-gguf@0.17:", type=("build", "run"))  # to be added
    depends_on("py-mistral-common@1.8.8: +image", type=("build", "run"))  # to be added
    depends_on("py-opencv-python@4.13: +headless", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-six@1.16:", when="^python@3.12:", type=("build", "run"))
    depends_on("py-einops", type=("build", "run"))
    depends_on("py-compressed-tensors@0.13.0", type=("build", "run"))  # to be added, exact version
    depends_on("py-depyf@0.20.0", type=("build", "run"))
    depends_on("py-cloudpickle", type=("build", "run"))
    depends_on("py-watchfiles", type=("build", "run"))
    depends_on("py-python-json-logger", type=("build", "run"))
    depends_on("py-pybase64", type=("build", "run"))  # not sure
    depends_on("py-cbor2", type=("build", "run"))
    depends_on("py-ijson", type=("build", "run"))  # not sure
    depends_on("py-setproctitle", type=("build", "run"))
    depends_on("py-openai-harmony@0.0.3:", type=("build", "run"))  # to be added
    depends_on("py-anthropic@0.71:", type=("build", "run"))  # to be added
    depends_on("py-model-hosting-container-standards@0.1.13:0", type=("build", "run"))
    depends_on("py-mcp", type=("build", "run"))
    depends_on("py-grpcio", type=("build", "run"))
    depends_on("py-grpcio-reflection", type=("build", "run"))  # to be added

    # Optional dependencies
    with default_args(type=("build", "link", "run")):
        depends_on("cuda", when="+cuda")

    with when("+rocm"):
        depends_on("hip")

    # https://docs.vllm.ai/en/v0.6.1/getting_started/installation.html
    # https://github.com/vllm-project/vllm/blob/main/setup.py

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        if self.spec.satisfies("+cuda"):
            env.set("CUDA_HOME", self.spec["cuda"].prefix)
        elif self.spec.satisfies("+rocm"):
            env.set("ROCM_HOME", self.spec["rocm"].prefix)
