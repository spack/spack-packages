# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyVllm(PythonPackage, CudaPackage):
    """A high-throughput and memory-efficient inference and serving engine for LLMs"""

    license("Apache-2.0")
    homepage = "https://docs.vllm.ai/"
    git = "https://github.com/vllm-project/vllm.git"
    url = "https://github.com/vllm-project/vllm/releases/download/v0.8.5.post1/vllm-0.8.5.post1.tar.gz"

    # Exact set of modules is version- and variant-specific, just attempt to import the
    # core libraries to ensure that the package was successfully installed.
    import_modules = ["vllm", "vllm.LLM", "vllm.SamplingParams"]

    version("main", branch="main")
    version(
        "0.8.5.post1",
        sha256="5e5be78ee00637de4ee29f75ce86edc6c224c05d9e58d067a511eb83c3afe32d",
    )

    with default_args(when="@0.8.5.post1", type=["run"]):
        depends_on("py-torch@2.6.0")
        depends_on("py-torchaudio@2.6.0")
        depends_on("py-torchvision@0.21.0")
        depends_on("py-triron@:3.2.0")
        depends_on("py-xgrammar@0.1.18")
        depends_on("py-numba@0.61.2")
        depends_on("py-llguidance@0.7.11:0.7.30")

    with default_args(type="build"):
        depends_on("c")
        depends_on("cxx")
        depends_on("cmake@3.26.1:")
        depends_on("ninja")
        depends_on("py-packaging")
        depends_on("py-setuptools@61:")
        depends_on("py-setuptools-scm@8:")
        depends_on("py-wheel")
        depends_on("py-jinja2")
    
    with default_args(type=type=["build", "run"]):
        depends_on("py-regex")
        depends_on("py-torch+custom-protobuf")

    with default_args(type="run"):
        depends_on("py-torchaudio")
        depends_on("py-torchvision")
        depends_on("py-triron")
        depends_on("py-pydantic@2.10.0:")
        depends_on("py-transformers@4.51.1:")
        depends_on("py-cachetools")
        depends_on("py-cloudpickle")
        depends_on("py-psutil")
        depends_on("py-pyzmq@25.0.0:")
        depends_on("py-msgspec")
        depends_on("py-pillow")
        depends_on("py-blake3")
        depends_on("py-openai@1.52.0:")
        depends_on("py-py-cpuinfo")
        depends_on("py-gguf@0.13.0:")
        depends_on("py-prometheus-client@0.18.0:")
        depends_on("py-llguidance")
        depends_on("py-xgrammar")
        depends_on("py-sentencepiece")
        depends_on("py-tiktoken@0.6.0:")
        depends_on("py-numba")
        depends_on("py-fastapi@0.115.0:+all")
        depends_on("py-partial-json-parser")
        depends_on("py-prometheus-fastapi-instrumentator")

    variant("cuda", default=True, description="Use CUDA")
    conflicts("~cuda")

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        # If oom error, try lowering the number of jobs with `spack install -j`
        env.set("MAX_JOBS", str(make_jobs))
